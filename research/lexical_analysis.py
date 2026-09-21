#!/usr/bin/env python3
"""Phân tích chọn từ: human vs AI trên corpus pilot (n=42).
- tỷ lệ từ chức năng (Georgiou 2025: người > AI)
- fightin' words: log-odds z-score (Monroe et al. 2008) từng âm tiết
- mật độ động từ Hán Việt, phó từ cường độ
Hạn chế: corpus người và AI khác chủ đề từng bài (chỉ khớp thể loại), nên danh sách từ đơn lẻ bị nhiễu chủ đề; chỉ các chỉ số mật độ/tỷ lệ mức văn phong là tương đối an toàn.
Chạy: python3 research/lexical_analysis.py
"""
import glob, math, re, sys
from collections import Counter

FUNCTION = set("""của và là có các những được cho với ở một này đó khi nếu nhưng mà thì
bằng từ về không cũng đã sẽ đang còn ra vào lên như để do bị tại trên dưới sau trước
hay hoặc vì nào cả lại đều vừa mới hơn nhất rất khá chỉ ngay mỗi vài
từng cùng trong ngoài giữa đến tới theo""".split())

INTENSIFIERS = ["rất", "khá", "vô cùng", "cực kỳ", "đặc biệt", "hoàn toàn", "chủ yếu",
                "tuyệt đối", "rõ ràng", "hết sức", "cực", "siêu"]
SINO_VERBS = ["triển khai", "tối ưu", "nâng cao", "đẩy mạnh", "tăng cường", "quản lý",
              "phát triển", "cung cấp", "hỗ trợ", "đảm bảo", "khắc phục", "nghiên cứu",
              "đánh giá", "xây dựng", "thực hiện", "tạo điều kiện", "hợp tác", "đầu tư",
              "cải thiện", "bảo vệ", "thúc đẩy", "khám phá", "khai thác", "ứng phó"]


def toks(path):
    t = open(path, encoding="utf-8").read()
    t = re.sub(r"```.*?```", " ", t, flags=re.S)
    t = re.sub(r"<[^>]+>", " ", t)
    return re.findall(r"[0-9a-zA-ZàáạảãâầấậẩẫăằắặẳẵèéẹẻẽêềếệểễìíịỉĩòóọỏõôồốộổỗơờớợởỡùúụủũưừứựửữỳýỵỷỹđĐ]+", t.lower())


def dens(words, phrases, per=1000):
    s = " ".join(words); n = len(words)
    return per * sum(s.count(p) for p in phrases) / max(n, 1)


def auc(xs, ys):  # Mann-Whitney, tie-averaged; xs = human, ys = ai
    vals = [(x, 0) for x in xs] + [(y, 1) for y in ys]
    vals.sort(key=lambda v: v[0])
    ranks, i = [], 0
    while i < len(vals):
        j = i
        while j < len(vals) and vals[j][0] == vals[i][0]: j += 1
        r = (i + j + 1) / 2
        ranks.extend([r] * (j - i)); i = j
    r1 = sum(r for r, g in zip(ranks, [v[1] for v in vals]) if g)
    n1, n0 = len(ys), len(xs)
    return (r1 - n1 * (n1 + 1) / 2) / (n1 * n0)


def main():
    H = sorted(glob.glob("corpus/human/**/*.txt", recursive=True))
    A = sorted(glob.glob("corpus/ai/**/*.md", recursive=True))
    th, ta = [toks(p) for p in H], [toks(p) for p in A]

    fh = [sum(1 for w in t if w in FUNCTION) / len(t) for t in th]
    fa = [sum(1 for w in t if w in FUNCTION) / len(t) for t in ta]
    print(f"tỷ_lệ_từ_chức_năng: người median {sorted(fh)[len(fh)//2]:.3f}, AI {sorted(fa)[len(fa)//2]:.3f}, AUC={auc(fh, fa):.3f}")

    sh = [dens(t, SINO_VERBS) for t in th]; sa = [dens(t, SINO_VERBS) for t in ta]
    print(f"hán_việt_động_từ/1000: người {sorted(sh)[len(sh)//2]:.1f}, AI {sorted(sa)[len(sa)//2]:.1f}, AUC={auc(sh, sa):.3f}")
    ih = [dens(t, INTENSIFIERS) for t in th]; ia = [dens(t, INTENSIFIERS) for t in ta]
    print(f"phó_từ_cường_độ/1000: người {sorted(ih)[len(ih)//2]:.1f}, AI {sorted(ia)[len(ia)//2]:.1f}, AUC={auc(ih, ia):.3f}")

    ch = Counter(w for t in th for w in t); ca = Counter(w for t in ta for w in t)
    nh, na = sum(ch.values()), sum(ca.values())
    bg = ch + ca; nb = nh + na; alpha0 = 100.0
    vocab = {w: alpha0 * c / nb for w, c in bg.items()}

    def z(w):
        a_w, b_w = ca.get(w, 0), ch.get(w, 0); al = vocab.get(w, 0.5)
        d = math.log((a_w + al) / (na + alpha0 - a_w - al)) - math.log((b_w + al) / (nh + alpha0 - b_w - al))
        return d / math.sqrt(1/(a_w + al) + 1/(b_w + al) + 1/(na - a_w) + 1/(nh - b_w))

    top_ai = sorted(((z(w), w) for w in bg if ca.get(w, 0) >= 4), reverse=True)[:22]
    top_hu = sorted(((z(w), w) for w in bg if ch.get(w, 0) >= 4))[:22]
    print("\n== AI DÙNG NHIỀU HƠN (z>0) ==")
    for zv, w in top_ai: print(f"  {w:<16} z={zv:+.1f} (AI {ca.get(w,0)} vs người {ch.get(w,0)})")
    print("== NGƯỜI DÙNG NHIỀU HƠN (z<0) ==")
    for zv, w in top_hu: print(f"  {w:<16} z={zv:+.1f} (người {ch.get(w,0)} vs AI {ca.get(w,0)})")


if __name__ == "__main__":
    main()
