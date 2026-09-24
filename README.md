# viet-humanize

`viet-humanize` là skill giúp AI biên tập lại văn tiếng Việt cho rõ người viết, đúng ngữ cảnh và bớt những câu chữ theo khuôn. Skill không cố biến mọi bài thành một kiểu giọng chung. Nó giữ lại cách xưng hô, mức độ trang trọng và thông tin của bản gốc, sau đó sửa những chỗ nghe giống văn máy hoặc không giống cách người Việt thường viết.

Skill giữ nguyên số liệu, URL, tên riêng và code khi sửa văn bản. Nó cũng không hứa làm văn bản vượt qua mọi công cụ dò AI. Những công cụ đó có thể báo sai, nhất là với tiếng Việt. Mục tiêu ở đây là chất lượng câu chữ, không phải một con số trên màn hình.

Skill dùng được trên pi, Claude Code, Cursor và các coding agent đọc được file `SKILL.md`.

## Cài đặt

```bash
git clone https://github.com/cuongducle/viet-humanize ~/.pi/agent/skills/viet-humanize
```

Với Claude Code, đặt thư mục skill vào `~/.claude/skills/`. Cursor và các agent khác dùng thư mục skill tương ứng của từng công cụ.

## Một bản rewrite được làm như thế nào?

Đổi vài từ trong câu thường không đủ. Một bản rewrite tốt phải xem lại cả cách chọn từ, nhịp câu và mạch triển khai ý. Quy trình của skill có năm bước:

1. Máy quét rà những dấu hiệu bề mặt như câu mở đầu sáo, từ ngữ quảng cáo, gạch ngang dài và nhịp câu quá đều.
2. Người viết đọc toàn văn. Đây là bước cần thiết vì regex không biết một cụm từ có hợp với ngữ cảnh hay không.
3. Văn bản được viết lại theo sự việc cụ thể. Chủ thể, hành động, số liệu và quan hệ giữa các câu phải rõ hơn.
4. Bản mới được đọc lại một lượt. Cách đọc này thường bắt được những câu máy quét bỏ sót, chẳng hạn một ẩn dụ tự chế hoặc một câu kết chỉ lặp ý ở trên.
5. Với file cần sửa trực tiếp, lệnh `verify` đối chiếu số liệu, URL và code trước khi giao bản cuối.

Một bản rewrite nghe tự nhiên hơn nhưng làm mất một con số vẫn là bản rewrite hỏng.

## Ba cách dùng

- **Viết lại.** Dán văn bản cần sửa. Agent rà dấu hiệu, viết lại, đọc lại và quét lần hai.
- **Chỉ dò.** Đặt `chỉ dò:` ở đầu yêu cầu nếu bạn chỉ muốn xem các điểm đáng chú ý mà chưa muốn sửa.
- **Sửa file.** Nêu đường dẫn file. Agent chỉ sửa phần văn xuôi, giữ nguyên code, YAML, URL, bảng và đường dẫn, sau đó trả diff cùng kết quả kiểm tra.

Máy quét không cần thư viện ngoài Python chuẩn:

```bash
python3 scripts/vi_scan.py scan FILE.md
python3 scripts/vi_scan.py verify TRUOC.md SAU.md
python3 scripts/vi_scan.py selftest
python3 scripts/vi_scan.py calibrate corpus/human corpus/ai
```

Điểm scan chỉ cho biết văn bản có những dấu hiệu đã được lập danh mục hay chưa. Nó không kết luận ai là tác giả. Các chỉ số về nhịp câu, độ đa dạng từ và dấu câu chỉ có giá trị tham khảo trong đúng register đã được đo.

## Điều cần nhìn khi đọc lại văn bản

Máy quét không trả lời được những câu hỏi quan trọng nhất:

- Đoạn này đang nói về người, vật hay việc nào?
- Câu sau thêm thông tin, lý do, ví dụ, ngoại lệ hay hệ quả gì?
- Hai câu nối nhau vì có quan hệ thật, hay chỉ vì có một từ nối nghe mạch lạc?
- Đoạn cuối có thêm điều gì không, hay chỉ nhắc lại câu đầu?

Nếu ý là gọi đúng người, vật hoặc việc, hãy gọi thẳng tên. Nếu ý là tạo nhịp câu tự nhiên, hãy xen câu ngắn với câu dài. Không nên tự chế những ẩn dụ kiểu biên tập chỉ để câu văn có vẻ sang hơn.

## Một ít số liệu, cùng những giới hạn của chúng

Bản pilot gồm 42 mẫu tiếng Việt. Trong đó có 21 bài từ Wikipedia và VnExpress, cùng 21 bài do LLM viết theo register tương ứng. Kết quả ban đầu như sau:

| Chỉ số | AUC |
|---|---:|
| CV độ dài câu | 0,991 |
| Mật độ động từ Hán Việt | 0,719 |
| TTR âm tiết | 0,943 |
| MATTR-50 | 0,910 |
| Entropy dấu câu | 0,848 |
| Điểm scan tổng hợp | 0,529 |

Với ngưỡng CV bằng 0,28, phép thử bắt được 16/21 mẫu AI và báo nhầm 0/21 mẫu văn người. Tuy vậy, bộ mẫu còn nhỏ, phần AI do một model viết và register khẩu ngữ chưa có đủ đại diện. Không nên biến những con số này thành ngưỡng áp dụng cho mọi văn bản.

Trong lớp từ vựng, các mẫu AI dùng động từ Hán Việt trừu tượng nhiều hơn, khoảng 10,4 so với 2,6 trên 1000 âm tiết. Đây là một gợi ý để biên tập viên xem lại những câu quá trừu tượng, không phải quy tắc thay từ máy móc. Với văn thân mật, tín hiệu này có thể đổi chiều.

Điểm scan tổng hợp chỉ đạt AUC 0,529 trên register bách khoa và báo chí, gần mức đoán ngẫu nhiên. Máy quét vì thế chỉ nên làm vòng rà đầu tiên. Vòng đọc hiểu và kiểm tra sự thật vẫn thuộc về người viết.

Muốn xem toàn bộ phép đo và các giới hạn, đọc `references/calibration.md`.

## Thử với các công cụ dò AI

Các lần thử dưới đây chỉ ghi lại phản hồi của từng công cụ với bộ mẫu đã gửi. Chúng không chứng minh văn bản là do người hay máy viết.

### Sapling

Ngày 22/09/2026, ba nhóm văn bản có độ dài gần nhau được gộp thành các file DOCX rồi tải lên Sapling AI Detector:

- 10 mẫu AI thô trong `corpus/rewrite-test/raw/`
- 10 mẫu tương ứng đã qua skill trong `corpus/rewrite-test/rewritten/`
- 3 bài crawl trong `corpus/v2/human-casual/`. Đây là các bài được gắn nhãn văn người trong corpus, không phải bằng chứng tuyệt đối về tác giả.

| Nhóm | Số token theo Sapling | Nhãn `Fake` |
|---|---:|---:|
| Bản AI thô | 917 | **99,2%** |
| Bản đã qua skill | 965 | **4,4%** |
| Văn crawl | 948 | **89,8%** |

Bản rewrite giảm mạnh tín hiệu mà Sapling bắt được, từ 99,2% xuống 4,4%. Nhưng văn crawl cũng bị gắn 89,8% Fake. Kết quả này cho thấy detector có thể phản ứng mạnh với tiếng Việt, kể cả khi dữ liệu được gắn nhãn văn người.

### GPTZero

GPTZero được đăng nhập bằng Google trên Chrome thật. README dài 1.595 từ, 7.741 ký tự nhận kết quả **69% AI, 5% hỗn hợp và 26% người**, với độ tin cậy vừa phải theo giao diện công cụ.

Sau đó, toàn bộ 21 file AI trong `corpus/ai/` được gộp thành một file khoảng 4.037 từ rồi quét một lần. Kết quả tổng hợp là **86% AI, 14% hỗn hợp và 0% người**. Đây là điểm của cả tập văn bản gộp chung, không phải điểm trung bình của 21 file.

GPTZero cũng nhận đủ 21 file khi tải lên theo lô. Tuy nhiên, tài khoản miễn phí báo đã vượt giới hạn sử dụng trong ngày. Ba file đầu hiện `Error`, các file còn lại không có điểm riêng. Vì vậy chưa thể báo kết quả từng file từ lần tải theo lô này.

### Các công cụ khác

| Công cụ | Kết quả nhận được | Ghi chú |
|---|---|---|
| **TextSight** | Bản AI thô dài 2.950 ký tự: **74% AI**. Bản qua skill: **76% AI**. | Lượt thứ ba bị chặn ở giới hạn 3/3 lượt thử trong ngày. |
| **Decopy** | Bản AI thô: **5% AI**. Bản qua skill: **0% AI**. Văn crawl: **1% AI, 2% hỗn hợp, 98% người**. | Kết quả giữa các công cụ không nhất quán. |
| **Smodin** | Hiện đồng thời `AI-Generated 91%` và `Human-Written 25%`. | Số liệu bị khóa và không tạo thành một phân bổ hợp lệ. |
| **QuillBot** | Với đoạn 955 từ, trả **98% AI** và **2% người**. Bản 1.424 từ vượt giới hạn miễn phí 1.200 từ nên chỉ hiện `--`. | Chỉ là phản hồi của công cụ với đoạn văn đã gửi. |

Những kết quả này không thể dùng để xếp hạng công cụ nào đúng hơn. TextSight chấm bản qua skill cao hơn bản AI thô, trong khi Decopy và Sapling cho chiều ngược lại. Đó là lý do không nên dùng một detector để kết luận tác giả hoặc chất lượng văn bản.

## Cấu trúc thư mục

| File | Nội dung |
|---|---|
| `SKILL.md` | Quy trình năm bước, ba mức P0, P1, P2 và bảng dung sai theo loại văn |
| `scripts/vi_scan.py` | Máy quét cùng các lệnh `verify`, `selftest`, `calibrate` |
| `references/patterns-full.md` | Hơn 30 dấu hiệu trước và sau, chia lớp A, B, C, kèm nguồn |
| `references/sources.md` | Nguồn trích dẫn và những khoảng trống chưa kiểm chứng |
| `references/methodology.md` | Cách bốn skill humanize nước ngoài xây dựng danh mục quan sát |
| `references/calibration.md` | Báo cáo pilot và các ngưỡng đã thử nghiệm |
| `corpus/` và `research/` | Dữ liệu cùng script thu thập để người khác kiểm tra lại |

## Nguồn và giới hạn

Danh mục dấu hiệu bắt đầu từ bài *Signs of AI writing* của Wikipedia và dự án WikiProject AI Cleanup. Phần phương pháp tham khảo cách tự quét và đo sai báo của `avoid-ai-writing`, quy trình bản địa hóa theo từng ngôn ngữ của `jurigis`, cùng các kết quả về nhịp văn trong bộ dữ liệu ViDetect, arXiv 2405.03206. Phần chọn từ tham khảo thêm Georgiou 2025, Gude 2026 và các nguồn tiếng Việt được liệt kê trong `references/sources.md`.

Khoảng trống lớn nhất hiện nay là văn khẩu ngữ. Trợ từ cuối câu, từ láy và từ nối đời thường chưa có đủ dữ liệu để đặt thành quy tắc chắc chắn. Những tín hiệu đó chỉ nên dùng như gợi ý khi sửa blog, bài đăng mạng xã hội hoặc văn nói được chép lại.

Một văn bản đạt 0/100 vẫn chỉ có nghĩa là nó không chứa các dấu hiệu mà máy quét hiện biết. Điều đó không biến văn bản thành văn người. Người đọc, ngữ cảnh và việc kiểm tra sự thật vẫn là vòng cuối.

Giấy phép MIT.
