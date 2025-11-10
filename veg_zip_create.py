# veg_zip_create.py
from pathlib import Path
import zipfile
import sys

ROOT = Path(__file__).resolve().parent
SEARCH_ROOT = ROOT / "images"        # फक्त images घ्या; आत काय आहे ते स्कॅन करू
ZIP_PATH = ROOT / "Veg_Fruit_Leafy_Marathi.zip"
EXTS = {".jpg", ".jpeg", ".png", ".webp"}

print(f"[info] CWD: {Path.cwd()}")
print(f"[info] Script dir: {ROOT}")
print(f"[info] Search root: {SEARCH_ROOT}")

if not SEARCH_ROOT.exists():
    print(f"[error] images folder सापडला नाही: {SEARCH_ROOT}")
    sys.exit(1)

count = 0
with zipfile.ZipFile(ZIP_PATH, "w", zipfile.ZIP_DEFLATED) as z:
    for p in SEARCH_ROOT.rglob("*"):
        if p.is_file() and p.suffix.lower() in EXTS:
            # ZIP मध्ये images/ पासून relative path जतन करा
            z.write(p, p.relative_to(SEARCH_ROOT))
            count += 1
            if count <= 5:
                print(f"[add] {p.relative_to(SEARCH_ROOT)}")

print(f"[done] Added files: {count}")
print(f"[done] ZIP size: {ZIP_PATH.stat().st_size if ZIP_PATH.exists() else 0} bytes")

if count == 0:
    print("[error] एकही image add नाही—repo path तपासा.")
    sys.exit(2)
