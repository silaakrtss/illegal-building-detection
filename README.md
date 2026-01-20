# Illegal Building Detection

Bu proje, uydu veya hava görüntüleri üzerinden
kaçak yapıların otomatik olarak tespit edilmesini amaçlayan
bir bilgisayarlı görü (Computer Vision) çalışmasıdır.

Proje kapsamında YOLOv8 tabanlı bir nesne tespit modeli
etiketlenmiş veriler kullanılarak eğitilmiştir.

---

##  Proje Amacı

- Kaçak yapıların görüntüler üzerinden otomatik tespiti
- Nesne tespit algoritmaları ile manuel denetim yükünün azaltılması
- Gerçek dünya senaryolarına uygun bir model geliştirilmesi

---

## Kullanılan Teknolojiler

- Python
- YOLOv8 (Ultralytics)
- PyTorch
- OpenCV
- NumPy
- Matplotlib
- AnyLabeling 

---

## 📁 Proje Yapısı

```text
illegal-building-detection/
├── train.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── dataset/
│   └── README.md
│
├── results/
│   ├── results.png
│   └── confusion_matrix.png
│   └── README.md
