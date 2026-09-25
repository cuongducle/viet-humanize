# Eval corpus v4-threads (2026-09-25)

Corpus: 24 bài Threads Việt Nam (khẩu ngữ thật, đã ẩn danh) và 12 bài AI cùng chủ đề viết ở chế độ mặc định, thu bằng Chrome thật qua browser-skill. Chi tiết: corpus/v4-threads/manifest.md.

### THREADS: 44 người vs 18 AI

| chỉ số | AUC | hướng | md người | md AI |
|---|---|---|---|---|
| `do_nen_zlib` | 0.912 | ng>AI | 0.77 | 0.57 |
| `ty_le_tu_rieng_ttr_am_tiet` | 0.842 | ng>AI | 0.86 | 0.73 |
| `han_viet_lex/1k` | 0.801 | AI>ng | 0.00 | 5.75 |
| `lech_do_dai_cau_skew` | 0.757 | AI>ng | 0.00 | 0.70 |
| `pho_tu/1k` | 0.754 | AI>ng | 0.00 | 6.13 |
| `diem_scan` | 0.720 | AI>ng | 0.00 | 3.00 |
| `lien_tu_hinh_thuc_tren_1000` | 0.639 | AI>ng | 0.00 | 0.00 |
| `tro_tu_cuoi_cau_tren_1000` | 0.627 | ng>AI | 0.00 | 0.00 |
| `han_viet_hanh_chinh_tren_1000` | 0.627 | AI>ng | 0.00 | 0.00 |
| `dai_cau_tb` | 0.609 | AI>ng | 20.00 | 21.60 |
| `mattr_cua_so_50` | 0.602 | AI>ng | 0.89 | 0.91 |
| `entropy_dau_cau_bit` | 0.602 | AI>ng | 1.00 | 1.27 |
| `bien_dong_do_dai_cau_cv` | 0.576 | AI>ng | 0.27 | 0.36 |
| `so_dau_bang_than` | 0.568 | ng>AI | 0.00 | 0.00 |
| `tu_chuc_nang` | 0.555 | AI>ng | 0.25 | 0.26 |
| `cau_trung_binh_doan` | 0.527 | AI>ng | 2.00 | 2.33 |
| `tu_noi_khau_ngu` | 0.523 | ng>AI | 0.00 | 0.00 |
| `tu_lay` | 0.505 | AI>ng | 0.00 | 0.00 |

Trợ từ cuối câu, từng file (trên 1000 âm tiết):

| bên | số file > 0 | trung vị | max |
|---|---|---|---|
| người | 13/44 | 0.0 | 83.3 |
| AI | 1/18 | 0.0 | 4.8 |
| replies | 5/7 | 3.7 | 57.1 |

Fightin' words (18 cặp khớp chủ đề):

AI lệch dương: tôi (+5.2), khi (+3.9), và (+3.4), việc (+3.4), đồng (+3.3), nhận (+3.0), mỗi (+2.8), nhiều (+2.8), một (+2.7), với (+2.7), trong (+2.6), của (+2.6)
Người lệch âm: mình (-6.5), thì (-4.2), mà (-3.8), anh (-3.3), con (-3.3), đi (-3.3), có (-2.9), mẹ (-2.5), nào (-2.5), làm (-2.4), gì (-2.4), cứ (-2.4)

## Đọc kết quả (bản 44 vs 18, 2026-09-25 đợt 2)

- zlib vẫn là tín hiệu mạnh nhất và ổn định nhất (0,912; người 0,77 cao hơn AI 0,57): văn người lộn xộn vì lỗi chính tả, viết tắt, emoji. Khớp hướng của eval Luna.
- TTR toàn cục nghiêng về người rõ hơn khi mẫu lớn lên (0,842; người 0,86, AI 0,73), ngược register báo chí ở eval v2. MATTR-50 vẫn AI cao hơn (0,602): câu AI đều tay từng đoạn.
- Hán Việt trừu tượng (0,801, AI 5,75 so với người 0) và phó từ cường độ (0,754, AI 6,13 so với người 0) tách tốt: văn chat người gần như không dùng hai loại từ này.
- Trợ từ cuối câu (B8): bài dài người 13/44 file có (tối đa 83,3/1000, trung vị 0), AI 1/18 (4,8). Replies: 5/7 bộ có, mật độ dao động rộng từ 3,7 đến 57,1/1000 tùy chủ đề (tâm sự dày, gợi ý du lịch thưa). Kết luận giữ nguyên: B8 là tín hiệu đã đo cho văn trả lời ngắn kiểu chat, nhưng mật độ phụ thuộc chủ đề nên chỉ dùng làm chỉ báo, không dùng làm dấu hiệu quyết định.
- CV độ dài câu đổi hướng so với register trang trọng: ở đây AI đều tay hơn người (0,576, AI 0,36 so với người 0,27). Người viết chat nhiều câu very ngắn xen câu dài, AI giữ nhịp dàn đều. CV không phải tín hiệu phổ quát, đúng cảnh báo cũ.
- Fightin' words 18 cặp: phía AI là tôi, khi, việc, đồng, nhận, nhiều, một, với (bộ từ báo cáo); phía người là mình, thì, mà, anh, con, đi, mẹ, nào, gì, cứ (xưng hô và từ nối khẩu ngữ). Đối lập mình/tao với tôi là khác biệt từ vựng rõ nhất của register này.

## Giới hạn

- AI-side là một mô hình ở chế độ mặc định, 18 cặp, chủ đề việc làm, tiền, tình cảm, dọn nhà là chính.
- Replies có 7 bộ, khoảng 1.500 từ. Mật độ trợ từ dao động rộng theo chủ đề; muốn khẳng định khoảng tin cậy cho B8 cần thêm khoảng 10 bộ nữa, ưu tiên chủ đề tâm sự.
- Một số bài Threads đang thịnh hành có thể do AI sinh để kéo tương tác; cách chọn đã loại listicle và quảng cáo nhưng không loại được bài kể chuyện do AI viết khéo.
- Điểm scan tổng hợp 0,720: vẫn dưới mức dùng làm detector, đúng chủ trương của skill.
