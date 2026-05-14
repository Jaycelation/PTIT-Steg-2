# PTIT-Steg-2

Kho lưu trữ này chứa 2 bài Labtainer về chủ đề giấu tin trong miền không gian ảnh:

- `image-spatial-lsb-embed`: Giấu tin trong miền không gian ảnh bằng phương pháp LSB.
- `image-spatial-permutation-embed`: Giấu tin trong miền không gian ảnh bằng phương pháp hoán vị điểm ảnh.

Mỗi bài có file `HUONG_DAN.md` riêng để hướng dẫn kiểm tra, đóng gói, build Docker image và chạy trên Labtainer VM.

## Cách chạy nhanh trên Labtainer VM

```bash
imodule https://github.com/Jaycelation/PTIT-Steg-2/raw/refs/heads/master/image-spatial-lsb-embed.tar
labtainer image-spatial-lsb-embed
```

```bash
imodule https://github.com/Jaycelation/PTIT-Steg-2/raw/refs/heads/master/image-spatial-permutation-embed.tar
labtainer image-spatial-permutation-embed
```

Hai lab đã khai báo `REGISTRY jaycedang` trong `start.config`, vì vậy Labtainer sẽ tự kéo Docker image tương ứng từ DockerHub khi khởi động lab.
