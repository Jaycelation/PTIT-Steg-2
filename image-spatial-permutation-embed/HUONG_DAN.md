# Huong dan bai image-spatial-permutation-embed

Ten tieng Viet: Giấu tin trong miền không gian ảnh bằng phương pháp hoán vị điểm ảnh

## Muc tieu

- Kiem tra anh grayscale dau vao.
- Doc seed va tao ke hoach cap diem anh deterministic.
- Ma hoa bit bang quan he thu tu cua tung cap pixel.
- Tao anh stego va tach lai thong diep bang cung ke hoach cap pixel.
- Kiem chung ket qua bang SHA-256 trong `instr_config/results.config`.

## Y tuong thuat toan

Lab dung pair-order permutation, khac voi LSB:

- bit `0`: pixel[i] <= pixel[j]
- bit `1`: pixel[i] > pixel[j]
- Neu quan he chua dung, script swap gia tri hai pixel.
- Khi extract, script dung lai seed va danh sach cap pixel de doc quan he va khoi phuc bit.

## Cau truc quan trong

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

## Lenh sinh vien chay trong Labtainer

```bash
cd ~/image-spatial-permutation-embed
python3 tools/check_image_metadata.py
python3 tools/check_permutation_plan.py
python3 tools/run_permutation_embed.py
python3 tools/run_permutation_extract.py
python3 tools/report_metrics.py
```

## Checkwork

Lab co 5 checkwork, deu dua tren file trong `work/`:

- `image_metadata_checked`: `work/image_metadata.txt` chua `IMAGE_METADATA_OK`.
- `permutation_plan_checked`: `work/permutation_plan.txt` chua `PERMUTATION_PLAN_OK`.
- `permutation_embed_ran`: `work/embed.log` chua `PERMUTATION_EMBED_OK`.
- `permutation_extract_ran`: `work/extract.log` chua `PERMUTATION_EXTRACT_OK`.
- `secret_recovered`: `work/answer.sha256` khop hash trong `results.config`.

## Dong goi GitHub tar

Tu thu muc repo:

```bash
tar -cf image-spatial-permutation-embed.tar image-spatial-permutation-embed
```

Kiem tra sach goi:

```bash
tar -tf image-spatial-permutation-embed.tar | grep -E "work/|answer|__pycache__|private|checker.py|generate.py|reference|LABTAINER|DEMO|EVALUATION"
```

Ket qua mong doi: khong co output.

## Build Docker image

Chay tren may co Docker va Labtainer base image:

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

docker tag image-spatial-permutation-embed.steg.student jaycedang/image-spatial-permutation-embed-steg-student:latest
docker push jaycedang/image-spatial-permutation-embed-steg-student:latest
```

Neu Labtainer VM dung registry khac, thay `registry=labtainers` bang registry dang co trong VM.

## Chay tren Labtainer VM

```bash
cd ~/labtainer/labtainer-student
imodule https://github.com/Jaycelation/PTIT-Steg-2/raw/refs/heads/master/image-spatial-permutation-embed.tar
docker pull jaycedang/image-spatial-permutation-embed-steg-student:latest
docker tag jaycedang/image-spatial-permutation-embed-steg-student:latest image-spatial-permutation-embed.steg.student
labtainer -r image-spatial-permutation-embed
```
