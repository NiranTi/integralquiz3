import scipy.integrate as spi
import re #untuk replace input matematika dan convert agar terbaca

# Program untuk menghitung integral tentu dari fungsi yang berbentuk akar
class integralTentu:
    def convert_input(self, fungsi):
        # Menangani input agar lebih mudah dibaca (misalnya sqrt(x) menjadi x**0.5)
        fungsi = fungsi.replace("^", "**")  # Ganti tanda ^ menjadi **

        # Menangani notasi akar seperti sqrt(x) menjadi x**0.5
        fungsi = fungsi.replace("sqrt(", "(")  # Ganti sqrt(x) menjadi (x**0.5)

        # Menangani notasi seperti 2x^2 menjadi 2*x**2
        fungsi = re.sub(r'(\d)(x)', r'\1*\2', fungsi)  # Memasukkan * antara angka dan x jika tidak ada
        
        return fungsi

    def integral_tentu(self):
        # Meminta input fungsi matematika dari pengguna
        fungsi = input("Masukkan fungsi untuk diintegralkan (misal 3x*(3x^2 - 2)**0.5): ")

        # Mengonversi input agar Python dapat memprosesnya
        fungsi = self.convert_input(fungsi)

        # Fungsi untuk mengonversi input dari pengguna menjadi fungsi Python
        def convert_to_function(fungsi):
            def func(x):
                # Memastikan bahwa kita tidak mengambil akar dari angka negatif
                if (3*x**2 - 2) < 0:
                    return float('0')  # Mengembalikan 0 jika nilai di dalam akar negatif
                return eval(fungsi)
            return func

        # Mengonversi ekspresi input menjadi fungsi Python
        f = convert_to_function(fungsi)

        # Meminta input batas bawah dan batas atas untuk integral
        a = float(input("\nMasukkan batas bawah integral (a): "))
        b = float(input("Masukkan batas atas integral (b): "))

        # Menghitung integral tentu menggunakan scipy.integrate.quad
        hasil, error = spi.quad(f, a, b)

        # Menampilkan hasil integral
        print(f"Hasil: {hasil}")

        input("\nTekan Enter untuk kembali ke menu...")
