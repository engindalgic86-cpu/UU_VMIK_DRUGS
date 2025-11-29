# 🧬 Veri Madenciliği Projesi - İlaçlar ve Yan Etkiler Analizi

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/engindalgiC86-cpu/UU_VMIK_DRUGS/blob/main/veri_madenciligi_projesi.ipynb)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-Educational-green.svg)]()

Bu proje, ilaçlar ve yan etkileri içeren veri seti üzerinde kapsamlı bir veri madenciliği analizi gerçekleştirmektedir.

---

## 🚀 Google Colab'da Çalıştırma (3 Kolay Adım)

### ✅ ADIM 1: Notebook'u Aç
Yukarıdaki **"Open in Colab"** butonuna tıklayın

### ✅ ADIM 2: Veri Setini Yükleyin

**İki seçenek var:**

#### 🎯 Seçenek A: Manuel Yükleme (Basit)
1. Google Colab'da **sol menüden 📁 (Dosyalar)** simgesine tıklayın
2. **📤 Upload** butonuna tıklayın
3. `real_drug_dataset.csv` dosyanızı seçin ve yükleyin
4. Dosya yüklendikten sonra notebook'u çalıştırın

#### 🎯 Seçenek B: Otomatik İndirme (Önerilen)
1. Notebook'un **ilk hücresini** aşağıdaki kod ile değiştirin veya ekleyin:

```python
# Veri setini otomatik indir
import os
if not os.path.exists('real_drug_dataset.csv'):
    print("📥 Veri seti indiriliyor...")
    !wget -q https://raw.githubusercontent.com/engindalgiC86-cpu/UU_VMIK_DRUGS/main/real_drug_dataset.csv
    print("✅ İndirildi!")
else:
    print("✅ Veri seti hazır!")
```

2. Bu hücreyi çalıştırın (Shift+Enter)
3. Veri seti otomatik olarak indirilecek

### ✅ ADIM 3: Analizi Çalıştır
- **Runtime → Run all** ile tüm analizi çalıştırın
- Veya her hücreyi tek tek çalıştırın (Shift+Enter)

---

## 📥 HTML Çıktısı Alma

Analiz tamamlandıktan sonra, notebook'un **en sonuna** yeni bir hücre ekleyin ve şu kodu çalıştırın:

```python
# HTML çıktısı oluştur ve indir
!pip install nbconvert -q
!jupyter nbconvert --to html *.ipynb --no-input

from google.colab import files
import glob
for html in glob.glob('*.html'):
    print(f"📥 İndiriliyor: {html}")
    files.download(html)
    
print("✅ HTML dosyanız indirildi!")
```

---

## 📊 Proje İçeriği

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

### 📈 Çıktılar
- ✅ **9 Profesyonel Görselleştirme** (PNG formatında)
- ✅ **İstatistiksel Analizler** ve yorumları
- ✅ **HTML Rapor** çıktısı

---

## 💻 Lokal Kurulum (Alternatif)

Google Colab yerine kendi bilgisayarınızda çalıştırmak isterseniz:

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

## 📁 Dosya Yapısı

```
UU_VMIK_DRUGS/
│
├── veri_madenciligi_projesi.ipynb    # Ana Jupyter Notebook
├── real_drug_dataset.csv             # Veri seti (100 KB altında)
├── README.md                          # Bu dosya
├── BASLANGIC.md                       # Başlangıç rehberi
├── HIZLI_BASLANGIC.md                # Hızlı başlangıç kılavuzu
├── COLAB_HTML_CIKTI_REHBERI.md       # HTML çıktısı rehberi
├── GITHUB_COLAB_LINK_REHBERI.md      # GitHub-Colab entegrasyonu
└── (Yardımcı scriptler...)
```

---

## ❓ Sık Karşılaşılan Hatalar ve Çözümleri

### ❌ Hata: "FileNotFoundError: real_drug_dataset.csv"

**Sebep:** Veri seti dosyası yüklenmemiş

**Çözüm:**
1. Sol menüden 📁 Dosyalar'ı açın
2. `real_drug_dataset.csv` dosyanızı yükleyin
3. VEYA yukarıdaki otomatik indirme kodunu çalıştırın

### ❌ Hata: "ModuleNotFoundError: No module named..."

**Sebep:** Gerekli kütüphane yüklü değil

**Çözüm:**
```python
!pip install pandas numpy matplotlib seaborn scipy
```

### ❌ Hata: "KeyError: 'Sütun_Adı'"

**Sebep:** Veri setinizin sütun isimleri farklı

**Çözüm:**
```python
# Sütun isimlerini kontrol edin
print(df.columns.tolist())

# Gerekirse notebook'taki sütun isimlerini güncelleyin
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

---

## 📖 Detaylı Kılavuzlar

- 📘 **[BASLANGIC.md](BASLANGIC.md)** - Genel başlangıç rehberi
- ⚡ **[HIZLI_BASLANGIC.md](HIZLI_BASLANGIC.md)** - 3 dakikalık hızlı başlangıç
- 🌐 **[COLAB_HTML_CIKTI_REHBERI.md](COLAB_HTML_CIKTI_REHBERI.md)** - HTML çıktısı alma
- 🔗 **[GITHUB_COLAB_LINK_REHBERI.md](GITHUB_COLAB_LINK_REHBERI.md)** - GitHub-Colab entegrasyonu

---

## 🎯 Öğrenme Hedefleri

Bu projeyi tamamladığınızda şunları öğreneceksiniz:

- ✅ Veri analizi ve ön işleme
- ✅ İstatistiksel testler ve yorumlama
- ✅ Profesyonel veri görselleştirme
- ✅ Hiyerarşik kümeleme algoritmaları
- ✅ Korelasyon ve olasılık analizi
- ✅ Python veri bilimi stack'i (pandas, numpy, matplotlib, seaborn)

---

## 📊 Örnek Çıktılar

Proje şu tür görselleştirmeler üretir:

- 📊 **Boxplot Grafikleri** - Tedavi sürelerinin dağılımı
- 🥧 **Pasta Grafikleri** - Kategorik veri oranları
- 🔥 **Heatmap** - İlaç-yan etki ilişkileri
- 📈 **Scatter Plot** - Korelasyon analizleri
- 🌳 **Dendrogram** - Hiyerarşik kümeleme ağacı

---

## 🤝 Katkıda Bulunma

Bu proje eğitim amaçlıdır. Önerileriniz için issue açabilirsiniz.

---

## 📝 Lisans

Bu proje eğitim amaçlı hazırlanmıştır.

---

## 👨‍💻 Geliştirici

- **GitHub:** [@engindalgiC86-cpu](https://github.com/engindalgiC86-cpu)
- **Repository:** [UU_VMIK_DRUGS](https://github.com/engindalgiC86-cpu/UU_VMIK_DRUGS)
- **Tarih:** 2024

---

## 🎓 Teşekkürler

Bu proje **Veri Madenciliğinde İleri Konular** dersi kapsamında hazırlanmıştır.

---

## ⭐ Beğendiyseniz Yıldız Verin!

[![GitHub stars](https://img.shields.io/github/stars/engindalgiC86-cpu/UU_VMIK_DRUGS.svg?style=social&label=Star)](https://github.com/engindalgiC86-cpu/UU_VMIK_DRUGS)

**Projeyi beğendiyseniz ⭐ vermeyi unutmayın!**
