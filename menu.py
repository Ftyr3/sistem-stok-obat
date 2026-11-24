import data
from prettytable import PrettyTable
from utils import bersihkan_layar
from data import daftar_obat

def tampilkan_menu_utama():
    try:
        bersihkan_layar()
        print("💊  SISTEM MANAJEMEN STOK OBAT  💊")
        tabel_menu = PrettyTable()
        tabel_menu.field_names = ["No", "🧭 Menu Utama"]
        tabel_menu.align = "l"
        tabel_menu.hrules = 1
        tabel_menu.add_row(["1", "🔑 Login"])
        tabel_menu.add_row(["2", "📝 Register"])
        tabel_menu.add_row(["3", "🚪 Keluar"])
        print(tabel_menu)
    except Exception as e:
        print(f"Error saat menampilkan menu utama: {e}")
        print("\n=== MENU UTAMA ===")
        print("1. Login")
        print("2. Register")
        print("3. Keluar")

def tampilkan_menu_admin():
    try:
        bersihkan_layar()
        print("=" * 60)
        print("  MENU ADMIN ".center(60))
        print("=" * 60)
        print(f"Login sebagai: {data.pengguna_login.capitalize()}".center(60))

        tabel_admin = PrettyTable()
        tabel_admin.field_names = ["No", "Pilihan Menu"]
        tabel_admin.align = "l"
        tabel_admin.hrules = 1
        tabel_admin.add_row(["1", "Lihat Semua Obat"])
        tabel_admin.add_row(["2", "Tambah Obat"])
        tabel_admin.add_row(["3", "Update Obat"])
        tabel_admin.add_row(["4", "Hapus Obat"])
        tabel_admin.add_row(["5", "Cari Obat"])
        tabel_admin.add_row(["6", "Urutkan Obat"])
        tabel_admin.add_row(["7", "Proses Penjualan"])
        tabel_admin.add_row(["8", "Laporan Ringkasan"])
        tabel_admin.add_row(["9", "Logout"])
        print(tabel_admin)

    except Exception as e:
        print(f"Error saat menampilkan menu admin: {e}")
        print("\n=== MENU ADMIN ===")
        print("1. Lihat Semua Obat")
        print("2. Tambah Obat")
        print("3. Update Obat")
        print("4. Hapus Obat")
        print("5. Cari Obat")
        print("6. Urutkan Obat")
        print("7. Proses Penjualan")
        print("8. Laporan Ringkasan")
        print("9. Logout")

def tampilkan_menu_user():
    try:
        bersihkan_layar()
        print("=== MENU USER ===")
        print(f"Login sebagai: {data.pengguna_login.capitalize()}".center(60))

        tabel_user = PrettyTable()
        tabel_user.field_names = ["No", "Pilihan Menu"]
        tabel_user.align = "l"
        tabel_user.hrules = 1
        tabel_user.add_row(["1", "Lihat Semua Obat"])
        tabel_user.add_row(["2", "Cari Obat"])
        tabel_user.add_row(["3", "Lihat Laporan"])
        tabel_user.add_row(["4", "Logout"])
        print(tabel_user)

    except Exception as e:
        print(f"Error saat menampilkan menu user: {e}")
        print("\n=== MENU USER ===")
        print("1. Lihat Semua Obat")
        print("2. Cari Obat")
        print("3. Lihat Laporan")
        print("4. Logout")

def tampilkan_tabel_obat(judul="=== Daftar Obat ===", data_obat=None):
    try:
        bersihkan_layar()
        print(judul)
        data_tampil = daftar_obat if data_obat is None else data_obat
        if len(data_tampil) == 0:
            print("Belum ada data obat")
        else:
            tabel = PrettyTable()
            tabel.field_names = ["No", "ID", "Nama Obat", "Kategori", "Stok", "Harga Jual", "Kadaluarsa"]
            tabel.align = "l"
            tabel.hrules = 1
            for i, (id_obat, info) in enumerate(data_tampil.items(), start=1):
                tabel.add_row([
                    i,
                    id_obat,
                    info["nama"].title(),
                    info["kategori"],
                    info["stok"],
                    f"{info['harga_jual']:,.0f}",
                    info["kadaluarsa"]
                ])
            print(tabel)
    except Exception as e:
        print(f"Error saat menampilkan tabel obat: {e}")
        print("Terjadi kesalahan saat menampilkan data obat.")
