Client gọi https://api.example.com/orders nên có cơ chế retry khi server trả lỗi 429. Tôi thường giới hạn 3 lần, chờ lần lượt 1, 2 rồi 4 giây. Endpoint này cho phép tối đa 100 request mỗi phút:

```python
for delay in [1, 2, 4]:
    response = call_api()
    if response.ok:
        break
    time.sleep(delay)
```

Mỗi lần thử nên ghi log để biết lỗi nằm ở server hay ở mạng của mình. Sau lần cuối thì trả lỗi rõ ràng cho tầng gọi bên trên. Cách này giảm việc dồn request liên tiếp, nhưng không thay thế được rate limit ở phía client. Nếu API có header Retry-After, hãy ưu tiên giá trị đó.
