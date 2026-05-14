# Giau tin trong mien khong gian anh bang LSB Matching

Day la lab LSB Matching, khong phai LSB replacement co ban.

Voi LSB replacement, khi bit can giau khac LSB hien tai, thuat toan ghi de truc tiep bit cuoi cua pixel. Voi LSB Matching, khi LSB hien tai khong khop bit can giau, pixel duoc tang hoac giam 1 don vi. Neu pixel bang 0 thi chi duoc tang len 1. Neu pixel bang 255 thi chi duoc giam xuong 254. Cac pixel nam trong khoang 1..254 se chon `+1` hoac `-1` bang PRNG seed.

Vi vay LSB Matching tao thay doi dang `+1/-1` tren gia tri pixel thay vi set bit bang phep toan bit. Khi tach, ta van doc LSB cua pixel sau matching.

## Chay lab

```bash
cd ~/image-spatial-lsb-matching
python3 tools/check_image_metadata.py
python3 tools/run_lsb_matching_embed.py
python3 tools/run_lsb_matching_extract.py
python3 tools/report_matching_metrics.py
```

## Ket qua

Tat ca ket qua duoc ghi trong thu muc `work/`:

- `image_metadata.txt`: thong tin anh grayscale va capacity.
- `stego.png`: anh sau khi nhung bang LSB Matching.
- `embed.log`: marker nhung, so pixel thay doi, so lan `+1`, so lan `-1`.
- `answer.txt`: thong diep tach lai.
- `answer.sha256`: SHA-256 cua thong diep tach lai.
- `metrics.json`: `changed_pixels`, `plus_one_count`, `minus_one_count`, `mse`, `psnr`, va `histogram_delta_simple`.
