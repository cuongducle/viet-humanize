# viet-humanize

[![MIT](https://img.shields.io/github/license/cuongducle/viet-humanize?style=flat-square)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/cuongducle/viet-humanize?style=flat-square&color=111111)](https://github.com/cuongducle/viet-humanize)

**Skill giúp AI viết tiếng Việt bớt sáo, rõ ý và đúng giọng hơn.**

AI thường viết đúng ngữ pháp nhưng đọc vẫn cứng: mở bài quá xa vấn đề, dùng từ trang trọng không cần thiết, nói lại một ý qua nhiều câu. `viet-humanize` hướng dẫn agent biên tập những chỗ đó mà không làm đổi nội dung.

Skill dùng cho cả viết mới lẫn sửa bài. Sau khi được agent nạp, skill được áp dụng khi viết tiếng Việt, không cần chọn chế độ hoặc nhắc lại một bộ quy tắc trong mỗi yêu cầu.

## Ví dụ

Hai ví dụ minh họa dưới đây tập trung vào cách diễn đạt, không thêm dữ kiện vào bản sửa.

### Bài hướng dẫn: bớt vòng vo

**Trước**

> Việc chia nhỏ công việc thành các bước cụ thể sẽ giúp bạn dễ dàng bắt đầu hơn. Điều quan trọng là cần xác định bước đầu tiên và tập trung hoàn thành bước đó trước khi chuyển sang bước tiếp theo.

**Sau**

> Chia công việc thành từng bước nhỏ cho dễ bắt đầu. Chọn bước đầu tiên, làm xong rồi mới sang bước tiếp theo.

### Email công việc: lịch sự mà không cứng

**Trước**

> Mình xin gửi bạn bản nháp bài viết trong file đính kèm. Rất mong bạn dành thời gian xem xét và gửi lại phản hồi trước 15h hôm nay, nhằm đảm bảo mình có đủ thời gian hoàn thiện bài viết trước 17h.

**Sau**

> Mình gửi bạn bản nháp bài viết trong file đính kèm. Bạn xem và góp ý giúp mình trước 15h hôm nay nhé, để mình kịp sửa xong trước 17h.

Không phải bài nào cũng cần rút ngắn hoặc thêm từ thân mật. Email gửi khách hàng, tài liệu kỹ thuật và bài đăng cá nhân cần cách viết khác nhau. Nếu có mẫu giọng của bạn, agent sẽ dựa vào mẫu đó.

## Cài đặt

### pi

```bash
pi install git:github.com/cuongducle/viet-humanize
```

### Claude Code

Thêm marketplace rồi cài plugin trong Claude Code:

```text
/plugin marketplace add cuongducle/viet-humanize
/plugin install viet-humanize@viet-humanize
```

Repo có sẵn manifest cho cách cài này, nhưng chưa kiểm thử toàn bộ luồng cài trên Claude Code.

### Agent khác

```bash
git clone https://github.com/cuongducle/viet-humanize.git
```

Thêm thư mục vừa tải vào nơi agent nạp skill, theo hướng dẫn của agent đó. File chính là [`SKILL.md`](SKILL.md). Giữ cả `scripts/` và `references/` đi kèm.

Nếu agent dùng `AGENTS.md` làm hướng dẫn dự án, bạn có thể ghép [bản quy tắc rút gọn](AGENTS.md) vào file đang có. Đừng ghi đè các quy tắc riêng của dự án. Chỉ clone repo mà chưa cấu hình nạp thì skill chưa hoạt động.

## Cách dùng

Yêu cầu agent làm việc như bình thường:

```text
Viết bài giới thiệu tính năng này dựa trên ghi chú bên dưới.
```

```text
Sửa bài này cho dễ đọc hơn. Giữ cách xưng hô và các chi tiết của mình.
```

```text
Sửa phần mô tả trong README.md, giữ nguyên code và các lệnh cài đặt.
```

Khi viết hoặc sửa, agent áp dụng quy tắc của skill và ghi ngắn những thay đổi đáng chú ý. Nếu bạn chỉ nhờ kiểm tra, agent nhận xét chứ chưa sửa văn bản.

Bạn không cần tự chạy máy quét để dùng skill. Agent có thể chạy script khi môi trường có Python 3.

## Nguyên tắc biên tập

- **Nói thẳng vào việc.** Bỏ phần dẫn nhập chung chung, để người đọc sớm biết bài đang nói về gì.
- **Sửa cách diễn đạt, giữ nội dung.** Không tự thêm số liệu, nguồn, thành tích hay trải nghiệm cá nhân. Khi sửa file, giữ code, URL và đường dẫn.
- **Đọc theo ngữ cảnh.** Không thay từ theo danh sách cứng. Từ chuyên môn đúng nghĩa thì giữ, câu trang trọng phù hợp thì không cần làm thân mật hơn.
- **Giữ giọng người viết.** Nhất quán cách xưng hô, tôn trọng phương ngữ và mẫu văn được cung cấp. Không rải tiếng lóng hoặc cố tình thêm lỗi chính tả.

Quy trình gồm quét văn bản, đọc toàn bài, viết lại rồi rà lần nữa. Với file, agent còn so bản trước và sau để phát hiện thay đổi ngoài ý muốn. Chi tiết nằm trong [`SKILL.md`](SKILL.md).

## Cơ sở của skill

Các quy tắc có nhãn nguồn để phân biệt kết quả nghiên cứu với quan sát và giả thuyết. Nguồn tham khảo gồm *Signs of AI writing* của WikiProject AI Cleanup, nghiên cứu ViDetect và các phép đo tiếng Việt trong repo.

Riêng văn trò chuyện có tập **77 bài Threads được tuyển chọn, 12 bộ trả lời và 30 bài AI cùng chủ đề**, cùng phép đối chiếu trên **16.319 bình luận ViHSD**. Các phép đo cho thấy dấu hiệu có ích ở văn trang trọng có thể không còn hữu ích ở chat. Vì vậy, skill không dùng chung một ngưỡng cho mọi loại văn.

Đây vẫn là các tập khảo sát nhỏ, có giới hạn về cách chọn mẫu và mô hình được thử. Chúng hỗ trợ xây dựng quy tắc, chưa chứng minh mức cải thiện chất lượng khi dùng skill.

- [Danh mục dấu hiệu và ví dụ](references/patterns-full.md)
- [Nguồn trích dẫn và những điểm chưa kiểm chứng](references/sources.md)
- [Phương pháp xây dựng skill](references/methodology.md)
- [Kết quả đo ban đầu](references/calibration.md), [v2](references/eval-v2.md), [Luna](references/eval-luna.md) và [Threads](references/eval-threads.md)

## Công cụ kiểm tra

`scripts/vi_scan.py` dùng thư viện chuẩn của Python 3, không cần cài thêm thư viện. Chạy từ thư mục repo:

```bash
# Tìm những chỗ cần đọc lại
python3 scripts/vi_scan.py scan FILE.md

# So số liệu, URL, code và frontmatter giữa hai bản
python3 scripts/vi_scan.py verify TRUOC.md SAU.md

# Kiểm tra script
python3 scripts/vi_scan.py selftest
```

Máy quét chỉ tìm dấu hiệu đã được lập danh mục. `verify` báo khác biệt nhưng không hiểu nghĩa câu, nên vẫn cần đọc đối chiếu. Điểm scan thấp không chứng minh văn bản hay hoặc do người viết.

**Skill là công cụ biên tập, không phải bộ phát hiện AI và không cam kết vượt qua detector.**

## Đóng góp

Nếu skill sửa lệch nghĩa hoặc làm mất giọng, hãy [mở issue](https://github.com/cuongducle/viet-humanize/issues) kèm bản trước, bản sau và ngữ cảnh. Bỏ thông tin riêng tư trước khi gửi.

Thêm dấu hiệu mới thì ghi ví dụ và nguồn vào `references/patterns-full.md`. Đổi quy tắc trong `SKILL.md` thì cập nhật cả `AGENTS.md`. Dữ liệu khảo sát nằm trong `corpus/`, script nghiên cứu nằm trong `research/`.

Trước khi gửi thay đổi, chạy:

```bash
python3 scripts/vi_scan.py selftest
git diff --check
```

## Giấy phép

[MIT](LICENSE).
