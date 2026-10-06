---
name: viet-humanize
description: 'Viết và biên tập tiếng Việt theo mục đích, người đọc và giọng của người dùng. Tự áp dụng khi soạn hoặc sửa câu trả lời, tin nhắn, email, bài viết, tài liệu, báo cáo, bản dịch và nội dung sáng tạo. Dùng khi muốn viết tự nhiên, rõ ý, bớt sáo hoặc giữ giọng riêng. Có công cụ rà văn bản và kiểm tra bảo toàn dữ kiện.'
license: MIT
metadata:
  version: "1.8.0"
---

# viet-humanize

Viết phù hợp với việc người dùng đang làm. Tự nhiên không đồng nghĩa với thân mật, ngắn hoặc ít từ Hán Việt. Không áp một giọng cho mọi loại văn.

## Áp dụng trong lúc làm việc

Không yêu cầu chọn chế độ hay nhắc tên skill. Làm đúng yêu cầu: viết, sửa, dịch, tóm tắt hoặc nhận xét. Không tự viết lại chỉ vì người dùng dán văn bản vào.

Ưu tiên yêu cầu cụ thể và mẫu giọng của người dùng hơn gợi ý văn phong ở đây. Khi đoạn văn đã phù hợp, giữ nguyên.

## Hiểu ngữ cảnh

Tự xác định mục đích, người đọc, quan hệ xưng hô, kênh sử dụng và phạm vi được sửa. Chỉ hỏi khi thiếu thông tin có thể làm sai nội dung hoặc giọng. Chưa rõ thì dùng tiếng Việt trung tính, rõ nghĩa.

| Ngữ cảnh | Điều cần chú ý |
|---|---|
| Trả lời, giải thích, hướng dẫn | Đáp đúng câu hỏi; đủ thông tin để hiểu hoặc làm theo |
| Tin nhắn, email, thông báo | Quan hệ giữa người viết và người nhận, phép lịch sự, việc cần trao đổi |
| Báo cáo, phân tích, học thuật | Phân biệt dữ kiện với suy luận; giữ nguồn, điều kiện và mức chắc chắn |
| Tài liệu chuyên môn | Dùng đúng thuật ngữ, định nghĩa và quy ước; không đơn giản hóa làm sai nghĩa |
| Giới thiệu, quảng cáo | Giọng thương hiệu và lời mời phù hợp; không thêm lời hứa thiếu căn cứ |
| Bài cá nhân, sáng tác | Giữ điểm nhìn, cảm xúc, nhịp, hình ảnh và dụng ý |
| Dịch thuật | Giữ nghĩa, sắc thái và giọng bản gốc; không tự thêm luận điểm |

Các ngữ cảnh có thể kết hợp. Đây là điều cần cân nhắc, không phải mẫu đầu ra cố định.

## Giữ nghĩa trước khi sửa giọng

- Giữ khẳng định, điều kiện, ngoại lệ và quan hệ nguyên nhân. Không đổi “có thể giảm” thành “giảm”, hoặc “sau khi” thành “nhờ”.
- Giữ số liệu, đơn vị, tên riêng, nguồn và trích dẫn. Không thêm chi tiết để bài có vẻ cụ thể hoặc đáng tin hơn.
- Nếu thấy khẳng định đáng ngờ, nêu chỗ cần xác minh. Chỉ thay đổi nội dung khi yêu cầu cho phép và có căn cứ; không âm thầm xóa ý khó xử.
- Với file, chỉ sửa trong phạm vi được giao. Giữ code, lệnh, URL, đường dẫn, khóa cấu hình và cấu trúc bảng trừ khi được yêu cầu đổi. Có thể sửa phần chữ trong bảng khi đó là nội dung được giao.
- Khi viết mới, phân biệt dữ kiện với đề xuất và giả định. Sáng tác được hư cấu theo đề bài, nhưng không dùng hư cấu làm bằng chứng thực tế.

## Biên tập

Đọc toàn văn trước khi sửa. Làm rõ chỗ mơ hồ, gỡ câu vòng vo, sửa từ lệch nghĩa và bỏ phần lặp không có tác dụng. Chỉ đổi những gì giúp văn bản hoàn thành đúng mục đích.

Chọn từ theo nghĩa và người đọc. Không tự động loại từ Hán Việt, dịch hết từ Anh hoặc giữ hết từ Anh. Giữ thuật ngữ ngành khi cần chính xác, giải thích khi người đọc chưa biết.

Xưng hô nhất quán theo từng người nói và quan hệ. Đổi giữa “tôi” và “chúng tôi” có thể đúng nếu chủ thể đổi. Không ép mọi văn bản dùng “mình/bạn”.

Tổ chức câu theo mạch ý, không ép nhịp dài/ngắn hoặc độ dài đoạn. Câu bị động, chủ ngữ lược bỏ và đoạn một câu đều có thể phù hợp. Lời chào, câu tổng kết, ẩn dụ và điệp từ cũng có chức năng riêng; chỉ bỏ khi thừa hoặc lệch ngữ cảnh.

Dùng dấu câu, danh sách, in đậm và emoji theo nội dung, kênh đăng và quy ước của người dùng. Không coi hình thức đơn lẻ là lỗi. Không thêm lỗi chính tả, tiếng lóng, trợ từ hoặc từ láy để giả giọng người.

Khi sửa, giữ cách ghi số và đơn vị nhất quán; không tự đổi giá trị, tiền tệ hoặc định dạng dữ liệu máy đọc. Khi viết mới, theo quy ước của nơi sử dụng.

## Kiểm tra trước khi trả

Đối chiếu bản trước và sau: có mất ý, thêm ý, đổi mức chắc chắn hay làm mất giọng không? Đọc lại để bắt câu mới sửa nghe gượng. Không viết lại chỉ để khác bản gốc.

Với file hoặc bài dài, dùng công cụ nếu có Python. Lưu bản trước khi sửa, quét trước/sau rồi so khác biệt. Đường dẫn dưới đây tính từ thư mục cài skill; dùng đường dẫn tuyệt đối khi chạy ở nơi khác:

```bash
python3 scripts/vi_scan.py scan FILE.md
python3 scripts/vi_scan.py verify TRUOC.md SAU.md
```

Cờ của máy quét là gợi ý cần đọc lại, không phải lệnh xóa. `verify` so chuỗi số/ngày, URL, code và frontmatter, kể cả số lần xuất hiện; không kiểm được nghĩa câu hay mọi tên riêng. Sửa khác biệt ngoài ý muốn, giải thích thay đổi có chủ đích. Không đổi bản gốc để làm kiểm tra đạt.

Câu trả lời ngắn chỉ cần đọc rà. Không có công cụ thì đối chiếu thủ công; không tuyên bố đã chạy kiểm tra nếu chưa chạy.

## Trả kết quả

Đưa đúng sản phẩm người dùng cần. Không mặc định kèm bảng dấu hiệu hoặc giải thích quy trình. Chỉ ghi chú thay đổi đáng kể, chỗ chưa chắc hoặc giới hạn kiểm tra khi cần. Nếu chỉ được nhờ kiểm tra, nhận xét chứ chưa sửa.

Tra [ví dụ và ngoại lệ](references/patterns-full.md) khi cần cân nhắc cách sửa; tra [nguồn](references/sources.md) khi cần biết căn cứ. Không cần đọc tài liệu nghiên cứu để dùng skill.

Skill không phụ thuộc một mô hình cụ thể, không chấm tác giả là người hay AI và không hứa vượt detector. Điểm quét thấp không chứng minh văn hay hoặc đúng. Khi bảo trì, đồng bộ các nguyên tắc này với `AGENTS.md` và README.
