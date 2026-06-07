import csv
import math
import random
import time

namaFile = "Snack Bar Protein and Sugar Value.csv"
batasGula = 15
jumlahPerulangan = 10000
suhuAwal = 100
pendinginan = 0.995


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


def hitungProtein(pilihan, produk):
    total = 0
    for i in range(len(produk)):
        if pilihan[i] == 1:
            total += produk[i]["protein"]
    return total


def hitungGula(pilihan, produk):
    total = 0
    for i in range(len(produk)):
        if pilihan[i] == 1:
            total += produk[i]["gula"]
    return total


def simulatedAnnealing(produk):
    random.seed(42)
    jumlahProduk = len(produk)
    pilihanSekarang = [0] * jumlahProduk
    pilihanTerbaik = pilihanSekarang[:]
    suhu = suhuAwal

    for _ in range(jumlahPerulangan):
        pilihanBaru = pilihanSekarang[:]
        indeks = random.randint(0, jumlahProduk - 1)
        if pilihanBaru[indeks] == 0:
            pilihanBaru[indeks] = 1
        else:
            pilihanBaru[indeks] = 0
        if hitungGula(pilihanBaru, produk) <= batasGula:
            proteinSekarang = hitungProtein(pilihanSekarang, produk)
            proteinBaru = hitungProtein(pilihanBaru, produk)
            selisih = proteinBaru - proteinSekarang
            if selisih > 0:
                pilihanSekarang = pilihanBaru[:]
            else:
                peluang = math.exp(selisih / suhu)
                if random.random() < peluang:
                    pilihanSekarang = pilihanBaru[:]

            proteinTerbaik = hitungProtein(pilihanTerbaik, produk)
            proteinSekarang = hitungProtein(pilihanSekarang, produk)
            gulaTerbaik = hitungGula(pilihanTerbaik, produk)
            gulaSekarang = hitungGula(pilihanSekarang, produk)
            if proteinSekarang > proteinTerbaik:
                pilihanTerbaik = pilihanSekarang[:]
            elif proteinSekarang == proteinTerbaik and gulaSekarang < gulaTerbaik:
                pilihanTerbaik = pilihanSekarang[:]

        suhu = suhu * pendinginan
        if suhu < 0.001:
            suhu = 0.001

    totalProtein = hitungProtein(pilihanTerbaik, produk)
    totalGula = hitungGula(pilihanTerbaik, produk)
    pilihanIndeks = []
    for i in range(jumlahProduk):
        if pilihanTerbaik[i] == 1:
            pilihanIndeks.append(i)

    return pilihanIndeks, totalProtein, totalGula


def tampilkanHasil(produk, pilihan, totalProtein, totalGula, waktu):
    print("HASIL SIMULATED ANNEALING")
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
pilihan, totalProtein, totalGula = simulatedAnnealing(produk)
selesai = time.perf_counter()
waktu = selesai - mulai
tampilkanHasil(produk, pilihan, totalProtein, totalGula, waktu)