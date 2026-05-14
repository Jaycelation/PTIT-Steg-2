# Hướng dẫn bài `image-spatial-permutation-embed`

Tên tiếng Việt: Giấu tin trong miền không gian ảnh bằng phương pháp hoán vị điểm ảnh

## Mục tiêu

- Kiểm tra ảnh grayscale đầu vào.
- Đọc seed và tạo kế hoạch cặp điểm ảnh deterministic.
- Mã hóa bit bằng quan hệ thứ tự của từng cặp pixel.
- Tạo ảnh stego và tách lại thông điệp bằng cùng kế hoạch cặp pixel.
- Kiểm chứng kết quả bằng SHA-256 trong `instr_config/results.config`.

## Ý tưởng thuật toán

Lab dùng pair-order permutation, khác với LSB:

- bit `0`: pixel[i] <= pixel[j]
- bit `1`: pixel[i] > pixel[j]
- Nếu quan hệ chưa đúng, script swap giá trị hai pixel.
- Khi extract, script dùng lại seed và danh sách cặp pixel để đọc quan hệ và khôi phục bit.

## Cấu trúc quan trọng

```text
image-spatial-permutation-embed/
  config/
  dockerfiles/
  instr_config/
  steg/
    _bin/
    image-spatial-permutation-embed/
      README.md
      output/input.png
      output/public_config.json
      src/
      tools/
```

## Lệnh sinh viên chạy trong Labtainer

```bash
cd ~/image-spatial-permutation-embed
python3 tools/check_image_metadata.py
python3 tools/check_permutation_plan.py
python3 tools/run_permutation_embed.py
python3 tools/run_permutation_extract.py
python3 tools/report_metrics.py
```

## Checkwork

Lab có 5 checkwork, đều dựa trên file trong `work/`:

- `image_metadata_checked`: `work/image_metadata.txt` chứa `IMAGE_METADATA_OK`.
- `permutation_plan_checked`: `work/permutation_plan.txt` chứa `PERMUTATION_PLAN_OK`.
- `permutation_embed_ran`: `work/embed.log` chứa `PERMUTATION_EMBED_OK`.
- `permutation_extract_ran`: `work/extract.log` chứa `PERMUTATION_EXTRACT_OK`.
- `secret_recovered`: `work/answer.sha256` khớp hash trong `results.config`.

## Đóng gói GitHub tar

Từ thư mục repo:

```bash
tar -cf image-spatial-permutation-embed.tar image-spatial-permutation-embed
```

Kiểm tra gói không chứa file sinh ra trong lúc làm bài:

```bash
tar -tf image-spatial-permutation-embed.tar | grep -E "work/|answer|__pycache__|private|checker.py|generate.py|reference|LABTAINER|DEMO|EVALUATION"
```

Kết quả mong đợi: không có output.

## Build Docker image

Chạy trên máy có Docker và Labtainer base image:

```bash
docker build \
  -f image-spatial-permutation-embed/dockerfiles/Dockerfile.image-spatial-permutation-embed.steg.student \
  --build-arg registry=labtainers \
  --build-arg lab=image-spatial-permutation-embed.steg.student \
  --build-arg labdir=image-spatial-permutation-embed \
  --build-arg imagedir=steg \
  --build-arg user_name=student \
  --build-arg password=student \
  --build-arg apt_source= \
  -t image-spatial-permutation-embed.steg.student .

docker tag image-spatial-permutation-embed.steg.student jaycedang/image-spatial-permutation-embed.steg.student:latest
docker tag image-spatial-permutation-embed.steg.student jaycedang/image-spatial-permutation-embed-steg-student:latest
docker push jaycedang/image-spatial-permutation-embed.steg.student:latest
docker push jaycedang/image-spatial-permutation-embed-steg-student:latest
```

Tag `jaycedang/image-spatial-permutation-embed.steg.student:latest` là tag Labtainer tự kéo khi lab khai báo `REGISTRY jaycedang`.

## Chạy trên Labtainer VM

```bash
imodule https://github.com/Jaycelation/PTIT-Steg-2/raw/refs/heads/master/image-spatial-permutation-embed.tar
labtainer image-spatial-permutation-embed
```

Người dùng không cần chạy `docker pull` hoặc `docker tag` thủ công.
