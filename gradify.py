def hitung_nilai_akhir(nilai_tugas, nilai_absen, nilai_uts, nilai_uas):
    
    bobot_tugas = 0.15
    bobot_absen = 0.05
    bobot_uts   = 0.35
    bobot_uas   = 0.45

    nilai_akhir = (nilai_tugas * bobot_tugas) + \
                  (nilai_absen * bobot_absen) + \
                  (nilai_uts * bobot_uts) + \
                  (nilai_uas * bobot_uas)

    return nilai_akhir

print("=== SISTEM CEK KELULUSAN MAHASISWA ===\n")

nama_mhs = input("Masukkan Nama Mahasiswa : ")
print("-" * 35) 

try:
    nilai_tugas = float(input("Masukkan Nilai Tugas : "))
    nilai_absen = float(input("Masukkan Nilai Absen : "))
    nilai_uts   = float(input("Masukkan Nilai UTS   : "))
    nilai_uas   = float(input("Masukkan Nilai UAS   : "))

    if all(0 <= n <= 100 for n in [nilai_tugas, nilai_absen, nilai_uts, nilai_uas]):
        
        skor_akhir = hitung_nilai_akhir(nilai_tugas, nilai_absen, nilai_uts, nilai_uas)
        
        batas_lulus = 60
        status = "LULUS" if skor_akhir >= batas_lulus else "TIDAK LULUS"

        print("\n" + "="*35)
        print(f"   LAPORAN HASIL STUDI: {nama_mhs.upper()}")
        print("="*35)
        print(f"Nilai Tugas : {nilai_tugas}")
        print(f"Nilai Absen : {nilai_absen}")
        print(f"Nilai UTS   : {nilai_uts}")
        print(f"Nilai UAS   : {nilai_uas}")
        print("-" * 35)
        print(f"NILAI AKHIR : {skor_akhir:.2f}")
        print(f"STATUS      : {status}")
        print("="*35)
        
        if status == "LULUS":
            print("Selamat! Pertahankan prestasimu.")
        else:
            print("Jangan menyerah, coba lagi semester depan!")

    else:
        print("\nError: Nilai harus berada di antara 0 sampai 100.")

except ValueError:
    print("\nError: Masukkan angka yang valid (bukan huruf).")
