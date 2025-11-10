# veg_zip_create.py
from pathlib import Path
import zipfile
import sys

# images/vegetable_images हा path नेमका repo मधून घ्या (स्क्रिप्ट जिथे आहे तिथून)
ROOT = Path(__file__).resolve().parent
FOLDER = ROOT / "images" / "vegetable_images"
ZIP_PATH = ROOT / "Veg_Fruit_Leafy_Marathi.zip"

print(f"[info] CWD: {Path.cwd()}")
print(f"[info] Script dir: {ROOT}")
print(f"[info] Images dir: {FOLDER}")

if not FOLDER.exists():
    print(f"[error] Images folder सापडला नाही: {FOLDER}")
    sys.exit(1)

count = 0
with zipfile.ZipFile(ZIP_PATH, "w", zipfile.ZIP_DEFLATED) as z:
    for p in FOLDER.rglob("*"):
        if p.is_file():
            # relative path जतन करा
            z.write(p, p.relative_to(FOLDER))
            count += 1

print(f"[info] Added files: {count}")
print(f"[info] ZIP: {ZIP_PATH} size={(ZIP_PATH.stat().st_size if ZIP_PATH.exists() else 0)} bytes")

if count == 0:
    print("[error] एकही फाइल add झाली नाही. Path तपासा.")
    sys.exit(2)
