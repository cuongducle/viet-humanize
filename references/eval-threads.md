# Eval corpus v4-threads (2026-09-25)

Corpus: 24 bài Threads Việt Nam (khẩu ngữ thật, đã ẩn danh) và 12 bài AI cùng chủ đề viết ở chế độ mặc định, thu bằng Chrome thật qua browser-skill. Chi tiết: corpus/v4-threads/manifest.md.

### THREADS: 24 người vs 12 AI

| chỉ số | AUC | hướng | md người | md AI |
|---|---|---|---|---|
| `do_nen_zlib` | 0.918 | ng>AI | 0.75 | 0.57 |
| `han_viet_lex/1k` | 0.812 | AI>ng | 0.00 | 5.81 |
| `ty_le_tu_rieng_ttr_am_tiet` | 0.781 | ng>AI | 0.84 | 0.75 |
| `lien_tu_hinh_thuc_tren_1000` | 0.708 | AI>ng | 0.00 | 0.00 |
| `mattr_cua_so_50` | 0.705 | AI>ng | 0.86 | 0.91 |
| `pho_tu/1k` | 0.688 | AI>ng | 0.00 | 5.88 |
| `diem_scan` | 0.681 | AI>ng | 0.00 | 0.00 |
| `lech_do_dai_cau_skew` | 0.653 | AI>ng | 0.00 | 0.72 |
| `dai_cau_tb` | 0.649 | AI>ng | 20.00 | 21.90 |
| `tro_tu_cuoi_cau_tren_1000` | 0.646 | ng>AI | 0.00 | 0.00 |
| `han_viet_hanh_chinh_tren_1000` | 0.642 | AI>ng | 0.00 | 0.00 |
| `cau_trung_binh_doan` | 0.609 | ng>AI | 3.00 | 2.33 |
| `tu_chuc_nang` | 0.576 | AI>ng | 0.24 | 0.26 |
| `entropy_dau_cau_bit` | 0.566 | AI>ng | 1.29 | 1.27 |
| `so_dau_bang_than` | 0.562 | ng>AI | 0.00 | 0.00 |
| `bien_dong_do_dai_cau_cv` | 0.557 | ng>AI | 0.40 | 0.29 |
| `tu_noi_khau_ngu` | 0.542 | ng>AI | 0.00 | 0.00 |

Trợ từ cuối câu, từng file (trên 1000 âm tiết):

| bên | số file > 0 | trung vị | max |
|---|---|---|---|
| người | 7/24 | 0.0 | 26.3 |
| AI | 0/12 | 0.0 | 0.0 |
| replies | 2/2 | 57.1 | 57.1 |

Fightin' words (12 cặp khớp chủ đề):

AI lệch dương: tôi (+3.4), khi (+3.2), với (+3.0), đồng (+3.0), và (+2.9), việc (+2.5), nhập (+2.4), nhiều (+2.4), thu (+2.3), mức (+2.3), chi (+2.1), triệu (+2.1)
Người lệch âm: mình (-5.0), thì (-3.3), con (-3.3), mà (-3.1), đi (-2.8), còn (-2.7), mẹ (-2.6), làm (-2.5), tao (-2.2), phải (-2.1), mày (-2.0), cô (-2.0)

## Đọc kết quả

- zlib là tín hiệu mạnh nhất trên register này (0,918, người 0,75 cao hơn AI 0,57): văn người lộn xộn hơn hẳn, lỗi chính tả, viết tắt, emoji làm văn bản khó nén. Khớp hướng của eval Luna (khẩu ý 1,000).
- Hán Việt trừu tượng tách tốt ở đây (0,812, AI 5,81/1000 so với người 0): sau Luna, lần này tín hiệu lại đúng hướng cũ. Kết luận của mục 12 (chỉ dùng làm tín hiệu yếu cho văn trang trọng) vẫn giữ, nhưng thêm dữ kiện: trên văn chat thật, phía người gần như không dùng loại từ này.
- TTR toàn cục lần đầu nghiêng về người (0,781, người 0,84 cao hơn AI 0,75), ngược với register báo chí ở eval v2. Trộn Anh, tiếng lóng và viết tắt khiến mực từ của người rộng hơn. MATTR cửa sổ 50 vẫn AI cao hơn (0,705): câu AI đều tay về từ vựng trong từng đoạn.
- Trợ từ cuối câu (B8): AI 0/12 file, bài Threads dài 7/24 file (tối đa 26,3/1000), còn hai bộ replies cùng đạt 57,1/1000. Vậy B8 không tách ở bài dài (người kể chuyện nhiều câu cũng viết tương đối trơn), nhưng tách rõ ở tầng trả lời ngắn. Nâng B8 từ "giả thuyết" lên "tín hiệu đã đo cho văn trả lời ngắn", vẫn không dùng cho văn dài.
- CV độ dài câu chỉ còn 0,557 trên register này: văn chat người thật nhiều câu ngắn xen câu dài kiểu riêng, AI mặc định cũng ngắn. Tín hiệu vua của register trang trọng mất sức ở đây, đúng cảnh báo cũ không dùng một ngưỡng cho mọi kiểu văn.
- Fightin' words khớp chủ đề: phía AI là tôi, khi, với, đồng, việc, thu, nhập, nhiều, mức, chi, triệu (bộ từ bàn về tiền lương kiểu báo cáo); phía người là mình, thì, con, mà, đi, mẹ, tao, mày, cô (đại từ xưng hô và từ nối khẩu ngữ). Đối lập xưng hô mình/tao/mày với tôi là tín hiệu từ vựng rõ nhất của register này.

## Giới hạn

- AI-side là một mô hình ở chế độ mặc định, 12 cặp, chủ đề tài chính việc làm là chính.
- Replies mới có 2 bộ, 457 từ. Muốn khẳng định B8 cho tầng ngắn cần thêm khoảng 10 bộ replies nữa.
- Một số bài Threads đang thịnh hành có thể do AI sinh để kéo tương tác; cách chọn đã loại kiểu listicle nhưng không loại được bài kể chuyện do AI viết khéo.
- Điểm scan tổng hợp 0,681: vẫn dưới mức dùng làm detector, đúng chủ trương của skill.
