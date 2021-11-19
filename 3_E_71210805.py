nama = input("Masukkan daftar siswa : ")
print("Daftar Siswa : ", nama.title().split(","))
tambah = input("Masukkan siswa yang ingin ditambahkan : ")
if tambah.split(",") == nama.split(",") :
    print("\nSiswa atas nama", tambah.upper(), "sudah berada dalam daftar siswa.")
else :
    print("Hasil penambahan pada daftar siswa : ", nama.title().split(","),tambah.upper())
