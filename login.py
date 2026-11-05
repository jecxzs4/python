
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import csv


class Main:
    def __init__(self, root):
        self.root = root
        self.root.title("azzaki")
        self.root.geometry("520x380")
        self.root.resizable(False, False)
        self.root.configure(bg="#F1F5F9")

        self.data_biodata = None
        self.form = None

        # ================= MENU BAR =================
        menubar = tk.Menu(root)

        self.file_menu = tk.Menu(menubar, tearoff=0)
        self.file_menu.add_command(
            label="Simpan",
            command=self.on_file_simpan
        )
        self.file_menu.add_separator()
        self.file_menu.add_command(
            label="Keluar",
            command=self.root.destroy
        )
        menubar.add_cascade(label="File", menu=self.file_menu)

        self.biodata_menu = tk.Menu(menubar, tearoff=0)
        self.biodata_menu.add_command(
            label="Buka Biodata",
            command=self.open_form_2
        )
        self.biodata_menu.add_command(
            label="Lihat Biodata",
            command=self.lihat_biodata
        )
        menubar.add_cascade(
            label="Biodata",
            menu=self.biodata_menu
        )

        root.configure(menu=menubar)

        # ================= JUDUL =================
        tk.Label(
            root,
            text="LOGIN PESERTA DIKLAT",
            font=("Arial", 18, "bold"),
            bg="#F1F5F9",
            fg="#1E3A8A"
        ).place(x=60, y=20, width=400, height=40)

        # ================= NAMA =================
        self.label1 = tk.Label(
            root,
            text="Nama",
            font=("Arial", 11),
            bg="#F1F5F9"
        )
        self.label1.place(x=50, y=95, width=90, height=26)

        self.text1 = ttk.Entry(root, font=("Arial", 11))
        self.text1.place(x=150, y=90, width=240, height=32)

        # ================= PASSWORD =================
        self.label2 = tk.Label(
            root,
            text="Password",
            font=("Arial", 11),
            bg="#F1F5F9"
        )
        self.label2.place(x=50, y=145, width=90, height=26)

        self.text2 = ttk.Entry(root, show="*", font=("Arial", 11))
        self.text2.place(x=150, y=140, width=240, height=32)

        # ================= TOMBOL LOGIN =================
        self.button1 = tk.Button(
            root,
            text="LOGIN",
            font=("Arial", 11, "bold"),
            bg="#2563EB",
            fg="white",
            cursor="hand2",
            command=self.on_button1
        )
        self.button1.place(x=190, y=205, width=120, height=38)

        tk.Label(
            root,
            text="Aplikasi Pendaftaran Peserta Diklat",
            font=("Arial", 9),
            bg="#F1F5F9",
            fg="gray"
        ).place(x=100, y=300, width=320)

    # ================= FUNGSI LOGIN =================
    def on_button1(self):
        nama = self.text1.get().strip()
        password = self.text2.get()

        if nama == "" or password == "":
            messagebox.showwarning(
                "Peringatan",
                "Nama dan Password wajib diisi!"
            )
            return

        messagebox.showinfo(
            "Login Berhasil",
            f"Selamat datang, {nama}!"
        )

        self.open_form_2(nama)

    # ================= BUKA FORM BIODATA =================
    def open_form_2(self, nama=None):
        if self.form is not None and self.form.root.winfo_exists():
            self.form.root.lift()
            return

        if nama is None:
            nama = self.text1.get().strip()

        self.form = Form2(
            self.root,
            nama,
            self.update_biodata
        )

    # ================= UPDATE DATA =================
    def update_biodata(self, data):
        self.data_biodata = data

    # ================= MENU SIMPAN =================
    def on_file_simpan(self):
        if not self.data_biodata:
            messagebox.showwarning(
                "Peringatan",
                "Belum ada biodata yang bisa disimpan!"
            )
            return

        lokasi = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV Files", "*.csv")],
            title="Simpan Biodata"
        )

        if not lokasi:
            return

        try:
            with open(
                lokasi,
                "w",
                newline="",
                encoding="utf-8-sig"
            ) as file:
                writer = csv.writer(file)

                writer.writerow([
                    "Nama",
                    "Kelas",
                    "Materi Diklat"
                ])

                writer.writerow([
                    self.data_biodata["nama"],
                    self.data_biodata["kelas"],
                    self.data_biodata["materi"]
                ])

            messagebox.showinfo(
                "Berhasil",
                "Biodata berhasil disimpan!"
            )

        except OSError as error:
            messagebox.showerror(
                "Error",
                f"Gagal menyimpan data:\n{error}"
            )

    # ================= LIHAT BIODATA =================
    def lihat_biodata(self):
        if not self.data_biodata:
            messagebox.showwarning(
                "Peringatan",
                "Belum ada biodata yang disimpan!"
            )
            return

        data = self.data_biodata

        messagebox.showinfo(
            "Data Biodata",
            f"Nama: {data['nama']}\n"
            f"Kelas: {data['kelas']}\n"
            f"Materi Diklat: {data['materi']}"
        )


# =====================================================
# FORM BIODATA
# =====================================================

class Form2:
    def __init__(self, master, nama="", callback=None):
        self.root = tk.Toplevel(master)
        self.root.title("Form Biodata Peserta")
        self.root.geometry("520x380")
        self.root.resizable(False, False)
        self.root.configure(bg="#F1F5F9")

        self.callback = callback
        self.choice_var = tk.StringVar(value="")

        # ================= JUDUL =================
        tk.Label(
            self.root,
            text="BIODATA PESERTA DIKLAT",
            font=("Arial", 16, "bold"),
            bg="#F1F5F9",
            fg="#1E3A8A"
        ).place(x=50, y=20, width=420, height=35)

        # ================= NAMA =================
        self.label1 = tk.Label(
            self.root,
            text="Nama",
            font=("Arial", 11),
            bg="#F1F5F9"
        )
        self.label1.place(x=30, y=85, width=100, height=26)

        self.text1 = ttk.Entry(
            self.root,
            font=("Arial", 11)
        )
        self.text1.place(x=150, y=80, width=240, height=32)
        self.text1.insert(0, nama)

        # ================= KELAS =================
        self.label2 = tk.Label(
            self.root,
            text="Kelas",
            font=("Arial", 11),
            bg="#F1F5F9"
        )
        self.label2.place(x=30, y=140, width=100, height=26)

        self.combobox1 = ttk.Combobox(
            self.root,
            state="readonly",
            values=[
                "XI PPLG",
                "XI MP 1",
                "XI BR",
                "XI MP 2",
                "XI DKV 1",
                "XI DKV 2",
                "XI AKL 1",
                "XI AKL 2"
            ],
            font=("Arial", 10)
        )
        self.combobox1.place(x=150, y=135, width=240, height=32)

        # ================= MATERI DIKLAT =================
        self.label3 = tk.Label(
            self.root,
            text="Materi Diklat",
            font=("Arial", 11),
            bg="#F1F5F9"
        )
        self.label3.place(x=30, y=200, width=110, height=26)

        self.radiobutton2 = tk.Radiobutton(
            self.root,
            text="Python",
            variable=self.choice_var,
            value="Python",
            bg="#F1F5F9",
            font=("Arial", 10)
        )
        self.radiobutton2.place(x=150, y=195, width=100, height=26)

        self.radiobutton3 = tk.Radiobutton(
            self.root,
            text="Budaya Kerja",
            variable=self.choice_var,
            value="Budaya Kerja",
            bg="#F1F5F9",
            font=("Arial", 10)
        )
        self.radiobutton3.place(x=260, y=195, width=130, height=26)

        # ================= TOMBOL SIMPAN =================
        self.button_simpan = tk.Button(
            self.root,
            text="SIMPAN",
            font=("Arial", 10, "bold"),
            bg="#16A34A",
            fg="white",
            cursor="hand2",
            command=self.simpan
        )
        self.button_simpan.place(x=140, y=270, width=100, height=35)

        # ================= TOMBOL RESET =================
        self.button_reset = tk.Button(
            self.root,
            text="RESET",
            font=("Arial", 10, "bold"),
            bg="#DC2626",
            fg="white",
            cursor="hand2",
            command=self.reset
        )
        self.button_reset.place(x=270, y=270, width=100, height=35)

    # ================= FUNGSI SIMPAN =================
    def simpan(self):
        nama = self.text1.get().strip()
        kelas = self.combobox1.get()
        materi = self.choice_var.get()

        if not nama or not kelas or not materi:
            messagebox.showwarning(
                "Peringatan",
                "Mohon lengkapi semua data!"
            )
            return

        data = {
            "nama": nama,
            "kelas": kelas,
            "materi": materi
        }

        if self.callback:
            self.callback(data)

        messagebox.showinfo(
            "Berhasil",
            "Data biodata berhasil disimpan!"
        )

    # ================= FUNGSI RESET =================
    def reset(self):
        self.text1.delete(0, tk.END)
        self.combobox1.set("")
        self.choice_var.set("")


# =====================================================
# MENJALANKAN APLIKASI
# =====================================================

if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    root.mainloop()
