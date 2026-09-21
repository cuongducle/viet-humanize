# Rewrite eval GPT Luna (2026-09-21)

## Thiết kế

- Model hiện tại: `gpt-5.6-luna`.
- 10 mẫu văn thô được viết ở chế độ mặc định, không áp dụng skill.
- 10 mẫu được viết lại bằng quy trình trong `SKILL.md`: scan, đọc tay, viết lại, scan vòng 2, verify.
- Nội dung gồm blog công nghệ, GitHub Actions, app, bảo mật, du lịch, marketing, tài chính, review phim, API và review quán.
- Mỗi mẫu có số liệu, URL hoặc code để kiểm tra bảo toàn.
- Đây là test dogfood có cùng ngữ cảnh dự án, chưa phải blind test với người chấm độc lập.

## Kết quả

| mẫu | trước | sau |
|---|---:|---:|
| cloud shop | 45 | 0 |
| GitHub Actions | 9 | 0 |
| NoteBox | 15 | 0 |
| password manager | 18 | 0 |
| Đà Lạt | 27 | 0 |
| AI caption | 6 | 0 |
| ngân sách cá nhân | 12 | 0 |
| review phim | 18 | 0 |
| API retry | 21 | 0 |
| quán cà phê | 19 | 0 |
| **trung bình** | **19,0** | **0,0** |

- Scan: 10/10 bản rewrite đạt 0/100 dấu hiệu bề mặt.
- Verify: 10/10 đạt; số, URL và code được bảo toàn.
- Tác động điểm: giảm 19 điểm trung bình mỗi mẫu.

## Lỗi thật mà quy trình bắt được

Lần verify đầu tiên thất bại 4/10 mẫu:

1. GitHub Actions làm mất một lần xuất hiện của số `9` và số `5`.
2. Password manager làm mất số `3` trong mô tả quy trình.
3. AI caption lặp thêm số `4` khi viết lại.
4. API retry làm mất `100`, đồng thời thêm một số `3` và inline code mới.

Sau khi sửa, verify đạt 10/10. Vòng đọc tay thứ hai còn bắt bốn dấu chấm phẩy và cụm `chuyên sâu`, rồi loại bỏ hết.

## Kết luận

Skill hiện làm tốt việc biến văn Luna có nhiều dấu AI bề mặt thành bản sạch hơn mà không làm mất dữ kiện được kiểm tra. Tuy nhiên, điểm 0 chỉ chứng minh đã hết các dấu hiệu scanner biết; chưa chứng minh người đọc sẽ thích bản viết lại hơn. Bước tiếp theo vẫn là đánh giá mù với người Việt thật và kiểm tra tính đúng đắn nội dung.
