import zipfile
import os

# --- Source folder path (auto resolve for any OS) ---
current_dir = os.path.dirname(os.path.abspath(__file__))
source_folder = os.path.join(current_dir, "images", "vegetable_images")

# --- Output ZIP file name ---
zip_filename = os.path.join(current_dir, "Veg_Fruit_Leafy_Marathi.zip")

# --- Check if folder exists ---
if not os.path.exists(source_folder):
    print(f"⚠️ Error: Folder सापडला नाही -> {source_folder}")
    exit(1)

# --- Create ZIP file ---
with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            filepath = os.path.join(root, file)
            zipf.write(filepath, os.path.relpath(filepath, source_folder))

print(f"✅ ZIP फाईल तयार झाली: {zip_filename}")
