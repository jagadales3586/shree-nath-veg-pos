import os
import zipfile

# --- Get full folder path for images ---
folder_path = os.path.join(os.getcwd(), "images", "vegetable_images")

# --- ZIP file name ---
zip_filename = "Veg_Fruit_Leafy_Marathi.zip"

# --- Create ZIP file ---
with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            arcname = os.path.relpath(file_path, folder_path)
            zipf.write(file_path, arcname)
            print(f"🟢 Added: {file_path}")

print(f"✅ ZIP तयार झाला: {zip_filename}")
