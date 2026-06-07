import csv
import time
from itertools import combinations

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


def bruteForce(produk):
    pilihanTerbaik = []
    proteinTerbaik = 0
    gulaTerbaik = 0
    jumlahProduk = len(produk)

    for banyakProduk in range(1, jumlahProduk + 1):
        for kombinasi in combinations(range(jumlahProduk), banyakProduk):
            totalProtein = 0
            totalGula = 0
            for i in kombinasi:
                totalProtein += produk[i]["protein"]
                totalGula += produk[i]["gula"]
            if totalGula <= batasGula:
                if totalProtein > proteinTerbaik:
                    proteinTerbaik = totalProtein
                    gulaTerbaik = totalGula
                    pilihanTerbaik = kombinasi
                elif totalProtein == proteinTerbaik and totalGula < gulaTerbaik:
                    gulaTerbaik = totalGula
                    pilihanTerbaik = kombinasi

    return pilihanTerbaik, proteinTerbaik, gulaTerbaik


def tampilkanHasil(produk, pilihan, totalProtein, totalGula, waktu):
    print("HASIL BRUTE FORCE")
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
pilihan, totalProtein, totalGula = bruteForce(produk)
selesai = time.perf_counter()
waktu = selesai - mulai
tampilkanHasil(produk, pilihan, totalProtein, totalGula, waktu)