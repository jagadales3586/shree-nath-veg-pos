import os
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

# ---------- सेटिंग्स ----------
ROOT_WIDTH = 1200
ROOT_HEIGHT = 800
IMAGE_FOLDER = "images/vegetable_images"   # तुमचे फोटो इथे ठेवा

# --------- उदाहरणार्थ काही भाज्या (तुम्ही ही लिस्ट वाढवू शकता) ----------
vegetables = [
    {"name": "बटाटा", "price": 40, "image": "batata.webp"},
    {"name": "टोमॅटो", "price": 30, "image": "tomato.webp"},
    {"name": "कांदा", "price": 25, "image": "onion.webp"},
    {"name": "कोबी", "price": 20, "image": "cabbage.webp"},
    {"name": "भेंडी", "price": 35, "image": "bhendi.webp"},
    {"name": "गाजर", "price": 45, "image": "gajar.webp"},
    {"name": "वांगी", "price": 30, "image": "vangi.webp"},
    {"name": "मिरची", "price": 80, "image": "mirchi.webp"},
    {"name": "काकडी", "price": 30, "image": "kakdi.webp"},
    {"name": "मका", "price": 25, "image": "corn.webp"},
    {"name": "पालेभाजी", "price": 20, "image": "palak.webp"},
    {"name": "लसूण", "price": 150, "image": "lasun.webp"},
    {"name": "आलं", "price": 120, "image": "aale.webp"},
    {"name": "भोपळा", "price": 25, "image": "bhopla.webp"},
    {"name": "फुलकोबी", "price": 50, "image": "phoolkobi.webp"},
    # अजून भरून घ्या...
]

# ---------- मुख्य विंडो ----------
root = Tk()
root.title("Shree Nath Veg POS")
root.geometry(f"{ROOT_WIDTH}x{ROOT_HEIGHT}")
root.configure(bg="white")

# शीर्ष बार (असला हवा असल्यास)
top_frame = Frame(root, bg="#2e7d32", height=60)
top_frame.pack(fill=X)
Label(top_frame, text="🧺 Shree Nath Veg POS", bg="#2e7d32", fg="white",
      font=("Arial", 18, "bold"), pady=10).pack()

# मुख्य कंटेनर — डावा (grid canvas) आणि उजवा (details panel)
container = Frame(root, bg="white")
container.pack(fill=BOTH, expand=True, padx=10, pady=10)

# --- डावा भाग: स्क्रोल करण्यायोग्य ग्रिड ---
left_frame = Frame(container, bg="white")
left_frame.pack(side=LEFT, fill=BOTH, expand=True)

# Canvas + vertical scrollbar
canvas = Canvas(left_frame, bg="white", highlightthickness=0)
v_scroll = Scrollbar(left_frame, orient=VERTICAL, command=canvas.yview)
canvas.configure(yscrollcommand=v_scroll.set)

v_scroll.pack(side=RIGHT, fill=Y)
canvas.pack(side=LEFT, fill=BOTH, expand=True)

# Inner frame inside canvas to place grid
grid_frame = Frame(canvas, bg="white")
canvas.create_window((0, 0), window=grid_frame, anchor="nw")

# Resize handler for canvas scrollregion
def on_frame_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))
grid_frame.bind("<Configure>", on_frame_configure)

# Enable mousewheel scrolling on canvas (Windows & others)
def _on_mousewheel(event):
    canvas.yview_scroll(int(-1*(event.delta/120)), "units")
canvas.bind_all("<MouseWheel>", _on_mousewheel)

# Keep references to images to avoid garbage collection
image_refs = {}

# Function called when user clicks a veg card
selected = {"name": None, "price": None, "image": None}
def select_vegetable(veg):
    selected["name"] = veg["name"]
    selected["price"] = veg["price"]
    selected["image"] = veg["image"]
    update_detail_panel()

# Create grid of veg cards (3 per row by default)
COLUMNS = 3
card_padx = 12
card_pady = 12
thumb_size = (160, 120)

for idx, veg in enumerate(vegetables):
    r = idx // COLUMNS
    c = idx % COLUMNS

    card = Frame(grid_frame, relief="ridge", borderwidth=1, bg="white")
    card.grid(row=r, column=c, padx=card_padx, pady=card_pady, sticky="n")

    # Load image if available
    img_path = os.path.join(IMAGE_FOLDER, veg["image"])
    if os.path.exists(img_path):
        try:
            im = Image.open(img_path)
            im = im.resize(thumb_size, Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(im)
            image_refs[f"{veg['name']}_{idx}"] = photo
            img_label = Label(card, image=photo, bg="white")
            img_label.pack(padx=10, pady=8)
            # click bind
            img_label.bind("<Button-1>", lambda e, v=veg: select_vegetable(v))
        except Exception as e:
            Label(card, text="फोटो लोड नाही\n", bg="white", fg="red").pack(pady=8)
    else:
        Label(card, text="❌ फोटो नाही", bg="white", fg="red").pack(pady=8)

    # Name and price labels
    Label(card, text=veg["name"], font=("Arial", 12, "bold"), bg="white").pack()
    Label(card, text=f"₹{veg['price']}/kg", font=("Arial", 11), bg="white", fg="#555555").pack()

    # Selectable frame click
    card.bind("<Button-1>", lambda e, v=veg: select_vegetable(v))

# --- उजवा भाग: तपशील पॅनेल ---
right_frame = Frame(container, width=340, bg="#f7f7f7", relief="groove", borderwidth=1)
right_frame.pack(side=RIGHT, fill=Y, padx=(10,0))

# Detail elements
detail_title = Label(right_frame, text="भाजी माहिती", bg="#f7f7f7", font=("Arial", 14, "bold"))
detail_title.pack(pady=10)

# Photo placeholder in detail
detail_img_label = Label(right_frame, text="", bg="#f7f7f7")
detail_img_label.pack(pady=10)

# Name, price, weight input, total
name_var = StringVar()
price_var = StringVar()
weight_var = StringVar()
total_var = StringVar()

Label(right_frame, text="नाव:", bg="#f7f7f7", anchor="w").pack(fill=X, padx=10)
name_entry = Entry(right_frame, textvariable=name_var, font=("Arial", 12))
name_entry.pack(fill=X, padx=10, pady=5)

Label(right_frame, text="दर (₹/kg):", bg="#f7f7f7", anchor="w").pack(fill=X, padx=10)
price_entry = Entry(right_frame, textvariable=price_var, font=("Arial", 12))
price_entry.pack(fill=X, padx=10, pady=5)

Label(right_frame, text="वजन (kg):", bg="#f7f7f7", anchor="w").pack(fill=X, padx=10)
weight_entry = Entry(right_frame, textvariable=weight_var, font=("Arial", 12))
weight_entry.pack(fill=X, padx=10, pady=5)

def calc_total():
    try:
        p = float(price_var.get())
        w = float(weight_var.get())
        total_var.set(f"₹{p * w:.2f}")
    except Exception:
        total_var.set("₹0.00")

ttk.Button(right_frame, text="किंमत मोजा", command=calc_total).pack(pady=8)

Label(right_frame, text="एकूण:", bg="#f7f7f7", anchor="w").pack(fill=X, padx=10)
total_label = Label(right_frame, textvariable=total_var, bg="#f7f7f7", font=("Arial", 14, "bold"))
total_label.pack(pady=5)

# Add to cart listbox
Label(right_frame, text="कार्ट:", bg="#f7f7f7", anchor="w").pack(fill=X, padx=10, pady=(10,0))
cart_box = Listbox(right_frame, height=8)
cart_box.pack(fill=X, padx=10, pady=5)

def add_to_cart():
    if name_var.get() and weight_var.get() and price_var.get():
        item = f"{name_var.get()} - {weight_var.get()}kg - {total_var.get()}"
        cart_box.insert(END, item)
        weight_var.set("")
        total_var.set("₹0.00")

ttk.Button(right_frame, text="कार्टमध्ये जोडा", command=add_to_cart).pack(pady=6)

# Remove selected from cart
def remove_from_cart():
    sel = cart_box.curselection()
    if sel:
        cart_box.delete(sel[0])
ttk.Button(right_frame, text="डिलीट", command=remove_from_cart).pack(pady=4)

# Function to update detail panel when a veg is selected
def update_detail_panel():
    # update image
    img_name = selected.get("image")
    if img_name:
        img_path = os.path.join(IMAGE_FOLDER, img_name)
        if os.path.exists(img_path):
            try:
                im = Image.open(img_path)
                im = im.resize((220, 160), Image.ANTIALIAS)
                photo = ImageTk.PhotoImage(im)
                detail_img_label.configure(image=photo, text="")
                detail_img_label.image = photo
            except Exception as e:
                detail_img_label.configure(text="फोटो लोड नाही", image="")
                detail_img_label.image = None
        else:
            detail_img_label.configure(text="फोटो फाईल नाही", image="")
            detail_img_label.image = None
    else:
        detail_img_label.configure(text="", image="")
        detail_img_label.image = None

    # update text fields
    name_var.set(selected.get("name") or "")
    price_var.set(str(selected.get("price") or ""))

# Initialize detail panel empty
total_var.set("₹0.00")
update_detail_panel()

# Run mainloop
root.mainloop()
