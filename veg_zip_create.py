import os, zipfile

# images चा पूर्ण path (CI आणि लोकल दोन्ही ठिकाणी चालेल)
folder_path = os.path.join(os.getcwd(), "images", "vegetable_images")

# आउटपुट ZIP repo root मध्येच तयार करा
zip_filename = os.path.join(os.getcwd(), "Veg_Fruit_Leafy_Marathi.zip")

print("Zipping from:", folder_path)
with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            # ZIP मधील relative path (images फोल्डरचं नाव दिसेल)
            arcname = os.path.relpath(file_path, folder_path)
            zipf.write(file_path, arcname)
            print("Added:", arcname)

print("ZIP तयार:", zip_filename)
