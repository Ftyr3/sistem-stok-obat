# Sistem Manajemen Stok Obat

Aplikasi console Python untuk mengelola stok obat di apotek/farmasi.

## Fitur

- Login & Register pengguna (role admin/user)
- Admin: CRUD obat, cari obat, urutkan obat, proses penjualan, laporan ringkasan
- User: lihat daftar obat, cari obat, lihat laporan
- Struktur data bertingkat: `dict` obat -> field -> `list` riwayat transaksi
- Validasi input dan error handling (`try/except`, `while` sampai input valid)

## Struktur Data Obat

Setiap obat menyimpan: `nama` (str), `kategori` (str), `stok` (int),
`harga_beli`/`harga_jual` (float), `supplier` (str), `kadaluarsa` (str),
dan `riwayat` (list of dict) untuk catatan transaksi masuk/keluar.

## Cara Menjalankan

```bash
# aktifkan virtual environment
source .venv/bin/activate

# jalankan program
python main.py
```

## Akun Demo

| Role  | Username | Password  |
|-------|----------|-----------|
| Admin | daniel    | admin123  |
| User  | user1    | user123   |

User baru dapat dibuat lewat menu **Register** (role `user`).

## Dependensi

- Python 3.x
- `prettytable`, `pwinput` (sudah terinstall di `.venv`)
