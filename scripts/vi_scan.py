#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
vi_scan.py — Máy quét dấu văn AI tiếng Việt (zero-dependency, Python 3.9+)

Ba việc:
  scan    : quét file/văn bản, báo dấu hiệu theo mức P0/P1/P2 + số nhịp học
  verify  : so before/after, phát hiện sửa nhầm vùng bảo tồn (code, URL, số, YAML)
  selftest: chạy fixture nhỏ tự kiểm

Cách dùng:
  python3 vi_scan.py scan FILE            # hoặc: cat x.md | python3 vi_scan.py scan
  python3 vi_scan.py scan FILE --json
  python3 vi_scan.py verify TRUOC SAU
  python3 vi_scan.py selftest

Điểm score 0-100: P0 tính 6 điểm, P1 tính 3 điểm, P2 tính 1 điểm, cộng hiệu chỉnh
nhịp học (đều câu/đều đoạn/thiếu từ riêng). Thang tham khảo, không phải chân lý.
"""

import json
import math
import re
import sys

# ---------------------------------------------------------------------------
# Dữ liệu dấu hiệu
# ---------------------------------------------------------------------------

# P0 — vỏ chatbot & dàn cảnh: gặp là sửa (đối chiếu Wikipedia Signs of AI writing,
# mục "Chatbot residue", "Staged run-up"; bản Việt hóa)
P0_PATTERNS = [
    (r"(?i)chúc\s+bạn\s+một\s+ngày\s+(tốt\s+ lành|tốt\s+lành)", "vỏ chatbot: lời chúc cuối"),
    (r"(?i)hy\s+vọng\s+(thông\s+tin|nội\s+dung|bài\s+viết|đoạn\s+van|này)[^.!?]*hữu\s+ích", "vỏ chatbot: 'hy vọng ... hữu ích'"),
    (r"(?i)^\s*(câu\s+hỏi\s+(rất\s+)?hay|great\s+question)\s*[!!.]", "vỏ chatbot: khen câu hỏi"),
    (r"(?i)(bạn\s+hoàn\s+toàn\s+đúng|đúng\s+như\s+bạn\s+nói|hỏi\s+hay\s+quá)", "vỏ chatbot: tán thưởng người hỏi"),
    (r"(?i)(hãy\s+cho\s+tôi\s+biết\s+nếu|đừng\s+ngần\s+ngại\s+(liên|hỏi)|nếu\s+bạn\s+cần\s+thêm)", "vỏ chatbot: mời hỏi thêm"),
    (r"(?i)(hãy\s+cùng|cùng\s+khám\s+phá|cùng\s+tìm\s+hiểu|hãy\s+khám\s+phá|hãy\s+tìm\s+hiểu)", "mở dàn cảnh: 'hãy cùng...'"),
    (r"(?i)dưới\s+đây\s+là\s+(một\s+)?(số\s+|những\s+)?(điều|cách|lưu\s+ý|dấu\s+hiệu|lý\s+do|nguyên\s+nhân|con\s+số)", "mở dàn cảnh: 'dưới đây là...'"),
    (r"(?i)trong\s+(thế\s+giới|kỷ\s+nguyên|thời\s+đại)\s+(kỹ\s+thuật\s+so|số\s+hóa|công\s+nghệ)[^.!?]{0,60}(ngày\s+nay|hôm\s+nay)", "mở sáo: 'trong thời đại công nghệ ngày nay'"),
    (r"(?i)trong\s+thời\s+đại\s+[^.,!?…\n]{1,40}\s+ngày\s+nay", "mở sáo tổng quát: 'trong thời đại X ngày nay' (phát hiện khi đọc tay README demo)"),
    (r"(?i)không\s+chỉ\s+[^.;!?]{1,80}?\s(mà\s+còn|mà\s+là|đó\s+là)", "tương phản bơm: 'không chỉ ... mà còn'"),
    (r"(?i)không\s+(đơn\s+thuần|phải\s+chỉ|đơn\s+giản\s+là)[^.;!?]{1,80}?\s(mà\s+(là|còn)|đó\s+là)", "tương phản bơm: 'không đơn thuần ... mà là'"),
    (r"(?i)^[^A-Za-z0-9]*(đó\s+(mới\s+)?là\s+(điều|điều\s+quan\s+trọng|câu\s+trả\s+lời|win))\s*[.!]?\s*$", "câu chốt một dòng nhại lại ý"),
    (r"(?i)(hãy\s+nghĩ\s+mà\s+xem|hãy\s+đọc\s+lại\s+câu\s+này)", "câu chốt kịch tính"),
    (r"—|–|\s--\s", "gạch ngang dài nối câu (em/en dash)"),
]

# P1 — từ vựng & khuôn khoa trương (quan sát thực hành nội địa + suy diễn có ghi
# rõ trong sources.md; CHƯA có thống kê tần suất công khai cho tiếng Việt)
P1_WORDS = [
    "tối ưu hóa", "nâng cao", "đột phá", "bứt phá", "tiềm năng to lớn",
    "đáng kinh ngạc", "không thể phủ nhận", "vượt trội", "toàn diện",
    "chuyên sâu", "hiện đại hóa", "cách mạng hóa", "kiến tạo", "tuyệt vời",
    "đỉnh cao", "nổi bật", "ấn tượng khó quên", "phong phú đa dạng",
    "đóng vai trò then chốt", "đánh dấu bước ngoặt", "mở ra kỷ nguyên",
    "kỷ nguyên mới", "tương lai tươi sáng", "hướng đi đúng đắn",
    "di sản bền vững", "sở hữu", "mang đến", "đáp ứng mọi nhu cầu",
    "giải pháp toàn diện", "trải nghiệm tuyệt vời", "nâng tầm",
    "bứt phá ngoạn mục", "vẻ đẹp tuyệt diệu", "tọa lạc giữa",
    "nơi hội tụ", "điểm đến lý tưởng", "quý khách", "quý đối tác",
    "hành trình đáng nhớ", "in đậm dấu ấn",
]

P1_PHRASE_STRUCT = [
    (r"(?i)đóng\s+vai\s+trò\s+(quan\s+trọng|then\s+chốt|chủ\s+chốt)", "né động từ 'là': 'đóng vai trò'"),
    (r"(?i)(được\s+xem\s+là|được\s+coi\s+là|hiện\s+diện\s+như\s+một)", "né động từ 'là'"),
    (r"(?i)(chuyên\s+gia\s+cho\s+rằng|các\s+nhà\s+nghiên\s+cứu\s+chỉ\s+ra|báo\s+cáo\s+ngành\s+chỉ\s+ra)", "mượn uy tín không tên"),
    (r"(?i)một\s+trong\s+những\s+[^.;!?]{1,60}?\s+nhất\s", "khuôn tối thượng: 'một trong những ... nhất'"),
    (r"(?i)(dù\s+(đối\s+mặt|gặp)\s*(một\s+số\s+|nhiều\s+)?thách\s+thức[^.!?]{0,100}?(vẫn|tiếp\s+tục)[^,.!?]{0,25}?(vươn\s+lên|phát\s+triển|thrive))", "khuôn 'dù thách thức ... vẫn vươn lên'"),
    (r"(?i)(qua\s+đó|nhằm\s+mục\s+đích)[^\n]{0,40}(khẳng\s+định|nhấn\s+mạnh|đề\s+cao|góp\s+phần)", "vế 'qua đó' cầm canh"),
    (r"(?i)về\s+lâu\s+dài[^.!?]{0,60}(vẫn\s+)?(xứng\s+đáng|đáng\s+giá|đáng\s+đồng)[^.!?]{0,30}(đầu\s+tư|khoản\s+đầu\s+tư)?", "ẩn dụ đầu tư: 'về lâu dài vẫn xứng đáng'"),
    (r"(?i)(khả\s+năng\s+(có\s+thể|nào\s+đó)|có\s+thể\s+nào\s+đó|một\s+cách\s+nào\s+đó)", "hạn định chất chồng"),
]

# P2 — biểu tượng trang trí, định dạng khuôn
P2_PATTERNS = [
    (r"(?i):?\s*(🚀|💡|✅|🎯|🔥|⭐|👉|✨)", "emoji trang trí"),
    (r"“|”", "ngoặc kép cong"),
    (r"(?i)^\s*(?:[-*]\s+)?\*\*[^*]{1,40}(\*\*:|:\*\*)", "nhãn in đậm + hai chấm mở câu"),
    (r";", "dấu chấm phẩy (rất hiếm trong văn người Việt)"),
    (r"(?i)\b(yêu\s+cầu\s+kéo|kho\s+mã\s+nguồn|thư\s+điện\s+tử|mạng\s+toàn\s+cầu)\b", "dịch thuật ngữ Anh phổ biến (giữ nguyên pull request, repo, email, web tự nhiên hơn)"),
    (r"^\s*-{3,}\s*$", "đường kẻ ngang ngăn phần"),
]

# ---------------------------------------------------------------------------
# Miễn trừ (học avoid-ai-writing applyExemptions): code, trích dẫn, bảng, link
# ---------------------------------------------------------------------------

def apply_exemptions(text: str) -> str:
    """Thay vùng miễn trừ bằng khoảng trắng, giữ độ dài dòng để số dòng không đổi."""
    def blank(m):
        return re.sub(r"[^\n]", " ", m.group(0))
    out = re.sub(r"```.*?```", blank, text, flags=re.S)
    out = re.sub(r"`[^`\n]*`", blank, out)
    out = re.sub(r"^\s*>.*$", blank, out, flags=re.M)          # blockquote
    out = re.sub(r"^\s*\|.*\|\s*$", blank, out, flags=re.M)   # bảng markdown
    out = re.sub(r'"[^"\n]{1,200}"', blank, out)              # trích dẫn trong ngoặc kép
    out = re.sub(r"(?<!\()https?://\S+", blank, out)           # URL
    return out

# ---------------------------------------------------------------------------
# Nhịp học (stylometry) — đối chiếu ViDetect 2405.03206: văn AI tiếng Việt
# có câu ít hơn, đoạn dài và đều hơn, kém bộc lộ cảm xúc
# ---------------------------------------------------------------------------

# Trợ từ cuối câu (Thompson 1965; Cao Xuân Hạo 1998): dấu khẩu ngữ tiếng Việt,
# đầu ra AI hầu như không dùng — tín hiệu NGƯỜI
FINAL_PARTICLES = {"nhé", "đấy", "đó", "cơ", "nhỉ", "ạ", "nghe", "nào", "thôi", "vậy"}
# Liên từ hình thức (sách vở) mà AI ưa
FORMAL_CONNECTIVES = ["ngoài ra", "bên cạnh đó", "hơn nữa", "thêm vào đó", "do đó",
                      "vì vậy", "bởi vậy", "do vậy", "ngoài việc", "đồng thời",
                      "trước hết", "tóm lại", "nhìn chung", "chung quy lại"]
# Từ nối khẩu ngữ mà người hay dùng
COLLOQUIAL_MARKERS = ["thế là", "cơ mà", "mà thôi", "thôi thì", "thật ra",
                      "tiện thể", "kiểu như", "rồi là", "à mà"]
# Động từ Hán Việt hành chính (mật độ cao = giọng công văn)
SINO_VERBS = ["triển khai", "ứng dụng", "giải pháp", "tiến hành", "đảm bảo",
              "tăng cường", "thúc đẩy", "quảng bá", "chủ trương", "phổ biến",
              "nâng cao", "thực hiện"]
STOP_ADJ = {"và", "của", "là", "một", "những", "các", "cho", "không", "có",
            "được", "với", "người", "bạn", "chúng", "ta", "nó", "họ", "anh",
            "chị", "em", "ông", "bà", "rất", "cũng", "đã", "sẽ", "vào", "ra"}

def _mattr(tokens, w=50):
    """MATTR (Covington & McFall 2010): TTR cửa sổ trượt, khống chế độ dài văn bản."""
    n = len(tokens)
    if n == 0:
        return 0.0
    if n <= w:
        return len(set(tokens)) / n
    vals = [len(set(tokens[i:i + w])) / w for i in range(n - w + 1)]
    return sum(vals) / len(vals)

def _skew(xs):
    """Hệ số lệch của phân bố độ dài câu (văn người thường lệch phải dương)."""
    n = len(xs)
    if n < 3:
        return 0.0
    mean = sum(xs) / n
    sd = math.sqrt(sum((x - mean) ** 2 for x in xs) / n)
    if sd == 0:
        return 0.0
    return sum(((x - mean) / sd) ** 3 for x in xs) / n

# Từ láy (Thompson 1965: đặc trưng hình thái tiếng Việt): người dùng giàu,
# AI gần như không sinh từ láy mới — tín hiệu NGƯỜI. Đếm bằng danh sách tuyển
# chọn để giữ độ chính xác (heuristic tự do bắn quá tay, xem methodology.md)
REDUP_LIST = [
    "lao xao", "lấp lánh", "lấp ló", "lom khom", "lũ lượt", "la liệt",
    "líu lo", "líu lưỡi", "lì lì", "rì rầm", "rộn ràng", "rạo rực",
    "run rẩy", "xào xạc", "sa sút", "lạnh lẽo", "rung rinh", "lắc lư",
    "mong manh", "mong ngóng", "mòn mỏi", "mỏi mòn", "sạch sẽ", "xinh xắn",
    "gọn gàng", "gầy gò", "gầy guộc", "ú ớ", "ấp úng", "nhấp nhô",
    "nhấp nháy", "với vã", "vội vàng", "méo mó", "lơ ngơ", "lấm lem",
    "lúng túng", "văng vẳng", "lè tẻ", "lê thê", "liu riu", "liu điu",
    "nhoè nhoẹt", "toe toé", "lù mù", "mù mịt", "mịt mù", "tù mù",
    "ủ rũ", "lung linh", "long lanh", "mơ màng", "mơ mộng", "thì thầm",
    "tí tách", "lách cách", "lạch cạch", "lục đục", "bâng khuâng",
    "lấp lửng", "lăn tăn", "lăn quay", "tím tái", "xanh xao", "trơn tru",
    "ấm áp", "náo nức", "nôn nao", "ngơ ngác", "ngẩn ngơ", "bồn chồn",
    "thấp thỏm", "thấp thoáng", "đông đúc", "chật chội",
]

def _reduplication(low_text):
    """Đếm từ láy xuất hiện trong văn bản (danh sách tuyển chọn)."""
    return sum(1 for w in set(REDUP_LIST) if w in low_text)

def _punct_entropy(text):
    counts = {}
    for ch in text:
        if ch in ".,!?;:…—-":
            counts[ch] = counts.get(ch, 0) + 1
    total = sum(counts.values())
    if total == 0:
        return 0.0
    return -sum((c / total) * math.log2(c / total) for c in counts.values())

def stylometry(text: str) -> dict:
    paras = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    sentences = [s.strip() for s in re.split(r"[.!?…]+", text) if s.strip()]
    lens = [len(s.split()) for s in sentences]
    plens = [len(p.split()) for p in paras]

    def cv(xs):
        if len(xs) < 2:
            return 0.0
        mean = sum(xs) / len(xs)
        if mean == 0:
            return 0.0
        var = sum((x - mean) ** 2 for x in xs) / len(xs)
        return math.sqrt(var) / mean

    words = re.findall(r"\w+", text.lower())
    ttr = len(set(words)) / len(words) if words else 0.0
    mattr = _mattr(words)
    bang = len(re.findall(r"!", text))
    sent_per_para = len(sentences) / len(paras) if paras else 0

    # Trợ từ cuối câu: từ cuối mỗi câu (bỏ dấu câu, ngoặc)
    particles = 0
    for s in sentences:
        ws = re.findall(r"\w+", s.lower())
        if ws and ws[-1] in FINAL_PARTICLES:
            particles += 1
    low = text.lower()
    formal = sum(low.count(c) for c in FORMAL_CONNECTIVES)
    colloq = sum(low.count(c) for c in COLLOQUIAL_MARKERS)
    sino = sum(low.count(v) for v in SINO_VERBS)
    per_k = lambda x: round(1000 * x / len(words), 1) if words else 0.0

    import zlib
    raw = text.encode("utf-8")
    gzip_ratio = round(len(zlib.compress(raw)) / len(raw), 3) if raw else 0.0

    return {
        "so_cau": len(sentences),
        "so_doan": len(paras),
        "cau_trung_binh_doan": round(sent_per_para, 2),
        "dai_cau_tb": round(sum(lens) / len(lens), 1) if lens else 0,
        "bien_dong_do_dai_cau_cv": round(cv(lens), 2),
        "lech_do_dai_cau_skew": round(_skew(lens), 2),
        "bien_dong_do_dai_doan_cv": round(cv(plens), 2),
        "ty_le_tu_rieng_ttr_am_tiet": round(ttr, 3),
        "mattr_cua_so_50": round(mattr, 3),
        "so_dau_bang_than": bang,
        "tro_tu_cuoi_cau": particles,
        "tro_tu_cuoi_cau_tren_1000": per_k(particles),
        "lien_tu_hinh_thuc": formal,
        "lien_tu_hinh_thuc_tren_1000": per_k(formal),
        "tu_noi_khau_ngu": colloq,
        "han_viet_hanh_chinh_tren_1000": per_k(sino),
        "tu_lay": _reduplication(low),
        "entropy_dau_cau_bit": round(_punct_entropy(text), 2),
        "do_nen_zlib": gzip_ratio,
        "canh_bao": [],
    }

def stylometry_warnings(m: dict) -> list:
    w = []
    # ViDetect: người viết nhiều câu hơn / đoạn ngắn hơn; AI: câu ít, đoạn dài đều
    if m["so_cau"] >= 12 and m["bien_dong_do_dai_cau_cv"] < 0.28:
        w.append("độ dài câu quá đều (CV < 0,28), thiếu 'burstiness' của văn người "
                 "[hiệu chỉnh pilot n=42: 0/21 văn người, 16/21 văn AI, AUC 0,99]")
    if m["so_doan"] >= 4 and m["bien_dong_do_dai_doan_cv"] < 0.25:
        w.append("độ dài đoạn quá đều (CV < 0,25), kết cấu khuôn")
    if m["so_cau"] >= 12 and m["cau_trung_binh_doan"] > 6:
        w.append("quá nhiều câu mỗi đoạn (> 6), dấu hiệu ViDetect: AI viết đoạn dài")
    if m["so_cau"] >= 12 and m["entropy_dau_cau_bit"] < 1.0:
        w.append("phân bố dấu câu nghèo (chủ yếu chấm + phẩy, entropy < 1,0 bit) "
                 "[pilot n=42: AUC 0,85, văn người md 1,33 / AI 0,99]")
    # Lưu ý: MATTR-50 KHÔNG dùng làm cảnh báo — pilot cho thấy hướng NGƯỢC
    # với suy đoán ban đầu (AI có MATTR cao hơn văn người: 0,92 so với 0,86)
    if m["so_dau_bang_than"] >= 3:
        w.append("dấu chấm than dàn trận (>= 3)")
    if (m["so_cau"] >= 12 and m["tro_tu_cuoi_cau"] == 0
            and m["lien_tu_hinh_thuc"] >= 3):
        w.append("không trợ từ cuối câu + nhiều liên từ hình thức: giọng sách vở "
                 "(hợp lệ với văn học thuật/formal, cân nhắc ngữ cảnh)")
    return w

# ---------------------------------------------------------------------------
# Quét
# ---------------------------------------------------------------------------

def scan(text: str) -> dict:
    clean = apply_exemptions(text)
    lines = clean.split("\n")
    hits = []

    def find_line(pos):
        return clean.count("\n", 0, pos) + 1

    for rx, label in P0_PATTERNS:
        for m in re.finditer(rx, clean, flags=re.M):
            hits.append({"muc": "P0", "dau_hieu": label,
                         "dong": find_line(m.start()),
                         "trich": m.group(0).strip()[:80]})
    for w in P1_WORDS:
        for m in re.finditer(re.escape(w), clean, flags=re.I):
            hits.append({"muc": "P1", "dau_hieu": f"từ vựng Tier: '{w}'",
                         "dong": find_line(m.start()),
                         "trich": m.group(0).strip()[:80]})
    for rx, label in P1_PHRASE_STRUCT:
        for m in re.finditer(rx, clean, flags=re.M):
            hits.append({"muc": "P1", "dau_hieu": label,
                         "dong": find_line(m.start()),
                         "trich": m.group(0).strip()[:80]})
    for rx, label in P2_PATTERNS:
        for m in re.finditer(rx, clean, flags=re.M):
            hits.append({"muc": "P2", "dau_hieu": label,
                         "dong": find_line(m.start()),
                         "trich": m.group(0).strip()[:80]})

    # Bộ ba: cụm "A, B và/plus C" gồm tính từ/danh từ dài tương đương
    for m in re.finditer(r"(\S+,{0,0}\S*)\s*,\s*(\S+)\s+(và|còn|hoặc)\s+(\S+)", clean):
        g = [m.group(1), m.group(2), m.group(4)]
        if all(len(x) >= 4 for x in g) and len(set(g)) == 3:
            hits.append({"muc": "P2", "dau_hieu": "nghi vấn bộ ba liệt kê",
                         "dong": find_line(m.start()),
                         "trich": m.group(0).strip()[:80]})

    # Mở câu lặp: >= 3 câu liên tiếp cùng từ mở đầu (bỏ qua ký hiệu đầu dòng)
    def first_word(s):
        s = re.sub(r"^[\s\-\*>#\d\.)\]]+", "", s)
        ws = s.split()
        return ws[0].lower() if ws else ""

    sent_spans = [(m.start(), m.group(0)) for m in re.finditer(r"[^.!?…\n]+", clean)]
    openers = []
    for pos, s in sent_spans:
        openers.append((find_line(pos), first_word(s)))
    run, prev = 1, ""
    for i in range(1, len(openers)):
        if openers[i][1] and openers[i][1] == openers[i - 1][1]:
            run += 1
            if run == 3:
                hits.append({"muc": "P1", "dau_hieu": f"mở câu lặp x3: '{openers[i][1]}'",
                             "dong": openers[i][0], "trich": ""})
        else:
            run = 1

    style = stylometry(clean)
    style["canh_bao"] = stylometry_warnings(style)

    weights = {"P0": 6, "P1": 3, "P2": 1}
    score = min(100, sum(weights[h["muc"]] for h in hits)
                + 4 * len(style["canh_bao"]))
    return {"score": score, "hits": hits, "nhip_hoc": style}

# ---------------------------------------------------------------------------
# Verify: bảo tồn vùng không được sửa (học detector/validate.js)
# ---------------------------------------------------------------------------

PROTECTED = [
    ("khối code", re.compile(r"```.*?```", re.S)),
    ("code inline", re.compile(r"`[^`\n]*`")),
    ("URL", re.compile(r"https?://\S+")),
    ("con số/ngày", re.compile(r"\d+([.,]\d+)*")),
    ("frontmatter", re.compile(r"^---.*?---", re.S | re.M)),
]

def verify(before: str, after: str) -> list:
    errors = []
    for name, rx in PROTECTED:
        b = sorted(m.group(0) for m in rx.finditer(before))
        a = sorted(m.group(0) for m in rx.finditer(after))
        if b != a:
            from collections import Counter
            cb, ca = Counter(b), Counter(a)
            lost = sorted((cb - ca).elements())
            added = sorted((ca - cb).elements())
            errors.append({"vung": name, "mat": lost[:5], "them": added[:5]})
    return errors

# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def read_input(path):
    if path and path != "-":
        with open(path, encoding="utf-8") as f:
            return f.read()
    return sys.stdin.read()

# ---------------------------------------------------------------------------
# Calibrate: đo khả năng phân tách người/AI của từng chỉ số trên corpus nhỏ
# (AUC theo Mann-Whitney, đồng hạng lấy hạng trung bình)
# ---------------------------------------------------------------------------

def _auc(pos, neg):
    """P(pos > neg) qua hạng trung bình; 0,5 = ngẫu nhiên."""
    if not pos or not neg:
        return None
    vals = [(v, 1) for v in pos] + [(v, 0) for v in neg]
    vals.sort(key=lambda x: x[0])
    ranks, i = [0.0] * len(vals), 0
    while i < len(vals):
        j = i
        while j + 1 < len(vals) and vals[j + 1][0] == vals[i][0]:
            j += 1
        avg = (i + j) / 2 + 1
        for k in range(i, j + 1):
            ranks[k] = avg
        i = j + 1
    sp = sum(r for r, (_, g) in zip(ranks, vals) if g == 1)
    np_, nn = len(pos), len(neg)
    u = sp - np_ * (np_ + 1) / 2
    return u / (np_ * nn)

def _file_metrics(path):
    text = open(path, encoding="utf-8").read()
    r = scan(text)
    m = r["nhip_hoc"]
    n = len(re.findall(r"\w+", apply_exemptions(text).lower())) or 1
    k = n / 1000
    return {
        "diem_scan": r["score"],
        "tro_tu_cuoi/1k": m["tro_tu_cuoi_cau"] / k,
        "lien_tu_hinh_thuc/1k": m["lien_tu_hinh_thuc"] / k,
        "tu_noi_khau_ngu/1k": m["tu_noi_khau_ngu"] / k,
        "han_viet/1k": m["han_viet_hanh_chinh_tren_1000"],
        "tu_lay/1k": m["tu_lay"] / k,
        "bang_than/1k": m["so_dau_bang_than"] / k,
        "MATTR50": m["mattr_cua_so_50"],
        "TTR_am_tiet": m["ty_le_tu_rieng_ttr_am_tiet"],
        "CV_do_dai_cau": m["bien_dong_do_dai_cau_cv"],
        "skew_do_dai_cau": m["lech_do_dai_cau_skew"],
        "CV_do_dai_doan": m["bien_dong_do_dai_doan_cv"],
        "cau/1doan": m["cau_trung_binh_doan"],
        "tu_trung_binh/câu": m["dai_cau_tb"],
        "entropy_dau_cau": m["entropy_dau_cau_bit"],
        "ty_le_nen_zlib": m["do_nen_zlib"],
    }

def cmd_calibrate(human_dir, ai_dir):
    from pathlib import Path
    hfiles = sorted(str(p) for p in Path(human_dir).rglob("*.txt"))
    afiles = sorted(str(p) for p in Path(ai_dir).rglob("*.md"))
    if not hfiles or not afiles:
        print(f"Thiếu corpus: người {len(hfiles)} file txt / AI {len(afiles)} file md")
        return 2
    hm = [_file_metrics(f) for f in hfiles]
    am = [_file_metrics(f) for f in afiles]
    print(f"corpus: {len(hm)} mẫu người ({human_dir}) vs {len(am)} mẫu AI ({ai_dir})")
    print(f"{'chỉ số':<22} {'AUC':>5} {'ng hướng':<10} {'md người':>9} {'md AI':>9}")
    print("-" * 62)
    rows = []
    for key in hm[0]:
        a = _auc([x[key] for x in am], [x[key] for x in hm])
        mh = sorted(x[key] for x in hm)[len(hm) // 2]
        ma = sorted(x[key] for x in am)[len(am) // 2]
        direction = "AI>ng" if a >= 0.5 else "ng>AI"
        rows.append((max(a, 1 - a), key, a, direction, mh, ma))
    for disp, key, a, direction, mh, ma in sorted(rows, reverse=True):
        print(f"{key:<22} {max(a, 1 - a):>5.3f} {direction:<10} {mh:>9.3f} {ma:>9.3f}")
    print("AUC > 0,5 = chỉ số cao hơn ở AI; in theo max(AUC, 1-AUC)")
    return 0

def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        return 0

    cmd = args[0]
    if cmd == "scan":
        path = args[1] if len(args) > 1 else "-"
        text = read_input(path)
        r = scan(text)
        if "--json" in args:
            print(json.dumps(r, ensure_ascii=False, indent=2))
            return 0
        print(f"ĐIỂM: {r['score']}/100 (0 = sạch dấu bề mặt)")
        order = {"P0": 0, "P1": 1, "P2": 2}
        for h in sorted(r["hits"], key=lambda x: (order[x["muc"]], x["dong"])):
            tr = f" — \"{h['trich']}\"" if h["trich"] else ""
            print(f"  [{h['muc']}] dòng {h['dong']}: {h['dau_hieu']}{tr}")
        if r["nhip_hoc"]["canh_bao"]:
            print("NHỊP HỌC:")
            for w in r["nhip_hoc"]["canh_bao"]:
                print(f"  [!] {w}")
        for k, v in r["nhip_hoc"].items():
            if k != "canh_bao":
                print(f"  {k}: {v}")
        return 0

    if cmd == "verify":
        if len(args) < 3:
            print("Cần 2 file: verify TRUOC SAU")
            return 2
        b = read_input(args[1])
        a = read_input(args[2])
        errs = verify(b, a)
        if not errs:
            print("OK: các vùng bảo tồn (code, URL, số liệu, frontmatter) nguyên vẹn.")
            return 0
        print("VI PHẠM BẢO TỒN:")
        for e in errs:
            print(f"  {e['vung']}: mất {e['mat']} / thêm {e['them']}")
        return 1

    if cmd == "selftest":
        dirty = ("Trong thời đại công nghệ số hóa ngày nay, hãy cùng tìm hiểu nhé! "
                 "Giải pháp của chúng tôi không chỉ là một công cụ, mà là một người bạn đồng hành, "
                 "được xem là bước đột phá, tối ưu hóa quy trình và mang đến trải nghiệm tuyệt vời. "
                 "Đó mới là điều quan trọng. Chúc bạn một ngày tốt lành!")
        clean = ("Công cụ này rút thời gian xử lý đơn từ 2 ngày xuống 20 phút. "
                 "Ba cửa hàng ở Hà Nội dùng thử hai tháng rồi ký hợp đồng. "
                 "Phí bản quyền 4 triệu đồng một tháng.")
        s_dirty, s_clean = scan(dirty)["score"], scan(clean)["score"]
        assert s_dirty > s_clean, f"selftest lỗi: {s_dirty} <= {s_clean}"
        print(f"selftest OK: văn AI-đậm score={s_dirty}, văn sạch score={s_clean}")
        return 0

    if cmd == "calibrate":
        if len(args) < 3:
            print("Cần 2 thư mục: calibrate THƯ_MỤC_NGƯỜI THƯ_MỤC_AI")
            return 2
        return cmd_calibrate(args[1], args[2])

    print(f"Lệnh không rõ: {cmd}")
    print(__doc__)
    return 2

if __name__ == "__main__":
    sys.exit(main())
