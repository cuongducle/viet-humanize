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

Lần tự kiểm thứ hai (2026-09-21, sau khi vá máy quét v1.1 phát hiện khi tự test trên chính output mặc định của trợ lý): bản "truoc" mẫu 42 điểm được bắt thêm "dưới đây là", "một trong những ... nhất", nhãn in đậm (dấu hai chấm trong lẫn ngoài cặp đậm), ẩn dụ đầu tư, lên 55; bản viết lại giữ 0 điểm; self-scan SKILL.md 13 (tự tham chiếu: nhãn Trước/Sau, danh sách P0/P1/P2). Điểm không bằng 0 vì danh mục chứa chính các dấu nó liệt kê, và các vùng miễn trừ (trích dẫn trong ngoặc kép) không phủ hết ngữ cảnh liệt kê. Đây là hiện tượng như avoid-ai-writing đã công bố trong PROOF.md của họ ("the catalog contains the words it catalogs"). Số này là Snapshot; chạy lại lệnh để có số hiện tại. Bản thân văn xuôi của skill đã được dọn một lượt theo luật của chính nó (từ 92 xuống 11 ở SKILL.md) trước khi công bố.

## 7. Nguồn ngôn ngữ học và phương pháp định lượng (v1.2)

Thêm sau câu hỏi "về mặt ngôn ngữ học thì còn cải thiện gì" (2026-09-21). Nền mô tả tiếng Việt:
- Thompson, Laurence (1965). *A Vietnamese Reference Grammar*. — mô tả chuẩn trợ từ, danh từ phân loại, từ láy.
- Nguyễn Tài Cẩn (1975). *Câu tiếng Việt*. — đặc tính ngữ pháp câu, chủ ngữ.
- Cao Xuân Hạo (1998). *Tiếng Việt, văn Việt, người Việt*. — tạp bút về phong cách và văn hóa ngôn ngữ.

Phương pháp định lượng:
- Covington & McFall (2010): MATTR (TTR cửa sổ trượt) — thay TTR toàn cục vốn lệ thuộc độ dài văn bản; tiếng Việt tính trên âm tiết do chưa tách từ.
- Gries (2008): độ phân tán từ vựng — cơ sở lý thuyết cho hướng mở (chưa cài).
- Jiang và cộng sự (2023): phân loại văn bản bằng compressor — cơ sở cho tỷ lệ nén zlib (chỉ tham khảo).

Trung thực về chỉ số mới: trợ từ cuối câu, liên từ hình thức, Hán Việt hành chính, từ láy, skewness, entropy dấu câu, zlib đều là **chỉ báo tham khảo, chưa hiệu chỉnh ngưỡng trên corpus song sinh tiếng Việt** (khoảng trống 1). Từ láy đếm bằng danh sách ~65 từ tuyển chọn: precision cao, recall thấp (có chấp nhận, đã ghi). Nhãn [NN] dùng cho sự kiện mô tả chuẩn, không được hiểu là thống kê AI.

## 8. Hiệu chỉnh pilot (v1.3, 2026-09-21)

Corpus 42 mẫu (21 người: Wikipedia VI + VnExpress; 21 AI: trợ lý LLM chế độ mặc định).
Kết quả chính: CV độ dài câu AUC 0,99; TTR/MATTR/entropy dấu câu 0,85-0,94; điểm scan
tổng hợp chỉ 0,529; MATTR ngược hướng suy đoán ban đầu. Chi tiết: references/calibration.md.
Khoảng trống 1 được thu hẹp một phần: ngưỡng nhịp học đã có số liệu riêng cho tiếng Việt
register trang trọng; register khẩu ngữ/blog vẫn chưa đo được (trợ từ, từ láy đều md=0).

## 9. Demo README bằng chính skill (2026-09-21)

Viết lại README.md của repo theo đúng workflow 5 bước: bản nháp mặc định 37/100,
bản cuối 0/100, verify bảo toàn pass sau khi nháp bổ sung đủ fact. Bước đọc tay
phát hiện biến thể tổng quát "trong thời đại X ngày nay" mà regex cũ (chỉ khớp
'công nghệ/số hóa') bỏ sót: đã vá P0. Verify cũng lộ bug hiển thị chênh lệch
multiset (trùng lặp số lần): đã vá Counter. Minh chứng cho vai trò của lớp đọc tay.

Vòng dogfood 2 (v1.4.1, trên chính README): scan 0/100 và mật độ Hán Việt 4,5/1000 vẫn còn 3 lỗi chỉ bắt được bằng đọc tay (typo 'hạn hạn chế', 'lẫn' lặp hai lần trong một câu, cụm 'đồng bộ tư tưởng với'). Kết luận lặp lại: điểm 0 không đồng nghĩa 'đã tự nhiên'.

## 10. Nguồn tầng chọn từ (2026-09-21)

- Georgiou 2025, MDPI Languages 10(5):166: văn AI nhiều từ khó, từ nội dung hơn; văn người nhiều từ chức năng hơn (tiếng Anh). Không tái lập ở tầng âm tiết tiếng Việt trên pilot (AUC 0,43), ghi nhận là kết quả âm.
- Gude, Santos-Ríos, Bond và cộng sự 2026, arXiv 2605.06030: model sau tinh chỉnh lệnh có đa dạng từ vựng và cú pháp giảm rõ so với model gốc; văn báo người gần như không đổi theo năm. Hợp lệ với hiện tượng "chọn từ đều nhau giữa các bài" (cùng Chen 2026, Oxford: văn AI đồng nhất về văn phong).
- Monroe, Colaresi, Quinn 2008: phương pháp log-odrs z-score (fightin' words) cho phân tích từ khác biệt, dùng trong research/lexical_analysis.py.
- Quy tắc giữ nguyên từ tiếng Anh thông dụng (B14): quan sát thực hành [TT], ăn khớp với chỉ số mật độ Hán Việt đo được (deploy dịch thành triển khai là đúng cụm bị đếm). Chưa có thống kê tần suất song hành Anh-Việt công khai, ghi là khoảng trống.
- Pilot (n=42, một mô hình, chủ đề chưa khớp từng cặp): mật độ động từ Hán Việt trừu tượng tách tốt (AUC 0,72, người 2,6 so với AI 10,4 trên 1000); phó từ cường độ yếu (0,55); tỷ lệ từ chức năng không tách (0,43). Danh sách từ lẻ nghiêng về từ trừu tượng kiểu sách vở ở phía AI (chương trình, hệ thống, dự án, cơ hội, chức năng, dữ liệu) và về năm tháng, vật cụ thể ở phía người, nhưng bị nhiễu chủ đề nên chỉ nêu làm giả thuyết.

## 11. Eval v2 (2026-09-21, corpus khớp chủ đề + register khẩu ý)

- Thiết kế: 20 cặp trang trọng (wiki/news) và 12 cặp khẩu ý (VnExpress Góc nhìn, Genk, Kenh14), AI cùng chủ đề từng cặp, một mô hình. Script research/eval_v2.py, báo cáo references/eval-v2.md.
- Tái hiện: CV độ dài câu vẫn tách gần tuyệt đối (0,993; ngưỡng 0,29 cho 0 FP người / 19 TP AI). TTR và MATTR vẫn AI CAO hơn người (0,92 / 0,90) — kết luận 'AI đa dạng từ hơn người' giờ đứng vững trên corpus khớp chủ đề.
- Fightin' words hết nhiễu chủ đề: phía AI toàn âm tiết trừu tượng (nổi, năng, tạo, hội, nhân, sản, cầu), phía người là năm, tháng, số, và (Genk/Kenh14) 'the' — bằng chứng trộn Anh của người thật, ủng hộ B14. Khẩu ý: người dùng tôi, anh, chơi; AI phi-ngôi.
- Kết quả âm công bố: trợ từ cuối câu KHÔNG tách trên register báo chí giọng trẻ (trung vị 0/0), hạ B8 xuống giả thuyết. Điểm scan 0,62 (trang trọng) / 0,76 (khẩu ý): máy quét bắt được nhiều hơn ở khẩu ý nhưng vẫn không phải detector.
- Giới hạn: n nhỏ (12 cặp khẩu ý), một mô hình, các chỉ số 1,000 cần corpus lớn hơn trước khi tin là tách tuyệt đối.

## 12. Test model-switch GPT Luna (2026-09-21)

- Model: `gpt-5.6-luna`, xác nhận qua `PI_MODEL`; 20 mẫu trang trọng và 12 mẫu khẩu ý, cùng chủ đề với human v2. Báo cáo: `references/eval-luna.md`, script: `research/eval_luna.py`.
- Tín hiệu xuyên model: CV độ dài câu (trang trọng AUC 0,965; khẩu ý 1,000), TTR/MATTR AI cao hơn người (trang trọng 0,955/0,931; khẩu ý 1,000/0,854), zlib (0,819/1,000), và cấu trúc đoạn khẩu ý (1,000).
- Tín hiệu không xuyên model: Hán Việt ở khẩu ý. AI cũ 10,75/1000, Luna 0, người 4,34; hướng Luna ngược lại. Chỉ giữ quy tắc Hán Việt như tín hiệu yếu cho văn trang trọng, không dùng để ép khẩu ngữ.
- Ngưỡng cũng không xuyên hoàn toàn: ngưỡng CV cũ `≤0,21` bắt 4/12 Luna khẩu ý; nới về `≤0,29` bắt 8/12 với 0 FP người. Không được coi đây là ngưỡng phổ quát.
- Luna khẩu ý dùng nhiều phó từ cường độ hơn (13,25/1000 so với người 4,22), nhưng n=12 và cùng một model nên chỉ ghi nhận, chưa nâng thành luật.
- Giới hạn phương pháp: đây là model-switch test chứ chưa phải blind test độc lập; Luna vẫn nhận cùng bối cảnh dự án và người viết không tách khỏi quá trình thiết kế corpus.

## 13. Tầng kết hợp từ và triển khai ý (2026-09-22)

Người dùng đọc bản README mới đã bắt đúng hai lỗi mà scanner không thể bắt: "danh từ có điểm tựa" và "nhịp câu bớt đồng phục" đều là cụm do người biên tập tự chế. Chúng không sai ngữ pháp, nhưng không phải cách nói tự nhiên. Vì vậy bổ sung một lớp kiểm tra thủ công, tách khỏi danh sách từ Hán Việt.

### Nguồn ngôn ngữ học và ngữ liệu

- Cao Xuân Hạo (1998), *Tiếng Việt, văn Việt, người Việt*. Nguồn đã có ở mục 7. Dùng cho nguyên tắc không áp một mô hình chủ ngữ-vị ngữ tiếng Anh vào mọi câu Việt, và để thận trọng khi nói về cấu trúc đề-thuyết.
- Nguyễn Thị Thu Hiền (2006), "Cấu trúc Đề-thuyết trong phân tích diễn ngôn bình luận tin báo chí tiếng Anh và tiếng Việt", *Tạp chí Khoa học Trường ĐH Sư phạm TP.HCM*, số 7, trang 24. DOI: https://doi.org/10.54607/hcmue.js.0.7.1280. Kết quả tìm kiếm mô tả đề ngữ có vai trò nối với phần trước, duy trì hoặc phát triển chủ đề, tạo tiêu điểm và hướng người đọc. Nguồn hỗ trợ quy tắc B17, không chứng minh đây là dấu AI.
- Phạm Hoàng và cộng sự (2019), *Constructing two Vietnamese corpora and building a lexical database*. Springer/ACM/JSTOR. Nguồn này xây hai corpus tiếng Việt đương đại và các chỉ số từ vựng, cho thấy việc nói "cụm tự nhiên" cần dựa vào ngữ liệu chứ không chỉ trực giác. Trang tra cứu: https://link.springer.com.
- Phạm và cộng sự (2008), *Corpora of Vietnamese Texts: Lexical effects of intended audience and age*. *Journal of Psycholinguistic Research*. Kết quả được lập chỉ mục cho thấy tần suất đại từ và từ xưng hô thay đổi theo người đọc, hỗ trợ việc giữ register và xưng hô theo đối tượng thay vì dùng một giọng cho mọi bài.
- Nguyễn Thị Ngọc Trang và cộng sự (2024), *ViLexNorm: A Lexical Normalization Corpus for Vietnamese Social Media Text*, EACL 2024, https://aclanthology.org/2024.eacl-long.85/. Nguồn này phân biệt dạng viết mạng xã hội và dạng chuẩn hóa, nhắc rằng "tự nhiên" phụ thuộc register; không được sửa khẩu ngữ thành văn in.

### Nguyên tắc rút ra

1. Không tự tạo ẩn dụ để mô tả thao tác biên tập. Nếu ý là gọi đúng sự vật, viết "gọi đúng người, vật hoặc việc".
2. Không nhầm đa dạng từ với tự nhiên. Lặp lại tên người, sản phẩm hoặc địa điểm khi đó là chủ đề; đừng xoay vòng bằng bốn danh từ trừu tượng chỉ để tránh lặp.
3. Mỗi câu mới phải thêm fact, nguyên nhân, ví dụ, ngoại lệ hoặc hệ quả. Nếu chỉ nhắc lại câu trước, cắt nó.
4. Khi chuyển chủ đề, báo bằng một chủ thể hoặc quan hệ thật. Không rải "ngoài ra", "hơn nữa", "do đó", "tóm lại" theo một khuôn cố định.
5. Quy tắc B16 và B17 hiện là hướng dẫn biên tập [TT]/[NN], chưa phải đặc trưng AI đã được đo. Cần corpus có gắn nhãn kết hợp từ và cấu trúc diễn ngôn trước khi nâng thành tín hiệu định lượng.

## 14. Nguồn dữ liệu Threads cho register khẩu ngữ (2026-09-25)

Điều tra bốn đường lấy dữ liệu Threads (mạng xã hội của Meta) để lấp khoảng trống khẩu ngữ của mục 4: bsk với Chrome đã login (khuyến nghị chính), permalink công khai kèm data ẩn `thread_items` không cần login (code mẫu MIT của scrapfly), API chính thức (chỉ phục vụ tài khoản được cấp quyền, bỏ qua), dịch vụ trả phí kiểu Apify. Kèm bốn dataset comment người thật cùng register (ViHSD, UIT-ViCTSD, ViLexNorm, UIT-VSFC) và quy trình thu corpus v4-threads kèm lưu ý ẩn danh. Chi tiết: `references/threads-data.md`.

## 15. Corpus v4-threads và đính chính báo cáo eval (2026-09-25)

- Thu 44 bài Threads Việt Nam và 7 bộ trả lời bằng Chrome thật (browser-skill) đúng quy trình của mục 14, trong hai đợt cùng ngày; 18 cặp AI cùng chủ đề viết ở chế độ mặc định. Script `research/eval_threads.py`, báo cáo `references/eval-threads.md`, nguồn corpus trong `corpus/v4-threads/manifest.md`.
- Kết quả chính: zlib 0,912 (người 0,77 cao hơn AI 0,57); TTR toàn cục nghiêng về người (0,842; người 0,86, AI 0,73) ngược register báo chí, trong khi MATTR-50 vẫn AI cao hơn (0,602); Hán Việt trừu tượng 0,801 (AI 5,75/1000, người 0); phó từ cường độ 0,754 (AI 6,13, người 0). CV độ dài câu đổi hướng so với trang trọng: ở đây AI đều tay hơn (0,576). Fightin' words: đối lập xưng hô mình/tao (người) với tôi (AI) là từ khác biệt rõ nhất.
- B8 (trợ từ cuối câu): AI 1/18 file (4,8/1000); bài dài người 13/44 (tối đa 83,3/1000, trung vị 0); replies 5/7 bộ có, dao động 3,7-57,1/1000 tùy chủ đề. Nâng B8 lên tín hiệu đã đo cho văn trả lời ngắn, kèm lưu ý mật độ phụ thuộc chủ đề; không dùng cho văn dài.
- Đính chính: hàm `table()` của `eval_v2.py` hoán cột trung vị ở các dòng đổi chiều (ng>AI) ngay từ đầu; đã sửa và sinh lại `references/eval-v2.md` hôm 2026-09-25. Mọi AUC và ngưỡng không đổi; các cột trung vị của dòng ng>AI trong bản cũ là số của bên kia. `eval_luna.py` không dính lỗi.
