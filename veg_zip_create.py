from pathlib import Path
import zipfile
import sys

# फोल्डर सेटअप
SEARCH_ROOT = Path("images/vegetable_images")   # इमेजेस इथे आहेत
ZIP_PATH = Path("Veg_Fruit_Leafy_Marathi.zip")  # तयार होणारी ZIP फाइल

EXTS = [".jpg", ".jpeg", ".png", ".webp"]

print(f"[Info] Search root: {SEARCH_ROOT}")

if not SEARCH_ROOT.exists():
    print(f"[Error] Folder सापडला नाही: {SEARCH_ROOT}")
    sys.exit(1)

count = 0
with zipfile.ZipFile(ZIP_PATH, "w", zipfile.ZIP_DEFLATED) as zipf:
    for p in SEARCH_ROOT.rglob("*"):
        if p.is_file() and p.suffix.lower() in EXTS:
            zipf.write(p, p.relative_to(SEARCH_ROOT))
            count += 1
            print(f"[Add] {p.relative_to(SEARCH_ROOT)}")

print(f"\n✅ Added {count} files")
print(f"📦 ZIP तयार: {ZIP_PATH.resolve()}")
