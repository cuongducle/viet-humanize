# Eval GPT-5.6-Luna trên ngưỡng v2

Mẫu Luna được sinh sau khi chuyển model (`PI_MODEL=gpt-5.6-luna`). So sánh với corpus người v2 và AI cũ. Ngưỡng được khóa từ v2, không điều chỉnh theo kết quả Luna. Đây là test model-switch, chưa phải blind test: cùng chủ đề và cùng ngữ cảnh dự án.

## TRANG TRỌNG (20 mẫu)

| chỉ số | AUC Luna | hướng | median người | median Luna | median AI cũ |
|---|---:|---|---:|---:|---:|
| `bien_dong_do_dai_cau_cv` | 0.965 | ng>AI | 0.43 | 0.19 | 0.22 |
| `ty_le_tu_rieng_ttr_am_tiet` | 0.955 | AI>ng | 0.62 | 0.77 | 0.74 |
| `mattr_cua_so_50` | 0.931 | AI>ng | 0.86 | 0.93 | 0.92 |
| `entropy_dau_cau_bit` | 0.816 | ng>AI | 1.33 | 0.99 | 1.00 |
| `do_nen_zlib` | 0.819 | AI>ng | 0.53 | 0.60 | 0.57 |
| `diem_scan` | 0.728 | ng>AI | 1.00 | 0.00 | 0.00 |
| `lech_do_dai_cau_skew` | 0.689 | ng>AI | 0.55 | 0.16 | 0.35 |
| `han_viet_lex/1k` | 0.635 | AI>ng | 3.12 | 6.58 | 5.68 |
| `tu_chuc_nang` | 0.547 | AI>ng | 0.21 | 0.23 | 0.19 |
| `pho_tu/1k` | 0.530 | ng>AI | 4.05 | 6.33 | 5.75 |
| `tro_tu_cuoi_cau_tren_1000` | 0.501 | AI>ng | 0.00 | 0.00 | 0.00 |
| `tu_lay` | 0.525 | AI>ng | 0.00 | 0.00 | 0.00 |
| `tu_noi_khau_ngu` | 0.500 | AI>ng | 0.00 | 0.00 | 0.00 |
| `lien_tu_hinh_thuc_tren_1000` | 0.534 | ng>AI | 0.00 | 0.00 | 0.00 |
| `cau_trung_binh_doan` | 0.630 | ng>AI | 9.00 | 7.00 | 7.00 |

Ngưỡng khóa từ v2 (không tối ưu lại):

- `bien_dong_do_dai_cau_cv` <= 0.29: FP người 0/20, TP Luna 18/20
- `entropy_dau_cau_bit` <= 0.96: FP người 1/20, TP Luna 8/20
- `han_viet_lex/1k` >= 17.045: FP người 1/20, TP Luna 2/20


## KHẨU NGỮ (12 mẫu)

| chỉ số | AUC Luna | hướng | median người | median Luna | median AI cũ |
|---|---:|---|---:|---:|---:|
| `bien_dong_do_dai_cau_cv` | 1.000 | ng>AI | 0.54 | 0.26 | 0.14 |
| `ty_le_tu_rieng_ttr_am_tiet` | 1.000 | AI>ng | 0.53 | 0.78 | 0.80 |
| `mattr_cua_so_50` | 0.854 | AI>ng | 0.90 | 0.93 | 0.95 |
| `entropy_dau_cau_bit` | 0.764 | ng>AI | 1.40 | 1.00 | 1.00 |
| `do_nen_zlib` | 1.000 | AI>ng | 0.46 | 0.60 | 0.57 |
| `diem_scan` | 0.733 | ng>AI | 2.00 | 0.00 | 0.00 |
| `lech_do_dai_cau_skew` | 0.656 | ng>AI | 0.63 | 0.29 | -0.19 |
| `han_viet_lex/1k` | 0.649 | ng>AI | 4.34 | 0.00 | 10.75 |
| `tu_chuc_nang` | 0.896 | AI>ng | 0.22 | 0.30 | 0.20 |
| `pho_tu/1k` | 0.639 | AI>ng | 4.22 | 13.25 | 0.00 |
| `tro_tu_cuoi_cau_tren_1000` | 0.649 | ng>AI | 0.00 | 0.00 | 0.00 |
| `tu_lay` | 0.500 | AI>ng | 0.00 | 0.00 | 0.00 |
| `tu_noi_khau_ngu` | 0.500 | AI>ng | 0.00 | 0.00 | 0.00 |
| `lien_tu_hinh_thuc_tren_1000` | 0.660 | ng>AI | 2.10 | 0.00 | 0.00 |
| `cau_trung_binh_doan` | 1.000 | AI>ng | 1.70 | 7.00 | 7.00 |

Ngưỡng khóa từ v2 (không tối ưu lại):

- `bien_dong_do_dai_cau_cv` <= 0.21: FP người 0/12, TP Luna 4/12
- `entropy_dau_cau_bit` <= 0.98: FP người 0/12, TP Luna 6/12
- `han_viet_lex/1k` >= 16.854: FP người 1/12, TP Luna 0/12


## Đọc kết quả

- AUC Luna vẫn cao chỉ cho thấy chỉ số tách được hai nhóm trong bộ mẫu này; không phải bằng chứng model Luna nói chung luôn như vậy.
- Nếu median Luna gần AI cũ ở một chỉ số, đó là tín hiệu có thể xuyên model. Nếu lệch mạnh, nhiều khả năng là tật riêng của model hoặc prompt.
- Ngưỡng khóa chỉ có ý nghĩa khi giữ được FP/TP trên Luna; không được chọn lại threshold sau khi xem kết quả.
