import time
import pwinput
from utils import bersihkan_layar
import data



def login():
    try:
        global pengguna_login
        bersihkan_layar()
        print("=== LOGIN ===")
        percobaan = 0
        berhasil = False
        level_akses = None

        while percobaan < 3 and not berhasil:
            try:
                username = input("Masukkan Username: ").lower()
                password = pwinput.pwinput(prompt="Masukkan Password: ", mask="*")

                if username in data.data_pengguna and password == data.data_pengguna[username]["password"]:
                    data.pengguna_login = username
                    level_akses = data.data_pengguna[username]["level"]
                    berhasil = True
                else:
                    percobaan += 1
                    sisa = 3 - percobaan
                    if sisa > 0:
                        print(f"Username atau password salah! Sisa percobaan: {sisa}")
                    else:
                        print("Username atau password salah 3 kali. Silakan tunggu 5 menit sebelum mencoba lagi.")
                        time.sleep(300)
            except KeyboardInterrupt:
                print("\nLogin dibatalkan.")
                return False, None
            except Exception as e:
                print(f"Error saat login: {e}")
                percobaan += 1

        return berhasil, level_akses
    except Exception as e:
        print(f"Error pada fungsi login: {e}")
        return False, None

def register():
    try:
        bersihkan_layar()
        print("=== REGISTER PENGGUNA BARU ===")
        username = input("Masukkan username: ").lower()
        
        if not username or username.strip() == "":
            print("Username tidak boleh kosong!")
            return
        
        password = pwinput.pwinput(prompt="Masukkan Password: ", mask="*")
        
        if not password or password.strip() == "":
            print("Password tidak boleh kosong!")
            return

        if username in data.data_pengguna:
            print("Username sudah digunakan!")
        else:
            data.data_pengguna[username] = {"password": password, "level": "user"}
            print("Registrasi berhasil! Silakan login.")
    except KeyboardInterrupt:
        print("\n\nRegistrasi dibatalkan.")
    except Exception as e:
        print(f"Error saat registrasi: {e}")
        print("Registrasi gagal. Silakan coba lagi.")