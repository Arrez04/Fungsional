# Data global untuk menyimpan informasi user, profil, dan friend list
users = {}  # Dictionary untuk menyimpan akun user dengan NIM sebagai key
profiles = {}  # Dictionary untuk menyimpan profil user
friends = {}  # Dictionary untuk menyimpan list teman user


def register():
    """ Fungsi untuk melakukan registrasi user baru """
    nim = input("Masukkan NIM: ")
    if nim in users:
        print("NIM sudah terdaftar.")
        return
    
    password = input("Masukkan Password: ")
    users[nim] = password
    print("Registrasi berhasil!")

    # Arahkan ke pengisian profil dan friends list (opsional)
    if input("Ingin mengisi biodata sekarang? (y/n): ").lower() == 'y':
        add_profile(nim)
    if input("Ingin menambahkan daftar teman sekarang? (y/n): ").lower() == 'y':
        add_friend(nim)


def login():
    """ Fungsi untuk login user """
    nim = input("Masukkan NIM: ")
    password = input("Masukkan Password: ")
    
    if users.get(nim) == password:
        print("Login berhasil!")
        user_menu(nim)
    else:
        print("NIM atau Password salah.")


def user_menu(nim):
    """ Menu utama setelah login """
    while True:
        print("\n===== USER MENU =====")
        print("1. Lihat Profil")
        print("2. Tambah/Edit Profil")
        print("3. Tambah/Edit Friend List")
        print("4. Hapus Profil/Friend")
        print("5. Logout")
        choice = input("Pilih opsi: ")

        if choice == '1':
            view_profile(nim)
        elif choice == '2':
            add_profile(nim)
        elif choice == '3':
            add_friend(nim)
        elif choice == '4':
            delete_data(nim)
        elif choice == '5':
            print("Logout berhasil.")
            break
        else:
            print("Pilihan tidak valid.")


def view_profile(nim):
    """ Fungsi untuk melihat profil dan friend list """
    print("\n===== PROFIL =====")
    if nim in profiles:
        print(f"Profil: {profiles[nim]}")
    else:
        print("Profil belum diisi.")

    print("\n===== FRIEND LIST =====")
    if nim in friends:
        print(f"Teman: {friends[nim]}")
    else:
        print("Belum ada teman.")


def add_profile(nim):
    """ Fungsi untuk menambah/mengedit profil """
    name = input("Masukkan Nama: ")
    age = input("Masukkan Usia: ")
    address = input("Masukkan Alamat: ")
    profiles[nim] = {"Nama": name, "Usia": age, "Alamat": address}
    print("Profil berhasil ditambahkan/diedit.")


def add_friend(nim):
    """ Fungsi untuk menambah/mengedit daftar teman """
    if nim not in friends:
        friends[nim] = []
    
    while True:
        friend_name = input("Masukkan nama teman (atau ketik 'q' untuk keluar): ")
        if friend_name.lower() == 'q':
            break
        friends[nim].append(friend_name)
        print(f"{friend_name} berhasil ditambahkan ke friend list.")


def delete_data(nim):
    """ Fungsi untuk menghapus profil atau friend list """
    print("\n1. Hapus Profil")
    print("2. Hapus Semua Teman")
    print("3. Hapus Teman Tertentu")
    choice = input("Pilih opsi: ")

    if choice == '1':
        if nim in profiles:
            del profiles[nim]
            print("Profil berhasil dihapus.")
        else:
            print("Profil tidak ditemukan.")
    
    elif choice == '2':
        if nim in friends:
            del friends[nim]
            print("Semua teman berhasil dihapus.")
        else:
            print("Belum ada teman.")
    
    elif choice == '3':
        if nim in friends and friends[nim]:
            friend_name = input("Masukkan nama teman yang ingin dihapus: ")
            if friend_name in friends[nim]:
                friends[nim].remove(friend_name)
                print(f"{friend_name} berhasil dihapus dari friend list.")
            else:
                print(f"{friend_name} tidak ditemukan di friend list.")
        else:
            print("Belum ada teman.")
    else:
        print("Pilihan tidak valid.")


def main():
    """ Fungsi utama untuk menjalankan program """
    while True:
        print("\n===== MAIN MENU =====")
        print("1. Register")
        print("2. Login")
        print("3. Keluar")
        choice = input("Pilih opsi: ")

        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == '3':
            print("Terima kasih Icik Boss.")
            break
        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    main()
