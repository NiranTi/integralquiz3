import os 
import sympy as sp
import scipy.integrate as spi
from integralTentu import integral_tentu
from integralTakTentu import integral_taktentu

def clear_screen():
    #Membersihkan layar terminal
    os.system('cls' if os.name == 'nt' else 'clear')

header = "\n===== Kalkulator Integral ====="

def welcomeScreen():
    #Menampilkan menu utama untuk kalkulator integral
    clear_screen()
    print(header)
    print("1. Menghitung integral tak tentu")
    print("2. Menghitung integral tentu")
    print("3. Keluar")

def main():
    #Fungsi utama untuk menjalankan kalkulator integral
    while True:
        welcomeScreen()
        pilihan = input("\nPilih menu (1/2/3): ")

        if pilihan == '1':
            clear_screen()
            print(header)
            integral_taktentu()
        elif pilihan == '2':
            clear_screen()
            print(header)
            integral_tentu()
        elif pilihan == '3':
            clear_screen()
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih antara 1 hingga 3.")
            input("\nTekan Enter untuk mencoba lagi...")

if __name__ == "__main__":
    main()
