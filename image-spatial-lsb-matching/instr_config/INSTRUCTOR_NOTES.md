# Instructor notes

Lab: Giau tin trong mien khong gian anh bang phuong phap LSB Matching

Checkwork uses files in `work/` and does not depend on shell history.

Expected SHA-256:

`ddf3af7daab306ea89c3005f91eaade4581e310fee2a972445951e81d2485bfb`

Student workflow:

```bash
cd ~/image-spatial-lsb-matching
python3 tools/check_image_metadata.py
python3 tools/run_lsb_matching_embed.py
python3 tools/run_lsb_matching_extract.py
python3 tools/report_matching_metrics.py
```
