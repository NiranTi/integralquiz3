import sympy as sp
import scipy.integrate as spi

def integral_taktentu():
    """Menghitung integral tak tentu simbolik"""
    x = sp.symbols('x')
    fungsi = input("\nMasukkan fungsi untuk diintegralkan (misal x**2 + 3*x + 2): ")
    fungsi = sp.sympify(fungsi)  # Mengonversi input string menjadi ekspresi simbolik
    hasil = sp.integrate(fungsi, x)

    print("Hasil :")
    print(f"{hasil} + c")

    input("\nTekan Enter untuk kembali ke menu...")
