# viet-humanize

Skill cho AI coding agent: biên tập văn tiếng Việt cho bớt "giọng máy", mà không làm hỏng số liệu lẫn khối code. Chạy được trên pi, Claude Code, Cursor, hoặc bất kỳ agent nào đọc được định dạng SKILL.md.

Đầu ra LLM bằng tiếng Việt có thói quen khá dễ nhận. Câu dài đều như nhau (hệ số biến thiên quanh 0,2, trong khi văn người vào khoảng 0,43), xoay vòng từ đồng nghĩa thay vì lặp lại từ khoá, mở bài kiểu sáo rỗng, nhãn in đậm đóng vai đề mục. Skill dạy agent nhận các thói quen đó rồi sửa theo quy trình 5 bước: máy quét chạy một lượt, agent tự đọc một lượt nữa cho bắt thứ regex bỏ sót, viết lại cả câu lẫn cách chọn từ, cuối cùng kiểm tra xem số liệu lẫn khối code còn nguyên hay không.

## Cài đặt

```
git clone https://github.com/cuongducle/viet-humanize ~/.pi/agent/skills/viet-humanize
```

Với Claude Code, đặt vào `~/.claude/skills/`. Cursor và các agent khác làm tương tự theo thư mục skill riêng.

## Ba cách dùng

- Mặc định: dán văn cần sửa, agent viết lại rồi chạy verify để chứng minh mọi con số, URL, khối code còn nguyên.
- Đặt "chỉ dò:" đầu yêu cầu khi chỉ muốn danh sách dấu hiệu, chưa cần sửa.
- Sửa file tại chỗ: agent chỉnh trực tiếp rồi trả kèm diff và kết quả verify.

Máy quét chạy độc lập, chỉ cần Python chuẩn, không cài thêm gì:

```
python3 scripts/vi_scan.py scan FILE.md
python3 scripts/vi_scan.py verify TRUOC.md SAU.md
python3 scripts/vi_scan.py selftest
python3 scripts/vi_scan.py calibrate corpus/human corpus/ai
```

## Số liệu đo được

Pilot 42 mẫu tiếng Việt (21 văn người lấy từ Wikipedia và VnExpress, 21 văn do LLM viết):

| Chỉ số | AUC |
|---|---|
| CV độ dài câu | 0,991 |
| Mật độ động từ Hán Việt | 0,719 |
| TTR âm tiết | 0,943 |
| MATTR-50 | 0,910 |
| Entropy dấu câu | 0,848 |
| Điểm scan tổng hợp | 0,529 |

Ngưỡng 0,28 bắt 16/21 văn AI với 0/21 sai báo trên văn người. Về chọn từ: văn AI dùng động từ Hán Việt trừu tượng kiểu triển khai, tối ưu đậm gấp 4 lần văn người, 10,4 so với 2,6 trên 1000 âm tiết, nên phần hướng dẫn biên tập cũng dạy cách cắt bớt chúng. Cần nói thẳng một điều: điểm scan tổng hợp chỉ ngang tung đồng xu trên register bách khoa và báo chí. Máy quét là công cụ biên tập bề mặt, không phải bộ phát hiện AI. Muốn tự chạy lại phép đo và xem hết hạn chế của nó, đọc references/calibration.md.

## Cấu trúc

| File | Nội dung |
|---|---|
| SKILL.md | quy trình 5 bước, 3 mức nghiêm trọng P0, P1, P2, bảng mức chấp nhận theo loại văn |
| scripts/vi_scan.py | máy quét kèm verify, selftest, calibrate |
| references/patterns-full.md | 30 dấu hiệu trước/sau, chia lớp A/B/C kèm nguồn từng dấu |
| references/sources.md | trích dẫn đầy đủ cùng các khoảng trống chưa kiểm chứng |
| references/methodology.md | khảo sát cách 4 skill humanize nước ngoài xây dựng quan sát |
| references/calibration.md | báo cáo pilot và các ngưỡng đã hiệu chỉnh |
| corpus/ và research/ | dữ liệu 42 mẫu cùng script thu thập, để ai cũng kiểm tra lại được |

## Nguồn và giới hạn

Danh sách dấu hiệu không tự bịa ra. Nó đồng bộ tư tưởng với bài "Signs of AI writing" của Wikipedia (dự án WikiProject AI Cleanup), kế thừa phương pháp tự quét và đo sai báo của avoid-ai-writing (conorbronsdon), quy trình bản địa hóa từng ngôn ngữ của jurigis, và các đặc trưng nhịp học từ bộ dữ liệu ViDetect (arXiv 2405.03206), cộng thêm so sánh từ vựng theo Georgiou 2025 và Gude 2026 (arXiv 2605.06030).

Giới hạn lớn nhất hiện nằm ở register khẩu ngữ: trợ từ cuối câu, từ láy, từ nối đời thường vẫn là suy diễn, vì corpus pilot chưa có văn thân mật để đo. Dùng skill cho blog, mạng xã hội thì nên đọc kỹ phần hạn hạn chế trong references/sources.md trước.

Giấy phép MIT.
