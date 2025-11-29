# 🚀 HIZLI BAŞLANGIÇ KILAVUZU

## ⏱️ 3 Dakikada Projeyi Çalıştırın

### 📥 1. VERİ SETİNİ YERLEŞTİRİN (30 saniye)

1. `real_drug_dataset.csv` dosyanızı hazırlayın
2. Bu dosyayı `veri_madenciligi_projesi.ipynb` ile **aynı dizine** kopyalayın

**Önemli:** Dosya adı tam olarak `real_drug_dataset.csv` olmalı!

### 🔧 2. GEREKLİ PROGRAMLARI YÜKLEYIN (2 dakika)

Terminalde şu komutu çalıştırın:

```bash
pip install pandas numpy matplotlib seaborn scipy jupyter
```

### ▶️ 3. NOTEBOOK'U ÇALIŞTIRIN (1 dakika)

```bash
jupyter notebook veri_madenciligi_projesi.ipynb
```

Tarayıcınızda açılan notebook'ta:
- Cell → Run All ile tüm analizi çalıştırın
- VEYA her hücreyi tek tek çalıştırın (Shift+Enter)

### 📄 4. HTML ÇIKTISI OLUŞTURUN (İsteğe bağlı)

Notebook çalıştıktan sonra:

**Jupyter'de:**
File → Download as → HTML (.html)

**VEYA Terminal'de:**
```bash
jupyter nbconvert --to html veri_madenciligi_projesi.ipynb
```

---

## 📋 PROJE DOSYALARI

✅ `veri_madenciligi_projesi.ipynb` - Ana analiz dosyası
✅ `README.md` - Detaylı kılavuz
✅ `convert_to_html.py` - HTML dönüştürme scripti
⬜ `real_drug_dataset.csv` - VERİ SETİ (Notebook ile aynı dizine koyun!)

---

## ❓ SORGULAR

**Veri seti bulunamıyor mu?**
→ CSV dosyasının notebook ile aynı klasörde olduğundan emin olun
→ Dosya adının tam olarak `real_drug_dataset.csv` olduğunu kontrol edin
→ Terminal/CMD'de `ls` (Mac/Linux) veya `dir` (Windows) ile dosyaları listeleyin

**Kütüphane hatası mı alıyorsunuz?**
→ `pip install <kütüphane_adı>` ile eksik kütüphaneyi yükleyin

**Sütun bulunamıyor hatası mı?**
→ Veri setindeki sütun isimleri farklı olabilir
→ Notebook'taki ilk hücreleri çalıştırarak sütun isimlerini görün

---

## 📊 PROJE ÇIKTILARI

Analiz tamamlandığında şunlar oluşur:

📈 **9 Farklı Analiz:**
1. Temel istatistikler
2. Kategorik veri grafikleri
3. Hastalık-tedavi süresi boxplot
4. İlaç-yan etki 2D histogram
5. Hiyerarşik kümeleme
6. Yaş-iyileşme korelasyonu
7. Cinsiyet-hastalık oranları
8. Baş dönmesi analizi
9. Metoprolol özel analizi

🖼️ **9 Adet Görsel:**
- Tüm grafikler PNG formatında kaydedilir
- Hem ekranda gösterilir hem de dosya olarak saklanır

---

## 💡 İPUÇLARI

✨ **Notebook kullanımı:**
- Shift+Enter: Hücreyi çalıştır ve bir sonrakine geç
- Ctrl+Enter: Sadece hücreyi çalıştır
- Cell → Run All: Tüm hücreleri çalıştır

✨ **Hata durumunda:**
- Kernel → Restart & Clear Output
- Sonra tekrar Cell → Run All

✨ **HTML için:**
- Notebook çalıştırıldıktan SONRA HTML'e çevirin
- Böylece tüm çıktılar ve grafikler HTML'de olur

---

## 🎯 HEDEF

Bu projeyi tamamladığınızda:
- Veri analizi yapabilecek
- İstatistiksel testler uygulayabilecek
- Profesyonel görselleştirmeler oluşturabilecek
- Veri madenciliği teknikleri kullanabilecek

seviyeye ulaşacaksınız!

---

## 📞 YARDIM

Detaylı bilgi için:
- `README.md` dosyasını okuyun
- `veri_seti_indirme_talimatlari.py` çalıştırın
- Notebook içindeki markdown açıklamalarını inceleyin

---

**BAŞARILAR! 🎉**

Projenizi tamamladıktan sonra:
- HTML çıktısını paylaşabilirsiniz
- Grafikleri raporlarınızda kullanabilirsiniz
- Kodu kendi veri setlerinize uyarlayabilirsiniz
