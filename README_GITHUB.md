# 🧬 Veri Madenciliği Projesi - İlaçlar ve Yan Etkiler Analizi

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/engindalgiC86-cpu/UU_VMIK_DRUGS/blob/main/veri_madenciligi_projesi.ipynb)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-Educational-green.svg)]()

Bu proje, ilaçlar ve yan etkileri içeren veri seti üzerinde kapsamlı bir veri madenciliği analizi gerçekleştirmektedir.

---

## 🚀 Hızlı Başlangıç

### Google Colab'da Çalıştırma (Önerilen - Kurulum Gerektirmez!)

1. **Yukarıdaki "Open in Colab" butonuna tıklayın** 🖱️
2. Google hesabınızla giriş yapın
3. `real_drug_dataset.csv` dosyasını Colab'a yükleyin:
   - Sol menüden 📁 simgesine tıklayın
   - Dosyayı sürükle-bırak yapın
4. **Runtime → Run all** ile tüm analizi çalıştırın
5. HTML çıktısı almak için notebook sonuna şu kodu ekleyin:
   ```python
   !pip install nbconvert -q
   !jupyter nbconvert --to html *.ipynb --no-input
   from google.colab import files
   import glob
   for html in glob.glob('*.html'):
       files.download(html)
   ```

### Lokal Kurulum

```bash
# Repository'i klonlayın
git clone https://github.com/engindalgiC86-cpu/UU_VMIK_DRUGS.git
cd UU_VMIK_DRUGS

# Gerekli paketleri yükleyin
pip install pandas numpy matplotlib seaborn scipy jupyter

# Jupyter'i başlatın
jupyter notebook veri_madenciligi_projesi.ipynb
```

---

## 📊 Proje İçeriği

Bu notebook 9 kapsamlı veri madenciliği analizi içerir:

1. ✅ **Temel İstatistikler** - Sayısal değişkenler için özet istatistikler
2. ✅ **Kategorik Görselleştirme** - Pasta grafikleri ile kategorik analiz
3. ✅ **Hastalık-Tedavi Süresi Analizi** - Boxplot görselleştirmesi
4. ✅ **İlaç-Yan Etki İlişkileri** - 2D Histogram ve frekans analizi
5. ✅ **Hiyerarşik Kümeleme** - Seaborn clustermap ile pattern tespiti
6. ✅ **Korelasyon Analizi** - Yaş ve iyileşme skoru ilişkisi
7. ✅ **Cinsiyet Bazlı Analiz** - Normalize edilmiş hastalık oranları
8. ✅ **Yan Etki Analizi** - Baş dönmesi vakalarının detaylı incelemesi
9. ✅ **İlaç Odaklı Analiz** - Metoprolol için özel yan etki profili

### 📈 Çıktılar

- **9 Profesyonel Görselleştirme** (PNG formatında)
- **İstatistiksel Analizler** ve yorumları
- **HTML Rapor** çıktısı

---

## 📁 Dosya Yapısı

```
UU_VMIK_DRUGS/
│
├── veri_madenciligi_projesi.ipynb    # Ana Jupyter Notebook (51 KB)
├── real_drug_dataset.csv             # Veri seti (100 KB altında)
├── README.md                          # Bu dosya
├── BASLANGIC.md                       # Başlangıç rehberi
├── HIZLI_BASLANGIC.md                # Hızlı başlangıç kılavuzu
├── COLAB_HTML_CIKTI_REHBERI.md       # HTML çıktısı alma rehberi
├── veri_seti_kontrol.py              # Veri seti kontrol aracı
├── colab_html_olustur.py             # HTML oluşturma scripti
└── convert_to_html.py                # Lokal HTML dönüştürme
```

---

## 🛠️ Gereksinimler

### Python Kütüphaneleri

- `pandas` - Veri manipülasyonu
- `numpy` - Sayısal hesaplamalar
- `matplotlib` - Temel görselleştirme
- `seaborn` - İleri seviye görselleştirme
- `scipy` - İstatistiksel analizler
- `jupyter` - Notebook ortamı

### Kurulum

```bash
pip install pandas numpy matplotlib seaborn scipy jupyter
```

---

## 📖 Kullanım Kılavuzları

- **[BASLANGIC.md](BASLANGIC.md)** - Genel başlangıç rehberi
- **[HIZLI_BASLANGIC.md](HIZLI_BASLANGIC.md)** - 3 dakikalık hızlı başlangıç
- **[COLAB_HTML_CIKTI_REHBERI.md](COLAB_HTML_CIKTI_REHBERI.md)** - Google Colab'da HTML çıktısı alma
- **[GITHUB_COLAB_LINK_REHBERI.md](GITHUB_COLAB_LINK_REHBERI.md)** - GitHub-Colab entegrasyonu

---

## 🎯 Öğrenme Hedefleri

Bu projeyi tamamladığınızda:

- ✅ Veri analizi ve ön işleme teknikleri
- ✅ İstatistiksel test ve yorumlama
- ✅ Veri görselleştirme best practices
- ✅ Hiyerarşik kümeleme algoritmaları
- ✅ Korelasyon analizi
- ✅ Olasılık hesaplamaları

konularında deneyim kazanacaksınız.

---

## 📊 Örnek Görselleştirmeler

Proje aşağıdaki gibi profesyonel görselleştirmeler üretir:

- 📊 Boxplot grafikleri
- 🥧 Pasta grafikleri
- 🔥 Heatmap (ısı haritaları)
- 📈 Scatter plot ve korelasyon grafikleri
- 🌳 Hiyerarşik kümeleme dendrogramları

---

## ❓ Sık Sorulan Sorular

### Veri seti nereden geliyor?
100 KB altında, ilaçlar ve yan etkileri içeren bir CSV dosyası (`real_drug_dataset.csv`).

### Google Colab'da nasıl çalıştırırım?
Yukarıdaki "Open in Colab" butonuna tıklayın ve veri setini yükleyin. Runtime → Run all ile çalıştırın.

### HTML çıktısı nasıl alırım?
[COLAB_HTML_CIKTI_REHBERI.md](COLAB_HTML_CIKTI_REHBERI.md) dosyasına bakın veya notebook sonuna şu kodu ekleyin:
```python
!pip install nbconvert -q
!jupyter nbconvert --to html *.ipynb --no-input
from google.colab import files
import glob
for html in glob.glob('*.html'): files.download(html)
```

### Kodlar çalışmıyor?
1. Tüm kütüphanelerin yüklü olduğundan emin olun
2. Veri setinin doğru konumda olduğunu kontrol edin (`real_drug_dataset.csv`)
3. Hücreleri sırayla çalıştırın (Runtime → Run all)

---

## 🔍 Veri Seti Hakkında

Veri seti şu sütunları içerir:
- `Drug_Name` - İlaç isimleri
- `Side_Effects` - Yan etkiler
- `Condition` - Hastalık türü
- `Treatment_Duration_days` - Tedavi süresi (gün)
- `Age` - Hasta yaşı
- `Gender` / `Sex` - Cinsiyet
- `Improvement_Score` - İyileşme skoru
- Ve daha fazlası...

---

## 🤝 Katkıda Bulunma

Bu proje eğitim amaçlıdır. Önerileriniz için issue açabilirsiniz.

---

## 📝 Lisans

Bu proje eğitim amaçlı hazırlanmıştır.

---

## 👨‍💻 Geliştirici

**Kullanıcı:** engindalgiC86-cpu  
**Repository:** UU_VMIK_DRUGS  
**Tarih:** 2024

---

## 🎓 Teşekkürler

Bu proje Veri Madenciliğinde İleri Konular dersi kapsamında hazırlanmıştır.

---

**⭐ Projeyi beğendiyseniz yıldız vermeyi unutmayın!**

[![GitHub stars](https://img.shields.io/github/stars/engindalgiC86-cpu/UU_VMIK_DRUGS.svg?style=social&label=Star)](https://github.com/engindalgiC86-cpu/UU_VMIK_DRUGS)
