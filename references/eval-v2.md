# Eval corpus v2 (2026-09-21)

Thiết kế: 20 cặp trang trọng (wiki/news) và 12 cặp khẩu ý (Góc nhìn/Genk/Kenh14), AI cùng chủ đề từng cặp, viết ở chế độ mặc định, một mô hình (nêu rõ hạn chế). So với v1: hết nhiễu chủ đề trong fightin' words, thêm register khẩu ý.

### TRANG TRỌNG (20 cặp, khớp chủ đề)

| chỉ số | AUC | hướng | md người | md AI |
|---|---|---|---|---|
| `bien_dong_do_dai_cau_cv` | 0.993 | ng>AI | 0.22 | 0.43 |
| `ty_le_tu_rieng_ttr_am_tiet` | 0.915 | AI>ng | 0.62 | 0.74 |
| `mattr_cua_so_50` | 0.902 | AI>ng | 0.86 | 0.92 |
| `entropy_dau_cau_bit` | 0.748 | ng>AI | 1.00 | 1.33 |
| `do_nen_zlib` | 0.730 | AI>ng | 0.53 | 0.57 |
| `diem_scan` | 0.620 | ng>AI | 0.00 | 1.00 |
| `dai_cau_tb` | 0.620 | ng>AI | 25.60 | 27.80 |
| `lech_do_dai_cau_skew` | 0.613 | ng>AI | 0.35 | 0.55 |
| `han_viet_lex/1k` | 0.608 | AI>ng | 3.12 | 5.68 |
| `cau_trung_binh_doan` | 0.586 | ng>AI | 7.00 | 9.00 |
| `tu_chuc_nang` | 0.578 | ng>AI | 0.19 | 0.21 |
| `pho_tu/1k` | 0.540 | AI>ng | 4.05 | 5.75 |
| `han_viet_hanh_chinh_tren_1000` | 0.530 | AI>ng | 0.00 | 0.00 |
| `tro_tu_cuoi_cau_tren_1000` | 0.525 | ng>AI | 0.00 | 0.00 |
| `lien_tu_hinh_thuc_tren_1000` | 0.515 | ng>AI | 0.00 | 0.00 |

Ngưỡng (FP người tối thiểu, TP cao nhất):
- `diem_scan`: ngưỡng ≥ 42.000 -> FP người 1/20, TP AI 0/20
- `bien_dong_do_dai_cau_cv`: ngưỡng ≤ 0.290 -> FP người 0/20, TP AI 19/20
- `entropy_dau_cau_bit`: ngưỡng ≤ 0.960 -> FP người 1/20, TP AI 2/20
- `han_viet_lex/1k`: ngưỡng ≥ 17.045 -> FP người 1/20, TP AI 2/20
- `tu_chuc_nang`: ngưỡng ≤ 0.144 -> FP người 1/20, TP AI 1/20
- `tro_tu_cuoi_cau_tren_1000`: ngưỡng ≤ 0.000 -> FP người 19/20, TP AI 20/20

Fightin' words (chủ đề đã khớp):

AI lệch dương: nổi (+2.9), đấu (+2.6), hóa (+2.6), năng (+2.5), vùng (+2.5), tạo (+2.3), tượng (+2.3), sống (+2.3), đế (+2.3), với (+2.3), tính (+2.2), phong (+2.1), hàng (+2.1), tiếng (+2.0), thuật (+2.0)
Người lệch âm: năm (-3.0), một (-2.9), được (-2.5), giải (-2.4), đã (-2.4), 1 (-2.3), hoặc (-2.2), ngày (-2.2), cũng (-2.1), dưới (-2.1), tháng (-2.0), the (-1.9), và (-1.9), xe (-1.8), bởi (-1.8)

### KHẨU Ữ (12 cặp, khớp chủ đề)

| chỉ số | AUC | hướng | md người | md AI |
|---|---|---|---|---|
| `ty_le_tu_rieng_ttr_am_tiet` | 1.000 | AI>ng | 0.53 | 0.80 |
| `do_nen_zlib` | 1.000 | AI>ng | 0.46 | 0.57 |
| `cau_trung_binh_doan` | 1.000 | AI>ng | 1.70 | 7.00 |
| `bien_dong_do_dai_cau_cv` | 1.000 | ng>AI | 0.14 | 0.54 |
| `mattr_cua_so_50` | 0.990 | AI>ng | 0.90 | 0.95 |
| `entropy_dau_cau_bit` | 0.938 | ng>AI | 1.00 | 1.40 |
| `diem_scan` | 0.764 | ng>AI | 0.00 | 2.00 |
| `lech_do_dai_cau_skew` | 0.750 | ng>AI | -0.19 | 0.63 |
| `lien_tu_hinh_thuc_tren_1000` | 0.726 | ng>AI | 0.00 | 2.10 |
| `dai_cau_tb` | 0.715 | AI>ng | 22.90 | 25.60 |
| `han_viet_lex/1k` | 0.681 | AI>ng | 4.34 | 10.75 |
| `tu_chuc_nang` | 0.667 | ng>AI | 0.20 | 0.22 |
| `tro_tu_cuoi_cau_tren_1000` | 0.649 | ng>AI | 0.00 | 0.00 |
| `pho_tu/1k` | 0.566 | ng>AI | 0.00 | 4.22 |
| `han_viet_hanh_chinh_tren_1000` | 0.556 | AI>ng | 0.00 | 0.00 |
| `tu_lay` | 0.542 | AI>ng | 0.00 | 0.00 |

Ngưỡng (FP người tối thiểu, TP cao nhất):
- `diem_scan`: ngưỡng ≥ 15.000 -> FP người 1/12, TP AI 0/12
- `bien_dong_do_dai_cau_cv`: ngưỡng ≤ 0.210 -> FP người 0/12, TP AI 12/12
- `entropy_dau_cau_bit`: ngưỡng ≤ 0.980 -> FP người 0/12, TP AI 6/12
- `han_viet_lex/1k`: ngưỡng ≥ 16.854 -> FP người 1/12, TP AI 3/12
- `tu_chuc_nang`: ngưỡng ≤ 0.148 -> FP người 1/12, TP AI 1/12
- `tro_tu_cuoi_cau_tren_1000`: ngưỡng ≤ 0.000 -> FP người 7/12, TP AI 11/12

Fightin' words (chủ đề đã khớp):

AI lệch dương: về (+3.1), hội (+3.0), nhân (+2.9), giới (+2.9), sản (+2.8), cầu (+2.8), ít (+2.7), xã (+2.7), thương (+2.7), cơ (+2.6), mạnh (+2.5), thực (+2.5), vùng (+2.4), cho (+2.4), chất (+2.4)
Người lệch âm: vào (-2.2), khoảng (-2.1), anh (-1.8), tôi (-1.8), một (-1.8), năm (-1.8), trường (-1.8), hợp (-1.8), chơi (-1.8), thời (-1.7), lý (-1.7), khi (-1.7), có (-1.7), được (-1.6), còn (-1.6)
