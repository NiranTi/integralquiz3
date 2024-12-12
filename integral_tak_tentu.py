import tkinter as tk
from tkinter import messagebox
import sympy as sp

def integral_parsial_gui():
    def hitung_integral_parsial():
        try:
            x = sp.symbols('x')
            fungsi_input = entry_fungsi.get()
            fungsi = sp.sympify(fungsi_input)
            hasil = sp.integrate(fungsi, x)
            label_hasil["text"] = f"Hasil: {hasil} + C"
        except Exception as e:
            messagebox.showerror("Error", f"Terjadi kesalahan: {e}")

    window = tk.Toplevel()
    window.title("Integral Tak Tentu")

    tk.Label(window, text="Masukkan fungsi:").pack(pady=5)
    entry_fungsi = tk.Entry(window, width=30)
    entry_fungsi.pack(pady=5)

    tk.Button(window, text="Hitung", command=hitung_integral_parsial).pack(pady=10)
    label_hasil = tk.Label(window, text="Hasil:")
    label_hasil.pack(pady=5)
