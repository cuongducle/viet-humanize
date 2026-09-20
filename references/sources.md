# Nguồn tham chiếu (VI-sources)

Liệt kê mọi nguồn đã dùng để xây skill, dấu nào mỗi nguồn hỗ trợ, và các khoảng trống chưa kiểm chứng được. Cập nhật file này mỗi lần thêm dấu hiệu mới.

## 1. Nghiên cứu học thuật

### ViDetect, "Vietnamese AI Generated Text Detection" (arXiv 2405.03206, 2024)
- URL: https://arxiv.org/abs/2405.03206 (đọc toàn văn qua ar5iv, 2026-09-21)
- Đơn vị: ĐH Công nghệ Thông tin, ĐH Quốc gia TP.HCM.
- Dataset: 6.800 bài luận tiếng Việt (3.400 người, chỉ lấy bài đăng trước 2021; 3.400 do GPT-3.5/4.0 viết lại), chia 7:1:2. Baseline: ViT5, BARTpho, PhoBERT, mDeBERTa-v3, mBERT.
- Kết quả: Accuracy ~0,84-0,87; F1 ~0,87-0,93; AUROC tăng theo độ dài: 0,8629 (64 token) → 0,9168 (256 token).
- Hỗ trợ dấu hiệu:
  - Viện dẫn trực tiếp từ paper: văn AI tiếng Việt **viết đoạn dài hơn, ít câu hơn**; người viết **nhiều câu hơn, phân tích nhiều góc**; AI "không biểu đạt cảm xúc, biểu hiện con người" dài được như người.
  - Cơ sở cho nhóm dấu nhịp học trong vi_scan.py: biến động độ dài câu (burstiness), biến động độ dài đoạn, số câu mỗi đoạn.
  - AUROC 0,92 của bộ phân loại học được chứng minh dấu tiếng Việt tồn tại thật (không chỉ là chuyện tiếng Anh).
- Giới hạn: domain hẹp (bài luận học sinh/sinh viên), AI-side là paraphrase của cùng nội dung (không phải sinh mới), chỉ GPT-3.5/4.0.

### VietAIDetector, "An Open-Source Zero-Shot Detector for Vietnamese AI Text" (SSRN/arXiv, 2026)
- Tìm thấy qua tìm kiếm; chưa đọc toàn văn.
- Hỗ trợ: khẳng định hướng nghiên cứu detector tiếng Việt còn tích cực (zero-shot, mã nguồn mở).
- Ghi chú: khi đọc chi tiết, bổ sung số liệu vào mục này.

### Nền tảng phương pháp (tiếng Anh)
- blader/humanizer v3 (MIT): https://github.com/blader/humanizer, bản SKILL.md là đồng bộ của Wikipedia "Signs of AI writing" (đọc toàn văn 2026-09-21). Hỗ trợ toàn bộ lớp A (dấu phổ quát) và khung mức nghiêm trọng "mạnh một mình / yếu khi đứng một mình".
- conorbronsdon/avoid-ai-writing (MIT): https://github.com/conorbronsdon/avoid-ai-writing, đọc README + PROOF.md + cấu trúc repo. Hỗ trợ: kiểu phân tầng từ vựng, máy quét deterministic, nguyên tắc miễn trừ (code/trích dẫn), kiểm bảo tồn, tự quét, cổng xuất bản số liệu. PROOF.md công bố ROC-AUC 0,501 (mức đoạn) cho detector bề mặt tiếng Anh, căn cứ cho mục Hạn chế.
- harshaneel/humanize (MIT): https://github.com/harshaneel/humanize, đọc README. Hỗ trợ: khung 9 đòn bẩy từ tài liệu nghiên cứu phát hiện (perplexity, burstiness, stylometry), cách nói rõ "trần" của phương pháp quy tắc.
- jurigis/avoid-ai-writing-multilingual (MIT): https://github.com/jurigis/avoid-ai-writing-multilingual, đọc README + CLAUDE.md (quy trình tác giả). Hỗ trợ: quy trình 5 bước bản địa hóa được skill này áp dụng.

## 2. Hệ sinh thái Wikipedia

- Wikipedia tiếng Anh: "Signs of AI writing" (https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), tài liệu sống do WikiProject AI Cleanup duy trì từ 2023. Nguồn của lớp A.
- Báo Việt xác nhận sự tồn tại của dự án và bản hướng dẫn:
  - Lao Động (21/11/2025): "Wikipedia chỉ ra những dấu hiệu nhận diện văn bản AI", https://laodong.vn/van-hoa/wikipedia-chi-ra-nhung-dau-hieu-nhan-dien-van-ban-ai-1610643.ldo (site chặn bot; xác nhận qua trích đoạn tìm kiếm).
  - Congdankhuyenhoc.vn (25/11/2025): "Hướng dẫn của Wikipedia về phát hiện văn bản do AI tạo", nêu "từ 2023 các biên tập viên Wikipedia triển khai Dự án Dọn dẹp AI".
  - Brands Vietnam (28/8/2025): "Cách cộng đồng Wikipedia đối phó với nội dung 'rác' do AI".

## 3. Báo chí và quan sát bản địa [TT]

- VnExpress (8/7/2026): "Công cụ 'nhân hóa' văn bản giúp che dấu vết AI lên ngôi", bối cảnh nhu cầu nhân hóa ở Việt Nam; xác nhận nhu cầu thực tế của skill.
- Znews (16/8/2024): "Cách phát hiện ra nội dung AI", cách trình bày phổ biến trên báo Việt về nhận diện văn AI.
- VietnamNet (9/8/2025): "Chấm bài của sinh viên, thầy cô 'đau đầu' không biết trò làm hay ChatGPT làm", bối cảnh người chấm bài.
- Báo Mới/Tuổi Trẻ (15/2/2025): "Sinh viên nhờ AI làm bài, giảng viên 'nhìn là biết ngay'", giảng viên Việt nêu dấu cảm quan.
- Nhóm Facebook "Tâm sự Content" (21/4/2025): thảo luận tổng hợp dấu hiệu bài AI của người làm content Việt (không đọc trực tiếp được; tồn tại qua trích đoạn tìm kiếm).
- VisionEdu (Scribd): "13 dấu hiệu văn viết bởi AI", trích đoạn thấy: "phân tích hời hợt", "ngôn từ kiểu quảng cáo du lịch PR", "gán ý kiến cho số đông mơ hồ".

Những nguồn này hỗ trợ các từ vựng khuôn [TT] trong P1 ("tối ưu hóa", "trải nghiệm tuyệt vời"...) ở mức "quan sát thực hành phổ biến", KHÔNG ở mức thống kê tần suất.

## 4. Khoảng trống chưa kiểm chứng được (ghi thẳng, không giấu)

1. **Không có thống kê tần suất từ vựng công khai cho tiếng Việt** tương đương GoWinston (Đức) hay Pangram (Anh, 28 triệu văn bản). Mọi từ Tier tiếng Việt trong skill hiện là [TT]/[HL]. Cách nâng cấp: thu corpus song song (bài người/bài AI cùng chủ đề tiếng Việt, mỗi bên >= 100 bài, >= 3 loại văn), đo tần suất, chỉ giữ từ vượt trội có ý nghĩa thống kê. Ghi nhớ con số của avoid-ai-writing: ngay cả khi có thống kê, điểm bề mặt vẫn chỉ đạt AUC ~0,5-0,62, đừng kỳ vọng phép màu.
2. **Wikipedia tiếng Việt chưa có trang dấu hiệu riêng**; lớp A mượn của bản tiếng Anh, về mặt cấu trúc khả năng cao là đúng (mô hình sinh tiếng Việt cũng chọn "an toàn mặc định"), nhưng chưa ai đối chiếu formal.
3. **ViDetect chưa mở kết luận ra ngoài domain bài luận** (SEO, mạng xã hội, PR chưa có số liệu).
4. **Các dấu [HL]** (suy diễn): câu bị động kiểu dịch, xưng hô lắc lư, sai sót nhẹ có chủ đích, hợp lý về lý thuyết stylometry nhưng chưa có nguồn tiếng Việt trực tiếp.

## 5. Hạn chế của chính skill (phải nói trước khi ai hỏi)

- Máy quét chỉ đo **tập con phát hiện được bằng regex + nhịp học**. Văn có thể rỗng ruột, đều tăm tắp, và sạch mọi dấu.
- Số của avoid-ai-writing cho thấy điểm bề mặt **không phân biệt nổi người/máy ở mức đoạn** (AUC 0,501). ViDetect cho thấy bộ phân loại học được mới đạt 0,92. Vậy mục tiêu đúng của skill là **chất biên tập**, không phải nhảy điểm tool dò.
- Tool dò AI (GPTZero, Turnitin...) bất ổn với văn không phải tiếng Anh và đổi hành vi theo thời gian; "qua tool" không phải tiêu chuẩn nghiệm thu. Văn người thật đôi khi vẫn bị cờ đỏ.

## 6. Tự quét (self-scan, mô phỏng PROOF.md)

Chạy `python3 scripts/vi_scan.py scan <file>` trên chính các file của skill, ngày 2026-09-21:

| File | Điểm | Ghi chú |
|---|---:|---|
| SKILL.md | 11 | còn lại: frontmatter `---`, dòng danh mục nêu tên ký tự gạch ngang, nhãn in đậm của chính hệ P0/P1/P2 |
| references/methodology.md | 4 | từ "vượt trội" nằm trong ngữ cảnh liệt kê danh mục |
| references/patterns-full.md | 10 | ký tự – được nêu tên trong luật A8; ba tiêu đề "Lớp A/B/C" liền nhau; một bộ ba thật (chấm, ngoặc, viết lại) trong luật A8 |
| references/sources.md | 3 | từ "vượt trội" trong bảng từ vựng |

Điểm không bằng 0 vì danh mục chứa chính các dấu nó liệt kê, và các vùng miễn trừ (trích dẫn trong ngoặc kép) không phủ hết ngữ cảnh liệt kê. Đây là hiện tượng như avoid-ai-writing đã công bố trong PROOF.md của họ ("the catalog contains the words it catalogs"). Số này là Snapshot; chạy lại lệnh để có số hiện tại. Bản thân văn xuôi của skill đã được dọn một lượt theo luật của chính nó (từ 92 xuống 11 ở SKILL.md) trước khi công bố.
