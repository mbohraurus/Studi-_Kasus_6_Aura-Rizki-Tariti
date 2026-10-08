# Studi-_Kasus_6_Aura-Rizki-Tariti

Nama: Aura Rizki Tariti<br>
Kelas: A<br>
Angkatan: 2026<br>
NIM: 2609116032<br>
Soal: Genap

Di Studi Kasus kali ini, saya menggunakan import json karena (entah kenapa) ekstensinya terasa lebih mudah untuk saya. Di sini, pengguna bisa mengecek isi data barang yang tercatat di json, mengubah data yang sudah ada, atau menambah data (jenis barang jualan) yang baru. Fitur-fitur ini dibuat dengan function, sehingga menurut saya agak lebih rapi sedikit. Bentuk file json yang saya gunakan adalah object, yang kelihatan mirip dictionary, sehingga saya menggunakan beberapa jenis operasi pada dictionary juga seperti pada daftar_barang[tipe] += restock. Tujuannya untuk menambah value (stok) pada key (jenis barang) yang dinyatakan dengan tipe, sesuai input restock yang diketik pengguna. 

Kalimat terakhir yang "Wokee gudang aman bosskuuhh" itu menandakan sesi run program yang sudah berakhir akibat break. Meski program dihentikan, perubahan data yang dilakukan sebelumnya tetap tersimpan (memengaruhi) dalam file json itu sendiri. Jadi, ketika pengguna melakukan restock shampo sebanyak 2 renteng (yang awalnya 5 renteng dalam file json), akhirnya mengubah data stok shampo secara permanen menjadi 7 renteng, perubahannya tetap bertahan sesi run program yang selanjutnya.

Percobaan run pertama: melibatkan fitur CEK dan UBAH stok (ada json.load dan json.dump)
<img width="1397" height="396" alt="Screenshot 2026-10-08 230038" src="https://github.com/user-attachments/assets/f8aa3ac9-f639-4eb5-8924-7f0b76b6b701" />

Percobaan run kedua: melibatkan fitur TAMBAH jenis barang (ada json.dump)
<img width="1386" height="281" alt="Screenshot 2026-10-08 234817" src="https://github.com/user-attachments/assets/550a22b6-f199-4efd-9b5c-cff000fc804f" />

Oiya, sistemnya ini bisa memberi output pengingat jika ada input pengguna yang tidak sesuai.
<img width="1407" height="470" alt="Screenshot 2026-10-08 230103" src="https://github.com/user-attachments/assets/30f2d080-fc12-4fb6-a874-a81865257ffb" />
