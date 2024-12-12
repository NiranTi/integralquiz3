import tkinter as tk
from tkinter import messagebox
import sympy as sp
import scipy.integrate as spi

def integral_tentu_gui():
    def hitung_integral_tentu():
        try:
            x = sp.symbols('x')
            fungsi_input = entry_fungsi.get()
            fungsi_sym = sp.sympify(fungsi_input)
            f = sp.lambdify(x, fungsi_sym, 'numpy')

            a = float(entry_bawah.get())
            b = float(entry_atas.get())

            hasil, error = spi.quad(f, a, b)
            label_hasil["text"] = f"Hasil: {hasil}"
        except Exception as e:
            messagebox.showerror("Error", f"Terjadi kesalahan: {e}")

    window = tk.Toplevel()
    window.title("Integral Tentu")

    tk.Label(window, text="Masukkan fungsi:").pack(pady=5)
    entry_fungsi = tk.Entry(window, width=30)
    entry_fungsi.pack(pady=5)

    tk.Label(window, text="Batas bawah:").pack(pady=5)
    entry_bawah = tk.Entry(window, width=10)
    entry_bawah.pack(pady=5)

    tk.Label(window, text="Batas atas:").pack(pady=5)
    entry_atas = tk.Entry(window, width=10)
    entry_atas.pack(pady=5)

    tk.Button(window, text="Hitung", command=hitung_integral_tentu).pack(pady=10)
    label_hasil = tk.Label(window, text="Hasil:")
    label_hasil.pack(pady=5)
