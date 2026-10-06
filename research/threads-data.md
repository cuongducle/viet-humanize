# Thu thập văn trò chuyện: trường hợp Threads

Tài liệu dành cho việc mở rộng corpus, không phải hướng dẫn viết bài. Threads là một nguồn văn trò chuyện trong số nhiều nguồn, không đại diện cho mọi cách viết tiếng Việt.

## Phạm vi và trạng thái

Đợt thu ngày 2026-09-25 đã tạo tập gồm 77 bài, 12 bộ trả lời và 30 bài AI cùng chủ đề, phủ 19 nhóm chủ đề đời sống. Chi tiết nguồn và các đợt thu nằm trong [manifest](../corpus/v4-threads/manifest.md). Muốn đo lại, chạy `python3 research/eval_threads.py` từ gốc repo; kết quả nằm trong `research/results/` và không phải hướng dẫn cho skill.

Đợt thu trả lời ở chủ đề trung tính chưa hoàn thành vì Chrome mất kết nối. Phép đối chiếu thay thế dùng số tổng hợp từ ViHSD: 8,0% bình luận có trợ từ, nhóm có trợ từ đạt trung vị 90,9/1000. Không đưa văn bản ViHSD vào repo.

Tập này bổ sung cho văn bách khoa và báo chí đã có. Không dùng cách xưng hô, viết tắt hoặc xuống dòng trên Threads làm chuẩn cho email, báo cáo, dịch thuật hay sáng tác.

## Xác định câu hỏi trước khi lấy dữ liệu

Chọn mẫu theo điều muốn kiểm tra. Nếu nghiên cứu trợ từ, cần phân biệt bài gốc với từng lời trả lời. Nếu nghiên cứu độ dài câu, cần ghi độ dài văn bản và cách tách câu. Không gộp nhiều người nói thành một văn bản rồi diễn giải như phong cách của một người.

Ghi kế hoạch về chủ đề, độ dài và cách chọn bài trước khi đọc kết quả. Đừng chỉ lấy bài có tiếng lóng, lỗi gõ hoặc xưng hô thân mật rồi dùng chính những đặc điểm đó để khẳng định đâu là văn người. Bài công khai có thể do AI hỗ trợ; nếu không xác minh được tác giả, ghi rõ nhãn nhóm là nhãn tuyển chọn.

## Các đường thu thập đã khảo sát

### Trình duyệt đăng nhập

Các đợt thu của repo dùng Chrome qua `browser-skill` và CLI `bsk`. Khi làm lại, đọc hướng dẫn của skill đang cài, giữ danh sách session và cửa sổ do tác vụ mở. Chỉ đọc nội dung công khai hoặc nội dung người dùng có quyền cung cấp cho mục đích này.

Tìm theo các chủ đề đã định, mở bài và trả lời để đọc đủ ngữ cảnh. Lưu xuất xứ ở manifest riêng, không chèn metadata vào văn dùng để tính chỉ số. Không lấy bản cắt cụt làm toàn văn mà không ghi chú.

### Permalink và dữ liệu trong trang

Các mẫu đã khảo sát có URL dạng `threads.net/@user/post/CODE` hoặc `threads.net/t/CODE`. Nội dung từng được tìm trong thẻ `<script type="application/json" data-sjs>` với khóa `thread_items`.

Nguồn tham khảo: `github.com/scrapfly/scrapfly-scrapers/tree/main/threads-scraper` và `Chuanyin1202/threads-toolkit`. Đây là cách từng được mô tả, không đảm bảo cấu trúc trang, quyền truy cập hoặc code bên ngoài vẫn còn hoạt động. Không suy rằng mọi bài và mọi trả lời đều nằm trong HTML tải lần đầu.

### API và dịch vụ ngoài

Kiểm tra tài liệu hiện hành tại `developers.facebook.com/docs/threads` trước khi chọn API. Bản khảo sát ban đầu chưa xác minh được đường API phù hợp cho yêu cầu thu corpus này; không dùng nhận định đó để kết luận API vĩnh viễn không có khả năng tìm kiếm.

Apify, SocialCrawl và ScrapFly là các lựa chọn từng được khảo sát. Kiểm tra phạm vi dữ liệu, điều khoản và chi phí trước khi dùng. Không tự đăng ký, mua hoặc nạp tiền khi chưa có xác nhận của người dùng.

## Nguồn bổ sung ngoài Threads

Các cỡ dữ liệu dưới đây là thông tin ghi nhận từ đợt khảo sát, không phải số mẫu đã đưa vào repo:

| Dataset | Loại văn | Cỡ công bố trong ghi chép | Nơi tra cứu |
|---|---|---|---|
| ViHSD | Bình luận Facebook/YouTube, nhãn CLEAN/OFFENSIVE/HATE | 33.400 bình luận | `github.com/ptnghia2809/ViHSD`, `tarudesu/ViHSD` |
| UIT-ViCTSD | Bình luận thuộc 10 chủ đề | 10.000 bình luận | `nlp.uit.edu.vn/datasets`, arXiv 2108.09612 |
| ViLexNorm | Văn mạng xã hội và bản chuẩn hóa | Hơn 11.000 câu | `aclanthology.org/2024.eacl-long.85` |
| UIT-VSFC | Phản hồi sinh viên về môn học | Khoảng 16.000 câu | `nlp.uit.edu.vn/datasets` |

Trong lần đối chiếu ViHSD, đường GitHub gốc không truy cập được; bản dữ liệu đã dùng được tìm ở `github.com/sonlam1102/vihsd`, file `data/vihsd.zip`. Việc tải được từ một bản sao không chứng minh quyền tái phân phối. Kiểm tra nguồn và giấy phép trước mỗi lần sử dụng.

Bình luận quá ngắn có thể không phù hợp một số phép đo. Ghi tiêu chí lọc và báo phần bị loại. Nếu gộp thành bộ trả lời, giữ ranh giới từng lời và báo rõ đơn vị phân tích. Nhãn CLEAN mô tả nội dung theo bộ nhãn của dataset, không xác minh tác giả là người hay cho phép công bố văn bản.

Phụ đề phim như OpenSubtitles có thể bổ sung lời thoại, nhưng đó là văn được viết và biên tập cho phim, không thay thế dữ liệu hội thoại tự phát.

## Quy trình thu một đợt mới

1. Chốt câu hỏi, nguồn và tiêu chí chọn/loại mẫu. Ghi trước cách xử lý bài trùng, nội dung quảng cáo, văn cắt cụt và khả năng có AI hỗ trợ.
2. Kiểm tra quyền sử dụng. Tách bản gốc có xuất xứ khỏi phần được phép đưa vào repo công khai.
3. Thu văn bản và metadata riêng; giữ nguyên cách viết trong mẫu đo. Không “làm sạch văn AI” hoặc sửa câu trong corpus.
4. Nếu cần nhóm AI, lưu mô hình, prompt và điều kiện sinh. Ghép chủ đề và kiểm tra khác biệt độ dài, kênh hoặc định dạng.
5. Chạy script đánh giá, báo cả kết quả không phân tách được. Không chọn ngưỡng từ mẫu rồi gọi đó là kiểm tra độc lập trên chính mẫu ấy.
6. Cập nhật manifest và báo cáo. Muốn đổi quy tắc biên tập, cần xét thêm ngoại lệ và chất lượng bản sửa, không chỉ AUC.

## Dọn cửa sổ Chrome sau mỗi đợt

Sự cố ngày 2026-09-25 có nhiều lần extension mất kết nối sau các đợt thu. Cửa sổ còn sót là một nghi vấn, chưa xác định được nguyên nhân gốc. Việc dọn cửa sổ chỉ giảm tần suất mất kết nối, không khôi phục hoàn toàn.

Nếu `bsk logs | tail` có “browser disconnected” và “browser connected” xen kẽ, dừng lặp lệnh và kiểm tra tình trạng kết nối. Dấu này không đủ để kết luận Chrome quá tải hoặc website có lỗi.

- Ghi session và cửa sổ đã mở ngay khi bắt đầu. Kết thúc các session của tác vụ trước khi đóng cửa sổ tương ứng.
- Ưu tiên thao tác dọn của công cụ đang dùng. Nếu cần điều khiển cửa sổ hệ điều hành, đọc skill computer-use hiện có.
- Không nhận diện cửa sổ của agent chỉ bằng tiêu đề Threads, tiêu đề trống hoặc việc không có phần tử giao diện. Phải đối chiếu với danh sách đã ghi.
- Không đóng session hoặc cửa sổ của người dùng và tác vụ khác. Không khởi động lại cả Chrome khi chưa có đồng ý vì có thể mất công việc chưa lưu.
- Không lặp cùng một lệnh lỗi quá hai lần mà không có chẩn đoán mới. Nếu chưa khôi phục được, lưu trạng thái và báo phần bị chặn.

Các lệnh Orca đã dùng trong lần xử lý cũ, chỉ tham khảo khi môi trường có đúng CLI này:

```bash
orca computer list-windows --app "Google Chrome" --json
orca computer hotkey --app "Google Chrome" --window-id <id> --key CmdOrCtrl+W --restore-window
```

Phím đóng có thể chỉ đóng tab đang chọn. Quan sát lại để xác nhận, không suy rằng cả cửa sổ đã đóng. Cửa sổ không điều khiển được thì ghi lại và báo, không coi là đã dọn xong.

## Quyền riêng tư và công bố

Chỉ công bố dữ liệu có quyền sử dụng phù hợp. Công khai trên mạng và bỏ tên không tự làm mất quyền tác giả hoặc rủi ro nhận diện lại. Chi tiết câu chuyện, địa chỉ và trích dẫn dài vẫn có thể xác định người viết.

Ưu tiên số tổng hợp hoặc trích đoạn được phép dùng. Không commit thông tin đăng nhập, ảnh, dữ liệu riêng tư hoặc bản tải thô có định danh. Giữ thông tin xuất xứ cần cho kiểm toán ở nơi có quyền truy cập phù hợp.
