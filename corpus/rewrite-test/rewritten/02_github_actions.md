GitHub Actions có thể chạy bộ test mỗi khi bạn push code. Với một dự án Python nhỏ, workflow 5 bước là đủ. Tạo .github/workflows/test.yml, rồi dán nguyên đoạn này:

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

Commit file xong, mở tab Actions để xem kết quả. Nếu job chạy quá 9 phút, thêm timeout-minutes: 9 vào cấu hình. Tài liệu chính thức nằm ở https://docs.github.com/actions. Phần còn lại là đọc log khi test hỏng và sửa từng lỗi một.
