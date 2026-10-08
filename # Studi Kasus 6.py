# Inventarisasi Gudang Toko

import json

def CEK_DOANG():
    with open("BarangJualan.json", "r", encoding="utf-8") as f:
        daftar_barang = json.load(f)
        print(daftar_barang)
        return daftar_barang
def UBAH_DATA():
    daftar_barang = CEK_DOANG()
    while True:
        konfirmasi = input("Ada barang yang bakal berubah stoknya? IYA/TIDAK? ")
        if konfirmasi == "IYA":
            tombol_baru = input("Restock/Terjual? ")
            tipe = input("Barangnya yang mana? ")
            if tombol_baru == "Restock" and tipe in daftar_barang:
                restock = int(input("Berapa dus/renteng yang baru datang? "))
                daftar_barang[tipe] += restock
            elif tombol_baru == "Terjual" and tipe in daftar_barang:
                terjual = int(input("Berapa eksemplar yang sudah terjual? "))
                daftar_barang[tipe] -= terjual
                if daftar_barang[tipe] == 0:
                    del daftar_barang[tipe]
            else:
                statement = print("Ini kenapa? Inputnya gak valid")
                return statement
        elif konfirmasi == "TIDAK":
            with open("BarangJualan.json", "w", encoding="utf-8") as f:
                json.dump(daftar_barang, f, indent=4)
            return
        else:
            statement = print("Ini kenapa? Inputnya gak valid. Perhatiin format penulisan daftar barangnya ya")
            return statement
def NAMBAH_JENIS():
    daftar_barang = CEK_DOANG()
    while True:
        print()
        barang_baru = input("Ketik jenis barang, terserah mau pake merek atau enggak: ")
        stoknya = int(input("Berapa dus/renteng yang didatangkan ke toko? "))
        daftar_barang[barang_baru] = stoknya
        nah = input("Lanjut? YA/TIDAK? ")
        if nah == "YA":
            continue
        elif nah == "TIDAK":
            return
        else:
            statement = print("Ini kenapa? Inputnya gak valid")
            return statement
        
print("Semangat jualannya, moga hari ini laris manis....")
while True:
    pilihan = input("Perlu ngurus stok lagi kah ini? IYA/TIDAK? ")
    if pilihan == "IYA":
        print()
        opsi = input("Mau dicek aja atau ada perubahan? CEK/UBAH/TAMBAH? ")
        if opsi == "CEK":
            CEK_DOANG()
            print()
        elif opsi == "UBAH":
            UBAH_DATA()
            CEK_DOANG()
            print()
        elif opsi == "TAMBAH":
            NAMBAH_JENIS()
        else:
            print("Ini kenapa? Inputnya gak valid")
            continue
    elif pilihan == "TIDAK":
        print("Wokee, gudang aman boskuuuhh")
        break