
📄 Dosyalar

 🔹 train.py

YOLOv8 tabanlı nesne tespit modelinin eğitimi için kullanılan ana dosyadır.

Bu dosyada:
- Etiketlenmiş görüntüler kullanılarak veri seti hazırlanır
- Veri, eğitim (train) ve doğrulama (val) olarak ayrılır
- YOLO formatına uygun `dataset.yaml` dosyası oluşturulur
- Ön eğitimli YOLOv8 modeli ile model eğitimi gerçekleştirilir

Model eğitimi Ultralytics YOLOv8 kütüphanesi kullanılarak yapılmaktadır.


🔹 requirements.txt

Projenin çalıştırılabilmesi için gerekli Python kütüphanelerini içerir.

🔹 .gitignore

GitHub’a yüklenmesi gerekmeyen dosya ve klasörleri belirtir.
