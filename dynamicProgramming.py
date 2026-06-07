import csv
import time

namaFile = "Snack Bar Protein and Sugar Value.csv"
batasGula = 15


def bacaData():
    produk = []
    with open(namaFile, newline="", encoding="utf-8-sig") as file:
        pembaca = csv.DictReader(file)
        for baris in pembaca:
            produk.append(
                {
                    "nama": baris["Nama Produk"],
                    "protein": int(float(baris["Protein (gram)"])),
                    "gula": int(float(baris["Gula (gram)"])),
                }
            )
    return produk


def dynamicProgramming(produk):
    jumlahProduk = len(produk)
    tabel = []
    for i in range(jumlahProduk + 1):
        baris = []
        for g in range(batasGula + 1):
            baris.append(0)
        tabel.append(baris)

    for i in range(1, jumlahProduk + 1):
        protein = produk[i - 1]["protein"]
        gula = produk[i - 1]["gula"]
        for batas in range(batasGula + 1):
            tidakDiambil = tabel[i - 1][batas]
            if gula <= batas:
                diambil = protein + tabel[i - 1][batas - gula]
                tabel[i][batas] = max(tidakDiambil, diambil)
            else:
                tabel[i][batas] = tidakDiambil
    pilihan = []
    batas = batasGula
    for i in range(jumlahProduk, 0, -1):
        if tabel[i][batas] != tabel[i - 1][batas]:
            pilihan.append(i - 1)
            batas -= produk[i - 1]["gula"]
    pilihan.reverse()
    totalProtein = sum(produk[i]["protein"] for i in pilihan)
    totalGula = sum(produk[i]["gula"] for i in pilihan)

    return pilihan, totalProtein, totalGula


def tampilkanHasil(produk, pilihan, totalProtein, totalGula, waktu):
    print("HASIL DYNAMIC PROGRAMMING")
    print("Batas gula:", batasGula, "gram")
    print("Total protein:", totalProtein, "gram")
    print("Total gula:", totalGula, "gram")
    print("Jumlah produk terpilih:", len(pilihan))
    print("Waktu eksekusi:", waktu, "detik")
    print("\nProduk terpilih:")
    for i in pilihan:
        print("-", produk[i]["nama"], ", Protein:", produk[i]["protein"], "g", ", Gula:", produk[i]["gula"], "g",)


produk = bacaData()
mulai = time.perf_counter()
pilihan, totalProtein, totalGula = dynamicProgramming(produk)
selesai = time.perf_counter()
waktu = selesai - mulai
tampilkanHasil(produk, pilihan, totalProtein, totalGula, waktu)