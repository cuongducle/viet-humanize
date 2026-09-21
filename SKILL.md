---
name: viet-humanize
description: Biên tập văn tiếng Việt bỏ dấu văn AI, dựa trên danh mục dấu hiệu có nguồn trích dẫn (Wikipedia Signs of AI writing, dataset ViDetect, báo chí và giáo viên Việt Nam). Ba chế độ: viết lại, chỉ đánh dấu, sửa tại chỗ file. Kèm máy quét deterministic scripts/vi_scan.py và trình kiểm bảo tồn số liệu. Dùng khi người dùng nói "viết tự nhiên", "không nghe giống AI", "humanize", "bỏ dấu AI", "qua tool dò AI", "kiểm tra văn bản AI", hoặc khi viết/sửa bài tiếng Việt dài.
license: MIT
metadata:
  version: "1.3.1"
---

# Viet-humanize: biên tập văn tiếng Việt bỏ dấu AI

Mục tiêu: văn đọc như MỘT người Việt thật viết cho MỘT độc giả cụ thể, không phải chạy điểm tool dò: tool dò không đáng tin tuyệt đối và không phải tiêu chuẩn hoàn thiện (xem references/sources.md, mục Hạn chế).

Mọi dấu hiệu trong skill này có nhãn nguồn:
- **[W]** đồng bộ từ Wikipedia "Signs of AI writing" (WikiProject AI Cleanup, biên tập viên dọn rác AI hằng ngày từ 2023)
- **[VD]** phát hiện thống kê từ dataset ViDetect (6.800 bài luận tiếng Việt, arXiv 2405.03206) hoặc VietAIDetector
- **[TT]** quan sát thực tiễn bản địa: báo Việt, giáo viên, nhóm content (chưa có thống kê công khai)
- **[HL]** suy diễn từ nghiên cứu phát hiện tiếng Anh, CHƯA kiểm chứng cho tiếng Việt, chỉ dùng kèm dấu khác
- **[NN]** sự kiện mô tả chuẩn trong ngôn ngữ học tiếng Việt (Thompson 1965; Nguyễn Tài Cẩn 1975; Cao Xuân Hạo 1998), chưa phải thống kê về đầu ra AI

## Ba chế độ

1. **Viết lại (mặc định)**: đánh dấu → viết lại → quét vòng 2 → nộp kèm bảng thay đổi.
2. **Chỉ đánh dấu**: khi người dùng nói "kiểm tra", "scan", "chỉ đánh dấu". Trả về danh sách theo mức P0/P1/P2, kèm nhận định dấu nào là vấn đề thật, dấu nào có thể cố ý.
3. **Sửa tại chỗ file**: khi người dùng nêu tên file. Sửa văn xuôi, giữ nguyên code, YAML, URL, bảng, đường dẫn. Chạy `verify` trước khi nộp (xem dưới).

## Quy trình

Bước 0 (nếu người dùng đưa mẫu văn của họ): đọc mẫu trước, bám theo độ dài câu, xưng hô, phương ngữ (Bắc/Nam), dấu câu của mẫu. Mẫu ghi đè mọi quy tắc dưới đây.

Bước 1, chạy máy quét deterministic:
```bash
python3 scripts/vi_scan.py scan FILE
```
Kết quả là điểm 0-100 + danh sách theo dòng + số nhịp học: CV và độ lệch (skewness) độ dài câu/đoạn, MATTR-50, trợ từ cuối câu, liên từ hình thức, mật độ Hán Việt hành chính, từ láy, entropy dấu câu, tỷ lệ nén zlib. Các chỉ số ngôn ngữ học chỉ tham khảo báo cáo (không cộng điểm, trừ khi tích thành cảnh báo giọng sách vở). Ngưỡng nhịp học chính đã hiệu chỉnh trên corpus pilot 42 mẫu (xem references/calibration.md): CV câu < 0,28 tách 0/21 văn người vs 16/21 văn AI; điểm scan tổng hợp chỉ đạt AUC 0,529 trên register trang trọng — máy quét là công cụ biên tập bề mặt, KHÔNG phải bộ phát hiện AI. Dùng làm rà vòng 1, KHÔNG dùng làm phán quyết.

Bước 2, đọc toàn văn và đánh dấu theo danh mục trong references/patterns-full.md, mạnh nhất trước. Nhìn cả hình khối: tương phản xẻ hai câu, bộ ba ở tầm đoạn, cùng một câu chốt lặp sau mỗi phần.

Bước 3, viết lại: giữ mọi khẳng định, con số, tên riêng, trích dẫn có trong nguyên bản. Không thêm fact không có nguồn. Thiếu chi tiết thì hỏi hoặc viết câu đơn giản hơn. Đảo độ dài câu: văn người xen câu ngắn và câu dài.

Bước 4, vòng 2 (bắt buộc): chạy lại máy quét + tự đọc thành tiếng. Rà năm dấu sống sót kinh điển: một "không chỉ... mà còn", một câu chốt một dòng, một gạch ngang dài, một bộ ba, một nhãn in đậm.

Bước 5 (chế độ sửa file): kiểm bảo tồn:
```bash
python3 scripts/vi_scan.py verify TRUOC.md SAU.md
```
Vi phạm (mất số, đổi URL, đụng code) là lỗi phải sửa trước khi nộp.

## Hệ mức nghiêm trọng

- **P0, gặp một lần là sửa**: vỏ chatbot ("Chúc bạn một ngày tốt lành!", "Hy vọng thông tin này hữu ích!") [W]; mở dàn cảnh ("Hãy cùng tìm hiểu nhé!", "Trong thời đại công nghệ số hóa ngày nay...") [W][TT]; tương phản bơm "không chỉ X mà còn Y" khi vế phủ định không mang thông tin [W][TT]; câu chốt một dòng nhại lại ý đoạn trên [W]; gạch ngang dài nối câu (—, --) [W][TT]; mượn uy tín không tên ("chuyên gia cho rằng") [W][TT].
- **P1, sửa khi xuất hiện hoặc cụm lại**: từ vựng khuôn ("tối ưu hóa", "đột phá", "bứt phá", "nâng tầm", "trải nghiệm tuyệt vời", "kiến tạo", "mang đến") [TT]; né động từ "là/có" ("đóng vai trò là", "được xem là", "sở hữu") [W][HL]; khuôn "dù đối mặt thách thức... vẫn không ngừng vươn lên" [W][TT]; hạn định chất chồng ("có thể nào đó", "một cách nào đó") [W]; mở câu lặp x3; kết sáo ("tương lai tươi sáng", "chỉ có thời gian mới trả lời được") [W][TT].
- **P2, cân nhắc theo ngữ cảnh**: bộ ba liệt kê khi chỉ hai ý thật [W]; emoji trang trí, nhãn in đậm + hai chấm, đường kẻ ngang ngăn phần [W][TT]; ngoặc kép cong; dấu chấm than dàn trận [TT]; nhịp quá đều (xem nhịp học) [VD].

Chi tiết từng dấu với ví dụ trước/sau: references/patterns-full.md.

## Đặc thù tiếng Việt (khác biệt với bản tiếng Anh)

1. **Giọng dịch (translationese)**: ngữ pháp đúng nhưng không ai viết thế ("Nó là điều quan trọng cần được xem xét", "; "có một điều cần phải nói rằng"). Người Việt đặt chủ ngữ sớm, chuộng động từ mạnh, tránh chuỗi danh từ hóa "việc thực hiện việc triển khai". [TT]
2. **Xưng hô nhất quán**: văn AI hay lắc lư giữa "bạn" / "chúng ta" / "mình" trong cùng bài. Chọn một hệ xưng hô theo loại văn và giữ. [TT]
3. **Đơn vị chuẩn Việt Nam**: dấu phẩy thập phân (9,81 triệu), "tệ" thay ký hiệu tiền Trung Quốc, tên riêng Latin giữ nguyên. Thuật ngữ nền tảng Trung Quốc phải latin hóa và giải thích lần đầu (Xianyu = chợ đồ cũ của Alibaba).
4. **Sai sót nhẹ có chủ đích**: giọng blog/mạng xã hội cho phép một câu cửa miệng, một cách nói địa phương, một chỗ trùng từ. Văn người không đều tăm tắp. [HL]
5. **Kết cấu đoạn theo ViDetect**: văn AI tiếng Việt viết đoạn dài, câu ít, phân tích đơn tuyến; người viết nhiều câu hơn, đổi góc nhìn trong đoạn. Khi viết lại: tách đoạn dài, tăng chuyển động. [VD]

## Ví dụ đầy đủ (ngữ cảnh bản địa: bài chuẩn SEO, nơi văn AI dày đặc nhất ở Việt Nam)

**Trước:**
> Trong thời đại công nghệ số hóa ngày nay, việc quản lý kho hàng đã trở thành bài toán quan trọng đối với các doanh nghiệp. Hãy cùng tìm hiểu giải pháp giúp doanh nghiệp không chỉ tối ưu hóa quy trình, mà còn nâng tầm trải nghiệm khách hàng. Phần mềm quản lý kho X được xem là bước đột phá, mang đến giải pháp toàn diện, sở hữu nhiều tính năng nổi bật và đóng vai trò then chốt trong hành trình chuyển đổi số. Chuyên gia cho rằng, giải pháp này sẽ mở ra kỷ nguyên mới. Tương lai đang chờ đón bạn — hãy liên hệ ngay hôm nay!

**Sau:**
> Kho 500 mét vuông của công ty dệt Phương Đông từng mất ba ngày để kiểm kê cuối tháng. Sau ba tháng dùng phần mềm X, họ kiểm kê xong trong một buổi sáng. Máy quét mã vạch 2,2 triệu đồng một chiếc, bản quyền 9 triệu đồng một năm cho năm tài khoản. Nếu kho dưới 100 mét vuông, sổ Excel cộng một người kỹ càng vẫn rẻ hơn.

Dấu đã bắt: mở sáo thời đại [P0], "hãy cùng tìm hiểu" [P0], "không chỉ... mà còn" [P0], "được xem là + đột phá + toàn diện + sở hữu + nổi bật" [P1], "đóng vai trò then chốt" [P1], "hành trình chuyển đổi số" [P1], mượn uy tín "chuyên gia cho rằng" [P0], "mở ra kỷ nguyên mới" + "tương lai đang chờ đón" [P1], gạch ngang dài [P0], không một con số cụ thể nào.

## Ma trận dung sai theo loại văn

| Loại văn | P0 | P1 | P2 | Ghi chú |
|---|---|---|---|---|
| Blog / mạng xã hội | 0 | <= 2 | thoải mái nếu cố ý | giữ khẩu ngữ, cảm xúc, câu cụt |
| SEO / content thương mại | 0 | <= 2 | hạn chế emoji | vẫn phải có số liệu thật |
| Tiểu luận / học thuật | 0 | 0 | tối thiểu | trung tính; cẩn thận giữ trích dẫn nguyên văn |
| Tài liệu kỹ thuật | 0 | <= 1 | tối thiểu | giữ nguyên code, lệnh, đường dẫn |
| PR / thông cáo báo chí | 0 | <= 3 | thoải mái | loại văn vốn huênh hoang, chỉ cắt dấu AI, không cắt giọng PR) |

## Bảo trì

Danh mục này có hạn sử dụng: thói quen từ ngữ đổi theo từng bản mô hình. Giao thức cập nhật (học từ quy trình của blader/humanizer và WikiProject AI Cleanup):
1. Gặp cụm mới hay lặp trong đầu ra AI tiếng Việt → ghi vào references/patterns-full.md kèm ví dụ thật và nhãn nguồn.
2. Mỗi quý: đối chiếu lại Wikipedia "Signs of AI writing" (bản gốc liên tục được biên tập viên cập nhật).
3. Từ chỉ nằm ở [HL] quá lâu không kiểm chứng được thì hạ xuống P2 hoặc bỏ.
4. Chạy selftest sau mỗi chỉnh máy quét: `python3 scripts/vi_scan.py selftest`.

## Cấu trúc skill

```
viet-humanize/
├── SKILL.md                    # file này
├── references/
│   ├── patterns-full.md        # danh mục 25+ dấu hiệu, trước/sau, nhãn nguồn
│   ├── sources.md              # mọi nguồn trích dẫn + khoảng trống chưa kiểm chứng
│   └── methodology.md          # 4 trường phái quan sát + quy trình tác giả đã áp dụng
└── scripts/
    └── vi_scan.py              # máy quét + verify + selftest
```
