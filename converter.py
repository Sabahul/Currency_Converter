import tkinter as tk
from tkinter import messagebox
from forex_python.converter import CurrencyRates

def real_time_currency_conversion():
    try:
        c = CurrencyRates()
        from_currency = variable1.get().split()[0]  # Extracting currency code without symbol
        to_currency = variable2.get().split()[0]

        if not amount_entry.get():
            raise ValueError("Amount Not Entered.\nPlease enter a valid amount.")
        elif from_currency == "currency" or to_currency == "currency":
            raise ValueError("Currency Not Selected.\nPlease select FROM and TO Currency from the menu.")

        amount = float(amount_entry.get())
        new_amt = c.convert(from_currency, to_currency, amount)
        new_amount = round(new_amt, 4)
        converted_amount_entry.delete(0, tk.END)
        converted_amount_entry.insert(0, f"{new_amount} {to_currency}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def clear_all():
    amount_entry.delete(0, tk.END)
    converted_amount_entry.delete(0, tk.END)

def create_widgets():
    currency_label = tk.Label(root, font=('lato black', 19, 'bold'), text='                               Currency Converter', bg='#363636', fg='white')
    currency_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky=tk.W)

    label1 = tk.Label(root, font=('lato black', 15, 'bold'), text="Amount:", bg="#363636", fg="white")
    label1.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)

    label2 = tk.Label(root, font=('lato black', 15, 'bold'), text="From Currency:", bg="#363636", fg="white")
    label2.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)

    label3 = tk.Label(root, font=('lato black', 15, 'bold'), text="To Currency:", bg="#363636", fg="white")
    label3.grid(row=4, column=0, padx=10, pady=5, sticky=tk.W)

    label4 = tk.Label(root, font=('lato black', 15, 'bold'), text="Converted Amount:", bg="#363636", fg="white")
    label4.grid(row=6, column=0, padx=10, pady=5, sticky=tk.W)

    from_currency_option = tk.OptionMenu(root, variable1, *CurrencyCode_list)
    to_currency_option = tk.OptionMenu(root, variable2, *CurrencyCode_list)

    from_currency_option.grid(row=3, column=1, padx=10, pady=5, sticky=tk.E)
    to_currency_option.grid(row=4, column=1, padx=10, pady=5, sticky=tk.E)

    amount_entry.grid(row=2, column=1, padx=10, pady=5, sticky=tk.E)
    converted_amount_entry.grid(row=6, column=1, padx=10, pady=5, sticky=tk.E)

    convert_button = tk.Button(root, font=('arial', 15, 'bold'), text="Convert", bg="#2ca02c", fg="white", command=real_time_currency_conversion)
    convert_button.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

    clear_button = tk.Button(root, font=('arial', 15, 'bold'), text="Clear All", bg="#d62728", fg="white", command=clear_all)
    clear_button.grid(row=7, column=0, columnspan=2, padx=10, pady=5)

root = tk.Tk()
root.title("GUI: Currency Conversion")
root.configure(background='#363636')
root.geometry("700x400")

variable1 = tk.StringVar(root)
variable2 = tk.StringVar(root)

variable1.set("currency")
variable2.set("currency")

CurrencyCode_list = ["INR ₹", "USD $", "EUR €", "JPY ¥", "GBP £", "AUD A$", "CAD C$", "CHF Fr", "CNY ¥", "SEK kr", "NZD NZ$", "RUB ₽", "BRL R$", "KRW ₩", "SGD S$", "ZAR R", "TRY ₺", "AED د.إ", "MXN $"]

amount_entry = tk.Entry(root)
converted_amount_entry = tk.Entry(root)

create_widgets()

root.mainloop()
