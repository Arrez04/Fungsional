# Kamus (nested dictionary) untuk menyimpan data nilai mahasiswa
nilai_mahasiswa = {
    "Mahasiswa1": {"Matematika": 80, "Fisika": 85, "Kimia": 78},
    "Mahasiswa2": {"Matematika": 88, "Fisika": 79, "Kimia": 92},
    "Mahasiswa3": {"Matematika": 70, "Fisika": 60, "Kimia": 65},
    "Mahasiswa4": {"Matematika": 90, "Fisika": 95, "Kimia": 85},
    "Mahasiswa5": {"Matematika": 75, "Fisika": 82, "Kimia": 80}
}

# Fungsi untuk menghitung rata-rata nilai setiap mahasiswa
def rata_rata_per_mahasiswa(nilai_mahasiswa):
    rata_rata_mahasiswa = {}
    for mahasiswa, nilai in nilai_mahasiswa.items():
        total_nilai = sum(nilai.values())
        jumlah_mata_kuliah = len(nilai)
        rata_rata = total_nilai / jumlah_mata_kuliah
        rata_rata_mahasiswa[mahasiswa] = rata_rata
    return rata_rata_mahasiswa

# Fungsi untuk menghitung rata-rata nilai seluruh mahasiswa
def rata_rata_semua_mahasiswa(nilai_mahasiswa):
    total_nilai = 0
    jumlah_mahasiswa = len(nilai_mahasiswa)
    jumlah_semua_nilai = 0

    for nilai in nilai_mahasiswa.values():
        total_nilai += sum(nilai.values())
        jumlah_semua_nilai += len(nilai)

    rata_rata = total_nilai / jumlah_semua_nilai
    return rata_rata

# Contoh penggunaan fungsi
rata_rata_mahasiswa = rata_rata_per_mahasiswa(nilai_mahasiswa)
print("Rata-rata nilai per mahasiswa:")
for mahasiswa, rata_rata in rata_rata_mahasiswa.items():
    print(f"{mahasiswa}: {rata_rata:.2f}")

rata_rata_semua = rata_rata_semua_mahasiswa(nilai_mahasiswa)
print(f"\nRata-rata nilai seluruh mahasiswa: {rata_rata_semua:.2f}")
