# Instructor Notes

Lab: Giấu tin trong miền không gian ảnh bằng phương pháp LSB

The checkwork is file-based. It does not inspect `.bash_history`.

Expected SHA-256:

`e0a1dde22dd527770740bd1dc4d42f62cc74affe42370d36460e5bf102965354`

The student workflow is:

```bash
cd ~/image-spatial-lsb-embed
python3 tools/check_image_metadata.py
python3 tools/run_lsb_embed.py
python3 tools/run_lsb_extract.py
python3 tools/report_metrics.py
```
