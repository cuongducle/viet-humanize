Trong bài viết này, chúng ta sẽ cùng tìm hiểu cách thiết lập GitHub Actions cho một dự án Python một cách đơn giản và hiệu quả. Quy trình gồm 5 bước quan trọng, từ việc tạo file workflow đến kiểm tra kết quả. Trước tiên, hãy tạo thư mục .github/workflows và thêm nội dung sau đây:

```yaml
name: test
on: [push]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: python -m unittest
```

Sau khi commit, workflow sẽ chạy tự động. Nếu muốn giới hạn thời gian chạy ở 9 phút, bạn có thể thêm timeout-minutes: 9. Cách làm này giúp đội ngũ tối ưu hóa quy trình review và đảm bảo chất lượng code. Để tìm hiểu thêm, hãy truy cập https://docs.github.com/actions. Chúc bạn triển khai thành công!
