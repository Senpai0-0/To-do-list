import os

# Görevleri tutacak liste. Her görev bir sözlük (dict) olacak:
# {"gorev": "Ekmek al", "tamamlandi": False}
gorevler = []


def ekranı_temizle():
    """Terminali temizler (Windows/Mac/Linux uyumlu)."""
    os.system("cls" if os.name == "nt" else "clear")


def menuyu_goster():
    print("=" * 40)
    print("📝 TO-DO LIST APP")
    print("=" * 40)
    print("1. ➕ Görev Ekle")
    print("2. 📋 Görevleri Görüntüle")
    print("3. ✅ Görevi Tamamla")
    print("4. ❌ Görevi Sil")
    print("5. 🚪 Çıkış")
    print("=" * 40)


def gorev_ekle():
    baslik = input("Eklenecek görevi yaz: ").strip()
    if baslik == "":
        print("⚠️  Boş görev eklenemez.\n")
        return
    gorevler.append({"gorev": baslik, "tamamlandi": False})
    print(f"✅ '{baslik}' eklendi.\n")


def gorevleri_goster():
    if not gorevler:
        print("📭 Henüz görev yok.\n")
        return

    print("\n--- GÖREV LİSTESİ ---")
    for i, gorev in enumerate(gorevler, start=1):
        durum = "✅" if gorev["tamamlandi"] else "🔲"
        print(f"{i}. {durum} {gorev['gorev']}")
    print()


def gorev_tamamla():
    gorevleri_goster()
    if not gorevler:
        return

    try:
        secim = int(input("Tamamlandı olarak işaretlenecek görevin numarası: "))
        if 1 <= secim <= len(gorevler):
            gorevler[secim - 1]["tamamlandi"] = True
            print(f"✅ '{gorevler[secim - 1]['gorev']}' tamamlandı olarak işaretlendi.\n")
        else:
            print("⚠️  Geçersiz numara.\n")
    except ValueError:
        print("⚠️  Lütfen bir sayı gir.\n")


def gorev_sil():
    gorevleri_goster()
    if not gorevler:
        return

    try:
        secim = int(input("Silinecek görevin numarası: "))
        if 1 <= secim <= len(gorevler):
            silinen = gorevler.pop(secim - 1)
            print(f"❌ '{silinen['gorev']}' silindi.\n")
        else:
            print("⚠️  Geçersiz numara.\n")
    except ValueError:
        print("⚠️  Lütfen bir sayı gir.\n")


def uygulamayi_calistir():
    while True:
        menuyu_goster()
        secim = input("Seçimin (1-5): ").strip()

        if secim == "1":
            gorev_ekle()
        elif secim == "2":
            gorevleri_goster()
        elif secim == "3":
            gorev_tamamla()
        elif secim == "4":
            gorev_sil()
        elif secim == "5":
            print("👋 Görüşürüz!")
            break
        else:
            print("⚠️  Geçersiz seçim, 1-5 arası bir sayı gir.\n")

        input("Devam etmek için Enter'a bas...")
        ekranı_temizle()


if __name__ == "__main__":
    uygulamayi_calistir()