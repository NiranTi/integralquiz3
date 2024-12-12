import tkinter as tk
from integral_tak_tentu import integral_parsial_gui
from integral_tentu import integral_tentu_gui

def main_gui():
    root = tk.Tk()
    root.title("Kalkulator Integral")

    tk.Label(root, text="Kalkulator Integral", font=("Arial", 16)).pack(pady=10)

    tk.Button(root, text="Integral Tak Tentu", command=integral_parsial_gui, width=20).pack(pady=10)
    tk.Button(root, text="Integral Tentu", command=integral_tentu_gui, width=20).pack(pady=10)
    tk.Button(root, text="Keluar", command=root.quit, width=20).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main_gui()
