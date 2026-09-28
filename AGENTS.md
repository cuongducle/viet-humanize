# viet-humanize — bộ quy tắc viết tiếng Việt cho agent

Áp dụng tự động mỗi khi viết hoặc sửa văn xuôi tiếng Việt. Bản đầy đủ kèm nguồn trích dẫn: `SKILL.md` trong repo này.

## Nguyên tắc gốc

Viết như MỘT người Việt thật viết cho MỘT độc giả cụ thể. Mục tiêu là chất biên tập, không phải chạy điểm tool dò AI.

## P0, gặp là sửa

- Vỏ chatbot: "Chúc bạn một ngày tốt lành!", "Hy vọng thông tin này hữu ích!"
- Mở dàn cảnh: "Trong thời đại công nghệ số hóa ngày nay...", "Hãy cùng tìm hiểu nhé!"
- "không chỉ X mà còn Y" khi vế phủ định không mang thông tin
- Câu chốt một dòng nhại lại ý đoạn trên
- Gạch ngang dài nối câu (—, --)
- Mượn uy tín không tên: "chuyên gia cho rằng"

## P1, sửa khi cụm lại

- Từ khuôn: tối ưu hóa, đột phá, bứt phá, nâng tầm, trải nghiệm tuyệt vời, kiến tạo, mang đến
- Né động từ gốc: "đóng vai trò là", "được xem là", "sở hữu"
- Kết sáo: "tương lai tươi sáng", "chỉ có thời gian mới trả lời được"

## Đặc thù tiếng Việt

1. Giọng dịch: tránh "Nó là điều quan trọng cần được xem xét". Chủ ngữ sớm, động từ mạnh, tránh chuỗi danh từ hóa.
2. Xưng hô nhất quán một hệ (bạn / mình / tôi / anh chị), không lắc lư.
3. Đơn vị Việt Nam: dấu phẩy thập phân (9,81 triệu), "tệ" thay ¥/RMB.
4. Từ Anh thông dụng GIỮ NGUYÊN: skill, repo, commit, review, feedback, deadline, file, link. Địch "yêu cầu kéo", "thư điện tử".
5. Viết register chat (caption, reply): trợ từ cuối câu (nhé, đấy, đó, cơ, nhỉ, ạ) là dấu người thật ở câu ngắn; câu cộc xen dài bình thường; Hán Việt trừu tượng và phó từ cường độ kiểu sách vở gần như vắng; xưng hô theo quan hệ (mình, tui, tao, em).
6. Mỗi câu mới thêm fact, lý do, ví dụ, ngoại lệ hoặc hệ quả. Không tự chế ẩn dụ biên tập.

## Quy trình mỗi lần viết lại

1. Có repo này: chạy `python3 scripts/vi_scan.py scan FILE` (chỉ Python chuẩn).
2. Đọc toàn văn, đánh dấu theo mức trên.
3. Viết lại: giữ nguyên mọi số liệu, tên riêng, URL, code, trích dẫn.
4. Quét vòng 2 + đọc lại thành tiếng.
5. Sửa file thì chạy `python3 scripts/vi_scan.py verify TRUOC.md SAU.md` trước khi nộp.

## Trung thực

Skill không đảm bảo vượt qua detector. Không bịa số liệu, nguồn, trải nghiệm cá nhân. Điểm 0 trên máy quét không chứng minh văn là văn người.

Giữ bản này khớp với `SKILL.md` mỗi lần đổi quy tắc.
