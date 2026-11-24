# {username: {password, level}}
data_pengguna = {
    "daniel": {
        "password": "admin123",
        "level": "admin"
    },
    "user1": {
        "password": "user123",
        "level": "user"
    }
}


kategori_obat = (
    "analgesik",
    "antibiotik",
    "antihistamin",
    "vitamin",
    "antacid",
    "obat luar",
    "lainnya"
)

# {id_obat: {nama, kategori, stok, harga_beli, harga_jual, supplier, kadaluarsa, riwayat}}
# Struktur bertingkat: dict -> dict -> list of dict (riwayat transaksi)
daftar_obat = {
    "OB001": {
        "nama": "Paracetamol 500 mg",
        "kategori": "analgesik",
        "stok": 150,
        "harga_beli": 400.0,
        "harga_jual": 750.0,
        "supplier": "PT Sehat Jaya",
        "kadaluarsa": "2027-03-15",
        "riwayat": [
            {"tanggal": "2026-01-05", "jenis": "masuk", "jumlah": 200},
            {"tanggal": "2026-02-10", "jenis": "keluar", "jumlah": 50}
        ]
    },
    "OB002": {
        "nama": "Amoxicillin 500 mg",
        "kategori": "antibiotik",
        "stok": 8,
        "harga_beli": 1200.0,
        "harga_jual": 2000.0,
        "supplier": "PT Kimia Farma",
        "kadaluarsa": "2026-08-20",
        "riwayat": [
            {"tanggal": "2026-01-12", "jenis": "masuk", "jumlah": 100}
        ]
    },
    "OB003": {
        "nama": "Vitamin C 1000 mg",
        "kategori": "vitamin",
        "stok": 75,
        "harga_beli": 1500.0,
        "harga_jual": 2500.0,
        "supplier": "PT Vita Sehat",
        "kadaluarsa": "2027-11-01",
        "riwayat": []
    },
    "OB004": {
        "nama": "Betadine Solution 30 ml",
        "kategori": "obat luar",
        "stok": 40,
        "harga_beli": 9000.0,
        "harga_jual": 15000.0,
        "supplier": "PT Antiseptik Nusantara",
        "kadaluarsa": "2027-01-25",
        "riwayat": [
            {"tanggal": "2026-02-01", "jenis": "masuk", "jumlah": 60}
        ]
    },
    "OB005": {
        "nama": "Antalgin 500 mg",
        "kategori": "analgesik",
        "stok": 3,
        "harga_beli": 600.0,
        "harga_jual": 1100.0,
        "supplier": "PT Sehat Jaya",
        "kadaluarsa": "2026-12-10",
        "riwayat": []
    }
}

pengguna_login = None
