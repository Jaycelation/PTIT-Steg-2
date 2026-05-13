# Instructor Notes

Lab: Giấu tin trong miền không gian ảnh bằng phương pháp hoán vị điểm ảnh

The checkwork is file-based. It does not inspect `.bash_history`.

Expected SHA-256:

`7aad003b360006da660f867970e3c65ee552f64de9127fad95b081e15aebe948`

The student workflow is:

```bash
cd ~/image-spatial-permutation-embed
python3 tools/check_image_metadata.py
python3 tools/check_permutation_plan.py
python3 tools/run_permutation_embed.py
python3 tools/run_permutation_extract.py
python3 tools/report_metrics.py
```
