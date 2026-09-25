# Nguồn dữ liệu Threads cho register khẩu ngữ

Ghi ngày 2026-09-25, sau câu hỏi "tìm nguồn data Threads cho skill tham khảo để viết". Threads ở đây là mạng xã hội của Meta (threads.net). Mục tiêu: lấp khoảng trống lớn nhất của corpus hiện tại, văn viết kiểu người thật đang kể chuyện.

## Vì sao Threads

Eval v2 và Luna đều cho thấy corpus khẩu ý hiện có (Góc nhìn, Genk, Kenh14) vẫn là văn đã biên tập: trợ từ cuối câu không xuất hiện (trung vị 0/0), từ láy không đo được. Đó là lý do B8 bị hạ xuống giả thuyết.

Threads Việt Nam khác ở chỗ:

- Nhiều bài dài 100-300 từ viết kiểu tâm sự, kể chuyện đi làm, tiền bạc, gia đình. Văn nói có đủ câu dài để đo nhịp học.
- Replies là tầng khẩu ngữ ngắn hơn nữa: xưng hô, teencode, trộn Anh, trợ từ cuối câu.
- Hai tầng này nằm chung một nền nên so sánh được với nhau.

## Bốn đường lấy data, xếp theo độ khả thi

### 1. Chrome thật qua browser-skill (bsk) - khuyến nghị

Tìm kiếm trên threads.net bản web bắt buộc đăng nhập, nên Chrome đã login của người dùng là đường rẻ và thẳng nhất.

Cách lấy: mở threads.net, gõ từ khóa tiếng Việt ("tâm sự", "đi làm", "lương", "sếp", "nhà trọ", "học lại" và tương tự), chọn tab bài viết, cuộn, chép text bài gốc kèm vài reply. Chỉ lấy bài công khai. Khi lưu thì bỏ handle, link và tên riêng.

Nhược: làm tay, chậm. Nhưng skill chỉ cần khoảng 30-60 mẫu cho một vòng đo, nên mức này chấp nhận được.

### 2. Permalink công khai, đọc data ẩn trong trang (không cần login)

Bài public có dạng `threads.net/@user/post/CODE` hoặc `threads.net/t/CODE`, xem được không đăng nhập. Trang cần JavaScript, nhưng toàn bộ nội dung nằm sẵn trong thẻ `<script type="application/json" data-sjs>` chứa khoá `thread_items`, gồm cả bài gốc và replies.

Cách làm đã có code mẫu (license MIT): `github.com/scrapfly/scrapfly-scrapers/tree/main/threads-scraper`, dùng Playwright tải trang, tìm script chứa `thread_items`, bóc JSON. Gọi nhẹ nhàng, mỗi URL một lần.

Một tool tương tự trên GitHub: `Chuanyin1202/threads-toolkit` (bóc post, profile, hashtag, không cần login; chưa tự kiểm tra).

Nhược: phải biết permalink trước. Kết hợp với đường 1: bsk tìm bài, script tải phần replies.

### 3. API chính thức của Meta - không dùng được cho việc này

API Threads (`developers.facebook.com/docs/threads`) phục vụ đăng bài, quản lý và đọc nội dung của tài khoản được cấp quyền. Không có endpoint tìm kiếm, không đọc hàng loạt bài của người khác, không có luồng dữ liệu công khai. Bỏ qua.

### 4. Dịch vụ scrape trả phí

Apify có actor "Threads Full Scraper" (tìm theo từ khóa, không cần login Threads), SocialCrawl và ScrapFly có sản phẩm tương tự. Tính phí theo lượt gọi. Chỉ đáng dùng khi cần cỡ nghìn mẫu trở lên; với 30-60 mẫu thì bsk rẻ hơn nhiều.

## Dataset người thật viết kiểu comment/chat (không phải Threads)

Dùng bổ sung khi cần cỡ mẫu lớn hơn mà không muốn thu thập tay. Text là comment công khai đã dán nhãn; nhãn toxicity của họ không dùng đến, chỉ lấy phần văn.

| Dataset | Nội dung | Cỡ | Link |
|---|---|---|---|
| ViHSD | Comment Facebook và YouTube, nhãn CLEAN/OFFENSIVE/HATE | 33.400 comment | `github.com/ptnghia2809/ViHSD`, bản HF `tarudesu/ViHSD` |
| UIT-ViCTSD | Comment 10 chủ đề, nhãn toxic/constructive | 10.000 comment | `nlp.uit.edu.vn/datasets`, paper arXiv 2108.09612 |
| ViLexNorm | Câu mạng xã hội kèm bản chuẩn hóa | hơn 11.000 câu | `aclanthology.org/2024.eacl-long.85` (đã có ở mục 13 sources.md) |
| UIT-VSFC | Feedback sinh viên về môn học | khoảng 16.000 câu | `nlp.uit.edu.vn/datasets` |

Hai điều cần lưu ý khi dùng:

- Nhiều comment ngắn dưới 10 từ, không đo được nhịp học. Lọc chỉ giữ câu đủ dài hoặc gộp nhiều comment của cùng người.
- License các repo này đa số cho mục đích nghiên cứu. Đọc lại điều khoản từng repo trước khi đưa văn bản vào corpus công khai.

Ngoài ra OpenSubtitles tiếng Việt cho register hội thoại phim, tham khảo được trợ từ nhưng là lời thoại dựng, không phải văn viết thật, nên chỉ coi là tài liệu phụ.

## Quy trình khi bắt đầu thu corpus v4-threads

1. Dùng bsk lấy 30-60 bài Threads Việt Nam dài (mỗi bài từ 60 từ trở lên) cùng 2-3 reply mỗi bài, rải trên ít nhất 5 chủ đề khác nhau.
2. Ẩn danh khi lưu: bỏ handle, link, tên người, ảnh. Lưu vào `corpus/v4-threads/` kèm một dòng ghi ngày lấy và từ khóa.
3. Sinh cặp AI cùng chủ đề theo cách của `research/eval_v2.py`.
4. Đo lại các tín hiệu đang treo: trợ từ cuối câu (B8), từ láy, CV độ dài câu, MATTR, zlib. Trợ từ tách được thì nâng B8 lên tín hiệu đã đo trên register này; không thì ghi kết quả âm như mọi vòng trước.
5. Ghi báo cáo vào `references/eval-threads.md` và thêm mục mới trong `sources.md`.

## Pháp lý và đạo đức

- Repo này công khai. Không commit văn nguyên văn dài kèm handle. Chỉ giữ trích đoạn đã ẩn danh, nêu rõ ngày lấy và cách lấy.
- Không lấy bài riêng tư, không lưu thông tin định danh cá nhân, không gọi API dồn dập.
- Dataset học thuật dùng đúng điều khoản của từng repo.

## Trạng thái

Ba vòng đã chạy ngày 2026-09-25: 77 bài, 12 bộ trả lời, 30 cặp AI, phủ 19 nhóm chủ đề (việc làm, lương, sếp, trọ, chia tay, học lại, dọn nhà, cuối tuần, nấu ăn, khám bệnh, mẹ chồng, hôn nhân, dạy con, gym, thú cưng, xe máy, cà phê, hàng xóm, tiết kiệm). Kết quả và giới hạn nằm trong `references/eval-threads.md`, tóm tắt ở mục 15 của `sources.md`.

Đợt 4 (replies chủ đề trung tính) dở vì Chrome đứt kết nối extension liên tục; đã lấy ViHSD đo đối chiếu thay thế (8,0% comment có trợ từ, nhóm có đạt 90,9/1000). Khi Chrome ổn, chạy lại bằng cùng quy trình bsk.
