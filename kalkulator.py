
# Designed with https://visualtkinter.com
import tkinter as tk
from tkinter import ttk, messagebox
import ast
import operator


class Application:
    def __init__(self, root):
        self.root = root
        root.title("Main")
        root.geometry("520x380")

        # Judul
        self.label1 = tk.Label(
            root,
            text="Kalkulator Diklat",
            font=("Helvetica", 10, "bold")
        )
        self.label1.place(x=170, y=20, width=140, height=30)

        self.label2 = tk.Label(
            root,
            text="Azzaki XI pplg",
            font=("Helvetica", 10, "italic")
        )
        self.label2.place(x=195, y=50, width=90, height=26)

        # Layar kalkulator
        self.text1 = tk.Text(root)
        self.text1.place(x=30, y=80, width=460, height=30)

        # Tombol angka dan operator
        self.button1 = tk.Button(root, text="7", command=self.on_button1)
        self.button1.place(x=40, y=130, width=100, height=40)

        self.button2 = tk.Button(root, text="9", command=self.on_button2)
        self.button2.place(x=270, y=130, width=100, height=40)

        self.button3 = tk.Button(root, text="8", command=self.on_button3)
        self.button3.place(x=156, y=130, width=100, height=40)

        self.button4 = tk.Button(root, text="/", command=self.on_button4)
        self.button4.place(x=380, y=130, width=100, height=40)

        self.button5 = tk.Button(root, text="4", command=self.on_button5)
        self.button5.place(x=40, y=180, width=100, height=40)

        self.button6 = tk.Button(root, text="5", command=self.on_button6)
        self.button6.place(x=156, y=180, width=100, height=40)

        self.button7 = tk.Button(root, text="6", command=self.on_button7)
        self.button7.place(x=270, y=180, width=100, height=40)

        self.button8 = tk.Button(root, text="*", command=self.on_button8)
        self.button8.place(x=380, y=180, width=100, height=40)

        self.button9 = tk.Button(root, text="1", command=self.on_button9)
        self.button9.place(x=40, y=230, width=100, height=40)

        self.button10 = tk.Button(root, text="2", command=self.on_button10)
        self.button10.place(x=156, y=230, width=100, height=40)

        self.button11 = tk.Button(root, text="3", command=self.on_button11)
        self.button11.place(x=270, y=230, width=100, height=40)

        self.button12 = tk.Button(root, text="-", command=self.on_button12)
        self.button12.place(x=380, y=230, width=100, height=40)

        self.button13 = tk.Button(root, text="0", command=self.on_button13)
        self.button13.place(x=40, y=280, width=100, height=40)

        self.button14 = tk.Button(root, text=".", command=self.on_button14)
        self.button14.place(x=156, y=280, width=100, height=40)

        self.button15 = tk.Button(root, text="=", command=self.on_button15)
        self.button15.place(x=270, y=280, width=100, height=40)

        self.button16 = tk.Button(root, text="+", command=self.on_button16)
        self.button16.place(x=380, y=280, width=100, height=40)

        # Keyboard
        self.root.bind("<Return>", self.on_button15)
        self.root.bind("<Escape>", self.clear)
        self.root.bind("<BackSpace>", self.delete_last)

    # Memasukkan angka atau operator
    def input_value(self, value):
        self.text1.insert(tk.INSERT, value)

    # Tombol angka 7
    def on_button1(self):
        self.input_value("7")

    # Tombol angka 9
    def on_button2(self):
        self.input_value("9")

    # Tombol angka 8
    def on_button3(self):
        self.input_value("8")

    # Tombol pembagian
    def on_button4(self):
        self.input_value("/")

    # Tombol angka 4
    def on_button5(self):
        self.input_value("4")

    # Tombol angka 5
    def on_button6(self):
        self.input_value("5")

    # Tombol angka 6
    def on_button7(self):
        self.input_value("6")

    # Tombol perkalian
    def on_button8(self):
        self.input_value("*")

    # Tombol angka 1
    def on_button9(self):
        self.input_value("1")

    # Tombol angka 2
    def on_button10(self):
        self.input_value("2")

    # Tombol angka 3
    def on_button11(self):
        self.input_value("3")

    # Tombol pengurangan
    def on_button12(self):
        self.input_value("-")

    # Tombol angka 0
    def on_button13(self):
        self.input_value("0")

    # Tombol desimal
    def on_button14(self):
        self.input_value(".")

    # Menghitung ekspresi secara aman
    def safe_calculate(self, expression):
        operations = {
            ast.Add: operator.add,
            ast.Sub: operator.sub,
            ast.Mult: operator.mul,
            ast.Div: operator.truediv
        }

        def evaluate(node):
            if isinstance(node, ast.Constant):
                if type(node.value) in (int, float):
                    return node.value
                raise ValueError()

            if isinstance(node, ast.BinOp):
                op = type(node.op)

                if op not in operations:
                    raise ValueError()

                return operations[op](
                    evaluate(node.left),
                    evaluate(node.right)
                )

            if isinstance(node, ast.UnaryOp):
                if isinstance(node.op, ast.USub):
                    return -evaluate(node.operand)

                if isinstance(node.op, ast.UAdd):
                    return evaluate(node.operand)

            raise ValueError()

        tree = ast.parse(expression, mode="eval")
        return evaluate(tree.body)

    # Tombol sama dengan
    def on_button15(self, event=None):
        expression = self.text1.get("1.0", "end-1c").strip()

        if not expression:
            return "break"

        try:
            result = self.safe_calculate(expression)

            if isinstance(result, float) and result.is_integer():
                result = int(result)

            self.text1.delete("1.0", tk.END)
            self.text1.insert("1.0", str(result))

        except ZeroDivisionError:
            messagebox.showerror(
                "Error",
                "Tidak bisa membagi dengan nol!"
            )
            self.clear()

        except (ValueError, SyntaxError, OverflowError):
            messagebox.showerror(
                "Error",
                "Perhitungan tidak valid!"
            )
            self.clear()

        return "break"

    # Tombol penjumlahan
    def on_button16(self):
        self.input_value("+")

    # Menghapus semua input dengan Escape
    def clear(self, event=None):
        self.text1.delete("1.0", tk.END)
        return "break"

    # Menghapus satu karakter dengan Backspace
    def delete_last(self, event=None):
        try:
            index = self.text1.index(tk.INSERT)
            if index != "1.0":
                self.text1.delete("insert-1c", tk.INSERT)
        except tk.TclError:
            pass
        return "break"


if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    root.mainloop()
