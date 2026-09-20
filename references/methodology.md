# Phương pháp luận: danh mục dấu hiệu này được quan sát như thế nào

Tài liệu này trả lời câu hỏi: các skill humanize nổi tiếng đã *quan sát và đối chiếu thực tế ra sao* để rút ra dấu hiệu, và bản skill tiếng Việt này áp dụng điều gì từ họ. Đọc khi cần bảo trì, mở rộng, hoặc biện minh cho một dấu hiệu trước người hoài nghi.

## 1. Bốn trường phái quan sát (khảo sát tháng 9/2026)

### 1.1. blader/humanizer (MIT), quan sát từ chiến trường Wikipedia

Cách họ rút ra danh mục 25 dấu hiệu:
- Nguồn chính là bài **Wikipedia "Signs of AI writing"** do **WikiProject AI Cleanup** duy trì, nhóm biên tập viên tự nhận nhiệm vụ dọn văn bản AI trên Wikipedia mỗi ngày, từ 2023. Đây là "quan sát thực địa" liên tục: mỗi dấu hiệu đều đến từ việc xem xét các bài bị lôi về rồi so với văn người.
- Skill được **đồng bộ có chủ đích** với bài đó (commit c2c6cad từng ghi nhận việc căn lại theo bản cập nhật của Wikipedia). Khi mô hình đổi thói quen từ ngữ, bài Wikipedia đổi theo, skill theo sau.
- Cụm mới vào qua **issue cộng đồng** (ví dụ issue #277 đề xuất thêm "This distinction matters."), cơ chế thu nhận quan sát từ người dùng thật.
- Tác giả **từ chối khung "đánh bại tool dò"**: đã gỡ từ khóa ai-detection khỏi mô tả repo sau khi thấy người dùng hiểu nhầm mục đích. Lý do bảo vệ fact: có phản hồi rằng skill từng làm rớt cấu trúc so sánh ("the single most important...").
- Bài học rút ra cho tiếng Việt: dấu hiệu cấu trúc (dàn cảnh, nhịp, khoa trương) bền hơn danh sách từ; danh sách từ phải là lớp mỏng thay được.

### 1.2. conorbronsdon/avoid-ai-writing (MIT), đo đạc và tự xét

Nghiêm ngặt nhất về mặt bằng chứng:
- **Động cơ deterministic** (`detector/patterns.js`): regex + tín hiệu nhịp học (phân bố dấu câu, entropy từ chức năng, TTR) chạy được không cần mô hình; có test, có CI.
- **Tự quét chính mình** (`PROOF.md`): chạy detector lên tài liệu của repo, công bố cả số xấu, đặt "ngân sách" trần trong CI. Quét tự thân từng phát hiện lỗi thật (hai hình thái gạch ngang không được miễn trừ) và dẫn đến bản sửa (#67).
- **Đo tỷ lệ báo sai trên corpus thật**: 875 đoạn người + 779 đoạn máy từ HC3 và RAID. Kết quả công bố thẳng: FPR 4,2% ở ngưỡng score >= 5 với TPR chỉ 7,2%; ROC-AUC mức đoạn là **0,501, tung đồng xu**; mức tài liệu 0,623.
- **Cổng xuất bản số liệu** riêng: mỗi con số phải có n >= 100, khoảng tin cậy, và nhiều "register" (loại văn) thật, và họ thừa nhận phép đo của mình **rớt cổng register** (HC3 chỉ có ChatGPT, RAID khác hình thái nhiệm vụ).
- Hệ từ vựng phân tầng có lý do: Tier 1A (tần suất đặc trưng máy) tách khỏi 1B (văn dài dòng nói chung) để "sửa văn vụng" không đẩy điểm phân loại AI.
- Bài học cho tiếng Việt: (a) tách "dấu AI" khỏi "văn dở"; (b) mọi con số cần cổng xuất bản; (c) tự quét chính skill là cách bắt lỗi rẻ nhất.

### 1.3. harshaneel/humanize (MIT), rút từ tài liệu nghiên cứu phát hiện

- Chín "đòn bẩy nhân hóa" rút từ **50+ nguồn bình duyệt 2024-2026** về phát hiện văn bản AI: perplexity, burstiness, stylometry, discourse.
- Tách hai skill: `humanize` (viết lại) và `ai-check` (giao thức phân tích, chấm 9 nhóm tín hiệu, kèm mức tin cậy).
- Trung thực về "trần": cách tiếp cận quy tắc tĩnh không qua được bộ phân loại học máy (Grammarly, GPTZero); nêu rõ kỹ thuật bổ sung để qua trần đó (paraphrase chéo mô hình, viết lại bằng base model, sửa tay).
- Bài học cho tiếng Việt: nhắm vào chất văn người chứ không nhắm vào điểm số; nói rõ trần của phương pháp ngay trong skill.

### 1.4. jurigis/avoid-ai-writing-multilingual (MIT), quy trình bản địa hóa

Đây là quy trình skill tiếng Việt này làm theo (được tinh gọn cho môi trường pi):
1. **Tra cứu bằng chính ngôn ngữ đích**, không tra tiếng Anh; tối thiểu 3 loại nguồn độc lập: trang cộng đồng Wikipedia, blog/SEO bản địa, nghiên cứu học thuật, báo cáo người làm nghề.
2. **Phân ba lớp**: (A) dấu phổ quát, dịch khái niệm, không dịch câu; (B) dấu riêng ngôn ngữ, phải có nguồn, không đoán (ví dụ Đức: cụm Nominalstil; Rumani: calque từ Anh); (C) ngữ cảnh văn hóa, loại văn nào dày AI nhất ở vùng đó (Đức: LinkedIn; Việt Nam theo khảo sát: bài chuẩn SEO, thông cáo PR, tiểu luận).
3. **Từ vựng Tier-1 phải có nguồn** chứng minh vượt trội trong đầu ra LLM; từ chỉ "văn dở" không được xếp Tier-1.
4. **Ví dụ đầy đủ phải sinh ra bản địa**, không dịch từ tiếng Anh.
5. **File nguồn riêng** liệt kê trích dẫn, ngày, dấu nào được nguồn nào hỗ trợ, và **ghi rõ khoảng trống** chưa kiểm chứng được.

## 2. Điều đã áp dụng cho tiếng Việt

| Việc | Theo trường phái | Kết quả |
|---|---|---|
| Nghiên cứu bằng tiếng Việt, 4 loại nguồn | jurigis bước 1 | xem sources.md |
| Phân lớp A/B/C dấu hiệu | jurigis bước 2 | patterns-full.md chia 3 lớp |
| Nhãn nguồn từng dấu [W][VD][TT][HL] | avoid-ai-writing (tách 1A/1B) | mọi dấu đều ghi nguồn |
| Máy quét deterministic + selftest | avoid-ai-writing | scripts/vi_scan.py |
| Kiểm bảo tồn số liệu/URL/code | avoid-ai-writing validate.js | lệnh verify |
| Trung thực về giới hạn của dấu bề mặt | PROOF.md + harshaneel | mục Hạn chế trong sources.md |
| Ví dụ bản địa (bài chuẩn SEO) | jurigis bước 4 | trong SKILL.md |
| Giao thức bảo trì định kỳ | blader (sync Wikipedia) | mục Bảo trì trong SKILL.md |

## 3. Điều tiếng Việt chưa có và cách xử lý

- **Chưa có** bài "dấu hiệu văn AI" riêng của Wikipedia tiếng Việt (dự án Dọn dẹp AI hoạt động ở bản tiếng Anh; báo Việt chỉ đưa tin về nó). Xử lý: lớp A lấy từ bản tiếng Anh qua sync của blader/humanizer, ghi nhãn [W].
- **Chưa có** danh sách từ Tier-1 tiếng Việt kèm thống kê tần suất công khai (kiểu GoWinston "từ ChatGPT hay dùng" của Đức). Xử lý: từ vựng hiện mang nhãn [TT] (quan sát thực hành) hoặc [HL] (suy diễn), đợi kiểm chứng; quy tắc bảo trì sẽ hạ bậc các từ [HL] chết.
- **Có** dataset học thuật ViDetect (6.800 mẫu) và VietAIDetector (2026): cho biết dấu tiếng Việt tồn tại thật và học được (AUROC tới 0,92 ở 256 token bằng PhoBERT-class), đồng thời cho quan sát cấu trúc: văn AI tiếng Việt câu ít hơn, đoạn dài hơn, kém bộc lộ cảm xúc. Đây là cơ sở nhóm dấu nhịp học.

## 4. Quy ước khi thêm dấu hiệu mới

1. Ghi ví dụ thật (câu nguyên văn gặp ngoài đời), không tự chế.
2. Gán nhãn nguồn đúng: chỉ [W]/[VD] khi trích được đúng nguồn; không gán nhãn [TT] cho ý kiến cá nhân.
3. Chỉ lên P0 khi dấu đó bền qua nhiều bản mô hình hoặc có nguồn trực tiếp.
4. Nếu dấu bắt được cả văn người viết cẩn thận thì hạ xuống P2 và bắt buộc "cần dấu bạn cùng đoạn".
