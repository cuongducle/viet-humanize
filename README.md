# viet-humanize

[![MIT](https://img.shields.io/github/license/cuongducle/viet-humanize?style=flat-square)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/cuongducle/viet-humanize?style=flat-square&color=111111)](https://github.com/cuongducle/viet-humanize)

**Skill viết và biên tập tiếng Việt theo ngữ cảnh.**

`viet-humanize` giúp agent diễn đạt rõ ý, bớt sáo và giữ giọng người viết. Dùng cho câu trả lời hằng ngày, email, bài viết, báo cáo, tài liệu chuyên môn, bản dịch và nội dung sáng tạo.

Không mặc định biến mọi bài thành văn ngắn hoặc giọng trò chuyện. Một lời nhắn cần đúng quan hệ xưng hô; một báo cáo cần giữ điều kiện và mức chắc chắn; một đoạn truyện có thể cần sự lặp lại và nhịp chậm.

Skill không phụ thuộc mô hình cụ thể. Sau khi được agent nạp, bạn không cần chọn chế độ hay nhắc lại quy tắc mỗi lần viết.

## Cài đặt

### pi

```bash
pi install git:github.com/cuongducle/viet-humanize
```

### Claude Code

Chạy trong Claude Code:

```text
/plugin marketplace add cuongducle/viet-humanize
/plugin install viet-humanize@viet-humanize
```

Repo có sẵn manifest cho cách cài này; luồng cài Claude Code chưa được kiểm thử đầu cuối.

### Agent khác

```bash
git clone https://github.com/cuongducle/viet-humanize.git
```

Thêm thư mục vào nơi agent nạp skill, theo hướng dẫn của agent đó. File chính là [`SKILL.md`](SKILL.md); giữ cả `scripts/` và `references/` đi kèm. Chỉ clone mà chưa cấu hình nạp thì skill chưa hoạt động.

Nếu agent đọc `AGENTS.md`, có thể ghép [bản quy tắc rút gọn](AGENTS.md) vào hướng dẫn dự án. Không ghi đè các quy tắc đang có.

## Cách dùng

Yêu cầu công việc như bình thường: soạn email, giải thích một vấn đề, sửa bài, dịch một đoạn hoặc kiểm tra cách diễn đạt. Nếu có yêu cầu về người đọc, giọng hay độ dài, đưa kèm như với bất kỳ việc viết nào.

Agent làm đúng việc được giao. Nhờ kiểm tra thì chỉ nhận xét; nhờ sửa file thì sửa trong phạm vi đó. Không tự viết lại mọi đoạn bạn dán vào, không bắt bạn chọn chế độ và không mặc định kèm bảng phân tích dài.

## Nguyên tắc

- **Giữ nghĩa.** Không tự thêm dữ kiện, bỏ điều kiện hoặc biến nhận định chưa chắc thành khẳng định.
- **Giữ giọng.** Ưu tiên mẫu của người dùng, quan hệ xưng hô và mục đích văn bản. Không ép mọi bài dùng “mình/bạn”.
- **Sửa có lý do.** Làm rõ ý mơ hồ, câu vòng vo và từ lệch nghĩa. Đoạn đã phù hợp thì giữ nguyên.
- **Không dùng danh sách từ cấm.** Từ Hán Việt, thuật ngữ Anh, câu bị động, ẩn dụ hay lời chào đều có chỗ dùng. Xét cả câu và ngữ cảnh.
- **Đọc lại sau khi sửa.** Kiểm tra ý bị mất, chi tiết tự thêm, giọng bị đổi và các phần không được đụng tới trong file.

Ví dụ: “Phương án này có thể giảm thời gian chờ, nhưng chưa được thử vào giờ cao điểm” không nên bị rút thành “Phương án này giảm thời gian chờ”. Bản ngắn hơn đã đổi cả độ chắc chắn lẫn phạm vi của nhận định.

Xem thêm [ví dụ và ngoại lệ](references/patterns-full.md) hoặc [hướng dẫn đầy đủ](SKILL.md).

## Công cụ đi kèm

Agent có thể dùng `vi_scan.py` để rà file hoặc bài dài. Script chỉ cần Python 3, không cần cài thư viện ngoài. Bạn không cần tự chạy nó để kích hoạt skill.

Chạy từ thư mục repo:

```bash
python3 scripts/vi_scan.py scan FILE.md
python3 scripts/vi_scan.py verify TRUOC.md SAU.md
python3 scripts/vi_scan.py selftest
```

`scan` tìm những mẫu cần đọc lại, không ra lệnh xóa. `verify` so số/ngày, URL, code và frontmatter giữa hai bản, không kiểm được nghĩa câu. Cả hai hỗ trợ việc đọc đối chiếu, không thay thế nó. Câu trả lời ngắn chỉ cần rà trực tiếp.

Đây là skill biên tập, không phải bộ phát hiện AI và không cam kết vượt detector. Điểm quét thấp không chứng minh văn hay hoặc đúng sự thật.

## Nội dung repo

| File | Vai trò |
|---|---|
| [`SKILL.md`](SKILL.md) | Hướng dẫn chính cho agent |
| [`AGENTS.md`](AGENTS.md) | Quy tắc rút gọn cho dự án |
| [`references/patterns-full.md`](references/patterns-full.md) | Cách xét ngữ cảnh, ví dụ sửa và giữ |
| [`references/sources.md`](references/sources.md) | Nguồn tham khảo và phạm vi sử dụng |
| [`scripts/vi_scan.py`](scripts/vi_scan.py) | Rà văn bản và kiểm tra bảo toàn |

`corpus/` và `research/` lưu dữ liệu cùng công cụ nghiên cứu riêng, không cần đọc hoặc chạy để dùng skill.

## Đóng góp

[Mở issue](https://github.com/cuongducle/viet-humanize/issues) nếu skill làm lệch nghĩa, mất giọng hoặc sửa quá tay. Gửi bản trước, bản sau và ngữ cảnh, nhớ bỏ thông tin riêng tư.

Khi thêm quy tắc, ghi rõ vấn đề cần sửa và trường hợp nên giữ. Đồng bộ `SKILL.md`, `AGENTS.md` và README; chạy `python3 scripts/vi_scan.py selftest` nếu sửa script, rồi kiểm tra bằng `git diff --check`.

## Giấy phép

[MIT](LICENSE).
