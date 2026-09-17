import json
import os

DOSYA_ADI = "gorevler.json"

def gorevleri_yukle():
    """Disk üzerindeki JSON dosyasından verileri okur."""
    if not os.path.exists(DOSYA_ADI):
        return []
    try:
        with open(DOSYA_ADI, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []

def gorevleri_kaydet(gorevler):
    """Mevcut görev listesini JSON dosyasına yazar."""
    with open(DOSYA_ADI, "w", encoding="utf-8") as f:
        json.dump(gorevler, f, ensure_ascii=False, indent=4)

def gorevleri_listele(gorevler):
    if not gorevler:
        print("\n📂 Henüz kayıtlı bir görev yok.\n")
        return
    print("\n=== GÖREV LİSTESİ ===")
    for i, g in enumerate(gorevler, 1):
        durum = "✓" if g["tamamlandi"] else " "
        print(f"{i}. [{durum}] {g['baslik']}")
    print()

def gorev_ekle(gorevler):
    baslik = input("Eklenecek görev: ").strip()
    if baslik:
        gorevler.append({"baslik": baslik, "tamamlandi": False})
        gorevleri_kaydet(gorevler)
        print("✅ Görev başarıyla eklendi!\n")

def gorev_tamamla(gorevler):
    gorevleri_listele(gorevler)
    if not gorevler:
        return
    try:
        num = int(input("Tamamlanan görev numarası: "))
        if 1 <= num <= len(gorevler):
            gorevler[num - 1]["tamamlandi"] = True
            gorevleri_kaydet(gorevler)
            print("🎉 Görev tamamlandı olarak işaretlendi!\n")
        else:
            print("Geçersiz numara!\n")
    except ValueError:
        print("Lütfen bir sayı girin!\n")

def gorev_sil(gorevler):
    gorevleri_listele(gorevler)
    if not gorevler:
        return
    try:
        num = int(input("Silinecek görev numarası: "))
        if 1 <= num <= len(gorevler):
            silinen = gorevler.pop(num - 1)
            gorevleri_kaydet(gorevler)
            print(f"🗑️ '{silinen['baslik']}' görevi silindi!\n")
        else:
            print("Geçersiz numara!\n")
    except ValueError:
        print("Lütfen bir sayı girin!\n")

def main():
    gorevler = gorevleri_yukle()
    while True:
        print("=== KİŞİSEL GÖREV YÖNETİCİSİ ===")
        print("1. Görevleri Listele")
        print("2. Yeni Görev Ekle")
        print("3. Görevi Tamamla")
        print("4. Görevi Sil")
        print("5. Çıkış")
        
        secim = input("Seçiminiz (1-5): ").strip()
        if secim == "1":
            gorevleri_listele(gorevler)
        elif secim == "2":
            gorev_ekle(gorevler)
        elif secim == "3":
            gorev_tamamla(gorevler)
        elif secim == "4":
            gorev_sil(gorevler)
        elif secim == "5":
            print("Programdan çıkılıyor. İyi çalışmalar!")
            break
        else:
            print("Geçersiz seçim, lütfen 1-5 arasında bir değer girin.\n")

if __name__ == "__main__":
    main()