# Eval corpus v4-threads (2026-09-25)

Corpus: 24 bài Threads Việt Nam (khẩu ngữ thật, đã ẩn danh) và 12 bài AI cùng chủ đề viết ở chế độ mặc định, thu bằng Chrome thật qua browser-skill. Chi tiết: corpus/v4-threads/manifest.md.

### THREADS: 77 người vs 30 AI

| chỉ số | AUC | hướng | md người | md AI |
|---|---|---|---|---|
| `do_nen_zlib` | 0.920 | ng>AI | 0.74 | 0.58 |
| `han_viet_lex/1k` | 0.762 | AI>ng | 0.00 | 5.75 |
| `ty_le_tu_rieng_ttr_am_tiet` | 0.757 | ng>AI | 0.83 | 0.74 |
| `pho_tu/1k` | 0.706 | AI>ng | 0.00 | 11.49 |
| `mattr_cua_so_50` | 0.697 | AI>ng | 0.85 | 0.91 |
| `diem_scan` | 0.661 | AI>ng | 0.00 | 0.00 |
| `han_viet_hanh_chinh_tren_1000` | 0.645 | AI>ng | 0.00 | 0.00 |
| `tro_tu_cuoi_cau_tren_1000` | 0.641 | ng>AI | 0.00 | 0.00 |
| `lech_do_dai_cau_skew` | 0.632 | AI>ng | 0.00 | 0.52 |
| `tu_chuc_nang` | 0.623 | AI>ng | 0.24 | 0.26 |
| `entropy_dau_cau_bit` | 0.610 | AI>ng | 1.00 | 1.27 |
| `lien_tu_hinh_thuc_tren_1000` | 0.583 | AI>ng | 0.00 | 0.00 |
| `cau_trung_binh_doan` | 0.567 | ng>AI | 2.67 | 2.33 |
| `so_dau_bang_than` | 0.545 | ng>AI | 0.00 | 0.00 |
| `dai_cau_tb` | 0.534 | AI>ng | 20.80 | 21.40 |
| `tu_noi_khau_ngu` | 0.526 | ng>AI | 0.00 | 0.00 |
| `tu_lay` | 0.514 | AI>ng | 0.00 | 0.00 |
| `bien_dong_do_dai_cau_cv` | 0.512 | AI>ng | 0.35 | 0.35 |

Trợ từ cuối câu, từng file (trên 1000 âm tiết):

| bên | số file > 0 | trung vị | max |
|---|---|---|---|
| người | 27/77 | 0.0 | 83.3 |
| AI | 3/30 | 0.0 | 8.4 |
| replies | 7/12 | 3.7 | 57.1 |

Fightin' words (30 cặp khớp chủ đề):

AI lệch dương: tôi (+8.1), khi (+5.0), một (+4.3), đồng (+4.1), việc (+4.1), và (+3.9), nhận (+3.7), nhiều (+3.4), mức (+3.3), trong (+3.3), chi (+3.2), những (+3.2)
Người lệch âm: mình (-7.3), thì (-5.1), mà (-4.5), mẹ (-4.1), đi (-3.8), t (-3.8), em (-3.8), 1 (-3.7), rồi (-3.4), con (-3.4), có (-3.3), anh (-3.1)

## Đọc kết quả (bản 77 vs 30, đợt 3 phủ 19 chủ đề)

- zlib qua ba lần đo (24, 44 rồi 77 bài) lần lượt 0,918 - 0,912 - 0,920: tín hiệu ổn định nhất của register này. Người 0,74 so với AI 0,58.
- Hán Việt trừu tượng 0,762 (AI 5,75, người 0) và phó từ cường độ 0,706 (AI 11,49, người 0): văn chat thật gần như không dùng hai loại từ này.
- TTR toàn cục vẫn nghiêng người (0,757; người 0,83, AI 0,74), MATTR-50 vẫn AI cao hơn (0,697). Kết luận giữ nguyên: người đa dạng từ toàn cục nhờ tiếng lóng, viết tắt, trộn Anh; AI đều tay trong từng cửa sổ.
- Trợ từ cuối câu (B8): bài dài người 27/77 file có (35%), AI 3/30 (10%, tối đa 8,4/1000); replies 7/12 bộ có, trung vị 3,7, tối đa 57,1/1000. Hiện tượng có/không tách rõ hơn mật độ: trợ từ là dấu hiệu tồn tại của register chat, không phải thước đo đều.
- Fightin' words thêm hai phát hiện mới ở phía người: viết tắt xưng hô "t" và cách viết số thẳng "1" thay "một". Phía AI vẫn là bộ tôi, khi, một, đồng, việc, nhận, nhiều, mức.
- CV độ dài câu về 0,512 khi mẫu lớn: khẳng định luôn đây không phải tín hiệu của register chat.

## Giới hạn

- AI-side là một mô hình ở chế độ mặc định, 30 cặp. Chủ đề đã phủ 19 nhóm đời sống: việc làm, lương, sếp, nhà trọ, chia tay, học lại, dọn nhà, cuối tuần, nấu ăn, khám bệnh, mẹ chồng, hôn nhân, dạy con, gym, thú cưng, xe máy, cà phê, hàng xóm, tiết kiệm.
- Replies 12 bộ, khoảng 2.400 từ. Mật độ trợ từ dao động rộng theo chủ đề; khoảng tin cậy cho B8 vẫn cần thêm mẫu ở các chủ đề trung tính (gợi ý, hỏi xin kinh nghiệm) hiện thưa trợ từ.
- Vài bài trong corpus có thể do AI sinh để kéo tương tác; đã loại listicle và quảng cáo nhưng không loại được bài kể chuyện do AI viết khéo.
- Điểm scan tổng hợp 0,661: máy quét chỉ là công cụ biên tập bề mặt, đúng chủ trương của skill.
