# =============================================================================
# GOOGLE COLAB - OTOMATİK VERİ SETİ YÜKLEME
# =============================================================================
# Bu hücreyi notebook'unuzun EN BAŞINA ekleyin (ilk hücre olarak)
# Veri seti otomatik olarak GitHub'dan indirilecek

# Google Colab'da mı çalışıyoruz kontrol et
try:
    import google.colab
    IN_COLAB = True
    print("🌐 Google Colab ortamı tespit edildi!")
except:
    IN_COLAB = False
    print("💻 Lokal ortamda çalışıyorsunuz")

if IN_COLAB:
    import os
    
    # Veri seti zaten var mı kontrol et
    if os.path.exists('real_drug_dataset.csv'):
        print("✅ Veri seti zaten mevcut!")
    else:
        print("📥 Veri seti GitHub'dan indiriliyor...")
        
        # GitHub'dan veri setini indir
        !wget -q https://raw.githubusercontent.com/engindalgiC86-cpu/UU_VMIK_DRUGS/main/real_drug_dataset.csv
        
        # İndirme başarılı mı kontrol et
        if os.path.exists('real_drug_dataset.csv'):
            file_size = os.path.getsize('real_drug_dataset.csv')
            print(f"✅ Veri seti başarıyla indirildi! ({file_size:,} bytes)")
        else:
            print("❌ HATA: Veri seti indirilemedi!")
            print("📝 Manuel yükleme gerekiyor:")
            print("   1. Sol menüden 📁 Dosyalar sekmesini açın")
            print("   2. 'real_drug_dataset.csv' dosyasını yükleyin")
else:
    # Lokal ortam - dosya kontrolü
    import os
    if os.path.exists('real_drug_dataset.csv'):
        print("✅ Veri seti bulundu!")
    else:
        print("⚠️ UYARI: 'real_drug_dataset.csv' bulunamadı!")
        print("   Lütfen veri setini bu dizine yerleştirin.")

print("\n🚀 Kurulum tamamlandı! Diğer hücreleri çalıştırabilirsiniz.")
print("="*70)
