import requests
from tkinter import *
from tkinter.ttk import Combobox

from tkinter import messagebox



root = Tk()
root.geometry("400x720")
root.resizable(0,0)
root.title("Modern Currency Convertor")
photo = PhotoImage(file='./media/logo.png')
root.iconphoto(False, photo)
# root.bind("<Key-a>",lambda e:root.configure(background="Black"))
# root.bind("<F2>",lambda e:root.configure(background="Green"))
# root.bind("<Delete>",lambda e:root.configure(background="blue"))
Title1 = Label(root, text='',  fg='red', borderwidth=3, font=('arial', 8, 'bold'))


currenices = []


url = "https://v6.exchangerate-api.com/v6/865b83dfc48807c7226ab6c8/latest/USD" # Our api key
try:
    all_data = requests.get(url).json() # Getting data from API
    currenices = all_data['conversion_rates']  # getting currency rates in a dictionary format
    Keys = currenices.keys()
    def convertor(from_cur, to_cur, amount):
        if from_cur != 'USD':
            in_usd = float((1 / currenices[from_cur]) * amount)
            in_to_cur = float(in_usd * currenices[to_cur])
            return round(in_to_cur, 3)
        elif from_cur == 'USD':
            usd_conv = amount * currenices[to_cur]
            return round(usd_conv, 3)
except requests.ConnectionError:
    currenices = {
        "USD": 1,
        "AED": 3.6725,
        "AFN": 78.5074,
        "ALL": 101.0547,
        "AMD": 520.3404,
        "ANG": 1.7900,
        "AOA": 645.7671,
        "ARS": 95.0251,
        "AUD": 1.2918,
        "AWG": 1.7900,
        "AZN": 1.7057,
        "BAM": 1.6009,
        "BBD": 2.0000,
        "BDT": 84.8383,
        "BGN": 1.6018,
        "BHD": 0.3760,
        "BIF": 1968.7577,
        "BMD": 1.0000,
        "BND": 1.3227,
        "BOB": 6.8945,
        "BRL": 5.0380,
        "BSD": 1.0000,
        "BTN": 72.9432,
        "BWP": 10.6038,
        "BYN": 2.5014,
        "BZD": 2.0000,
        "CAD": 1.2076,
        "CDF": 1994.5543,
        "CHF": 0.8956,
        "CLP": 717.8011,
        "CNY": 6.3891,
        "COP": 3594.1884,
        "CRC": 617.3167,
        "CUC": 1.0000,
        "CUP": 25.7500,
        "CVE": 90.2545,
        "CZK": 20.8764,
        "DJF": 177.7210,
        "DKK": 6.1065,
        "DOP": 57.0040,
        "DZD": 133.8728,
        "EGP": 15.6675,
        "ERN": 15.0000,
        "ETB": 43.4874,
        "EUR": 0.8186,
        "FJD": 2.0336,
        "FKP": 0.7065,
        "FOK": 6.1065,
        "GBP": 0.7065,
        "GEL": 3.1354,
        "GGP": 0.7065,
        "GHS": 5.8192,
        "GIP": 0.7065,
        "GMD": 51.8528,
        "GNF": 9828.3935,
        "GTQ": 7.7240,
        "GYD": 209.6050,
        "HKD": 7.7586,
        "HNL": 24.0483,
        "HRK": 6.1672,
        "HTG": 91.1927,
        "HUF": 285.5122,
        "IDR": 14268.3011,
        "ILS": 3.2556,
        "IMP": 0.7065,
        "INR": 72.9435,
        "IQD": 1462.8854,
        "IRR": 41944.6745,
        "ISK": 120.4761,
        "JMD": 149.2040,
        "JOD": 0.7090,
        "JPY": 109.5172,
        "KES": 107.9121,
        "KGS": 84.7354,
        "KHR": 4091.5076,
        "KID": 1.2918,
        "KMF": 402.6873,
        "KRW": 1116.2420,
        "KWD": 0.2996,
        "KYD": 0.8333,
        "KZT": 427.2520,
        "LAK": 9450.0916,
        "LBP": 1507.5000,
        "LKR": 198.2804,
        "LRD": 171.5634,
        "LSL": 13.6427,
        "LYD": 4.4680,
        "MAD": 8.8163,
        "MDL": 17.6731,
        "MGA": 3780.5921,
        "MKD": 50.6755,
        "MMK": 1647.6091,
        "MNT": 2864.0553,
        "MOP": 7.9913,
        "MRU": 36.2610,
        "MUR": 40.8553,
        "MVR": 15.4250,
        "MWK": 797.8860,
        "MXN": 19.6939,
        "MYR": 4.1169,
        "MZN": 62.0019,
        "NAD": 13.6427,
        "NGN": 423.3992,
        "NIO": 35.1823,
        "NOK": 8.2595,
        "NPR": 116.7091,
        "NZD": 1.3917,
        "OMR": 0.3845,
        "PAB": 1.0000,
        "PEN": 3.9199,
        "PGK": 3.5148,
        "PHP": 47.7562,
        "PKR": 155.3645,
        "PLN": 3.6663,
        "PYG": 6678.2145,
        "QAR": 3.6400,
        "RON": 4.0368,
        "RSD": 96.5548,
        "RUB": 72.1660,
        "RWF": 987.2161,
        "SAR": 3.7500,
        "SBD": 7.9300,
        "SCR": 15.7445,
        "SDG": 431.2930,
        "SEK": 8.2585,
        "SGD": 1.3227,
        "SHP": 0.7065,
        "SLL": 10268.8817,
        "SOS": 580.0618,
        "SRD": 14.1536,
        "SSP": 176.0846,
        "STN": 20.0538,
        "SYP": 1599.3698,
        "SZL": 13.6427,
        "THB": 31.1874,
        "TJS": 11.3386,
        "TMT": 3.5010,
        "TND": 2.7235,
        "TOP": 2.2160,
        "TRY": 8.5877,
        "TTD": 6.7514,
        "TVD": 1.2918,
        "TWD": 27.7080,
        "TZS": 2318.4830,
        "UAH": 27.0380,
        "UGX": 3524.9477,
        "UYU": 43.5912,
        "UZS": 10599.5876,
        "VES": 3128393.4863,
        "VND": 22960.8164,
        "VUV": 108.0438,
        "WST": 2.5093,
        "XAF": 536.9164,
        "XCD": 2.7000,
        "XDR": 0.6929,
        "XOF": 536.9164,
        "XPF": 97.6761,
        "YER": 249.5195,
        "ZAR": 13.6432,
        "ZMW": 22.5559
    }
    def convertor(from_cur, to_cur, amount):
        if from_cur != 'USD':
            in_usd = float((1 / currenices[from_cur]) * amount)
            in_to_cur = float(in_usd * currenices[to_cur])
            return round(in_to_cur, 3)
        elif from_cur == 'USD':
            usd_conv = amount * currenices[to_cur]
            return round(usd_conv, 3)

    Title1.configure(text='Please Connect to internet, too get updated values,')





Title = Label(root, text = 'Currency Convertor',  fg = 'black', borderwidth = 3,font = ('arial',25,'bold')).pack(pady=10)
Title1.pack(pady=10)

Lable1 = Label(root, text="Enter the Amount to Convert :- ",  fg="black", font=("arial", 14, "bold")).pack(pady=10)
# Lable1.place(x=15, y=100)

feeder_var = IntVar()
feeder = Entry(root, width=20, textvariable=feeder_var ,fg="black", font=("arial", 11, "bold"),relief="groove", justify='center').pack()
# feeder.place(x=280, y=100)

from_currency_var = StringVar()
to_currency_var = StringVar()
from_currency_var.set('USD')
to_currency_var.set('PKR')


def conversion():
    from_currency = from_currency_var.get()
    to_currency = to_currency_var.get()
    amount = feeder_var.get()
    result = convertor(from_currency, to_currency, amount)
    converted_amount.configure(text= result)


def clear():
    feeder_var.set(0)
    from_currency_var.set('USD')
    to_currency_var.set('PKR')
    converted_amount.configure(text= '')


def Exit():
    root.destroy()



from_currency_label = Label(root, text="From Currency :- ", fg="black", font=("arial", 12, "bold"))

from_currency_dropdown = Combobox(root,textvariable=from_currency_var,values=[*currenices.keys()], width=10,  state="readonly",
                                  justify='center', font=("arial", 10))

to_currency_label = Label(root, text="To Currency :-  ", fg="black", font=("arial", 12, "bold"))

to_currency_dropdown = Combobox(root, width=10, textvariable=to_currency_var, values=[*currenices.keys()], state="readonly",
                                justify='center', font=("arial", 10))

converted_amount = Label(root, text='' , fg="red", bg="white",width=17, font=("arial", 13, "bold"), relief='groove',
                         justify='center')

convert_btn = Button(root, bg="#1abc9c", text="Convert",width=10 , fg="black", font=("arial", 15, "bold"), relief=RAISED,
                     cursor="hand2", command= conversion)

converted_amount_label = Label(root, text="Converted Amount :- ", fg="red", font=("arial", 13, "bold"))

clear_btn = Button(root, bg='#f39c12', text='Clear',width=10 , fg='#2d3436', font=('arial', 15, 'bold'), relief=RAISED,cursor='hand2',
                   command=clear)

exit_btn = Button(root, bg='#ff7675', text='Exit',width=10, fg='#2d3436', font=('arial', 15, 'bold'), relief=RAISED,cursor='hand2',
                   command=Exit)

footer = Label(root, text="Developed and Designed By Zain & Umer ", fg="grey",
               font=("arial", 10, "bold"))






#*currenices.keys()
from_currency_label.place(x=60, y=200)

from_currency_dropdown.place(x=200, y=200)

to_currency_label.place(x=80, y=250)

to_currency_dropdown.place(x=200, y=250)

convert_btn.place(x=148, y=300)

converted_amount_label.place(x=25, y=370)

converted_amount.place(x=202, y=370)

clear_btn.place(x=60, y=450)

exit_btn.place(x=210, y = 450)

footer.place(x=130, y=700)





root.mainloop()


