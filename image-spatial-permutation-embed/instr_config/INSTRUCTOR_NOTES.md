# Ghi chú cho giảng viên

Lab: Giấu tin trong miền không gian ảnh bằng phương pháp hoán vị điểm ảnh

Checkwork của lab dựa trên file trong thư mục `work/`. Lab không kiểm tra `.bash_history`.

SHA-256 kỳ vọng:

`7aad003b360006da660f867970e3c65ee552f64de9127fad95b081e15aebe948`

Quy trình sinh viên cần chạy:

```bash
cd ~/image-spatial-permutation-embed
python3 tools/check_image_metadata.py
python3 tools/check_permutation_plan.py
python3 tools/run_permutation_embed.py
python3 tools/run_permutation_extract.py
python3 tools/report_metrics.py
```
