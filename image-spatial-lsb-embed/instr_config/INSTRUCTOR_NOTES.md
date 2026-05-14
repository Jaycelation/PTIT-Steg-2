# Ghi chú cho giảng viên

Lab: Giấu tin trong miền không gian ảnh bằng phương pháp LSB

Checkwork của lab dựa trên file trong thư mục `work/`. Lab không kiểm tra `.bash_history`.

SHA-256 kỳ vọng:

`e0a1dde22dd527770740bd1dc4d42f62cc74affe42370d36460e5bf102965354`

Quy trình sinh viên cần chạy:

```bash
cd ~/image-spatial-lsb-embed
python3 tools/check_image_metadata.py
python3 tools/run_lsb_embed.py
python3 tools/run_lsb_extract.py
python3 tools/report_metrics.py
```
