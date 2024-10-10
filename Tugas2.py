# Data pengguna: NIM sebagai key, password sebagai value
users = {
    "194": "pass123",
    "127": "pass321",

}

# Data buku yang tersedia di toko (Tuple: judul, penulis, harga)
books = {
    1: ("Is It Bad Or Good Habits", "Sabrina Ara", 300000),
    2: ("Atomic Habits", "James Clear", 250000),
    3: ("Kamus Pintar Hukum", "Galang Taufani, S.H.,M.H.", 400000),
}

# Dictionary untuk menyimpan pembelian buku user (NIM sebagai key, value berupa list pembelian)
transactions = {}

# Fungsi untuk menampilkan buku yang tersedia
def display_books():
    print("\n===== Daftar Buku Tersedia =====")
    for book_id, book_info in books.items():
        title, author, price = book_info
        print(f"{book_id}. {title} oleh {author} - Rp {price}")

# Fungsi untuk login user
def login():
    nim = input("Masukkan NIM: ")
    password = input("Masukkan Password: ")
    
    if nim in users and users[nim] == password:
        print(f"Login berhasil, selamat datang {nim}!")
        user_menu(nim)
    else:
        print("NIM atau Password salah.")

# Fungsi untuk menambahkan buku ke dalam pembelian
def add_purchase(nim):
    display_books()
    book_id = input("Masukkan ID buku yang ingin dibeli: ")
    
    if not book_id.isdigit() or int(book_id) not in books:
        print("ID buku tidak valid.")
        return
    
    book_id = int(book_id)
    if nim not in transactions:
        transactions[nim] = []
    
    transactions[nim].append(books[book_id])
    print(f"Buku '{books[book_id][0]}' berhasil ditambahkan ke keranjang.")

# Fungsi untuk menghapus buku dari pembelian
def remove_purchase(nim):
    if nim not in transactions or not transactions[nim]:
        print("Keranjang belanja kosong.")
        return
    
    print("\n===== Buku dalam keranjang =====")
    for idx, book in enumerate(transactions[nim], 1):
        print(f"{idx}. {book[0]} oleh {book[1]}")
    
    choice = input("Masukkan nomor buku yang ingin dihapus: ")
    
    if not choice.isdigit() or int(choice) > len(transactions[nim]):
        print("Pilihan tidak valid.")
        return
    
    choice = int(choice) - 1
    removed_book = transactions[nim].pop(choice)
    print(f"Buku '{removed_book[0]}' berhasil dihapus dari keranjang.")

# Fungsi untuk menampilkan ringkasan transaksi
def view_transaction(nim):
    if nim not in transactions or not transactions[nim]:
        print("Keranjang belanja kosong.")
        return
    
    print("\n===== Ringkasan Pembelian =====")
    total_price = 0
    for idx, book in enumerate(transactions[nim], 1):
        print(f"{idx}. {book[0]} oleh {book[1]} - Rp {book[2]}")
        total_price += book[2]
    
    print(f"\nTotal: Rp {total_price}")

# Menu utama setelah login
def user_menu(nim):
    while True:
        print("\n===== MENU =====")
        print("1. Lihat Buku Tersedia")
        print("2. Tambah Buku ke Keranjang")
        print("3. Hapus Buku dari Keranjang")
        print("4. Lihat Ringkasan Pembelian")
        print("5. Logout")
        
        choice = input("Pilih opsi: ")
        
        if choice == '1':
            display_books()
        elif choice == '2':
            add_purchase(nim)
        elif choice == '3':
            remove_purchase(nim)
        elif choice == '4':
            view_transaction(nim)
        elif choice == '5':
            print("Logout berhasil.")
            break
        else:
            print("Pilihan tidak valid.")

# Fungsi utama untuk menjalankan program
def main():
    while True:
        print("\n===== APLIKASI MANAJEMEN TOKO BUKU =====")
        print("1. Login")
        print("2. Keluar")
        
        choice = input("Pilih opsi: ")
        
        if choice == '1':
            login()
        elif choice == '2':
            print("Terima kasih icik boss.")
            break
        else:
            print("Pilihan tidak valid.")

# Menjalankan program utama
if __name__ == "__main__":
    main()
 