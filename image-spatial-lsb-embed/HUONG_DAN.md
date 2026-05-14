# Hướng dẫn bài `image-spatial-lsb-embed`

Tên tiếng Việt: Giấu tin trong miền không gian ảnh bằng phương pháp LSB

## Mục tiêu

- Kiểm tra ảnh đầu vào và tính capacity.
- Nhúng thông điệp vào bit ít quan trọng nhất của kênh màu RGB.
- Tạo ảnh stego và tách lại thông điệp.
- Kiểm chứng kết quả bằng SHA-256 trong `instr_config/results.config`.

## Cấu trúc quan trọng

```text
image-spatial-lsb-embed/
  config/
  dockerfiles/
  instr_config/
  steg/
    _bin/
    image-spatial-lsb-embed/
      README.md
      output/input.png
      output/public_config.json
      src/
      tools/
```

## Lệnh sinh viên chạy trong Labtainer

```bash
cd ~/image-spatial-lsb-embed
python3 tools/check_image_metadata.py
python3 tools/run_lsb_embed.py
python3 tools/run_lsb_extract.py
python3 tools/report_metrics.py
```

## Checkwork

Lab có 5 checkwork, đều dựa trên file trong `work/`:

- `image_metadata_checked`: `work/image_metadata.txt` chứa `IMAGE_METADATA_OK`.
- `lsb_embed_ran`: `work/embed.log` chứa `LSB_EMBED_OK`.
- `lsb_extract_ran`: `work/extract.log` chứa `LSB_EXTRACT_OK`.
- `answer_file_created`: `work/answer_status.txt` chứa `ANSWER_FILE_CREATED`.
- `secret_recovered`: `work/answer.sha256` khớp hash trong `results.config`.

## Đóng gói GitHub tar

Từ thư mục repo:

```bash
tar -cf image-spatial-lsb-embed.tar image-spatial-lsb-embed
```

Kiểm tra gói không chứa file sinh ra trong lúc làm bài:

```bash
tar -tf image-spatial-lsb-embed.tar | grep -E "work/|answer|__pycache__|private|checker.py|generate.py|reference|LABTAINER|DEMO|EVALUATION"
```

Kết quả mong đợi: không có output.

## Build Docker image

Chạy trên máy có Docker và Labtainer base image:

```bash
docker build \
  -f image-spatial-lsb-embed/dockerfiles/Dockerfile.image-spatial-lsb-embed.steg.student \
  --build-arg registry=labtainers \
  --build-arg lab=image-spatial-lsb-embed.steg.student \
  --build-arg labdir=image-spatial-lsb-embed \
  --build-arg imagedir=steg \
  --build-arg user_name=student \
  --build-arg password=student \
  --build-arg apt_source= \
  -t image-spatial-lsb-embed.steg.student .

docker tag image-spatial-lsb-embed.steg.student jaycedang/image-spatial-lsb-embed.steg.student:latest
docker tag image-spatial-lsb-embed.steg.student jaycedang/image-spatial-lsb-embed-steg-student:latest
docker push jaycedang/image-spatial-lsb-embed.steg.student:latest
docker push jaycedang/image-spatial-lsb-embed-steg-student:latest
```

Tag `jaycedang/image-spatial-lsb-embed.steg.student:latest` là tag Labtainer tự kéo khi lab khai báo `REGISTRY jaycedang`.

## Chạy trên Labtainer VM

```bash
imodule https://github.com/Jaycelation/PTIT-Steg-2/raw/refs/heads/master/image-spatial-lsb-embed.tar
labtainer image-spatial-lsb-embed
```

Người dùng không cần chạy `docker pull` hoặc `docker tag` thủ công.
