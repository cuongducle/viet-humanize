<p align="center"><img src="assets/banner.svg" alt="viet-humanize" width="640"></p>

# viet-humanize

[![License: MIT](https://img.shields.io/github/license/cuongducle/viet-humanize?style=flat-square)](LICENSE)
[![GitHub](https://img.shields.io/github/stars/cuongducle/viet-humanize?style=flat-square&color=111111)](https://github.com/cuongducle/viet-humanize)
[![Works with](https://img.shields.io/badge/works%20with-pi%20%C2%B7%20Claude%20Code%20%C2%B7%20Codex%20%C2%B7%20any%20agent-111111?style=flat-square)](#install)
[![Trendshift](https://trendshift.io/repositories/cuongducle/viet-humanize/badge)](https://trendshift.io/repositories/cuongducle/viet-humanize)

**Make your agent write Vietnamese like a person, not a press release.**

viet-humanize is a skill for AI coding agents that edits AI-flavored Vietnamese into natural prose. It installs in one line and applies itself whenever the agent writes or revises Vietnamese text — no modes to pick, no commands to remember.

Why it is different from a prompt wrapper:

- **Evidence, not vibes.** The rulebook is calibrated against 119 real human texts: 77 live Threads posts across 19 everyday topics, plus Wikipedia and news articles. Every signal carries a source label; the eval reports (including the negative results) ship with the repo.
- **Numbers survive the rewrite.** A deterministic `verify` step checks that figures, URLs, and code from the original are intact before anything is returned.
- **Register-aware, measured.** Formal prose and casual chat get different rules — because the corpus says so. The sentence-rhythm threshold that separates AI from human in formal writing is useless in chat (AUC 0.51 there); forcing one style everywhere would be wrong.
- **Honest about what it is not.** It is an editor, not an AI detector or a "beat Turnitin" tool. The repo publishes the measurements that prove surface scanners can barely detect AI text (AUC 0.53–0.72).

**Before**

> Trong thời đại công nghệ số hóa ngày nay, việc quản lý kho hàng đã trở thành bài toán quan trọng đối với các doanh nghiệp. Hãy cùng tìm hiểu giải pháp giúp doanh nghiệp không chỉ tối ưu hóa quy trình, mà còn nâng tầm trải nghiệm khách hàng.

**After**

> Kho 500 mét vuông của công ty dệt Phương Đông từng mất ba ngày để kiểm kê cuối tháng. Sau ba tháng dùng phần mềm X, họ kiểm kê xong trong một buổi sáng.

## Install

| Agent | How |
|---|---|
| **pi** | `pi install git:github.com/cuongducle/viet-humanize` |
| **Claude Code** | `/plugin marketplace add cuongducle/viet-humanize` then `/plugin install viet-humanize@viet-humanize` |
| **Codex** | `codex plugin marketplace add cuongducle/viet-humanize` then `codex plugin add viet-humanize@viet-humanize` |
| **Any other agent** | Copy `AGENTS.md` into your project rules, or point your skill loader at `SKILL.md` |

After installing, just ask: *"Viết lại đoạn này cho tự nhiên, giữ nguyên số liệu."*

The scanner needs nothing beyond Python's standard library:

```bash
python3 scripts/vi_scan.py scan FILE.md     # 0-100 surface score + rhythm metrics
python3 scripts/vi_scan.py verify A.md B.md # numbers/URLs/code preserved?
python3 scripts/vi_scan.py selftest
```

## How it works

1. Deterministic scanner flags surface patterns (bot openers, "không chỉ... mà còn", marketing vocabulary, even rhythm).
2. The agent reads the whole text and marks by severity P0/P1/P2 — regex cannot judge context; a human-style read can.
3. Rewrite: every claim, number, name, and quote survives; sentences vary in length; the register of the original is kept (a tech doc is not forced into slang, a Threads caption is not forced into officialese).
4. Second pass: re-scan plus read-aloud for the five classic survivors.
5. File edits run `verify` before delivery.

Full rulebook with sources and before/after examples: [`SKILL.md`](SKILL.md) · [`references/patterns-full.md`](references/patterns-full.md) · eval reports in [`references/`](references/).

## Numbers

| Signal (human vs same-topic AI) | AUC | Note |
|---|---:|---|
| zlib compression ratio — chat register | 0.920 | stable across 3 sample sizes |
| Abstract Sino-Vietnamese verbs | 0.762 | humans: 0/1000 in chat |
| Final particles (ạ, nhé, đấy, cơ...) | present/absent | 27/77 human posts vs 3/30 AI |
| Combined surface score | 0.53–0.72 | hence: an editor, not a detector |

Corpus: 119 human texts + 59 paired AI texts. Collected with a real logged-in browser from public Vietnamese Threads, with anonymization; cross-checked against ViHSD (16,319 real comments). Methodology in [`references/eval-threads.md`](references/eval-threads.md).

## License

MIT.

---

# Bản tiếng Việt

## Viết tiếng Việt như một người đang nói điều mình hiểu

`viet-humanize` là skill cho AI coding agent. Nó giúp viết lại tiếng Việt cho tự nhiên hơn, nhưng không biến mọi bài thành cùng một giọng.

Skill giữ nguyên thông tin của bản gốc, rồi xem lại ba thứ thường làm văn AI lộ ra:

- Cách chọn từ, nhất là từ Hán Việt trừu tượng và lối dịch từng chữ.
- Nhịp câu, độ dài đoạn và những câu mở hoặc câu chốt theo khuôn.
- Mạch ý, tức là câu sau đang thêm thông tin hay chỉ nối vào câu trước bằng một từ nghe có vẻ mạch lạc.

Mục tiêu là một bản viết rõ người viết, đúng ngữ cảnh và dễ đọc. Điểm của công cụ dò AI không phải mục tiêu của skill.

## Cài đặt

### Pi

```bash
pi install git:github.com/cuongducle/viet-humanize
```

### Claude Code

```
/plugin marketplace add cuongducle/viet-humanize
/plugin install viet-humanize@viet-humanize
```

### Codex

```bash
codex plugin marketplace add cuongducle/viet-humanize
codex plugin add viet-humanize@viet-humanize
```

Với Cursor, Windsurf, Cline hoặc agent khác, chép `AGENTS.md` vào rules của dự án hoặc trỏ skill loader tới `SKILL.md`. Sau khi cài, chỉ cần yêu cầu agent viết lại văn bản; không cần chạy script để kích hoạt.

## Dùng ngay

Bạn có thể bắt đầu bằng một yêu cầu ngắn:

```text
Viết lại đoạn dưới cho tự nhiên, giữ nguyên số liệu và ý chính. Đừng thêm thông tin mới.
```

Không cần chọn chế độ hay gõ lệnh đặc biệt. Agent tự áp dụng skill mỗi khi viết hoặc sửa văn tiếng Việt: dán văn vào là được viết lại kèm bảng dấu đã sửa; nêu đường dẫn file là agent sửa trực tiếp (phần code, URL, bảng, số liệu giữ nguyên và kiểm bằng `verify`); hỏi "kiểm tra" thì nhận danh sách chỗ đáng ngờ mà chưa sửa gì.

## Skill thực sự sửa những gì?

### Bỏ lớp văn theo khuôn

Các câu như mở đầu dàn cảnh, lời chúc kiểu chatbot, câu kết nhắc lại cả đoạn và những cụm quảng cáo có thể làm bài mất giọng riêng. Skill không xóa chúng chỉ vì chúng nghe trang trọng. Nó xem chúng có cần thiết trong đúng ngữ cảnh hay không.

### Chọn từ gần với việc đang nói

Khi nghĩa không đổi, `giúp` thường nhẹ hơn `hỗ trợ`, `làm` thường rõ hơn `triển khai`, còn gọi lại tên người hoặc tên sản phẩm thường tốt hơn việc liên tục thay bằng những danh từ trừu tượng. Những từ tiếng Anh quen thuộc trong văn công nghệ như `skill`, `repo`, `commit`, `review`, `feedback` và `deadline` được giữ nguyên khi cách dùng đó tự nhiên.

### Đưa chủ thể và hành động trở lại câu

Mỗi đoạn nên cho người đọc biết nó đang nói về ai, vật gì hoặc việc gì. Câu tiếp theo cần thêm một dữ kiện, lý do, ví dụ, ngoại lệ hoặc hệ quả. Không dùng từ nối chỉ để che một mối liên hệ chưa được viết rõ.

### Giữ đúng giọng của loại văn

Một bài hướng dẫn kỹ thuật không cần giả giọng trò chuyện. Một bài blog không cần viết như thông cáo. Skill điều chỉnh mức độ khẩu ngữ, cách xưng hô và độ dài câu theo văn bản gốc, thay vì cố làm mọi bài có cùng một kiểu "tự nhiên".

### Viết register chat có số liệu riêng

Từ corpus 77 bài Threads thật: trợ từ cuối câu là dấu người thật ở câu ngắn, câu cộc xen dài là bình thường, Hán Việt trừu tượng và phó từ cường độ kiểu sách vở gần như vắng. Chi tiết trong `references/eval-threads.md`.

## Ví dụ ngắn

**Trước**

> Trong thời đại công nghệ số hóa ngày nay, phần mềm X không chỉ tối ưu hóa quy trình mà còn nâng tầm trải nghiệm khách hàng.

**Sau**

> Phần mềm X giúp quy trình gọn hơn. Khách hàng cũng dễ sử dụng hơn.

Bản sau không phải công thức thay thế máy móc. Nếu bản gốc có số liệu, điều kiện hoặc giới hạn, những thông tin đó phải được giữ trong bản rewrite.

## Quy trình năm bước

1. Máy quét rà các dấu hiệu bề mặt.
2. Agent đọc cả văn bản, không sửa theo danh sách từ một cách mù quáng.
3. Agent viết lại câu, đoạn và cách triển khai ý.
4. Agent đọc lại một lượt để bắt những chỗ máy quét bỏ sót.
5. Agent chạy vòng kiểm tra cuối nếu đang sửa file.

Vòng đọc tay rất quan trọng. Máy quét có thể nhận ra một cụm quen thuộc, nhưng không biết một câu có đúng giọng người viết hay đang dùng một ẩn dụ nghe gượng.

## Máy quét đi kèm

`vi_scan.py` là công cụ rà bề mặt, không phải bộ phán đoán tác giả. Nó không cần thư viện ngoài Python:

```bash
python3 scripts/vi_scan.py scan README.md
python3 scripts/vi_scan.py verify TRUOC.md SAU.md
python3 scripts/vi_scan.py selftest
python3 scripts/vi_scan.py calibrate corpus/human corpus/ai
```

`verify` giúp phát hiện việc làm mất số, URL hoặc code khi viết lại. `selftest` kiểm tra máy quét có còn hoạt động. `calibrate` dùng corpus đi kèm để xem tín hiệu nào có ích trong đúng bộ dữ liệu đó.

Điểm 0 chỉ có nghĩa là máy quét không thấy những dấu hiệu đã được lập danh mục. Nó không chứng minh văn bản là văn người.

## Cơ sở và mức độ tin cậy

Danh mục của skill được xây dựng từ bốn hướng:

- Các dấu hiệu do WikiProject AI Cleanup duy trì trong bài *Signs of AI writing*.
- Nghiên cứu ViDetect trên 6.800 bài luận tiếng Việt.
- Nguồn tiếng Việt từ báo chí, giáo viên và người làm nội dung.
- Đo thử trên corpus tiếng Việt có tách văn trang trọng và văn thân mật, gồm cả 77 bài Threads thật.

Trong pilot 42 mẫu, độ biến thiên của độ dài câu là tín hiệu tách nhóm tốt nhất. Ngược lại, điểm scan tổng hợp chỉ đạt AUC 0,529 trên văn bách khoa và báo chí, gần mức đoán ngẫu nhiên. Đây là lý do skill dùng máy quét để hỗ trợ biên tập, không dùng nó làm công cụ phát hiện AI.

Nguồn, cách lấy mẫu và các kết quả chi tiết nằm trong:

- [`references/methodology.md`](references/methodology.md)
- [`references/sources.md`](references/sources.md)
- [`references/calibration.md`](references/calibration.md)
- [`references/eval-v2.md`](references/eval-v2.md)
- [`references/eval-luna.md`](references/eval-luna.md)
- [`references/eval-threads.md`](references/eval-threads.md)

## Điều skill không hứa

Skill không đảm bảo vượt qua một detector cụ thể. Nó không biến văn bản thành văn người bằng cách thêm lỗi chính tả hoặc tiếng lóng, cũng không tự bịa số liệu, nguồn, tên riêng hay trải nghiệm cá nhân. Một danh sách từ duy nhất cũng không thể áp dụng cho mọi kiểu văn.

Trợ từ cuối câu xuất hiện ở 7/12 bộ trả lời và 27/77 bài dài phía người so với 3/30 bài AI, nên tín hiệu này chỉ dùng làm chỉ báo cho văn ngắn kiểu chat. Từ láy vẫn là gợi ý. Người viết vẫn cần đọc lại bản cuối và tự kiểm tra sự thật.

## Cấu trúc thư mục

| Đường dẫn | Vai trò |
|---|---|
| `SKILL.md` | Hướng dẫn đầy đủ cho agent |
| `AGENTS.md` | Bộ quy tắc gọn cho agent đọc rules dự án |
| `scripts/vi_scan.py` | Máy quét, `verify`, `selftest` và `calibrate` |
| `references/patterns-full.md` | Danh mục dấu hiệu kèm ví dụ trước và sau |
| `references/sources.md` | Nguồn trích dẫn và khoảng trống nghiên cứu |
| `references/methodology.md` | Cách xây dựng skill theo từng ngôn ngữ |
| `references/eval-threads.md` | Đo register chat trên corpus Threads |
| `corpus/` | Các tập văn dùng cho phép đo và kiểm tra |
| `research/` | Script thu thập và đánh giá corpus |

## Phát triển

Sau khi sửa máy quét, chạy:

```bash
python3 scripts/vi_scan.py selftest
python3 scripts/vi_scan.py scan README.md
git diff --check
```

Khi thêm một dấu hiệu mới, ghi lại ví dụ thật và nguồn trong `references/patterns-full.md`. Những giả thuyết chưa có dữ liệu tiếng Việt không nên được trình bày như quy tắc chắc chắn. Đổi quy tắc trong `SKILL.md` thì cập nhật luôn `AGENTS.md` để hai bản không lệch nhau.

## Giấy phép

MIT.

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=cuongducle/viet-humanize&type=Date)](https://www.star-history.com/chart#cuongducle/viet-humanize&Date)
