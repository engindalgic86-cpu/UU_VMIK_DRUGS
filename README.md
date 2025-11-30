# 🧬 Veri Madenciliği Projesi - İlaçlar ve Yan Etkiler Analizi

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/engindalgiC86-cpu/UU_VMIK_DRUGS/blob/main/veri_madenciligi_projesi.ipynb)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-Educational-green.svg)]()

## Veri Madenciliğinde İleri Konular Projesi

**Veri Seti:** İlaçlar ve Yan Etkileri (real_drug_dataset.csv)

Hazırlayan: Mustafa Engin Dalgıç
Öğrenci No: 254309502
Program: Bilgisayar Mühendisliği Tezli Yüksek Lisans Programı
Kurum: Üsküdar Üniversitesi, Fen Bilimleri Enstitüsü
E-posta: engindalgic86@gmail.com
Bu projede, ilaçlar ve yan etkileri içeren veri seti üzerinde kapsamlı dokuz aşamalı bir veri madenciliği analizi gerçekleştirlmiştir.Program Çıktılar: Proje raporu(html), 9 görsel(png),1 html çıktısı

---

## Google Colab'da Çalıştırma 

### ✅ ADIM 1: Notebook'u Aç
Yukarıdaki **"Open in Colab"** butonuna tıklayın

### ✅ ADIM 2: Veri Setini Yükleyin

**İki seçenek var:**

####  Seçenek A: Manuel Yükleme (Basit)
1. Google Colab'da **sol menüden 📁 (Dosyalar)** simgesine tıklayın
2. ** Upload** butonuna tıklayın
3. `real_drug_dataset.csv` dosyanızı seçin ve yükleyin
4. Dosya yüklendikten sonra notebook'u çalıştırın

####  Seçenek B: Otomatik İndirme (Kaggle Account Gerektirir)
1.  Analizi Çalıştır
- **Runtime → Run all** ile tüm analizi çalıştırın
- Veya her hücreyi tek tek çalıştırın (Shift+Enter)
- Kaggle account ve şifre bilgisini girin

---

##  HTML Çıktısı Alma

Analiz tamamlandıktan sonra proje raporu adıyla çıkacaktır.


##  Proje İçeriği

Bu notebook **9 kapsamlı veri madenciliği analizi** içerir:

| # | Analiz | Açıklama |
|---|--------|----------|
| 1 | **Temel İstatistikler** | Mean, std, min, max, çeyrekler |
| 2 | **Kategorik Görselleştirme** | Pasta grafikleri ile kategorik analiz |
| 3 | **Hastalık-Tedavi Süresi** | Boxplot görselleştirmesi |
| 4 | **İlaç-Yan Etki İlişkileri** | 2D Histogram ve frekans analizi |
| 5 | **Hiyerarşik Kümeleme** | Seaborn clustermap ile pattern tespiti |
| 6 | **Korelasyon Analizi** | Yaş ve iyileşme skoru ilişkisi |
| 7 | **Cinsiyet Bazlı Analiz** | Normalize edilmiş hastalık oranları |
| 8 | **Yan Etki Analizi** | Baş dönmesi vakalarının detaylı incelemesi |
| 9 | **İlaç Odaklı Analiz** | Metoprolol için özel yan etki profili |

###  Çıktılar
- ✅ **9 Profesyonel Görselleştirme** (PNG formatında)
- ✅ **İstatistiksel Analizler** ve yorumları
- ✅ **HTML Rapor** çıktısı

---

##  Lokal Kurulum (Alternatif)

Google Colab yerine kendi bilgisayarınızda çalıştırmak isterseniz:

```bash
# Repository'i klonlayın , yada dosyaları indirin
git clone https://github.com/engindalgiC86-cpu/UU_VMIK_DRUGS.git
cd UU_VMIK_DRUGS

# Gerekli paketleri yükleyin
pip install pandas numpy matplotlib seaborn scipy jupyter

# Jupyter'i başlatın
jupyter notebook veri_madenciligi_projesi.ipynb
```

---
 
## 🛠️ Gereksinimler

### Python Kütüphaneleri
- `pandas` - Veri manipülasyonu
- `numpy` - Sayısal hesaplamalar
- `matplotlib` - Temel görselleştirme
- `seaborn` - İleri görselleştirme
- `scipy` - İstatistiksel analizler

Google Colab'da tüm kütüphaneler **önceden yüklüdür**! ✅

##  Proje Hedefleri

Bu projeyi tamamladığınızda şunları öğreneceksiniz:

- ✅ Veri analizi ve ön işleme
- ✅ İstatistiksel testler ve yorumlama
- ✅ Profesyonel veri görselleştirme
- ✅ Hiyerarşik kümeleme algoritmaları
- ✅ Korelasyon ve olasılık analizi
- ✅ Python veri bilimi stack'i (pandas, numpy, matplotlib, seaborn)

---

##  Çıktılar

Proje şu tür görselleştirmeler üretir:

- 📊 **Boxplot Grafikleri** - Süreç dağılımı
- 🥧 **Pasta Grafikleri** - Kategorik veri oranları
- 🔥 **Heatmap** - İlaç-yan etki ilişkileri
- 📈 **Scatter Plot** - Korelasyon analizleri
- 🌳 **Dendrogram** - Hiyerarşik kümeleme ağacı

---
 
## 📝 Lisans

Bu proje eğitim amaçlı hazırlanmıştır.

---

## 👨‍💻 Geliştirici
    Mustafa Engin Dalgıç
- **GitHub:** [@engindalgiC86-cpu](https://github.com/engindalgiC86-cpu)
- **Repository:** [UU_VMIK_DRUGS](https://github.com/engindalgiC86-cpu/UU_VMIK_DRUGS)
- **Tarih:** 30.11.2025

---

##  Teşekkürler

Bu proje **Veri Madenciliğinde İleri Konular** dersi kapsamında hazırlanmıştır.
 
