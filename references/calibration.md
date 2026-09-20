# Hiệu chỉnh ngưỡng trên corpus pilot (v1.3, 2026-09-21)

Nghiên cứu thử (pilot) đo khả năng phân tách văn người/AI của từng chỉ số, theo tinh thần
PROOF.md của avoid-ai-writing (đo FPR/AUC thật, công bố cả kết quả xấu).

## Phương pháp

- Corpus: 42 mẫu tiếng Việt, mỗi mẫu 120-330 từ.
  - **Người (21):** 11 đoạn mở bài bách khoa Wikipedia tiếng Việt (API, ngẫu nhiên)
    + 10 đoạn bài báo VnExpress (6 chuyên mục, 2026-09-21). Thu thập: `research/fetch_human.py`.
  - **AI (21):** 11 mẫu giọng bách khoa + 10 mẫu giọng báo chí, do chính trợ lý LLM viết
    ở chế độ mặc định (không bật skill, không cố tình cài dấu) — cùng phương pháp self-test.
- Đo lẻ từng chỉ số, tính AUC bằng Mann-Whitney (đồng hạng lấy hạng trung bình).
- Tái hiện: `python3 scripts/vi_scan.py calibrate corpus/human corpus/ai`.

## Kết quả AUC (xếp theo sức tách)

| Chỉ số | AUC (đã lật hướng) | Hướng | md người | md AI |
|---|---|---|---|---|
| CV độ dài câu | **0,991** | người > AI | 0,43 | 0,21 |
| TTR âm tiết | **0,943** | AI > người | 0,62 | 0,74 |
| MATTR-50 | **0,910** | AI > người | 0,86 | 0,92 |
| Entropy dấu câu (bit) | **0,848** | người > AI | 1,33 | 0,99 |
| Skewness độ dài câu | 0,715 | người > AI | 0,43 | -0,04 |
| Hán Việt hành chính/1k | 0,687 | AI > người | 0,0 | 0,0 (khác nhau ở phần đuôi) |
| Câu mỗi đoạn | 0,661 | người > AI | 9,0 | 6,0 |
| Tỷ lệ nén zlib | 0,627 | AI > người | 0,530 | 0,552 |
| Từ mỗi câu | 0,565 | AI > người | 27,8 | 30,2 |
| Liên từ hình thức/1k | 0,560 | AI > người | 0,0 | 0,0 |
| **Điểm scan tổng hợp** | **0,529** | (ng > AI) | 1,0 | 3,0 |
| Trợ từ cuối câu/1k | 0,524 | ng > AI | 0,0 | 0,0 |
| Từ láy, từ nối khẩu ngữ, chấm than, CV đoạn | ~0,50-0,55 | — | 0,0 | 0,0 |

## Phát hiện trung thực

1. **Điểm scan tổng hợp KHÔNG phân tách được** (AUC 0,529 = tung đồng xu) trên register
   bách khoa/báo chí. Nó chỉ hoạt động trên register chatbot/blog (self-test 55 vs 0).
   Trùng khớp kết luận của avoid-ai-writing trên corpus HC3+RAID (0,501). Máy quét là
   công cụ *biên tập bề mặt*, không phải bộ phát hiện.
2. **MATTR ngược hướng suy đoán**: AI có vốn từ "đa dạng" hơn (xịt từ đồng nghĩa),
   văn người lặp từ khoá chủ đề nhiều hơn. Cảnh báo "TTR/MATTR thấp = AI" đã bị gỡ bỏ.
3. 4 chỉ số nhịp học tách rất mạnh: CV câu (0,99), TTR (0,94), MATTR (0,91), entropy
   dấu câu (0,85). Đây là tầng đáng tin hơn nhiều so với danh sách từ.

## Ngưỡng đã hiệu chỉnh trong máy quét

| Quy tắc cảnh báo | FP trên 21 mẫu người | TPR trên 21 mẫu AI |
|---|---|---|
| CV câu < 0,28 (đổi từ 0,35) | 0/21 | 16/21 (76%) |
| Entropy dấu câu < 1,0 bit (mới) | 3/21 (14%) | 14/21 (67%) |
| Kết hợp 2 quy tắc | 3/21 | 18/21 (86%) |

Hướng viết lại từ dữ liệu: **phân bố độ dài câu rộng hơn** (luân phiên câu ngắn-dài),
**lặp từ khoá chủ đề tự nhiên** thay vì xoay vòng từ đồng nghĩa, **làm giàu hệ dấu câu**
(hai chấm, ngoặc, ngắt quãng đời thường).

## Hạn chế (đọc trước khi dùng số liệu)

- n nhỏ (21+21), một mô hình AI duy nhất, một ngày lấy mẫu; AI do chính trợ lý viết
  (bias tự biết dấu hiệu — dù đã cố viết ở chế độ mặc định).
- Corpus chỉ bao register trang trọng (bách khoa, báo chí). Trợ từ cuối câu, từ láy,
  từ nối khẩu ngữ có md = 0 ở cả hai nhóm: **chưa kiểm chứng được trên register khẩu
  ngữ/blog**, nơi chúng dự kiến phát huy tác dụng ([HL] giữ nguyên).
- Mẫu người và AI khác độ dài/hình thức nhẹ (wiki có đề mục đã được lọc; báo có mốc
  định lượng) — còn nhiễu confound.
- Không khẳng định tổng quát cho các mô hình AI khác, cho văn sáng tác, hay cho tiếng
  Việt chuẩn miền Nam/Bắc riêng.
