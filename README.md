# viet-humanize

[![License: MIT](https://img.shields.io/github/license/cuongducle/viet-humanize?style=flat-square)](LICENSE)
[![GitHub](https://img.shields.io/badge/github-cuongducle%2Fviet--humanize-111111?style=flat-square&logo=github)](https://github.com/cuongducle/viet-humanize)

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
git clone https://github.com/cuongducle/viet-humanize ~/.pi/agent/skills/viet-humanize
```

### Claude Code

```bash
git clone https://github.com/cuongducle/viet-humanize ~/.claude/skills/viet-humanize
```

Với Cursor hoặc agent khác, đặt thư mục này vào thư mục skill của công cụ. Sau khi cài, chỉ cần yêu cầu agent viết lại văn bản. Không cần chạy script để kích hoạt skill.

## Dùng ngay

Bạn có thể bắt đầu bằng một yêu cầu ngắn:

```text
Viết lại đoạn dưới cho tự nhiên, giữ nguyên số liệu và ý chính. Đừng thêm thông tin mới.
```

Có ba cách làm việc:

- **Viết lại.** Agent đọc toàn văn, sửa cách diễn đạt và tự kiểm tra lại.
- **Chỉ dò.** Gõ `chỉ dò:` nếu bạn muốn xem những chỗ đáng ngờ mà chưa muốn sửa.
- **Sửa file.** Nêu đường dẫn file nếu muốn agent sửa trực tiếp. Phần code, URL, bảng và số liệu được giữ lại rồi kiểm tra bằng `verify`.

## Skill thực sự sửa những gì?

### Bỏ lớp văn theo khuôn

Các câu như mở đầu dàn cảnh, lời chúc kiểu chatbot, câu kết nhắc lại cả đoạn và những cụm quảng cáo có thể làm bài mất giọng riêng. Skill không xóa chúng chỉ vì chúng nghe trang trọng. Nó xem chúng có cần thiết trong đúng ngữ cảnh hay không.

### Chọn từ gần với việc đang nói

Khi nghĩa không đổi, `giúp` thường nhẹ hơn `hỗ trợ`, `làm` thường rõ hơn `triển khai`, còn gọi lại tên người hoặc tên sản phẩm thường tốt hơn việc liên tục thay bằng những danh từ trừu tượng. Những từ tiếng Anh quen thuộc trong văn công nghệ như `skill`, `repo`, `commit`, `review`, `feedback` và `deadline` được giữ nguyên khi cách dùng đó tự nhiên.

### Đưa chủ thể và hành động trở lại câu

Mỗi đoạn nên cho người đọc biết nó đang nói về ai, vật gì hoặc việc gì. Câu tiếp theo cần thêm một dữ kiện, lý do, ví dụ, ngoại lệ hoặc hệ quả. Không dùng từ nối chỉ để che một mối liên hệ chưa được viết rõ.

### Giữ đúng giọng của loại văn

Một bài hướng dẫn kỹ thuật không cần giả giọng trò chuyện. Một bài blog không cần viết như thông cáo. Skill điều chỉnh mức độ khẩu ngữ, cách xưng hô và độ dài câu theo văn bản gốc, thay vì cố làm mọi bài có cùng một kiểu "tự nhiên".

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
- Đo thử trên corpus tiếng Việt có tách văn trang trọng và văn thân mật.

Trong pilot 42 mẫu, độ biến thiên của độ dài câu là tín hiệu tách nhóm tốt nhất. Ngược lại, điểm scan tổng hợp chỉ đạt AUC 0,529 trên văn bách khoa và báo chí, gần mức đoán ngẫu nhiên. Đây là lý do skill dùng máy quét để hỗ trợ biên tập, không dùng nó làm công cụ phát hiện AI.

Nguồn, cách lấy mẫu và các kết quả chi tiết nằm trong:

- [`references/methodology.md`](references/methodology.md)
- [`references/sources.md`](references/sources.md)
- [`references/calibration.md`](references/calibration.md)
- [`references/eval-v2.md`](references/eval-v2.md)
- [`references/eval-luna.md`](references/eval-luna.md)

## Điều skill không hứa

Skill không đảm bảo vượt qua một detector cụ thể. Nó không biến văn bản thành văn người bằng cách thêm lỗi chính tả hoặc tiếng lóng, cũng không tự bịa số liệu, nguồn, tên riêng hay trải nghiệm cá nhân. Một danh sách từ duy nhất cũng không thể áp dụng cho mọi kiểu văn.

Từ tháng 9/2026 corpus có thêm 44 bài Threads Việt Nam và 7 bộ trả lời. Trợ từ cuối câu xuất hiện ở 5/7 bộ trả lời và 13/44 bài dài phía người (tối đa 83 lần mỗi 1000 âm tiết) so với 1/18 bài AI, nên tín hiệu này chỉ dùng làm chỉ báo cho văn ngắn kiểu chat. Từ láy vẫn là gợi ý. Người viết vẫn cần đọc lại bản cuối và tự kiểm tra sự thật.

## Cấu trúc thư mục

| Đường dẫn | Vai trò |
|---|---|
| `SKILL.md` | Hướng dẫn đầy đủ cho agent |
| `scripts/vi_scan.py` | Máy quét, `verify`, `selftest` và `calibrate` |
| `references/patterns-full.md` | Danh mục dấu hiệu kèm ví dụ trước và sau |
| `references/sources.md` | Nguồn trích dẫn và khoảng trống nghiên cứu |
| `references/methodology.md` | Cách xây dựng skill theo từng ngôn ngữ |
| `corpus/` | Các tập văn dùng cho phép đo và kiểm tra |
| `research/` | Script thu thập và đánh giá corpus |

## Phát triển

Sau khi sửa máy quét, chạy:

```bash
python3 scripts/vi_scan.py selftest
python3 scripts/vi_scan.py scan README.md
git diff --check
```

Khi thêm một dấu hiệu mới, ghi lại ví dụ thật và nguồn trong `references/patterns-full.md`. Những giả thuyết chưa có dữ liệu tiếng Việt không nên được trình bày như quy tắc chắc chắn.

## Giấy phép

MIT.
