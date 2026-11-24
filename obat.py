from utils import validasi_angka, generate_id_baru, bersihkan_layar, input_angka, input_desimal
from data import daftar_obat, kategori_obat
from prettytable import PrettyTable
from menu import tampilkan_tabel_obat

batas_stok_menipis = 10

def _pilih_obat(judul):      #Menampilkan daftar obat bernomor, mengembalikan key obat yang dipilih atau None
    if len(daftar_obat) == 0:
        print("Belum ada obat untuk dipilih!")
        return None

    tabel = PrettyTable()
    tabel.field_names = ["No", "ID", "Nama Obat", "Kategori", "Stok", "Harga Jual"]
    tabel.align = "l"
    tabel.hrules = 1
    for i, (id_obat, info) in enumerate(daftar_obat.items(), start=1):
        tabel.add_row([i, id_obat, info["nama"].title(), info["kategori"], info["stok"], f"{info['harga_jual']:,.0f}"])
    print(judul)
    print(tabel)

    kunci = list(daftar_obat.keys())
    pilih = input("Masukkan nomor obat (0 untuk batal): ")

    if validasi_angka(pilih) and 1 <= int(pilih) <= len(kunci):
        return kunci[int(pilih) - 1]
    elif pilih == "0":
        print("Dibatalkan.")
    else:
        print("Nomor tidak valid!")
    return None

def _pilih_kategori():   #Meminta user memilih kategori dari tuple kategori_obat
    print("Pilih kategori obat:")
    for i, kategori in enumerate(kategori_obat, start=1):
        print(f"  {i}. {kategori.title()}")

    while True:
        pilih = input("Masukkan nomor kategori: ").strip()
        if validasi_angka(pilih) and 1 <= int(pilih) <= len(kategori_obat):
            return kategori_obat[int(pilih) - 1]
        print("Pilihan tidak valid!")

def lihat_obat():
    try:
        tampilkan_tabel_obat()
        input("\nTekan Enter untuk kembali...")
    except KeyboardInterrupt:
        print("\n\nKembali ke menu...")
    except Exception as e:
        print(f"Error saat menampilkan obat: {e}")
        input("\nTekan Enter untuk kembali...")

def tambah_obat():
    try:
        bersihkan_layar()
        print("=== TAMBAH OBAT ===")

        id_baru = generate_id_baru()
        nama = input("Nama obat: ").strip().title()

        if not nama:
            print("Nama obat tidak boleh kosong!")
            input("Tekan Enter untuk kembali...")
            return

        kategori = _pilih_kategori()
        stok = input_angka("Stok awal: ", minimal=0)
        harga_beli = input_desimal("Harga beli: ", minimal=0)
        harga_jual = input_desimal("Harga jual: ", minimal=0)
        supplier = input("Supplier: ").strip()
        kadaluarsa = input("Tanggal kadaluarsa (YYYY-MM-DD): ").strip()

        if len(kadaluarsa) != 10 or kadaluarsa[4] != "-" or kadaluarsa[7] != "-":
            print("Format kadaluarsa tidak valid! Gunakan YYYY-MM-DD.")
            input("Tekan Enter untuk kembali...")
            return

        daftar_obat[id_baru] = {
            "nama": nama,
            "kategori": kategori,
            "stok": stok,
            "harga_beli": harga_beli,
            "harga_jual": harga_jual,
            "supplier": supplier,
            "kadaluarsa": kadaluarsa,
            "riwayat": [{"tanggal": "2026-11-25", "jenis": "masuk", "jumlah": stok}]
        }
        print(f"Obat '{nama}' berhasil ditambahkan dengan ID {id_baru}!")
        input("Tekan Enter untuk kembali...")
    except KeyboardInterrupt:
        print("\n\nPenambahan obat dibatalkan.")
        input("Tekan Enter untuk kembali...")
    except Exception as e:
        print(f"Error saat menambah obat: {e}")
        print("Gagal menambahkan obat.")
        input("Tekan Enter untuk kembali...")

def update_obat():
    try:
        bersihkan_layar()
        print("=== UPDATE DATA OBAT ===")

        if len(daftar_obat) == 0:
            print("Belum ada obat untuk diupdate!")
            input("Tekan Enter untuk kembali...")
            return

        id_obat = _pilih_obat("Pilih obat yang ingin diupdate:")
        if id_obat is None:
            input("Tekan Enter untuk kembali...")
            return

        obat = daftar_obat[id_obat]
        print("Kosongkan jika tidak ingin mengubah.")

        nama_baru = input(f"Nama baru ({obat['nama']}): ").strip()
        kategori_baru = input(f"Kategori baru ({obat['kategori']}): ").strip().lower()
        stok_baru = input(f"Stok baru ({obat['stok']}): ").strip()
        harga_beli_baru = input(f"Harga beli baru ({obat['harga_beli']}): ").strip()
        harga_jual_baru = input(f"Harga jual baru ({obat['harga_jual']}): ").strip()
        supplier_baru = input(f"Supplier baru ({obat['supplier']}): ").strip()
        kadaluarsa_baru = input(f"Kadaluarsa baru ({obat['kadaluarsa']}): ").strip()

        berhasil = False
        if nama_baru:
            obat["nama"] = nama_baru.title()
            berhasil = True
        if kategori_baru:
            if kategori_baru in kategori_obat:
                obat["kategori"] = kategori_baru
                berhasil = True
            else:
                print("Kategori tidak dikenal, tidak diubah.")
        if stok_baru:
            if validasi_angka(stok_baru):
                obat["stok"] = int(stok_baru)
                berhasil = True
            else:
                print("Stok harus angka, tidak diubah.")
        if harga_beli_baru:
            try:
                obat["harga_beli"] = float(harga_beli_baru)
                berhasil = True
            except ValueError:
                print("Harga beli harus angka, tidak diubah.")
        if harga_jual_baru:
            try:
                obat["harga_jual"] = float(harga_jual_baru)
                berhasil = True
            except ValueError:
                print("Harga jual harus angka, tidak diubah.")
        if supplier_baru:
            obat["supplier"] = supplier_baru
            berhasil = True
        if kadaluarsa_baru:
            if len(kadaluarsa_baru) == 10 and kadaluarsa_baru[4] == "-" and kadaluarsa_baru[7] == "-":
                obat["kadaluarsa"] = kadaluarsa_baru
                berhasil = True
            else:
                print("Format kadaluarsa tidak valid, tidak diubah.")

        if berhasil:
            print("Data berhasil diperbarui.")
        else:
            print("Tidak ada perubahan.")
        input("Tekan Enter untuk kembali...")
    except KeyboardInterrupt:
        print("\n\nUpdate obat dibatalkan.")
        input("Tekan Enter untuk kembali...")
    except Exception as e:
        print(f"Error saat update obat: {e}")
        print("Gagal mengupdate obat.")
        input("Tekan Enter untuk kembali...")

def hapus_obat():
    try:
        bersihkan_layar()
        print("=== HAPUS OBAT ===")

        if len(daftar_obat) == 0:
            print("Belum ada obat untuk dihapus!")
            input("Tekan Enter untuk kembali...")
            return

        id_obat = _pilih_obat("Pilih obat yang ingin dihapus:")
        if id_obat is None:
            input("Tekan Enter untuk kembali...")
            return

        konfirmasi = input(f"Yakin hapus '{daftar_obat[id_obat]['nama']}'? (y/n): ").strip().lower()
        if konfirmasi == "y":
            del daftar_obat[id_obat]
            print("Data berhasil dihapus.")
        else:
            print("Penghapusan dibatalkan.")
        input("Tekan Enter untuk kembali...")
    except KeyboardInterrupt:
        print("\n\nPenghapusan obat dibatalkan.")
        input("Tekan Enter untuk kembali...")
    except Exception as e:
        print(f"Error saat menghapus obat: {e}")
        print("Gagal menghapus obat.")
        input("Tekan Enter untuk kembali...")

def cari_obat():
    try:
        bersihkan_layar()
        print("=== CARI OBAT ===")
        keyword = input("Masukkan kata kunci (nama/ID/kategori): ").strip().lower()

        if not keyword:
            print("Kata kunci tidak boleh kosong!")
            input("Tekan Enter untuk kembali...")
            return

        hasil = {}
        ditemukan = False
        for id_obat, info in daftar_obat.items():
            if (keyword in info["nama"].lower()
                    or keyword in id_obat.lower()
                    or keyword in info["kategori"].lower()):
                hasil[id_obat] = info
                ditemukan = True

        if ditemukan:
            tampilkan_tabel_obat("=== HASIL PENCARIAN ===", hasil)
        else:
            print(f"Tidak ditemukan obat dengan kata kunci '{keyword}'.")
        input("\nTekan Enter untuk kembali...")
    except KeyboardInterrupt:
        print("\n\nPencarian dibatalkan.")
        input("Tekan Enter untuk kembali...")
    except Exception as e:
        print(f"Error saat mencari obat: {e}")
        input("Tekan Enter untuk kembali...")

def urutkan_obat():
    try:
        bersihkan_layar()
        print("=== URUTKAN OBAT ===")
        print("Urutkan berdasarkan:")
        print("  1. Nama obat")
        print("  2. Harga jual")
        print("  3. Harga beli")
        print("  4. Stok")

        kriteria_list = [
            ("nama", lambda kv: kv[1]["nama"].lower()),
            ("harga_jual", lambda kv: kv[1]["harga_jual"]),
            ("harga_beli", lambda kv: kv[1]["harga_beli"]),
            ("stok", lambda kv: kv[1]["stok"])
        ]

        while True:
            pilih = input("Pilih kriteria (0 untuk batal): ").strip()
            if pilih == "0":
                print("Dibatalkan.")
                input("Tekan Enter untuk kembali...")
                return
            if validasi_angka(pilih) and 1 <= int(pilih) <= len(kriteria_list):
                nama_kriteria, key_func = kriteria_list[int(pilih) - 1]
                urut = dict(sorted(daftar_obat.items(), key=key_func))
                tampilkan_tabel_obat(f"=== OBAT URUT BERDASARKAN {nama_kriteria.upper().replace('_', ' ')} ===", urut)
                input("\nTekan Enter untuk kembali...")
                return
            print("Pilihan tidak valid!")
    except KeyboardInterrupt:
        print("\n\nPengurutan dibatalkan.")
        input("Tekan Enter untuk kembali...")
    except Exception as e:
        print(f"Error saat mengurutkan obat: {e}")
        input("Tekan Enter untuk kembali...")

def jual_obat():   #Memproses penjualan obat: mengurangi stok dan mencatat riwayat
    try:
        bersihkan_layar()
        print("=== PROSES PENJUALAN ===")

        id_obat = _pilih_obat("Pilih obat yang dijual:")
        if id_obat is None:
            input("Tekan Enter untuk kembali...")
            return

        obat = daftar_obat[id_obat]
        print(f"Stok tersedia: {obat['stok']} | Harga jual: Rp {obat['harga_jual']:,.0f}")

        jumlah = input_angka("Jumlah obat yang dijual: ", minimal=1)
        stok_cukup = jumlah <= obat["stok"]

        if not stok_cukup:
            print(f"Stok tidak mencukupi! Sisa stok hanya {obat['stok']}.")
            input("Tekan Enter untuk kembali...")
            return

        total_penjualan = jumlah * obat["harga_jual"]
        obat["stok"] -= jumlah
        obat["riwayat"].append({"tanggal": "2026-11-25", "jenis": "keluar", "jumlah": jumlah})

        print(f"Penjualan berhasil!")
        print(f"  Obat       : {obat['nama']}")
        print(f"  Jumlah     : {jumlah}")
        print(f"  Total      : Rp {total_penjualan:,.0f}")
        print(f"  Sisa stok  : {obat['stok']}")
        input("Tekan Enter untuk kembali...")
    except KeyboardInterrupt:
        print("\n\nPenjualan dibatalkan.")
        input("Tekan Enter untuk kembali...")
    except Exception as e:
        print(f"Error saat proses penjualan: {e}")
        input("Tekan Enter untuk kembali...")

def laporan_obat():
    try:
        bersihkan_layar()
        print("=== LAPORAN RINGKASAN STOK OBAT ===")

        if len(daftar_obat) == 0:
            print("Belum ada data obat!")
            input("Tekan Enter untuk kembali...")
            return

        total_nilai_stok = 0.0
        total_potensi_laba = 0.0
        total_unit = 0
        kategori_terpakai = set()
        stok_menipis = []

        for id_obat, info in daftar_obat.items():
            nilai_stok = info["stok"] * info["harga_beli"]
            laba = (info["harga_jual"] - info["harga_beli"]) * info["stok"]
            total_nilai_stok += nilai_stok
            total_potensi_laba += laba
            total_unit += info["stok"]
            kategori_terpakai.add(info["kategori"])
            if info["stok"] <= batas_stok_menipis:
                stok_menipis.append((id_obat, info["nama"], info["stok"]))

        print("-" * 45)
        print(f"Jumlah jenis obat      : {len(daftar_obat)}")
        print(f"Total unit obat        : {total_unit}")
        print(f"Kategori terpakai      : {', '.join(sorted(kategori_terpakai))}")
        print(f"Nilai stok (harga beli): Rp {total_nilai_stok:,.0f}")
        print(f"Potensi laba           : Rp {total_potensi_laba:,.0f}")
        print("-" * 45)

        if stok_menipis:
            print("PERINGATAN - Stok menipis (<= 10):")
            for id_obat, nama, stok in stok_menipis:
                print(f"  [{id_obat}] {nama} - sisa {stok} unit")
        else:
            print("Semua stok di atas batas minimum.")

        input("\nTekan Enter untuk kembali...")
    except KeyboardInterrupt:
        print("\n\nLaporan dibatalkan.")
        input("Tekan Enter untuk kembali...")
    except Exception as e:
        print(f"Error saat membuat laporan: {e}")
        input("Tekan Enter untuk kembali...")
