# Giấu tin trong miền không gian ảnh bằng phương pháp hoán vị điểm ảnh

Lab này dùng ảnh `output/input.png`, chuyển sang grayscale và mã hóa từng bit bằng quan hệ thứ tự của một cặp pixel:

- bit `0`: pixel thứ nhất nhỏ hơn hoặc bằng pixel thứ hai.
- bit `1`: pixel thứ nhất lớn hơn pixel thứ hai.

## Các bước thực hiện

```bash
cd ~/image-spatial-permutation-embed
python3 tools/check_image_metadata.py
python3 tools/check_permutation_plan.py
python3 tools/run_permutation_embed.py
python3 tools/run_permutation_extract.py
python3 tools/report_metrics.py
```

## Kết quả tạo ra

Các kết quả được ghi trong thư mục `work/`:

- `image_metadata.txt`: thông tin ảnh grayscale.
- `permutation_plan.txt`: seed, pair_count và capacity theo số cặp hợp lệ.
- `stego.png`: ảnh sau khi giấu tin.
- `embed.log`: log số cặp được dùng và số lần swap.
- `answer.txt`: thông điệp tách lại.
- `answer.sha256`: mã băm SHA-256 của thông điệp.
- `metrics.json`: số pixel thay đổi, MSE và PSNR.
