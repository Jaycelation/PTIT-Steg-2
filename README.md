# PTIT-Steg-2

Kho luu tru nay chua cac bai Labtainer ve chu de giau tin trong mien khong gian anh:

- `image-spatial-lsb-embed`: Giau tin bang phuong phap LSB replacement co ban.
- `image-spatial-lsb-matching`: Giau tin bang phuong phap LSB Matching / +/-1 embedding.
- `image-spatial-permutation-embed`: Giau tin bang phuong phap hoan vi diem anh.

Moi bai co cau hinh Labtainer rieng de kiem tra, dong goi, build Docker image va chay tren Labtainer VM.

## Chay nhanh tren Labtainer VM

```bash
imodule https://github.com/Jaycelation/PTIT-Steg-2/raw/refs/heads/master/image-spatial-lsb-embed.tar
labtainer image-spatial-lsb-embed
```

```bash
imodule https://github.com/Jaycelation/PTIT-Steg-2/raw/refs/heads/master/image-spatial-lsb-matching.tar
labtainer image-spatial-lsb-matching
```

```bash
imodule https://github.com/Jaycelation/PTIT-Steg-2/raw/refs/heads/master/image-spatial-permutation-embed.tar
labtainer image-spatial-permutation-embed
```

Hai lab cu va lab moi deu khai bao `REGISTRY jaycedang` trong `start.config`, vi vay Labtainer co the keo Docker image tu DockerHub khi khoi dong lab.
