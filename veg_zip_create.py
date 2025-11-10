from pathlib import Path
import zipfile
import sys

# --- Path setup ---
SEARCH_ROOT = Path("C:/Users/Jagad/Desktop/vegetable_images")
ZIP_PATH = Path("C:/Users/Jagad/Desktop/Veg_Fruit_Leafy_Marathi.zip")

EXTS = [".jpg", ".jpeg", ".png", ".webp"]

print(f"[Info] Search root: {SEARCH_ROOT}")

if not SEARCH_ROOT.exists():
    print(f"[Error] images folder सापडला नाही: {SEARCH_ROOT}")
    sys.exit(1)

count = 0
with zipfile.ZipFile(str(ZIP_PATH), "w", zipfile.ZIP_DEFLATED) as zipf:
    for p in SEARCH_ROOT.rglob("*"):
        if p.is_file() and p.suffix.lower() in EXTS:
            zipf.write(p, p.relative_to(SEARCH_ROOT).as_posix())
            count += 1
            print(f"[Add] {p.relative_to(SEARCH_ROOT)}")

print(f"\n✅ Done! Added files: {count}")
print(f"📦 ZIP तयार झाला: {ZIP_PATH} (Size: {ZIP_PATH.stat().st_size} bytes)")
