import tkinter as tk
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error


class Form4:
    def __init__(self, root):
        self.root = root
        root.title("Form 4")
        root.geometry("520x380")

        self.label1 = tk.Label(
            root, text="Belum Terhubung", fg="red"
        )
        self.label1.place(x=195, y=60, width=130, height=30)

        self.button1 = tk.Button(
            root, text="Hubungkan",
            command=self.on_button1
        )
        self.button1.place(x=212, y=158, width=96, height=32)

        self.connection = None

    def open_form_2(self):
        return Form2(self.root, self.connection)

    def on_button1(self):
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="bengkell",
                port=3306
            )

            if self.connection.is_connected():
                self.label1.config(
                    text="Koneksi Berhasil!", fg="green"
                )
                self.open_form_2()

        except Error as e:
            self.label1.config(
                text="Koneksi Gagal!", fg="red"
            )
            messagebox.showerror(
                "Database Error", str(e)
            )


class Form2:
    def __init__(self, master, connection):
        self.root = tk.Toplevel(master)
        self.root.title("Form 2")
        self.root.geometry("520x380")

        self.connection = connection

        self.label1 = tk.Label(self.root, text="NIK")
        self.label1.place(x=80, y=106, width=60, height=20)

        self.label2 = tk.Label(self.root, text="Nama")
        self.label2.place(x=270, y=101, width=60, height=30)

        self.text1 = tk.Entry(self.root)
        self.text1.place(x=100, y=131, width=160, height=30)

        self.text2 = tk.Entry(self.root)
        self.text2.place(x=280, y=131, width=160, height=30)

        self.text3 = tk.Entry(self.root)
        self.text3.place(x=280, y=190, width=160, height=30)

        self.text4 = tk.Entry(self.root)
        self.text4.place(x=100, y=190, width=160, height=30)

        self.text5 = tk.Entry(self.root)
        self.text5.place(x=100, y=250, width=160, height=30)

        self.text6 = tk.Entry(self.root)
        self.text6.place(x=280, y=250, width=160, height=30)

        self.label3 = tk.Label(self.root, text="Alamat")
        self.label3.place(x=80, y=170, width=70, height=20)

        self.label4 = tk.Label(self.root, text="Kab/Kota")
        self.label4.place(x=270, y=170, width=70, height=20)

        self.label5 = tk.Label(self.root, text="Mobile")
        self.label5.place(x=80, y=230, width=70, height=20)

        self.label6 = tk.Label(self.root, text="Email")
        self.label6.place(x=265, y=230, width=70, height=20)

        self.button1 = tk.Button(
            self.root, text="Simpan",
            command=self.on_button1, bg="#00ff04"
        )
        self.button1.place(x=52, y=300, width=96, height=32)

        self.button2 = tk.Button(
            self.root, text="Ubah",
            command=self.on_button2,
            fg="white", bg="#1100ff"
        )
        self.button2.place(x=164, y=300, width=96, height=32)

        self.button3 = tk.Button(
            self.root, text="Clear",
            command=self.on_button3, bg="#fbff00"
        )
        self.button3.place(x=282, y=300, width=96, height=32)

        self.button4 = tk.Button(
            self.root, text="Delete",
            command=self.on_button4, bg="#ff0000"
        )
        self.button4.place(x=392, y=300, width=96, height=32)

    # Get values from input fields
    def get_values(self):
        return (
            self.text1.get().strip(),
            self.text2.get().strip(),
            self.text4.get("1.0", "end-1c").strip()
                if isinstance(self.text4, tk.Text)
                else self.text4.get().strip(),
            self.text3.get().strip(),
            self.text5.get().strip(),
            self.text6.get().strip()
        )

    # SIMPAN DATA (INSERT)
    def on_button1(self):
        try:
            nik, nama, alamat, kab_kota, mobile, email = (
                self.get_values()
            )

            if not nik or not nama:
                messagebox.showwarning(
                    "Peringatan",
                    "NIK dan Nama harus diisi!"
                )
                return

            cursor = self.connection.cursor()

            sql = """
                INSERT INTO konsumen
                (nik, nama, alamat, kab_kota, mobile, email)
                VALUES (%s, %s, %s, %s, %s, %s)
            """

            values = (
                nik, nama, alamat, kab_kota, mobile, email
            )

            cursor.execute(sql, values)
            self.connection.commit()
            cursor.close()

            messagebox.showinfo(
                "Sukses", "Data berhasil disimpan!"
            )

            self.on_button3()

        except Error as e:
            self.connection.rollback()
            messagebox.showerror(
                "Database Error", str(e)
            )

    # UBAH DATA (UPDATE)
    def on_button2(self):
        try:
            nik, nama, alamat, kab_kota, mobile, email = (
                self.get_values()
            )

            if not nik:
                messagebox.showwarning(
                    "Peringatan", "Masukkan NIK!"
                )
                return

            cursor = self.connection.cursor()

            sql = """
                UPDATE konsumen
                SET nama=%s, alamat=%s, kab_kota=%s,
                    mobile=%s, email=%s
                WHERE nik=%s
            """

            values = (
                nama, alamat, kab_kota,
                mobile, email, nik
            )

            cursor.execute(sql, values)
            self.connection.commit()

            if cursor.rowcount > 0:
                messagebox.showinfo(
                    "Sukses", "Data berhasil diubah!"
                )
            else:
                messagebox.showwarning(
                    "Informasi", "NIK tidak ditemukan!"
                )

            cursor.close()

        except Error as e:
            self.connection.rollback()
            messagebox.showerror(
                "Database Error", str(e)
            )

    # CLEAR INPUT
    def on_button3(self):
        for widget in (
            self.text1, self.text2, self.text3,
            self.text4, self.text5, self.text6
        ):
            widget.delete(0, tk.END)

    # DELETE DATA
    def on_button4(self):
        nik = self.text1.get().strip()

        if not nik:
            messagebox.showwarning(
                "Peringatan", "Masukkan NIK!"
            )
            return

        confirm = messagebox.askyesno(
            "Konfirmasi",
            "Yakin ingin menghapus data ini?"
        )

        if not confirm:
            return

        try:
            cursor = self.connection.cursor()

            sql = "DELETE FROM konsumen WHERE nik=%s"
            cursor.execute(sql, (nik,))

            self.connection.commit()

            if cursor.rowcount > 0:
                messagebox.showinfo(
                    "Sukses", "Data berhasil dihapus!"
                )
                self.on_button3()
            else:
                messagebox.showwarning(
                    "Informasi", "NIK tidak ditemukan!"
                )

            cursor.close()

        except Error as e:
            self.connection.rollback()
            messagebox.showerror(
                "Database Error", str(e)
            )


if __name__ == "__main__":
    root = tk.Tk()
    app = Form4(root)
    root.mainloop()