# Giấu tin trong miền không gian ảnh bằng phương pháp LSB

Lab này dùng ảnh `output/input.png` và nhúng thông điệp vào bit ít quan trọng nhất của các kênh màu RGB.

Chạy lần lượt:

```bash
cd ~/image-spatial-lsb-embed
python3 tools/check_image_metadata.py
python3 tools/run_lsb_embed.py
python3 tools/run_lsb_extract.py
python3 tools/report_metrics.py
```

Các kết quả được ghi trong thư mục `work/`:

- `image_metadata.txt`: thông tin ảnh và capacity.
- `stego.png`: ảnh sau khi giấu tin.
- `embed.log`: log quá trình nhúng.
- `answer.txt`: thông điệp tách lại.
- `answer.sha256`: mã băm SHA-256 của thông điệp.
- `metrics.json`: số pixel thay đổi, MSE và PSNR.
