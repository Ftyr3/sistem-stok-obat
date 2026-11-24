from data import daftar_obat
import os

def bersihkan_layar():
    try:
        os.system("cls || clear")
    except Exception as e:
        print(f"Error saat membersihkan layar: {e}")
        pass

def validasi_angka(input_str):
    try:
        return input_str.isdigit()
    except Exception:
        return False

def input_angka(prompt, minimal=0):
    while True:
        try:
            nilai = int(input(prompt))
            if nilai < minimal:
                print(f"Nilai minimal {minimal}!")
                continue
            return nilai
        except ValueError:
            print("Input harus berupa bilangan bulat!")
        except KeyboardInterrupt:
            raise

def input_desimal(prompt, minimal=0.0):
    while True:
        try:
            nilai = float(input(prompt))
            if nilai < minimal:
                print(f"Nilai minimal {minimal}!")
                continue
            return nilai
        except ValueError:
            print("Input harus berupa angka!")
        except KeyboardInterrupt:
            raise

def generate_id_baru(n=1):
    try:
        id_baru = f"OB{n:03d}"
        if id_baru not in daftar_obat:
            return id_baru
        else:
            return generate_id_baru(n + 1)
    except RecursionError:
        print("Error: terlalu banyak obat!")
        return f"OB{len(daftar_obat)+1:03d}"
    except Exception as e:
        print(f"Error saat generate ID: {e}")
        return f"OB{len(daftar_obat)+1:03d}"
