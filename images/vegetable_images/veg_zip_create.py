from pathlib import Path
import zipfile
import sys

# Path setup
ROOT = Path(__file__).resolve().parent
SEARCH_ROOT = ROOT / "images" / "vegetable_images"
ZIP_PATH = ROOT / "Veg_Fruit_Leafy_Marathi.zip"

EXTS = (".jpg", ".jpeg", ".png", ".webp")

print(f"[Info] Search root: {SEARCH_ROOT}")

if not SEARCH_ROOT.exists():
    print(f"[Error] Folder सापडत नाही: {SEARCH_ROOT}")
    sys.exit(1)

count = 0
with zipfile.ZipFile(ZIP_PATH, "w", zipfile.ZIP_DEFLATED) as zipf:
    for p in SEARCH_ROOT.rglob("*"):
        if p.is_file() and p.suffix.lower() in EXTS:
            zipf.write(p, p.relative_to(SEARCH_ROOT))
            count += 1
            print(f"[add] {p.relative_to(SEARCH_ROOT)}")

print(f"\n[Done] Added files: {count}")
print(f"[OK] ZIP तयार: {ZIP_PATH} (size: {ZIP_PATH.stat().st_size} bytes)")
