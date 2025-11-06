import zipfile
import os

# फोल्डर जिथे फोटो आहेत (तू स्वतःचे फोटो ठेवू शकतोस)
source_folder = "images/vegitable_images"

# ZIP फाईलचं नाव
zip_filename = "Veg_Fruit_Leafy_Marathi.zip"

with zipfile.ZipFile(zip_filename, "w") as zipf:
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            filepath = os.path.join(root, file)
            zipf.write(filepath, os.path.relpath(filepath, source_folder))

print(f"✅ ZIP फाईल तयार झाली: {zip_filename}")
