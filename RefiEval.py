from tkinter import *
import  numpy_financial as np

class RefiEval:
    def __init__(self):
        window=Tk()                     #declaring window as a Tk object
        window.title("Refinance Calculator")

        #Inputs
        #sticky to align to the window sticking the elements
        Label(window,text="Loan Amount", font="Helvetica 16").grid(row=1, column=1, sticky=W)
        Label(window, text="Interest Rate", font="Helvetica 16").grid(row=2, column=1, sticky=W)
        Label(window, text="Term(in years)", font="Helvetica 16").grid(row=3, column=1, sticky=W)
        Label(window, text=None).grid(row=4, column=1, sticky=W)

        #Outputs
        Label(window, text="Payment", font="Helvetica 16").grid(row=5, column=1, sticky=W)
        Label(window, text="Total Payments", font="Helvetica 16").grid(row=6, column=1, sticky=W)

        #Variables to store inputs
        self.present_value= StringVar()     #to store how much you are borrowing
        self.interest_rate= StringVar()
        self.term = StringVar()

        #Variables to store the outputs
        self.payment=StringVar()
        self.total=StringVar()

        #Adding widgets

        Entry(window, textvariable=self.present_value, justify=RIGHT).grid(row=1, column=2, padx=(0,5))
        Entry(window, textvariable=self.interest_rate, justify=RIGHT).grid(row=2, column=2, padx=(0,5))
        Entry(window, textvariable=self.term, justify=RIGHT).grid(row=3, column=2, padx=(0,5))

        Label(window,textvariable=self.payment, font="Helvetica 12 bold",
              justify=RIGHT).grid(row=5, column=2,sticky=E)
        Label(window, textvariable=self.total, font="Helvetica 12 bold",
              justify=RIGHT).grid(row=6, column=2, sticky=E)

        Button(window, text="Calculate Payment", command=self.calcPayment, font="Helvetica 14").grid(
            row=7, column=2, padx=(100,5), pady=5
        )

        window.mainloop()  # running the main loop

    def calcPayment(self):
        presentvalue=float(self.present_value.get())         #convert String to Float
        rate=float(self.interest_rate.get())
        term = int(self.term.get())

        # Division with months and 100 as rate will be in percent
        payment= np.pmt(rate /(12*100),term*12, -presentvalue,0)
        #presentvalue as flag set to negative, 0 for telling that mortgage has been cleared & future value will be 0

        total= payment*12*term

        self.payment.set("$" + format(payment, "5,.2f"))
        self.total.set("$" + format(total, "8,.2f"))













RefiEval()                          #calling the class




