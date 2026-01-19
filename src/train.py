import os
import random
import shutil
from ultralytics import YOLO

# --- AYARLAR ---
dataset_path = "dataset"
images_folder = os.path.join(dataset_path, "images")
labels_folder = os.path.join(dataset_path, "labels")
classes_file = os.path.join(dataset_path, "classes.txt")

train_ratio = 0.8
epochs = 100
imgsz = 640

# ---  classes.txt oku ---
with open(classes_file, "r") as f:
    class_names = [line.strip() for line in f.readlines()]

# --- SADECE ham görselleri al (train/val yokken) ---
all_images = [
    f for f in os.listdir(images_folder)
    if f.lower().endswith((".jpg", ".png"))
]

random.shuffle(all_images)
split = int(len(all_images) * train_ratio)
train_images = all_images[:split]
val_images = all_images[split:]

# ---  train / val klasörlerini oluştur ---
for subset in ["train", "val"]:
    os.makedirs(os.path.join(images_folder, subset), exist_ok=True)
    os.makedirs(os.path.join(labels_folder, subset), exist_ok=True)

# --- DOSYALARI KOPYALA  ---
def copy_files(img_list, subset):
    for img in img_list:
        shutil.copy(
            os.path.join(images_folder, img),
            os.path.join(images_folder, subset, img)
        )

        label_file = img.rsplit(".", 1)[0] + ".txt"
        shutil.copy(
            os.path.join(labels_folder, label_file),
            os.path.join(labels_folder, subset, label_file)
        )

copy_files(train_images, "train")
copy_files(val_images, "val")

# ---  dataset.yaml oluştur ---
yaml_path = os.path.join(dataset_path, "dataset.yaml")
with open(yaml_path, "w") as f:
    f.write(f"path: {dataset_path}\n")
    f.write("train: images/train\n")
    f.write("val: images/val\n")
    f.write(f"nc: {len(class_names)}\n")
    f.write(f"names: {class_names}\n")

# --- YOLOv8 ile TRAIN ---
model = YOLO("yolov8n.pt")
model.train(
    data=yaml_path,
    epochs=epochs,
    imgsz=imgsz
)
