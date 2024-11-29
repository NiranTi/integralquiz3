import scipy.integrate as spi

# Program untuk menghitung integral tentu
class integral_tentu():
    def integrate():
        # Meminta input fungsi matematika dari pengguna
        fungsi = input("Masukkan fungsi untuk diintegralkan (misal x**2 + 3*x + 2): ")

        # Fungsi untuk mengonversi input dari pengguna menjadi fungsi Python
        def convert_to_function(fungsi):
            # Membuat fungsi dari string input menggunakan eval
            # Perlu hati-hati dengan penggunaan eval di sini, pastikan input aman
            def func(x):
                return eval(fungsi)
            return func

        # Mengonversi ekspresi input menjadi fungsi Python
        f = convert_to_function(fungsi)

        # Meminta input batas bawah dan batas atas untuk integral
        a = float(input("\nMasukkan batas bawah integral (a): "))
        b = float(input("Masukkan batas atas integral (b): "))

        # Menghitung integral tentu menggunakan scipy.integrate.quad
        hasil, error = spi.quad(f, a, b)

        # Menampilkan hasil integral dan kesalahan
        print(f"\nHasil integral tentu dari {fungsi} dari {a} hingga {b} adalah: {hasil}")
        input("\nTekan Enter untuk kembali ke menu...")