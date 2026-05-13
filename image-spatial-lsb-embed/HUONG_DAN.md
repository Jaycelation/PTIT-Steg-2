# Huong dan bai image-spatial-lsb-embed

Ten tieng Viet: Giấu tin trong miền không gian ảnh bằng phương pháp LSB

## Muc tieu

- Kiem tra anh dau vao va tinh capacity.
- Nhung thong diep vao bit it quan trong nhat cua kenh mau RGB.
- Tao anh stego va tach lai thong diep.
- Kiem chung ket qua bang SHA-256 trong `instr_config/results.config`.

## Cau truc quan trong

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

## Lenh sinh vien chay trong Labtainer

```bash
cd ~/image-spatial-lsb-embed
python3 tools/check_image_metadata.py
python3 tools/run_lsb_embed.py
python3 tools/run_lsb_extract.py
python3 tools/report_metrics.py
```

## Checkwork

Lab co 5 checkwork, deu dua tren file trong `work/`:

- `image_metadata_checked`: `work/image_metadata.txt` chua `IMAGE_METADATA_OK`.
- `lsb_embed_ran`: `work/embed.log` chua `LSB_EMBED_OK`.
- `lsb_extract_ran`: `work/extract.log` chua `LSB_EXTRACT_OK`.
- `answer_file_created`: `work/answer_status.txt` chua `ANSWER_FILE_CREATED`.
- `secret_recovered`: `work/answer.sha256` khop hash trong `results.config`.

## Dong goi GitHub tar

Tu thu muc repo:

```bash
tar -cf image-spatial-lsb-embed.tar image-spatial-lsb-embed
```

Kiem tra sach goi:

```bash
tar -tf image-spatial-lsb-embed.tar | grep -E "work/|answer|__pycache__|private|checker.py|generate.py|reference|LABTAINER|DEMO|EVALUATION"
```

Ket qua mong doi: khong co output.

## Build Docker image

Chay tren may co Docker va Labtainer base image:

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

docker tag image-spatial-lsb-embed.steg.student jaycedang/image-spatial-lsb-embed-steg-student:latest
docker push jaycedang/image-spatial-lsb-embed-steg-student:latest
```

Neu Labtainer VM dung registry khac, thay `registry=labtainers` bang registry dang co trong VM.

## Chay tren Labtainer VM

```bash
cd ~/labtainer/labtainer-student
imodule https://github.com/Jaycelation/PTIT-Steg-2/raw/refs/heads/master/image-spatial-lsb-embed.tar
docker pull jaycedang/image-spatial-lsb-embed-steg-student:latest
docker tag jaycedang/image-spatial-lsb-embed-steg-student:latest image-spatial-lsb-embed.steg.student
labtainer -r image-spatial-lsb-embed
```
