# 🎯 VERİ MADENCİLİĞİ PROJESİ

## ✨ Projeniz Hazır!

Bu klasörde Veri Madenciliği projeniz için gereken tüm dosyalar bulunmaktadır.

---

## 📁 DOSYALAR

| Dosya | Açıklama | Durum |
|-------|----------|-------|
| `veri_madenciligi_projesi.ipynb` | Ana Jupyter Notebook (9 analiz adımı) | ✅ Hazır |
| `real_drug_dataset.csv` | Veri seti dosyanız | ⬜ **SİZ EKLEYİN** |
| `README.md` | Detaylı kullanım kılavuzu | ✅ Hazır |
| `HIZLI_BASLANGIC.md` | 3 dakikalık hızlı rehber | ✅ Hazır |
| `veri_seti_kontrol.py` | Veri seti kontrol aracı | ✅ Hazır |
| `convert_to_html.py` | HTML dönüştürme scripti | ✅ Hazır |

---

## 🚀 HIZLI BAŞLANGIÇ (3 Adım)

### 1️⃣ VERİ SETİNİ YERLEŞTİRİN
```
real_drug_dataset.csv dosyanızı bu klasöre kopyalayın
```

### 2️⃣ KONTROL EDİN (İsteğe bağlı)
```bash
python veri_seti_kontrol.py
```

### 3️⃣ ÇALIŞTIRIN
```bash
jupyter notebook veri_madenciligi_projesi.ipynb
```

Notebook açıldığında: **Cell → Run All**

---

## 📊 PROJE İÇERİĞİ

Notebook şu analizleri içerir:

1. ✅ **Temel İstatistikler** - mean, std, min, max, çeyrekler
2. ✅ **Kategorik Görselleştirme** - Pasta grafikleri  
3. ✅ **Hastalık-Tedavi Süresi** - Boxplot analizi
4. ✅ **İlaç-Yan Etki 2D Histogram** - Frekans haritası
5. ✅ **Hiyerarşik Kümeleme** - Seaborn clustermap
6. ✅ **Yaş-İyileşme Korelasyonu** - Pearson & Spearman
7. ✅ **Cinsiyet-Hastalık Oranları** - Normalize edilmiş analiz
8. ✅ **Baş Dönmesi Analizi** - İlaç bazında sıklık
9. ✅ **Metoprolol Analizi** - Yan etki olasılığı

**Çıktı:** 9 profesyonel görselleştirme + Detaylı istatistiksel analizler

---

## 🛠️ GEREKLİ KÜTÜPHANELER

Terminalden yükleyin:
```bash
pip install pandas numpy matplotlib seaborn scipy jupyter
```

**veya** Jupyter içinde:
```python
!pip install pandas numpy matplotlib seaborn scipy
```

---

## 📄 HTML ÇIKTISI

Analiz bittikten sonra HTML formatında kaydetmek için:

**Yöntem 1:** Jupyter menüsünde
```
File → Download as → HTML (.html)
```

**Yöntem 2:** Terminal'de
```bash
jupyter nbconvert --to html veri_madenciligi_projesi.ipynb
```

**Yöntem 3:** Python scripti ile
```bash
python convert_to_html.py
```

---

## ❓ SORUN GİDERME

### 🔴 "real_drug_dataset.csv bulunamadı" hatası
**Çözüm:**
- Dosyanın bu klasörde olduğundan emin olun
- Dosya adının TAM OLARAK `real_drug_dataset.csv` olduğunu kontrol edin
- `python veri_seti_kontrol.py` çalıştırın

### 🔴 "ModuleNotFoundError" hatası
**Çözüm:**
```bash
pip install <eksik_kütüphane_adı>
```

### 🔴 "Sütun bulunamadı" hatası
**Çözüm:**
- Notebook'taki ilk hücreleri çalıştırın
- `df.columns` ile sütun isimlerini görün
- Gerekirse notebook'taki sütun isimlerini güncelleyin

---

## 💡 KULLANIM İPUÇLARI

✨ **Jupyter Kısayolları:**
- `Shift + Enter` → Hücreyi çalıştır, sonrakine geç
- `Ctrl + Enter` → Sadece hücreyi çalıştır
- Cell → Run All → Tüm analizi çalıştır

✨ **Hata Durumunda:**
- Kernel → Restart & Clear Output
- Sonra Cell → Run All

✨ **En İyi Deneyim:**
1. Veri setini ekleyin
2. Tüm hücreleri çalıştırın
3. Sonuçları inceleyin
4. HTML olarak kaydedin

---

## 📚 YARDIMCI DÖKÜMANLAR

- **Detaylı Kılavuz:** `README.md` dosyasını okuyun
- **Hızlı Başlangıç:** `HIZLI_BASLANGIC.md` dosyasına bakın
- **Veri Kontrol:** `python veri_seti_kontrol.py` çalıştırın

---

## 🎓 PROJE ÖZELLİKLERİ

- ✨ Tamamen Türkçe açıklamalar
- 📊 9 farklı analiz tekniği
- 🎨 Profesyonel görselleştirmeler
- 📈 İstatistiksel yorumlar
- 🔬 Bilimsel metodoloji
- 📝 Detaylı markdown açıklamaları

---

## 🎉 BAŞARILAR!

Projenizi tamamladığınızda:
- ✅ Veri analizi yapabilecek
- ✅ İstatistiksel testler uygulayabilecek
- ✅ Profesyonel grafikler oluşturabilecek
- ✅ Veri madenciliği teknikleri kullanabilecek

seviyeye ulaşacaksınız!

---

**Hazırlayan:** Claude  
**Tarih:** 2024  
**Amaç:** Eğitim

---

## 📞 SONRAKİ ADIMLAR

1. ✅ Dosyaları indirdiniz
2. ⬜ `real_drug_dataset.csv` dosyanızı ekleyin
3. ⬜ Jupyter Notebook'u çalıştırın
4. ⬜ Analizi tamamlayın
5. ⬜ HTML çıktısını alın

**Şimdi başlayabilirsiniz! 🚀**
