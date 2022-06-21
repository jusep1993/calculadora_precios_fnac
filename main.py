import tkinter
from tkinter import ttk


def app():
    def disable_financing():
        if b_is_member.get() == "0":
            financin_yes_rbtn.config(state="disabled")
            financin_no_rbtn.config(state="disabled")
            list_months.config(state="disabled")

        if b_is_member.get() == "1":
            financin_yes_rbtn.config(state="normal")
            financin_no_rbtn.config(state="normal")
            list_months.config(state="normal")

    def cal_membership():
        if b_is_member.get() == "0":
            d_total_price.set(d_entry_product_price.get())

        if b_is_member.get() == "1":
            temp = float(d_entry_product_price.get()) * 0.05
            temp = round(temp, 2)

            result = float(d_entry_product_price.get()) - temp
            result = round(result, 2)
            d_total_price.set(str(result))

    def cal_financing():
        if b_want_financing.get() == "1":
            if list_months.get() == "3 Meses":
                temp = float(d_total_price.get()) / 3
                result = round(temp, 2)
                d_total_monthly_fees.set(str(result))

            elif list_months.get() == "10 Meses":
                temp = float(d_total_price.get()) / 10
                result = round(temp, 2)
                d_total_monthly_fees.set(str(result))

            elif list_months.get() == "20 Meses":
                temp = float(d_total_price.get()) / 20
                result = round(temp, 2)
                d_total_monthly_fees.set(str(result))

        else:
            d_total_monthly_fees.set(" ")

    def calculate():
        cal_membership()
        cal_financing()

    window = tkinter.Tk()

    # ***********************************************************
    # Variables
    d_entry_product_price = tkinter.StringVar()
    d_total_price = tkinter.StringVar()
    d_total_monthly_fees = tkinter.StringVar()
    b_is_member = tkinter.StringVar()
    b_want_financing = tkinter.StringVar()
    list_financing_months = ["3 Meses", "10 Meses", "20 Meses"]
    # ***********************************************************

    window.geometry("500x280")
    window.config(background="#808080")
    window.title("Calculadora de precios FNAC")

    # Header
    header_text = tkinter.Label(window, text="Calculadora de precios de Fnac", font=("Arial", 25), bg="#808080",
                                relief=tkinter.RAISED)
    header_text.pack()

    frame = tkinter.Frame(window)
    frame.pack()

    # Linea y entrada precio producto
    product_price = tkinter.Label(frame, text="Precio del Producto:", font=("Arial", 15))
    product_price.grid(row=0, column=0)

    entry_product_price = tkinter.Entry(frame, textvariable=d_entry_product_price)
    entry_product_price.grid(row=0, column=1)

    euros_symbol_1 = tkinter.Label(frame, text="€", font=("Arial", 15))
    euros_symbol_1.grid(row=0, column=2)

    # Linea miembro cluc socios fnac
    are_you_member = tkinter.Label(frame, text="Tienes carnet de Socio del Fnac?", font=("Arial", 15))
    are_you_member.grid(row=1, column=0, columnspan=2, sticky="w")

    member_yes_rbtn = tkinter.Radiobutton(frame, text="Si", variable=b_is_member, value="1")
    member_no_rbtn = tkinter.Radiobutton(frame, text="No", variable=b_is_member, value="0")
    member_yes_rbtn.grid(row=1, column=1, sticky="")
    member_no_rbtn.grid(row=1, column=2)

    # Linea prgunta financiacion
    want_financing = tkinter.Label(frame, text="¿Quieres financiar el pago?", font=("Arial", 15))
    want_financing.grid(row=2, column=0)
    financin_yes_rbtn = tkinter.Radiobutton(frame, text="Si", variable=b_want_financing, value="1",
                                            command=disable_financing)
    financin_no_rbtn = tkinter.Radiobutton(frame, text="No", variable=b_want_financing, value="0",
                                           command=disable_financing)
    financin_yes_rbtn.grid(row=2, column=1)
    financin_no_rbtn.grid(row=2, column=2)

    # Añadir un if no socio no puedes financiar

    # Linea de a cuantos meses la financiacion
    many_months = tkinter.Label(frame, text="¿A cuantos meses quieres financiar?", font=("Arial", 15))
    many_months.grid(row=3, column=0, columnspan=2, sticky="w")

    list_months = ttk.Combobox(frame, values=list_financing_months, width=8)
    list_months.set("Meses")
    list_months.grid(row=3, column=1, sticky="e")

    # Añadir funcion para recuperar la seleccion

    # Boton Calcular

    calculate_button = tkinter.Button(frame, text="Calcular", font=("Arial", 15), command=calculate)
    calculate_button.grid(row=4, column=0, sticky="e", pady=5)

    separator = ttk.Separator(frame, orient="horizontal")
    separator.grid(row=5, column=0, columnspan=3, ipadx=200)

    # Linea total a pagar

    total_to_be_paid = tkinter.Label(frame, text="Precio total a pagar:", font=("Arial", 15))
    total_to_be_paid.grid(row=6, column=0, sticky="w")

    total_price = tkinter.Label(frame, textvariable=d_total_price, font=("Arial", 15), relief="sunken")
    total_price.grid(row=6, column=1, sticky="w")

    euros_symbol_2 = tkinter.Label(frame, text="€", font=("Arial", 15))
    euros_symbol_2.grid(row=6, column=1, sticky="e")

    # Linea total mensualidades

    monthly_fees = tkinter.Label(frame, text="Mensualidades:", font=("Arial", 15))
    monthly_fees.grid(row=7, column=0, sticky="w")

    total_monthly_fees = tkinter.Label(frame, textvariable=d_total_monthly_fees, font=("Arial", 15), relief="sunken")
    total_monthly_fees.grid(row=7, column=1, sticky="w")

    euros_symbol_3 = tkinter.Label(frame, text="€/mes", font=("Arial", 15))
    euros_symbol_3.grid(row=7, column=1, sticky="e")

    # window.update()
    window.mainloop()

    # TODO 1.No se porque si eliges que no quieres financiar pero escojes mensualidad te hace el calculo igualmente.
    #  Mirarlo 2.Si selecionas que no eres socio, le das a financiar se bloque pero si despues le das que si eres socio
    #  no se desbloquea


if __name__ == "__main__":
    app()
