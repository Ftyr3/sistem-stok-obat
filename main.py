from menu import tampilkan_menu_utama, tampilkan_menu_admin, tampilkan_menu_user, tampilkan_tabel_obat
from auth import login, register
from obat import lihat_obat, tambah_obat, update_obat, hapus_obat, cari_obat, urutkan_obat, jual_obat, laporan_obat
import time


def menu_admin():
    try:
        while True:
            try:
                tampilkan_menu_admin()
                opsi_admin = input("Pilih menu: ")

                if opsi_admin == "1":
                    lihat_obat()
                elif opsi_admin == "2":
                    tambah_obat()
                elif opsi_admin == "3":
                    update_obat()
                elif opsi_admin == "4":
                    hapus_obat()
                elif opsi_admin == "5":
                    cari_obat()
                elif opsi_admin == "6":
                    urutkan_obat()
                elif opsi_admin == "7":
                    jual_obat()
                elif opsi_admin == "8":
                    laporan_obat()
                elif opsi_admin == "9":
                    break
                else:
                    print("Pilihan tidak valid!")
                    input("Tekan Enter untuk lanjut...")
            except KeyboardInterrupt:
                print("\n\nKembali ke menu...")
                time.sleep(1)
            except Exception as e:
                print(f"Error di menu admin: {e}")
                input("Tekan Enter untuk lanjut...")
    except Exception as e:
        print(f"Error fatal di menu admin: {e}")
        print("Kembali ke menu utama...")

def menu_user():
    try:
        while True:
            try:
                tampilkan_menu_user()
                pilih_user = input("Pilih menu: ")

                if pilih_user == "1":
                    tampilkan_tabel_obat("=== DAFTAR OBAT ===")
                    input("\nTekan Enter untuk kembali...")
                elif pilih_user == "2":
                    cari_obat()
                elif pilih_user == "3":
                    laporan_obat()
                elif pilih_user == "4":
                    break
                else:
                    print("Pilihan tidak valid!")
                    input("Tekan Enter untuk lanjut...")
            except KeyboardInterrupt:
                print("\n\nKembali ke menu...")
                time.sleep(1)
            except Exception as e:
                print(f"Error di menu user: {e}")
                input("Tekan Enter untuk lanjut...")
    except Exception as e:
        print(f"Error fatal di menu user: {e}")
        print("Kembali ke menu utama...")

def main():
    try:
        while True:
            try:
                tampilkan_menu_utama()
                opsi = input("Pilih Menu : ")

                if opsi == "1":
                    berhasil, level_akses = login()

                    if berhasil:
                        if level_akses == "admin":
                            menu_admin()
                        elif level_akses == "user":
                            menu_user()

                elif opsi == "2":
                    register()

                elif opsi == "3":
                    print("Terima kasih telah menggunakan Program ini!")
                    break
                else:
                    print("Pilihan tidak valid!")
                    input("Tekan Enter untuk lanjut...")
            except KeyboardInterrupt:
                print("\n\nProgram dihentikan oleh user.")
                konfirmasi = input("Apakah Anda yakin ingin keluar? (y/n): ").lower()
                if konfirmasi == 'y':
                    print("Terima kasih telah menggunakan Program ini!")
                    break
            except Exception as e:
                print(f"Error tidak terduga: {e}")
                print("Program akan melanjutkan...")
                input("Tekan Enter untuk lanjut...")
    except Exception as e:
        print(f"Error fatal pada program: {e}")
        print("Program berhenti.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram dihentikan.")
    except Exception as e:
        print(f"Error fatal: {e}")
        print("Program berhenti.")
