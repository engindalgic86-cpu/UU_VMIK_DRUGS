# ============================================================================
# GOOGLE COLAB - HTML ÇIKTI OLUŞTURMA
# ============================================================================
# 
# Bu kodu Colab'da notebook'unuzun EN SONUNA yeni bir hücre olarak ekleyin
# ve çalıştırın. HTML dosyanız otomatik olarak indirilecek!
#
# ============================================================================

print("🌐 HTML ÇIKTI OLUŞTURULUYOR...")
print("="*70)

# ADIM 1: nbconvert'i yükle
print("\n📦 1. Gerekli paketler kontrol ediliyor...")
import subprocess
import sys

try:
    import nbconvert
    print("   ✅ nbconvert zaten yüklü")
except ImportError:
    print("   ⬇️ nbconvert yükleniyor...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "nbconvert", "-q"])
    print("   ✅ nbconvert yüklendi")

# ADIM 2: Notebook dosyasını bul
print("\n📋 2. Notebook dosyası bulunuyor...")
import glob
import os

notebook_files = glob.glob('*.ipynb')

if not notebook_files:
    print("   ❌ HATA: Notebook dosyası bulunamadı!")
else:
    print(f"   ✅ {len(notebook_files)} notebook bulundu:")
    for nb in notebook_files:
        print(f"      - {nb}")

# ADIM 3: HTML'e çevir
print("\n🔄 3. HTML dönüştürme başlıyor...")

for notebook_file in notebook_files:
    print(f"\n   🔄 {notebook_file} dönüştürülüyor...")
    
    # HTML'e çevir (kod hücreleri gizli, sadece çıktılar)
    !jupyter nbconvert --to html "{notebook_file}" --no-input --no-prompt
    
    html_file = notebook_file.replace('.ipynb', '.html')
    
    if os.path.exists(html_file):
        size_kb = os.path.getsize(html_file) / 1024
        print(f"   ✅ {html_file} oluşturuldu ({size_kb:.1f} KB)")
    else:
        print(f"   ❌ {html_file} oluşturulamadı!")

# ADIM 4: HTML dosyalarını listele
print("\n📂 4. Oluşturulan HTML dosyaları:")
html_files = glob.glob('*.html')
if html_files:
    for html in html_files:
        size_kb = os.path.getsize(html) / 1024
        print(f"   ✅ {html} ({size_kb:.1f} KB)")
else:
    print("   ⚠️ HTML dosyası bulunamadı!")

# ADIM 5: İndir
print("\n📥 5. HTML dosyaları indiriliyor...")

try:
    from google.colab import files
    
    for html_file in html_files:
        print(f"   ⬇️ İndiriliyor: {html_file}")
        files.download(html_file)
    
    print("\n" + "="*70)
    print("🎉 İŞLEM TAMAMLANDI!")
    print("="*70)
    print("\n✅ HTML dosyaları tarayıcınızın indirilenler klasöründe!")
    print("\n💡 İpuçları:")
    print("   - HTML dosyasına çift tıklayarak açabilirsiniz")
    print("   - Tüm grafikler ve analizler dahil!")
    print("   - Kod hücreleri gizli (sadece sonuçlar görünür)")
    
except ImportError:
    print("\n⚠️ UYARI: Bu kod Google Colab'da çalışır!")
    print("\nMANUEL İNDİRME:")
    print("   1. Sol menüden 📁 Dosyalar sekmesini açın")
    print("   2. HTML dosyasını bulun")
    print("   3. Sağ tıklayıp 'İndir' seçin")
except Exception as e:
    print(f"\n❌ HATA: {str(e)}")
    print("\nMANUEL İNDİRME:")
    print("   1. Sol menüden 📁 Dosyalar sekmesini açın")
    print("   2. HTML dosyasını bulun")
    print("   3. Sağ tıklayıp 'İndir' seçin")

print("\n" + "="*70)


# ============================================================================
# ALTERNATİF 1: KOD HÜCRELERİ DAHİL (KODLAR DA GÖRÜNSÜN)
# ============================================================================
"""
# Kod hücreleri de dahil HTML oluştur
!jupyter nbconvert --to html *.ipynb

from google.colab import files
import glob
for html in glob.glob('*.html'):
    files.download(html)
"""


# ============================================================================
# ALTERNATİF 2: MODERN TASARIM (LAB TEMPLATE)
# ============================================================================
"""
# Modern görünüm ile HTML oluştur
!jupyter nbconvert --to html *.ipynb --template lab --no-input

from google.colab import files
import glob
for html in glob.glob('*.html'):
    files.download(html)
"""


# ============================================================================
# ALTERNATİF 3: TEK SATIR (EN BASIT)
# ============================================================================
"""
!pip install nbconvert -q
!jupyter nbconvert --to html *.ipynb --no-input
from google.colab import files
import glob
for h in glob.glob('*.html'): files.download(h)
"""
