import tkinter as tk
from tkinter import ttk, messagebox
from sympy import symbols, integrate, simplify, Rational

# Membuat simbol x untuk integral
x = symbols('x')

def format_fraction(expr):
    """
    Fungsi untuk memformat fraksi menjadi bentuk 1/3 * x^3.
    Misalnya x**3/3 menjadi 1/3 * x^3
    """
    # Jika bentuknya adalah fraksi, kita pisahkan pembilang dan penyebut
    if isinstance(expr, float) or isinstance(expr, int):
        return str(expr)
    
    # Menyederhanakan fraksi jika ada
    expr_str = str(expr)
    
    if '/' in expr_str:
        num, denom = expr_str.split('/')
        # Menggunakan 1/denom * num untuk menghasilkan 1/3 * x^3
        return f"1/{denom} * {num}"
    else:
        return expr_str

def calculate_integral():
    try:
        # Mendapatkan input dari pengguna
        function = entry_function.get()
        lower_limit = entry_lower.get()
        upper_limit = entry_upper.get()

        # Mengganti simbol √ (akar) dengan sqrt untuk SymPy
        function = function.replace('√', 'sqrt')

        # Mengganti kesalahan umum seperti sqrt3 menjadi sqrt(3)
        function = function.replace('sqrt3', 'sqrt(3)')

        # Mengganti simbol ^ menjadi ** untuk SymPy
        function = function.replace('^', '**')

        # Mengubah string menjadi fungsi simbolik
        expr = eval(function)

        # Menyederhanakan ekspresi
        simplified_expr = simplify(expr)

        steps = []  # Menyimpan langkah-langkah integral
        steps.append(f"Fungsi disederhanakan: {simplified_expr}")

        # Mengecek apakah integral tak tentu atau tentu
        if lower_limit and upper_limit:
            lower_limit = eval(lower_limit)
            upper_limit = eval(upper_limit)
            indefinite_integral = integrate(simplified_expr, x)
            definite_integral = integrate(simplified_expr, (x, lower_limit, upper_limit))

            steps.append(f"Hasil integral tentu: {format_fraction(definite_integral)}")

            result_text = f"Hasil Integral Tentu:\n{format_fraction(definite_integral)}\n\nLangkah-langkah:\n" + "\n".join(steps)
        else:
            indefinite_integral = integrate(simplified_expr, x)
            steps.append(f"Hasil integral tak tentu: {format_fraction(indefinite_integral)}")

            result_text = f"Hasil Integral Tak Tentu:\n{format_fraction(indefinite_integral)}\n\nLangkah-langkah:\n" + "\n".join(steps)

        # Menampilkan hasil pada text box
        text_output.config(state='normal')
        text_output.delete('1.0', tk.END)
        text_output.insert(tk.END, result_text)
        text_output.config(state='disabled')

    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan: {e}")

# Membuat GUI utama
root = tk.Tk()
root.title("Kalkulator Integral")

# Frame Input
frame_input = ttk.LabelFrame(root, text="Input Integral")
frame_input.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

# Input fungsi
label_function = ttk.Label(frame_input, text="Fungsi f(x):")
label_function.grid(row=0, column=0, padx=5, pady=5, sticky="w")
entry_function = ttk.Entry(frame_input, width=30)
entry_function.grid(row=0, column=1, padx=5, pady=5, sticky="w")

# Input batas bawah
label_lower = ttk.Label(frame_input, text="Batas Bawah:")
label_lower.grid(row=1, column=0, padx=5, pady=5, sticky="w")
entry_lower = ttk.Entry(frame_input, width=30)
entry_lower.grid(row=1, column=1, padx=5, pady=5, sticky="w")

# Input batas atas
label_upper = ttk.Label(frame_input, text="Batas Atas:")
label_upper.grid(row=2, column=0, padx=5, pady=5, sticky="w")
entry_upper = ttk.Entry(frame_input, width=30)
entry_upper.grid(row=2, column=1, padx=5, pady=5, sticky="w")

# Tombol Hitung
button_calculate = ttk.Button(frame_input, text="Hitung Integral", command=calculate_integral)
button_calculate.grid(row=3, column=0, columnspan=2, pady=10)

# Output
frame_output = ttk.LabelFrame(root, text="Output")
frame_output.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

text_output = tk.Text(frame_output, height=15, width=50, state='disabled')
text_output.grid(row=0, column=0, padx=5, pady=5)

# Menjalankan aplikasi
root.mainloop()
