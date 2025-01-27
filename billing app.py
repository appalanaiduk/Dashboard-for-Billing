from tkinter import*
from tkinter import Tk , messagebox, END
import random
import os

class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.title("Billing software by Naidu")
        self.root.geometry("1550x900+0+0")
        self.search_bill = StringVar()
        bg_color = '#40E0D0'
        title = Label(self.root, text="Naidukk Store Billing Dashboard", font=('times new roman', 30, 'bold'), pady=2, bd=12, bg="#40E0D0", fg="#186990", relief=GROOVE)
        title.pack(fill=X)
        # Ensure the 'bills' directory exists
        if not os.path.exists('bills'):
            os.makedirs('bills')

        self.sanitizer = IntVar()
        self.mask = IntVar()
        self.dettol = IntVar()
        self.handgloves = IntVar()
        self.disprin =IntVar()
        self.thermal_gun = IntVar()
        
        self.rice = IntVar()
        self.food_oil = IntVar()
        self.wheat = IntVar()
        self.pulses = IntVar()
        self.flour = IntVar()
        self.sugar = IntVar()
        
        self.coke = IntVar()
        self.sprite = IntVar()
        self.limca = IntVar()
        self.fanta = IntVar()
        self.maaza = IntVar()
        self.mountain_dew = IntVar()
        
        self.medical_price = StringVar()
        self.grocery_price = StringVar()
        self.cold_drinks_price = StringVar()
        
        self.c_name = StringVar()
        self.c_phone = StringVar()
        self.bill_no = StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.search_bill = StringVar()
        
        self.medical_tax = StringVar()
        self.grocery_tax = StringVar()
        self.cold_drinks_tax = StringVar()
        
        F1 = LabelFrame(self.root, text="Customer Details", font=('times new roman', 15, 'bold'), bd=10, fg='Black', bg="#40E0D0")
        F1.place(x=0, y=80, relwidth=1)
        cname_lbl = Label(F1, text="Customer Name:", bg="#A7D8DE", font=('times new roman', 15, 'bold'))
        cname_lbl.grid(row=0,column=0, padx=20, pady=5)
        cname_txt = Entry(F1, width=15, textvariable=self.c_name, font='arial 15', bd=7, relief=GROOVE)
        cname_txt.grid(row=0,column=1, padx=10, pady=5)
        
        cphn_lbl = Label(F1, text="Customer Phone:", bg="#A7D8DE", font=('times new roman', 15, 'bold'))
        cphn_lbl.grid(row=0,column=2, padx=20, pady=5)
        cphn_txt = Entry(F1, width=15, textvariable=self.c_phone, font='arial 15', bd=7, relief=GROOVE)
        cphn_txt.grid(row=0,column=3, padx=10, pady=5)
        
        c_bill_lbl = Label(F1, text="Bill Number:", bg="#A7D8DE", font=('times new roman', 15, 'bold'))
        c_bill_lbl.grid(row=0, column=4, padx=20, pady=5)

        c_bill_txt = Entry(F1, width=15, textvariable=self.search_bill, font='arial 15', bd=7, relief=GROOVE)
        c_bill_txt.grid(row=0, column=5, padx=10, pady=5)
        
        bill_btn = Button(F1, text="Search", command=self.find_bill, width=10, bd=7, font=('arial', 12, 'bold'),bg="#67b0d3", relief=GROOVE)
        bill_btn.grid(row=0,column=6, padx=10, pady=5)
        
        
        F2 = LabelFrame(self.root, text="Medical Purpose", font=('times new roman', 16, 'bold'), bd=10, fg='Black', bg="#40E0D0")
        F2.place(x=5,y=180,width=325,height=380)
        
        sanitizer_lbl= Label(F2, text="Sanitizer:", font=('times new roman', 16, 'bold'), bg='#A7D8DE', fg="black")
        sanitizer_lbl.grid(row=0,column=0, padx=10, pady=10,sticky='W')
        sanitizer_text = Entry(F2, width=10, textvariable=self.sanitizer, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        sanitizer_text.grid(row=0,column=1, padx=10, pady=10,sticky='W')
                               
        mask_lbl= Label(F2, text="Mask:", font=('times new roman', 16, 'bold'), bg='#A7D8DE', fg="black")
        mask_lbl.grid(row=1,column=0, padx=10, pady=10,sticky='W')
        mask_text = Entry(F2, width=10, textvariable=self.mask, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        mask_text.grid(row=1,column=1, padx=10, pady=10,sticky='W')                               
                               
        dettol_lbl= Label(F2, text="Dettol:", font=('times new roman', 16, 'bold'), bg='#A7D8DE', fg="black")
        dettol_lbl.grid(row=2,column=0, padx=10, pady=10,sticky='W')
        dettol_text = Entry(F2, width=10, textvariable=self.dettol, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        dettol_text.grid(row=2,column=1, padx=10, pady=10,sticky='W')                               
                               
        handgloves_lbl= Label(F2, text="Hand Gloves:", font=('times new roman', 16, 'bold'), bg='#A7D8DE', fg="black")
        handgloves_lbl.grid(row=3,column=0, padx=10, pady=10,sticky='W')
        handgloves_text = Entry(F2, width=10, textvariable=self.handgloves, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        handgloves_text.grid(row=3,column=1, padx=10, pady=10,sticky='W')                               
                                                         
        disprin_lbl= Label(F2, text="Disprin:", font=('times new roman', 16, 'bold'), bg='#A7D8DE', fg="black")
        disprin_lbl.grid(row=4,column=0, padx=10, pady=10,sticky='W')
        disprin_text = Entry(F2, width=10, textvariable=self.disprin, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        disprin_text.grid(row=4,column=1, padx=10, pady=10,sticky='W')                               
                                                  
        thermal_gun_lbl= Label(F2, text="Thermal Gun:  ", font=('times new roman', 16, 'bold'), bg='#A7D8DE', fg="black")
        thermal_gun_lbl.grid(row=5,column=0, padx=10, pady=10,sticky='W')
        thermal_gun_text = Entry(F2, width=10, textvariable=self.thermal_gun, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        thermal_gun_text.grid(row=5,column=1, padx=10, pady=10,sticky='W')                               
                  
                                 
        F3 = LabelFrame(self.root, text="Grocery Items", font=('times new roman', 16, 'bold'), bd=10, fg='Black', bg="#40E0D0")
        F3.place(x=340.5,y=180,width=325,height=380)
        
        rice_lbl= Label(F3, text="Rice:", font=('times new roman', 16, 'bold'), bg='#A7D8DE', fg="black")
        rice_lbl.grid(row=0,column=0, padx=10, pady=10,sticky='W')
        rice_text = Entry(F3, width=10, textvariable=self.rice, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        rice_text.grid(row=0,column=1, padx=10, pady=10,sticky='W')
                               
        food_oil_lbl= Label(F3, text="Food Oil:          ", font=('times new roman', 16, 'bold'), bg='#A7D8DE', fg="black")
        food_oil_lbl.grid(row=1,column=0, padx=10, pady=10,sticky='W')
        food_oil_text = Entry(F3, width=10, textvariable=self.food_oil, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        food_oil_text.grid(row=1,column=1, padx=10, pady=10,sticky='W')                               
                               
        wheat_lbl= Label(F3, text="Wheat:", font=('times new roman', 16, 'bold'), bg='#A7D8DE', fg="black")
        wheat_lbl.grid(row=2,column=0, padx=10, pady=10,sticky='W')
        wheat_text = Entry(F3, width=10, textvariable=self.wheat, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        wheat_text.grid(row=2,column=1, padx=10, pady=10,sticky='W')                               
                               
        pulses_lbl= Label(F3, text="Pulses:", font=('times new roman', 16, 'bold'), bg='#A7D8DE', fg="black")
        pulses_lbl.grid(row=3,column=0, padx=10, pady=10,sticky='W')
        pulses_text = Entry(F3, width=10, textvariable=self.pulses, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        pulses_text.grid(row=3,column=1, padx=10, pady=10,sticky='W')                               
                                                         
        flour_lbl= Label(F3, text="Flour:", font=('times new roman', 16, 'bold'), bg='#A7D8DE', fg="black")
        flour_lbl.grid(row=4,column=0, padx=10, pady=10,sticky='W')
        flour_text = Entry(F3, width=10, textvariable=self.flour, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        flour_text.grid(row=4,column=1, padx=10, pady=10,sticky='W')                               
                                                  
        sugar_lbl= Label(F3, text="Sugar:", font=('times new roman', 16, 'bold'), bg='#A7D8DE', fg="black")
        sugar_lbl.grid(row=5,column=0, padx=10, pady=10,sticky='W')
        sugar_text = Entry(F3, width=10, textvariable=self.sugar, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        sugar_text.grid(row=5,column=1, padx=10, pady=10,sticky='W')                               

        F4 = LabelFrame(self.root, text="Beverage", font=('times new roman', 16, 'bold'), bd=10, fg='Black', bg="#40E0D0")
        F4.place(x=676,y=180,width=325,height=380)
        
        coke_lbl= Label(F4, text="Coke:", font=('times new roman', 16, 'bold'), bg='#A7D8DE', fg="black")
        coke_lbl.grid(row=0,column=0, padx=10, pady=10,sticky='W')
        coke_text = Entry(F4, width=10, textvariable=self.coke, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        coke_text.grid(row=0,column=1, padx=10, pady=10,sticky='W')
                               
        sprite_lbl= Label(F4, text="Sprite:", font=('times new roman', 16, 'bold'), bg='#A7D8DE', fg="black")
        sprite_lbl.grid(row=1,column=0, padx=10, pady=10,sticky='W')
        sprite_text = Entry(F4, width=10, textvariable=self.sprite, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        sprite_text.grid(row=1,column=1, padx=10, pady=10,sticky='W')                               
                               
        limca_lbl= Label(F4, text="Limca:", font=('times new roman', 16, 'bold'), bg='#A7D8DE', fg="black")
        limca_lbl.grid(row=2,column=0, padx=10, pady=10,sticky='W')
        limca_text = Entry(F4, width=10, textvariable=self.limca, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        limca_text.grid(row=2,column=1, padx=10, pady=10,sticky='W')                               
                               
        fanta_lbl= Label(F4, text="Fanta:", font=('times new roman', 16, 'bold'), bg='#A7D8DE', fg="black")
        fanta_lbl.grid(row=3,column=0, padx=10, pady=10,sticky='W')
        fanta_text = Entry(F4, width=10, textvariable=self.fanta, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        fanta_text.grid(row=3,column=1, padx=10, pady=10,sticky='W')                               
                                                         
        maaza_lbl= Label(F4, text="Maaza:", font=('times new roman', 16, 'bold'), bg='#A7D8DE', fg="black")
        maaza_lbl.grid(row=4,column=0, padx=10, pady=10,sticky='W')
        maaza_text = Entry(F4, width=10, textvariable=self.maaza, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        maaza_text.grid(row=4,column=1, padx=10, pady=10,sticky='W')                               
                                                  
        mountain_dew_lbl= Label(F4, text="Mountain Dew:", font=('times new roman', 16, 'bold'), bg='#A7D8DE', fg="black")
        mountain_dew_lbl.grid(row=5,column=0, padx=10, pady=10,sticky='W')
        mountain_dew_text = Entry(F4, width=10, textvariable=self.mountain_dew, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        mountain_dew_text.grid(row=5,column=1, padx=10, pady=10,sticky='W')                               
                                                       
        F5 = Frame(self.root, bd=10, relief=GROOVE)
        F5.place(x=1010,y=180,width=325,height=380) 
        
        bill_title = Label(F5, text="Bill Details Area", font='arial 15 bold', bd=7, relief=GROOVE)
        bill_title.pack(fill=X)
        scroll_y = Scrollbar(F5, orient=VERTICAL)
        self.txtarea = Text(F5, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)
        
        F6 = LabelFrame(self.root, text="Bill Details Area", font=('times new roman', 14, 'bold'), bd=10, fg='Black', bg="#40E0D0")
        F6.place(x=0,y=560,relwidth=1,height=140)
        
        m1_lbl = Label(F6, text="Total Medical Price", font=('times new roman', 14, 'bold'), fg='black', bg="#67b0d3")
        m1_lbl.grid(row=0,column=0,padx=20,pady=1,sticky='W')
        m1_txt =Entry(F6,width=18, textvariable=self.medical_price,font='arial 10 bold', bd=7, relief=GROOVE)
        m1_txt.grid(row=0,column=1,padx=18,pady=1)
                               
        m2_lbl = Label(F6, text="Total Grocery Price", font=('times new roman', 14, 'bold'), fg='black', bg="#67b0d3")
        m2_lbl.grid(row=1,column=0,padx=20,pady=1,sticky='W')
        m2_txt =Entry(F6,width=18, textvariable=self.grocery_price,font='arial 10 bold', bd=7, relief=GROOVE)
        m2_txt.grid(row=1,column=1,padx=18,pady=1)                               
                               
        m3_lbl = Label(F6, text="Total Cold Drinks Price", font=('times new roman', 14, 'bold'), fg='black', bg="#67b0d3")
        m3_lbl.grid(row=2,column=0,padx=20,pady=1,sticky='W')
        m3_txt =Entry(F6,width=18, textvariable=self.cold_drinks_price,font='arial 10 bold', bd=7, relief=GROOVE)
        m3_txt.grid(row=2,column=1,padx=18,pady=1)
        
        m4_lbl = Label(F6, text="Medical Tax", font=('times new roman', 14, 'bold'), fg='black', bg="#67b0d3")
        m4_lbl.grid(row=0,column=2,padx=20,pady=1,sticky='W')
        m4_txt =Entry(F6,width=18, textvariable=self.medical_tax,font='arial 10 bold', bd=7, relief=GROOVE)
        m4_txt.grid(row=0,column=3,padx=18,pady=1)        
             
        m5_lbl = Label(F6, text="Grocery Tax", font=('times new roman', 14, 'bold'), fg='black', bg="#67b0d3")
        m5_lbl.grid(row=1,column=2,padx=20,pady=1,sticky='W')
        m5_txt =Entry(F6,width=18, textvariable=self.grocery_tax,font='arial 10 bold', bd=7, relief=GROOVE)
        m5_txt.grid(row=1,column=3,padx=18,pady=1)        
              
        m6_lbl = Label(F6, text="Cold Drinks Tax", font=('times new roman', 14, 'bold'), fg='black', bg="#67b0d3")
        m6_lbl.grid(row=2,column=2,padx=20,pady=1,sticky='W')
        m6_txt =Entry(F6,width=18, textvariable=self.cold_drinks_tax,font='arial 10 bold', bd=7, relief=GROOVE)
        m6_txt.grid(row=2,column=3,padx=18,pady=1)
        
        
        btn_f = Frame(F6, bd=7, relief=GROOVE)
        btn_f.place(x=760, width=580, height=105)
        
        total_btn= Button(btn_f, command=self.total, text="Total", fg = "black", bg="#67b0d3", bd=2, pady=15, width=12, font='arial 13 bold')
        total_btn.grid(row=0,column=0,padx=5,pady=5)
        
        generateBill_btn= Button(btn_f, command=self.bill_area, text="Generate Bill", fg = "black", bg="#67b0d3", bd=2, pady=15, width=12, font='arial 13 bold')
        generateBill_btn.grid(row=0,column=1,padx=5,pady=5)        
        
        
        clear_btn= Button(btn_f, command=self.clear_data, text="Clear", fg = "black", bg="#67b0d3", bd=2, pady=15, width=12, font='arial 13 bold')
        clear_btn.grid(row=0,column=2,padx=5,pady=5)        
        
        
        exit_btn= Button(btn_f, command=self.exit_app, text="Exit", fg = "black", bg="#67b0d3", bd=2, pady=15, width=12, font='arial 13 bold')
        exit_btn.grid(row=0,column=3,padx=5,pady=5)        
        
    def total(self):
        try:
            # Medical Products
            self.m_s_p = float(self.sanitizer.get() or 0) * 20
            self.m_m_p = float(self.mask.get() or 0) * 5
            self.m_de_p = float(self.dettol.get() or 0) * 30
            self.m_h_g_p = float(self.handgloves.get() or 0) * 12
            self.m_d_p = float(self.disprin.get() or 0) * 2
            self.m_t_g_p = float(self.thermal_gun.get() or 0) * 150
            
            self.total_medical_price = self.m_s_p + self.m_m_p + self.m_de_p + self.m_h_g_p + self.m_d_p + self.m_t_g_p
            self.medical_price.set(f"Rs. {self.total_medical_price}")
            
            self.m_tax = round(self.total_medical_price * 0.05, 2)
            self.medical_tax.set(f"Rs. {self.m_tax}")

            # Grocery Products
            self.g_r_p = float(self.rice.get() or 0) * 100
            self.g_f_o_p = float(self.food_oil.get() or 0) * 150
            self.g_w_p = float(self.wheat.get() or 0) * 25
            self.g_p_p = float(self.pulses.get() or 0) * 45
            self.g_f_p = float(self.flour.get() or 0) * 100
            self.g_s_p = float(self.sugar.get() or 0) * 60
            
            self.total_grocery_price = self.g_r_p + self.g_f_o_p + self.g_w_p + self.g_p_p + self.g_f_p + self.g_s_p
            self.grocery_price.set(f"Rs. {self.total_grocery_price}")
            
            self.g_tax = round(self.total_grocery_price * 0.05, 2)
            self.grocery_tax.set(f"Rs. {self.g_tax}")

            # Cold Drinks
            self.c_d_c_p = float(self.coke.get() or 0) * 40
            self.c_d_s_p = float(self.sprite.get() or 0) * 40
            self.c_d_l_p = float(self.limca.get() or 0) * 40
            self.c_d_f_p = float(self.fanta.get() or 0) * 40
            self.c_d_m_p = float(self.maaza.get() or 0) * 40
            self.c_d_m_d_p = float(self.mountain_dew.get() or 0) * 40
            
            self.total_cold_drinks_price = self.c_d_c_p + self.c_d_s_p + self.c_d_l_p + self.c_d_f_p + self.c_d_m_p + self.c_d_m_d_p
            self.cold_drinks_price.set(f"Rs. {self.total_cold_drinks_price}")
            
            self.c_d_tax = round(self.total_cold_drinks_price * 0.1, 2)
            self.cold_drinks_tax.set(f"Rs. {self.c_d_tax}")

            # Total Bill
            self.total_bill = self.total_medical_price + self.total_grocery_price + self.total_cold_drinks_price + self.m_tax + self.g_tax + self.c_d_tax
            # You can set total_bill to an appropriate widget if needed
            # Example: self.total.set(f"Rs. {self.total_bill}")
            
        except Exception as e:
            print(f"Error in calculation: {e}")

    def welcome_bill(self):
        self.txtarea.delete('1.0', END)
        self.txtarea.insert(END, "Welcome to Naidu Retail Store")
        self.txtarea.insert(END, f"\nBill Number: {self.bill_no.get()}")
        self.txtarea.insert(END, f"\nCustomer Name: {self.c_name.get()}")
        self.txtarea.insert(END, f"\nPhone Number: {self.c_phone.get()}")
        self.txtarea.insert(END, f"\n=================================")

        # Fixed indentation here
        self.txtarea.insert(END, f"\nProducts\t\tQTY\tPrice")

        
    def bill_area(self):
    # Ensure customer details are filled
        if not self.c_name.get().strip() or not self.c_phone.get().strip():
            messagebox.showerror("ERROR", "Customer Details are required")
    # Ensure that products are purchased
        elif self.medical_price.get() == "Rs. 0.0" and self.grocery_price.get() == "Rs. 0.0" and self.cold_drinks_price.get() == "Rs. 0.0":
            messagebox.showerror("ERROR", "No Products Purchased")
        else:
            self.welcome_bill()

    # Insert purchased medical products into the bill
        if self.sanitizer.get() != 0:
            self.txtarea.insert(END, f"\nSanitizer\t\t{self.sanitizer.get()}\t{self.m_s_p}")

        if self.mask.get() != 0:
            self.txtarea.insert(END, f"\nMask\t\t{self.mask.get()}\t{self.m_m_p}")        

        if self.dettol.get() != 0:
            self.txtarea.insert(END, f"\nDettol\t\t{self.dettol.get()}\t{self.m_de_p}")        

        if self.handgloves.get() != 0:
            self.txtarea.insert(END, f"\nHand Gloves\t\t{self.handgloves.get()}\t{self.m_h_g_p}")        

        if self.disprin.get() != 0:
            self.txtarea.insert(END, f"\nDisprin\t\t{self.disprin.get()}\t{self.m_d_p}")        

        if self.thermal_gun.get() != 0:
            self.txtarea.insert(END, f"\nThermal Gun\t\t{self.thermal_gun.get()}\t{self.m_t_g_p}") 

        # Insert purchased grocery products into the bill
        if self.rice.get() != 0:
            self.txtarea.insert(END, f"\nRice\t\t{self.rice.get()}\t{self.g_r_p}")

        if self.food_oil.get() != 0:
            self.txtarea.insert(END, f"\nFood Oil\t\t{self.food_oil.get()}\t{self.g_f_o_p}")        

        if self.wheat.get() != 0:
            self.txtarea.insert(END, f"\nWheat\t\t{self.wheat.get()}\t{self.g_w_p}")        

        if self.pulses.get() != 0:
            self.txtarea.insert(END, f"\nPulses\t\t{self.pulses.get()}\t{self.g_p_p}")        

        if self.flour.get() != 0:
            self.txtarea.insert(END, f"\nFlour\t\t{self.flour.get()}\t{self.g_f_p}")        

        if self.sugar.get() != 0:
            self.txtarea.insert(END, f"\nSugar\t\t{self.sugar.get()}\t{self.g_s_p}")             

        # Insert purchased cold drinks into the bill
        if self.coke.get() != 0:
            self.txtarea.insert(END, f"\nCoke\t\t{self.coke.get()}\t{self.c_d_c_p}")

        if self.sprite.get() != 0:
            self.txtarea.insert(END, f"\nSprite\t\t{self.sprite.get()}\t{self.c_d_s_p}")        

        if self.limca.get() != 0:
            self.txtarea.insert(END, f"\nLimca\t\t{self.limca.get()}\t{self.c_d_l_p}")        

        if self.fanta.get() != 0:
            self.txtarea.insert(END, f"\nFanta\t\t{self.fanta.get()}\t{self.c_d_f_p}")        

        if self.maaza.get() != 0:
            self.txtarea.insert(END, f"\nMaaza\t\t{self.maaza.get()}\t{self.c_d_m_p}")        

        if self.mountain_dew.get() != 0:
            self.txtarea.insert(END, f"\nMountain Dew\t\t{self.mountain_dew.get()}\t{self.c_d_m_d_p}")             

        # Add line separator
        self.txtarea.insert(END, f"\n=================================")

        # Add taxes to the bill
        if self.medical_tax.get() != 0:
            self.txtarea.insert(END, f"\nMedical Tax\t\t{self.medical_tax.get()}")                               

        if self.grocery_tax.get() != 0:
            self.txtarea.insert(END, f"\nGrocery Tax\t\t{self.grocery_tax.get()}")            

        if self.cold_drinks_tax.get() != 0:
            self.txtarea.insert(END, f"\nCold Drinks Tax\t\t{self.cold_drinks_tax.get()}")                              

        # Display total bill
        self.txtarea.insert(END, f"\nTotal Bill:\t\t\tRs. {self.total_bill}")            
        self.txtarea.insert(END, f"\n=================================")

        # Save the bill after everything has been printed
        self.save_bill()
                            
    def save_bill(self):
        op = messagebox.askyesno("Save Bill", "Do You want to save the bill?")
        if op > 0:
            try:
                self.bill_data = self.txtarea.get('1.0', END)
                file_path = f"bills/{str(self.bill_no.get())}.txt"
                with open(file_path, "w") as f1:
                    f1.write(self.bill_data)
                messagebox.showinfo("Saved", f"Bill no.{self.bill_no.get()} Saved Successfully")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save the bill: {e}")
        else:
            return 


    def find_bill(self):
        bills_directory = "bills"
        # Ensure the 'bills' directory exists
        if not os.path.exists(bills_directory):
            messagebox.showerror("Error", f"'{bills_directory}' directory not found.")
            return

        # Get the bill number from the input field
        bill_no = self.search_bill.get().strip()
        if not bill_no:
            messagebox.showerror("Error", "Please enter a valid bill number.")
            return

        # Construct the file path
        file_path = os.path.join(bills_directory, f"{bill_no}.txt")
        print(f"Looking for file: {file_path}")  # Debug statement

        # Check if the file exists
        if os.path.exists(file_path):
            try:
                # Read the file content
                with open(file_path, "r") as file:
                    content = file.read()
                    print(f"File content:\n{content}")  # Debug statement

                # Display the content in the Text widget
                self.txtarea.delete("1.0", END)  # Clear existing content
                self.txtarea.insert(END, content)  # Insert the bill content
                messagebox.showinfo("Success", f"Bill {bill_no} found and displayed.")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to read the bill: {e}")
                print(f"Exception: {e}")
        else:
            messagebox.showerror("Error", f"Bill {bill_no} not found.")

    def clear_data(self):
        # Ask the user if they really want to clear the data
        op = messagebox.askyesno("Clear", "Do You really want to clear?")
        
        if op:  # Check if op is True (Yes clicked)
            # Reset all product quantities to 0
            self.sanitizer.set(0)
            self.mask.set(0)
            self.dettol.set(0)
            self.handgloves.set(0)
            self.disprin.set(0)
            self.thermal_gun.set(0)
                            
            self.rice.set(0)
            self.food_oil.set(0)
            self.wheat.set(0)
            self.pulses.set(0)
            self.flour.set(0)
            self.sugar.set(0)
                            
            self.coke.set(0)
            self.sprite.set(0)
            self.limca.set(0)
            self.fanta.set(0)
            self.maaza.set(0)
            self.mountain_dew.set(0)
                                    
            # Clear price fields
            self.medical_price.set("")
            self.grocery_price.set("")
            self.cold_drinks_price.set("")

            # Clear tax fields
            self.medical_tax.set("")
            self.grocery_tax.set("")
            self.cold_drinks_tax.set("")

            # Clear customer details
            self.c_name.set("")
            self.c_phone.set("")
            
            # Reset bill number and generate a new one
            self.bill_no.set("")
            x = random.randint(1000, 9999)  # Generate a random bill number
            self.bill_no.set(str(x))  # Set the new bill number
            
            # Clear the bill details area
            self.txtarea.delete('1.0', END)
            # self.welcome_bill()  # Reset to the welcome message

            # Reset total bill amount
            self.total_bill = 0
        
            # Clear any error messages or status updates
            self.root.update()
        
            messagebox.showinfo("Clear", "All data has been cleared successfully!")
                                        
    def exit_app(self):
            op = messagebox.askyesno("Exit", "Do You really want to exit?")
            if op:  # Check if op is True (Yes clicked)
                self.root.destroy()  # Close the application window

if __name__ == "__main__":
    root = Tk()  # Initialize the Tkinter window
    obj = Bill_App(root)  # Create an instance of the Bill_App class
    root.mainloop()  # Start the Tkinter event loop
