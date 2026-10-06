# viet-humanize

Áp dụng khi viết hoặc biên tập tiếng Việt. Bản đầy đủ: [SKILL.md](SKILL.md).

## Nguyên tắc

- Làm đúng yêu cầu: viết, sửa, dịch, tóm tắt hoặc nhận xét. Không tự sửa chỉ vì người dùng dán văn bản vào.
- Xét mục đích, người đọc, quan hệ xưng hô và kênh sử dụng. Ưu tiên yêu cầu và mẫu giọng của người dùng; chưa rõ thì viết trung tính.
- Tự nhiên không đồng nghĩa với thân mật hoặc ngắn. Không áp giọng chat cho báo cáo, tài liệu chuyên môn hay sáng tác.
- Nếu văn bản đã phù hợp, giữ nguyên. Không bắt người dùng chọn chế độ.

## Khi viết và sửa

- Giữ dữ kiện, điều kiện, ngoại lệ, mức chắc chắn và quan hệ nguyên nhân. Không đổi “có thể” thành khẳng định chắc chắn.
- Giữ số liệu, đơn vị, tên riêng, nguồn và trích dẫn. Không thêm dữ kiện hoặc trải nghiệm để bài có vẻ thật hơn.
- Chỗ đáng ngờ thì nêu điều cần xác minh. Chỉ đổi nội dung khi được phép và có căn cứ.
- Chỉ sửa file trong phạm vi được giao. Giữ code, lệnh, URL, đường dẫn, cấu hình và cấu trúc bảng trừ khi được yêu cầu đổi.
- Làm rõ ý mơ hồ, sửa câu vòng vo và từ lệch nghĩa. Chỉ bỏ sự lặp không có tác dụng.
- Chọn từ theo nghĩa và người đọc, không cấm từ Hán Việt hoặc bắt dùng tiếng Anh. Giữ thuật ngữ cần chính xác.
- Xưng hô theo từng người nói và quan hệ. Giữ cảm xúc, phương ngữ, hình ảnh và nhịp có dụng ý.
- Không ép câu dài/ngắn, cắt mọi lời chào hoặc cấm một loại dấu câu. Trình bày theo nội dung và quy ước được yêu cầu.
- Không thêm lỗi, tiếng lóng, trợ từ hoặc từ láy để giả giọng người. Không tự đổi giá trị hay định dạng dữ liệu máy đọc.
- Sáng tác có thể hư cấu theo đề bài, nhưng không dùng hư cấu làm bằng chứng thực tế.

## Kiểm tra và trả kết quả

Đọc toàn văn trước khi sửa, rồi đối chiếu ý nghĩa và giọng với bản gốc. Với file hoặc bài dài, lưu bản trước và dùng công cụ nếu có Python. Đường dẫn tính từ thư mục cài skill:

```bash
python3 scripts/vi_scan.py scan FILE.md
python3 scripts/vi_scan.py verify TRUOC.md SAU.md
```

Quét trước/sau, rà từng khác biệt. Cờ của máy quét không phải lệnh xóa. `verify` so chuỗi số, URL, code và frontmatter, không kiểm được nghĩa câu. Không đổi bản gốc để làm kiểm tra đạt, không nói đã chạy bước chưa chạy. Câu trả lời ngắn chỉ cần đọc rà.

Trả đúng sản phẩm người dùng cần, không mặc định kèm bảng dấu hiệu hay giải thích dài. Chỉ ghi chú chỗ chưa chắc, thay đổi đáng kể hoặc giới hạn kiểm tra khi cần. Chỉ được nhờ kiểm tra thì chưa sửa.

Skill không phụ thuộc mô hình cụ thể. Không hứa vượt detector hoặc coi điểm quét thấp là chứng nhận chất lượng. Giữ bản này đồng bộ với `SKILL.md`.
