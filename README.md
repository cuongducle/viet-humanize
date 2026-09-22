# viet-humanize

AI viết tiếng Việt thường không sai. Vấn đề là nó **đúng theo một kiểu rất dễ nhận ra**: câu nào cũng tròn trịa, đoạn nào cũng đi cùng một nhịp, ý nào cũng được bọc trong lớp từ ngữ bóng bẩy.

viet-humanize là skill cho AI coding agent để gỡ lớp vỏ đó. Nó giúp agent biên tập tiếng Việt bớt đều, bớt sáo và gần với cách một người thật đang nghĩ, đang viết hơn. Số liệu vẫn giữ nguyên. URL và code cũng vậy.

Skill chạy được trên pi, Claude Code, Cursor, hoặc bất kỳ agent nào đọc được định dạng SKILL.md. Một đoạn văn có hệ số biến thiên quanh 0,2 thường đều hơn nhiều so với văn người, khoảng 0,43.

## Cài đặt

```
git clone https://github.com/cuongducle/viet-humanize ~/.pi/agent/skills/viet-humanize
```

Với Claude Code, đặt skill vào `~/.claude/skills/`. Cursor và các agent khác làm tương tự theo thư mục skill riêng.

## Nó làm gì với một đoạn văn?

Không phải cứ đổi vài từ là văn sẽ thành văn người. Skill đi qua một quy trình 5 bước:

- Máy quét tìm những dấu hiệu bề mặt.
- Đọc toàn văn, vì regex không hiểu ngữ cảnh.
- Viết lại cả nhịp câu lẫn cách chọn từ.
- Tự đọc lại để bắt những câu vẫn còn mùi khuôn mẫu.
- Lệnh verify đối chiếu số liệu, URL và code trước khi giao bản cuối.

Bước cuối khá quan trọng. Một bản rewrite nghe tự nhiên hơn nhưng làm mất một con số vẫn là bản rewrite hỏng.

## Ba cách dùng

- **Mặc định.** Dán văn cần sửa. Agent viết lại, scan vòng hai rồi chạy verify.
- **Chỉ dò.** Đặt chữ chỉ dò: ở đầu yêu cầu nếu bạn chỉ muốn thấy các dấu hiệu, chưa muốn sửa.
- **Sửa file tại chỗ.** Agent chỉnh trực tiếp file, trả kèm diff và kết quả verify.

Máy quét không cần thư viện ngoài Python chuẩn:

```
python3 scripts/vi_scan.py scan FILE.md
python3 scripts/vi_scan.py verify TRUOC.md SAU.md
python3 scripts/vi_scan.py selftest
python3 scripts/vi_scan.py calibrate corpus/human corpus/ai
```

## Một chút dữ liệu, và rất nhiều sự dè chừng

Pilot gồm 42 mẫu tiếng Việt: 21 mẫu từ Wikipedia và VnExpress, 21 mẫu do LLM viết.

| Chỉ số | AUC |
|---|---|
| CV độ dài câu | 0,991 |
| Mật độ động từ Hán Việt | 0,719 |
| TTR âm tiết | 0,943 |
| MATTR-50 | 0,910 |
| Entropy dấu câu | 0,848 |
| Điểm scan tổng hợp | 0,529 |

Ngưỡng 0,28 bắt được 16/21 mẫu AI và báo nhầm 0/21 mẫu văn người.

Ở tầng chọn từ, văn AI dùng các động từ Hán Việt trừu tượng đậm gấp 4 lần văn người: 10,4 so với 2,6 trên 1000 âm tiết. Vì thế skill không chỉ sửa những câu mở đầu sáo rỗng. Nó còn kéo bài viết về phía những động từ cụ thể hơn, những danh từ có điểm tựa hơn và một nhịp câu bớt đồng phục hơn.

Nhưng đây không phải bộ phát hiện AI. Điểm scan tổng hợp chỉ ngang tung đồng xu trên register bách khoa và báo chí. Máy quét chỉ là một người biên tập vòng đầu. Nó biết gõ cửa, không biết thay bạn phán xét cả bài.

Muốn tự chạy lại phép đo và xem các giới hạn, đọc references/calibration.md.

## Cấu trúc thư mục

| File | Nội dung |
|---|---|
| SKILL.md | quy trình 5 bước, 3 mức P0, P1, P2 và bảng dung sai theo loại văn |
| scripts/vi_scan.py | máy quét cùng các lệnh verify, selftest, calibrate |
| references/patterns-full.md | 30 dấu hiệu trước và sau, chia lớp A, B, C, kèm nguồn |
| references/sources.md | trích dẫn đầy đủ và những khoảng trống chưa kiểm chứng |
| references/methodology.md | khảo sát cách 4 skill humanize nước ngoài xây dựng quan sát |
| references/calibration.md | báo cáo pilot và các ngưỡng đã hiệu chỉnh |
| corpus/ và research/ | dữ liệu 42 mẫu cùng script thu thập để người khác kiểm tra lại |

## Nguồn và giới hạn

Danh sách dấu hiệu không xuất hiện từ trực giác của người viết. Nó lấy nền từ bài *Signs of AI writing* của Wikipedia và dự án WikiProject AI Cleanup, kế thừa phương pháp tự quét và đo sai báo của avoid-ai-writing (conorbronsdon), học quy trình bản địa hóa từng ngôn ngữ của jurigis, rồi đối chiếu với đặc trưng nhịp học trong bộ dữ liệu ViDetect (arXiv 2405.03206). Phần chọn từ tham khảo thêm Georgiou 2025 và Gude 2026 (arXiv 2605.06030).

Giới hạn lớn nhất hiện nằm ở register khẩu ngữ. Trợ từ cuối câu, từ láy và từ nối đời thường vẫn là giả thuyết, vì corpus pilot chưa có đủ văn thân mật để đo. Dùng skill cho blog hoặc mạng xã hội thì nên đọc phần giới hạn trong references/sources.md trước.

Một giới hạn khác cũng cần nói rõ: văn bản sạch dấu scanner chưa chắc đã là văn người. Người đọc vẫn là vòng kiểm tra cuối.

Giấy phép MIT.
