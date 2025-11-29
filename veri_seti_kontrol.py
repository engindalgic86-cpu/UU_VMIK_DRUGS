#!/usr/bin/env python3
"""
Veri seti varlığını ve yapısını kontrol eden yardımcı script
"""

import os
import sys

def check_dataset():
    """Veri setinin varlığını ve temel yapısını kontrol eder"""
    
    print("="*70)
    print(" VERİ SETİ KONTROL ARACI")
    print("="*70)
    
    # Mevcut dizini göster
    current_dir = os.getcwd()
    print(f"\n📁 Mevcut Dizin: {current_dir}")
    
    # Dizindeki dosyaları listele
    print("\n📋 Bu Dizindeki Dosyalar:")
    print("-"*70)
    files = os.listdir('.')
    for i, file in enumerate(files, 1):
        size = os.path.getsize(file) if os.path.isfile(file) else 0
        file_type = "📄" if os.path.isfile(file) else "📁"
        print(f"{i:2d}. {file_type} {file:40s} ({size:>10,} bytes)")
    
    # Veri setini kontrol et
    dataset_name = 'real_drug_dataset.csv'
    print(f"\n{'='*70}")
    print(f" VERİ SETİ KONTROLÜ: {dataset_name}")
    print("="*70)
    
    if os.path.exists(dataset_name):
        print(f"\n✅ BAŞARILI: '{dataset_name}' bulundu!")
        
        # Dosya boyutunu göster
        file_size = os.path.getsize(dataset_name)
        print(f"\n📊 Dosya Bilgileri:")
        print(f"   - Boyut: {file_size:,} bytes ({file_size/1024:.2f} KB)")
        
        if file_size > 100 * 1024:
            print(f"   ⚠ Uyarı: Dosya 100 KB'dan büyük ({file_size/1024:.2f} KB)")
        
        # İçeriği kontrol et
        try:
            import pandas as pd
            
            print("\n🔍 Veri Seti İçerik Kontrolü:")
            print("-"*70)
            
            df = pd.read_csv(dataset_name)
            
            print(f"   ✓ Satır sayısı: {df.shape[0]:,}")
            print(f"   ✓ Sütun sayısı: {df.shape[1]}")
            
            print(f"\n   📋 Sütun İsimleri:")
            for i, col in enumerate(df.columns, 1):
                dtype = df[col].dtype
                null_count = df[col].isnull().sum()
                print(f"      {i:2d}. {col:30s} (Tip: {dtype}, Eksik: {null_count})")
            
            print(f"\n   📈 Veri Önizleme (İlk 3 Satır):")
            print("-"*70)
            print(df.head(3).to_string())
            
            print("\n" + "="*70)
            print("✅ VERİ SETİ HAZIR! Jupyter Notebook'u çalıştırabilirsiniz.")
            print("="*70)
            
            return True
            
        except ImportError:
            print("\n⚠ Pandas yüklü değil. Detaylı kontrol yapılamadı.")
            print("   Yüklemek için: pip install pandas")
            return True
            
        except Exception as e:
            print(f"\n❌ HATA: Veri seti okunamadı!")
            print(f"   Hata mesajı: {str(e)}")
            print("\n💡 Olası Çözümler:")
            print("   1. Dosyanın gerçekten CSV formatında olduğundan emin olun")
            print("   2. Dosyanın bozuk olmadığını kontrol edin")
            print("   3. Dosyayı bir metin editörü ile açıp içeriğe bakın")
            return False
    
    else:
        print(f"\n❌ HATA: '{dataset_name}' bulunamadı!")
        print("\n💡 Çözüm Adımları:")
        print(f"   1. '{dataset_name}' dosyanızın bu dizinde olduğundan emin olun")
        print(f"   2. Dosya adının TAM OLARAK '{dataset_name}' olduğunu kontrol edin")
        print("   3. Büyük/küçük harf duyarlılığına dikkat edin")
        print("\n📝 CSV Dosyası Nasıl Olmalı:")
        print("   - Dosya adı: real_drug_dataset.csv")
        print("   - Format: CSV (virgül ile ayrılmış)")
        print("   - Boyut: Tercihen 100 KB altında")
        print("   - İlk satır: Sütun başlıkları")
        
        # CSV dosyalarını ara
        csv_files = [f for f in files if f.endswith('.csv')]
        if csv_files:
            print("\n📄 Bu dizinde bulunan CSV dosyaları:")
            for csv_file in csv_files:
                print(f"   - {csv_file}")
            print(f"\n💡 Bu dosyalardan birini '{dataset_name}' olarak yeniden adlandırabilirsiniz.")
        
        return False

def print_notebook_check():
    """Notebook dosyasını kontrol et"""
    
    notebook_name = 'veri_madenciligi_projesi.ipynb'
    
    print(f"\n{'='*70}")
    print(f" NOTEBOOK KONTROLÜ: {notebook_name}")
    print("="*70)
    
    if os.path.exists(notebook_name):
        print(f"\n✅ BAŞARILI: '{notebook_name}' bulundu!")
        file_size = os.path.getsize(notebook_name)
        print(f"   - Boyut: {file_size:,} bytes ({file_size/1024:.2f} KB)")
    else:
        print(f"\n⚠ UYARI: '{notebook_name}' bulunamadı!")
        
        # .ipynb dosyalarını ara
        ipynb_files = [f for f in os.listdir('.') if f.endswith('.ipynb')]
        if ipynb_files:
            print("\n📓 Bu dizinde bulunan notebook dosyaları:")
            for nb_file in ipynb_files:
                print(f"   - {nb_file}")

def main():
    """Ana fonksiyon"""
    
    dataset_ok = check_dataset()
    print_notebook_check()
    
    print("\n" + "="*70)
    if dataset_ok:
        print("🎉 HER ŞEY HAZIR!")
        print("\n📝 Sonraki Adımlar:")
        print("   1. Terminal'de: jupyter notebook veri_madenciligi_projesi.ipynb")
        print("   2. Notebook'ta: Cell → Run All")
        print("   3. Analiz sonuçlarını inceleyin!")
    else:
        print("⚠ VERİ SETİ EKSİK!")
        print("\nÖnce veri setini düzeltin, sonra tekrar çalıştırın.")
    print("="*70)
    print()

if __name__ == "__main__":
    main()
