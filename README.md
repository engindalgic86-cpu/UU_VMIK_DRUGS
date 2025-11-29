# Veri Madenciliği Projesi - Kullanım Kılavuzu

## 📋 Proje Hakkında

Bu proje, ilaçlar ve yan etkileri içeren veri seti üzerinde kapsamlı bir veri madenciliği analizi gerçekleştirmektedir.

## 📦 Gerekli Dosyalar

1. `veri_madenciligi_projesi.ipynb` - Ana Jupyter Notebook dosyası
2. `real_drug_dataset.csv` - Veri seti (100 KB altında, manuel yükleme)

## 🚀 Kurulum ve Çalıştırma Adımları

### Adım 1: Veri Setini Yükleme

1. `real_drug_dataset.csv` dosyanızı hazırlayın
2. Bu dosyayı notebook ile aynı dizine yerleştirin

**Önemli:** Dosya adının tam olarak `real_drug_dataset.csv` olduğundan emin olun!

### Adım 2: Gerekli Kütüphaneleri Yükleme

Terminalde şu komutları çalıştırın:

```bash
pip install pandas numpy matplotlib seaborn scipy jupyter
```

### Adım 3: Jupyter Notebook'u Çalıştırma

```bash
jupyter notebook veri_madenciligi_projesi.ipynb
```

Tarayıcınızda notebook açılacaktır. Her hücreyi sırayla çalıştırın (Shift+Enter).

### Adım 4: HTML Çıktısı Oluşturma

Notebook'u HTML formatına çevirmek için:

**Yöntem 1: Jupyter içinden**
- File → Download as → HTML (.html)

**Yöntem 2: Komut satırından**
```bash
jupyter nbconvert --to html veri_madenciligi_projesi.ipynb
```

**Yöntem 3: Hazır script ile**
```bash
python convert_to_html.py
```

## 📊 Proje Adımları

Proje 9 ana analiz adımından oluşmaktadır:

1. **Temel İstatistikler** - Sayısal değişkenler için mean, std, min, max vb.
2. **Kategorik Görselleştirme** - Pasta grafikleri
3. **Hastalık-Tedavi Süresi** - Boxplot analizi
4. **İlaç-Yan Etki 2D Histogram** - Frekans haritası
5. **Hiyerarşik Kümeleme** - Clustermap analizi
6. **Yaş-İyileşme Korelasyonu** - Pearson/Spearman korelasyon
7. **Cinsiyet Bazında Hastalık Oranları** - Normalize edilmiş dağılım
8. **Baş Dönmesi Analizi** - İlaç bazında sıklık analizi
9. **Metoprolol Özel Analizi** - Yan etki olasılık hesaplama

## 📁 Çıktı Dosyaları

Notebook çalıştırıldığında aşağıdaki görseller oluşturulur:

- `kategorik_sutunlar_pasta_grafikleri.png`
- `hastalik_tedavi_suresi_boxplot.png`
- `ilac_yanetki_2d_histogram.png`
- `hiyerarsik_kumeleme_clustermap.png`
- `yas_iyilesme_korelasyon.png`
- `cinsiyet_hastalik_oranlari.png`
- `bas_donmesi_ilaclar.png`
- `bas_donmesi_dagilim_pasta.png`
- `metoprolol_bas_donmesi_analizi.png`

## ⚠️ Önemli Notlar

1. **Veri Seti:** Veri setini mutlaka indirip doğru isimle kaydetmelisiniz
2. **Sütun İsimleri:** Veri setindeki sütun isimleri farklı olabilir, gerekirse notebook'taki sütun isimlerini güncelleyin
3. **Eksik Değerler:** Veri setinde eksik değerler varsa, bunlar otomatik olarak işlenir
4. **Görselleştirmeler:** Tüm grafikler hem ekranda gösterilir hem de dosya olarak kaydedilir

## 🔧 Sorun Giderme

### Veri seti bulunamıyor hatası
```python
# Dosya adını ve konumunu kontrol edin
# Notebook ile aynı dizinde mi?
import os
print(os.getcwd())  # Mevcut dizini gösterir
print(os.listdir('.'))  # Dizindeki dosyaları listeler
```

### Sütun bulunamıyor hatası
```python
# Mevcut sütunları kontrol edin:
print(df.columns.tolist())

# Gerekirse sütun isimlerini güncelleyin
```

### Kütüphane hatası
```bash
# Eksik kütüphaneyi yükleyin:
pip install KUTUPHANE_ADI
```

## 📚 Kullanılan Teknolojiler

- **Python 3.x**
- **Pandas** - Veri manipülasyonu
- **NumPy** - Sayısal hesaplamalar
- **Matplotlib** - Temel görselleştirme
- **Seaborn** - İleri görselleştirme
- **SciPy** - İstatistiksel analizler

## 📖 Ek Kaynaklar

- **Pandas Dökümantasyonu:** https://pandas.pydata.org/docs/
- **Seaborn Tutorial:** https://seaborn.pydata.org/tutorial.html
- **Matplotlib Gallery:** https://matplotlib.org/stable/gallery/

## 👤 İletişim

Sorularınız için:
- Proje dosyalarını kontrol edin
- Hata mesajlarını dikkatlice okuyun

## 📝 Lisans

Bu proje eğitim amaçlıdır.

---

**Başarılar! 🎉**

Bu notebook'u tamamladığınızda, veri madenciliği konusunda:
- İstatistiksel analiz yapabilecek
- Veri görselleştirmesi oluşturabilecek
- Hiyerarşik kümeleme uygulayabilecek
- Korelasyon analizi gerçekleştirebilecek
- Olasılık hesaplamaları yapabilecek

seviyeye ulaşacaksınız!
