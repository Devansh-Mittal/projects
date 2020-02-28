from tkinter import *
import math,random,os
from tkinter import messagebox
class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1650x700+0+0")
        self.root.title("Billing Software")
        title=Label(self.root,text="Billing Software",bd=12,relief=GROOVE,bg="#074463",fg="white",font=("times new roman",30,"bold"),pady=2).pack(fill=X)
        ####HARDWARES####
        self.harddisk=IntVar()
        self.smartwatch=IntVar()
        self.keybord=IntVar()
        self.headphone=IntVar()
        #####softwares#####
        self.msoffice=IntVar()
        self.coraldraw=IntVar()
        self.photoshop=IntVar()
        self.scilab=IntVar()
        ####processor###
        self.i3=IntVar()
        self.i7=IntVar()
        self.i5=IntVar()
        self.i9=IntVar()
        ########TAX$#####
        self.hprice=StringVar()
        self.sprice=StringVar()
        self.pprice=StringVar()

        self.htax=StringVar()
        self.stax=StringVar()
        self.ptax=StringVar()
        self.total_price=IntVar()
    
        ###Customer#####
        self.c_name=StringVar()
        self.c_phone=StringVar()
        
        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill=StringVar()
        
        F1=LabelFrame(self.root,bd=10,relief=GROOVE,text="Customer Details",font=("times new roman",15,"bold"),fg="gold",bg="#074463")
        F1.place(x=0,y=80,relwidth=1)

        cname_lbl=Label(F1,text="Customer Name",bg="#074463",fg="white",font=("times new roman",15,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_txt=Entry(F1,width=15,textvariable=self.c_name,font="arial 15 ",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)

        cphone_lbl=Label(F1,text="Phone Number",bg="#074463",fg="white",font=("times new roman",15,"bold")).grid(row=0,column=2,padx=20,pady=5)
        cphone_txt=Entry(F1,width=15,textvariable=self.c_phone,font="arial 15 ",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)

        cbill_lbl=Label(F1,text="Bill Number",bg="#074463",fg="white",font=("times new roman",15,"bold")).grid(row=0,column=4,padx=20,pady=5)
        cbill_txt=Entry(F1,width=15,textvariable=self.bill_no,font="arial 15 ",bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)

        bill_btn=Button(F1,text="Search",command=self.find_bill,width=10,bd=7,font="arial 12 bold").grid(row=0,column=6,pady=10,padx=10)
        ######################HARDWARES##########################

        F2=LabelFrame(self.root,bd=10,relief=GROOVE,text="Hardware Products",font=("times new roman",15,"bold"),fg="gold",bg="#074463")
        F2.place(x=5,y=185,width=325,height=380)

        Memory_lbl=Label(F2,text="External HD",font=("arial",12,"bold"),bg="#074463",fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        memory_txt=Entry(F2,width=10,textvariable=self.harddisk,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        headphone_lbl=Label(F2,text="Head Phone",font=("arial",12,"bold"),bg="#074463",fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        headphone_txt=Entry(F2,width=10,textvariable=self.headphone,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        smartwatch_lbl=Label(F2,text="Smart Watch",font=("arial",12,"bold"),bg="#074463",fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        smartwatch_txt=Entry(F2,width=10,textvariable=self.smartwatch,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        keybord_lbl=Label(F2,text="BTH keybord",font=("arial",12,"bold"),bg="#074463",fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        keybord_txt=Entry(F2,width=10,textvariable=self.keybord,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)
        ################SOFTWARES#########################
        F3=LabelFrame(self.root,bd=10,relief=GROOVE,text="Softwares",font=("times new roman",15,"bold"),fg="gold",bg="#074463")
        F3.place(x=340,y=185,width=325,height=380)

        msoffice_lbl=Label(F3,text="MS OFFICE",font=("arial",12,"bold"),bg="#074463",fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        msoffice=Entry(F3,width=10,textvariable=self.msoffice,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        Photoshop_lbl=Label(F3,text="Photoshop",font=("arial",12,"bold"),bg="#074463",fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        Photoshop_txt=Entry(F3,width=10,textvariable=self.photoshop,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        coroldraw_lbl=Label(F3,text="Coral Draw",font=("arial",12,"bold"),bg="#074463",fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        coroldraw_txt=Entry(F3,width=10,textvariable=self.coraldraw,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        scilab_lbl=Label(F3,text="SCI lab subs.",font=("arial",12,"bold"),bg="#074463",fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        scilab_txt=Entry(F3,width=10,textvariable=self.scilab,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)
        ###################PRocessor############################
        F4=LabelFrame(self.root,bd=10,relief=GROOVE,text="Processor",font=("times new roman",15,"bold"),fg="gold",bg="#074463")
        F4.place(x=675,y=185,width=325,height=380)

        i3_lbl=Label(F4,text="INTEL CORE 3",font=("arial",12,"bold"),bg="#074463",fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        i3_txt=Entry(F4,width=10,textvariable=self.i3,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        i9_lbl=Label(F4,text="INTEL CORE 9",font=("arial",12,"bold"),bg="#074463",fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        i9_txt=Entry(F4,width=10,textvariable=self.i9,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        i5_lbl=Label(F4,text="INTEL CORE 5",font=("arial",12,"bold"),bg="#074463",fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        i5_txt=Entry(F4,width=10,textvariable=self.i5,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        i6_lbl=Label(F4,text="INTEL CORE 7",font=("arial",12,"bold"),bg="#074463",fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,)
        i6_txt=Entry(F4,width=10,textvariable=self.i7,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10,sticky="w")
        ####################BILL AREA###############################
        F5=Frame(self.root,bd=10,relief=GROOVE)
        F5.place(x=1010,y=185,width=500,height=380)
        bill_title=Label(F5,text="BILL AREA",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH)
        
        ############BILL FRAME###############

        F6=LabelFrame(self.root,bd=10,relief=GROOVE,text="BILL MENU",font=("times new roman",15,"bold"),fg="gold",bg="#074463")
        F6.place(x=0,y=560,relwidth=1,height=240)

        h1_lbl=Label(F6,text="Total Hardware price",font=("times new roman",14,"bold"),bg="#074463",fg="yellow").grid(row=0,column=0,padx=20,pady=1,sticky="w")
        h1_txt=Entry(F6,width=18,textvariable=self.hprice,font="arial 18 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=5)
        
        h2_lbl=Label(F6,text="Total Software price",font=("times new roman",14,"bold"),bg="#074463",fg="yellow").grid(row=1,column=0,padx=20,pady=1,sticky="w")
        h2_txt=Entry(F6,width=18,textvariable=self.sprice,font="arial 18 bold",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=5)

        h3_lbl=Label(F6,text="Total Processor price",font=("times new roman",14,"bold"),bg="#074463",fg="yellow").grid(row=2,column=0,padx=20,pady=1,sticky="w")
        h3_txt=Entry(F6,width=18,textvariable=self.pprice,font="arial 18 bold",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=5)

        h4_lbl=Label(F6,text="Hardware Tax",font=("times new roman",14,"bold"),bg="#074463",fg="yellow").grid(row=0,column=2,padx=20,pady=1,sticky="w")
        h4_txt=Entry(F6,width=18,textvariable=self.htax,font="arial 18 bold",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=5)
        
        h5_lbl=Label(F6,text="Software Tax",font=("times new roman",14,"bold"),bg="#074463",fg="yellow").grid(row=1,column=2,padx=20,pady=1,sticky="w")
        h5_txt=Entry(F6,width=18,textvariable=self.stax,font="arial 18 bold",bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=5)
        
        h6_lbl=Label(F6,text="Processor Tax",font=("times new roman",14,"bold"),bg="#074463",fg="yellow").grid(row=2,column=2,padx=20,pady=1,sticky="w")
        h6_txt=Entry(F6,width=18,textvariable=self.ptax,font="arial 18 bold",bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=5)
        
        btn_F=Frame(F6,bd=7,relief=GROOVE)
        btn_F.place(x=929,width=580,height=185)
        totoal_btn=Button(btn_F,text="Total",command=self.total,bd=5,font="arial 15 bold",bg="cadetblue",fg="white",pady=15,width=9).grid(row=0,column=0,pady=5,padx=5)
        GB_btn=Button(btn_F,text="Generate Bill",command=self.bill_area,bd=5,font="arial 15 bold",bg="cadetblue",fg="white",pady=15,width=11).grid(row=0,column=1,pady=5,padx=5)
        clear_btn=Button(btn_F,text="Clear",bd=5,command=self.clear_data,font="arial 15 bold",bg="cadetblue",fg="white",pady=15,width=9).grid(row=0,column=2,pady=5,padx=5)
        exit_btn=Button(btn_F,text="Exit",command=self.exit_app,bd=5,font="arial 15 bold",bg="cadetblue",fg="white",pady=15,width=9).grid(row=0,column=3,pady=5,padx=5)
        self.welcome_bill()
    def total(self):
    
        self.total_hprice=float((self.harddisk.get()*4000)+(self.keybord.get()*500)+(self.smartwatch.get()*5000)+(self.headphone.get()*400))
        self.hprice.set("Rs. "+str(self.total_hprice))


        self.total_sprice=float((self.msoffice.get()*2000)+(self.photoshop.get()*1000)+(self.coraldraw.get()*700)+(self.scilab.get()*4000))
        self.sprice.set("Rs. "+str(self.total_sprice))

        self.total_pprice=float((self.i3.get()*4000)+(self.i9.get()*5000)+(self.i5.get()*5000)+(self.i7.get()*5000))
        self.pprice.set("Rs. "+str(self.total_pprice))

        self.htax.set("Rs. "+str(self.total_hprice*0.05))
        self.stax.set("Rs. "+str(self.total_sprice*0.07))
        self.ptax.set("Rs. "+str(self.total_pprice*0.09))
        self.h_hd_p=self.harddisk.get()*4000
        self.h_kb_p=self.keybord.get()*500
        self.h_sw_p=self.smartwatch.get()*5000
        self.h_hp_p=self.headphone.get()*400
        self.s_mso_p=self.msoffice.get()*2000
        self.s_p_p=self.photoshop.get()*1000
        self.s_cd_p=self.coraldraw.get()*700
        self.s_sl_p=self.scilab.get()*4000
        self.p_i3_p=self.i3.get()*4000
        self.p_i9_p=self.i9.get()*5000
        self.p_i5_p=self.i5.get()*5000
        self.p_i7_p=self.i7.get()*5000
        self.total_price.set=("Rs. "+str(self.total_hprice + self.total_sprice + self.total_pprice + self.htax + self.stax + self.ptax))
    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\t\tWelcome at Devansh's store\n")
        self.txtarea.insert(END,f"\nBILL NUMBER     : {self.bill_no.get()}")
        self.txtarea.insert(END,f"\nCustomer Name   : {self.c_name.get()}")
        self.txtarea.insert(END,f"\nCustomer Number : {self.c_phone.get()}")
        self.txtarea.insert(END,f"\n*********************************************************")
        self.txtarea.insert(END,f"\n Products\t\t\tQuantity\t\tPrice")
        self.txtarea.insert(END,f"\n*********************************************************")        
    def bill_area(self):
        if self.c_name.get()=="" or self.c_phone.get()=="":
            messagebox.showerror("Error","Customer details are must")
        elif self.hprice.get()=="Rs. 0.0" and self.sprice.get()=="Rs. 0.0" and self.pprice.get()=="Rs. 0.0":
            messagebox.showerror("ERROR","NO PRODUCT SELECTED")
        else:
            
            self.welcome_bill()
            if self.harddisk.get()!=0:
                self.txtarea.insert(END,f"\n Hard Disk \t\t\t{self.harddisk.get()}\t\t{self.h_hd_p}")
            if self.keybord.get()!=0:
                self.txtarea.insert(END,f"\n keybord \t\t\t{self.keybord.get()}\t\t{self.h_kb_p}")
            if self.smartwatch.get()!=0:
                self.txtarea.insert(END,f"\n Smart Watch \t\t\t{self.smartwatch.get()}\t\t{self.h_sw_p}")
            if self.headphone.get()!=0:
                self.txtarea.insert(END,f"\n Head Phone \t\t\t{self.headphone.get()}\t\t{self.h_hp_p}")
            if self.msoffice.get()!=0:
                self.txtarea.insert(END,f"\n MS Office \t\t\t{self.msoffice.get()}\t\t{self.s_mso_p}")
            if self.photoshop.get()!=0:
                self.txtarea.insert(END,f"\n Photoshop \t\t\t{self.photoshop.get()}\t\t{self.s_p_p}")
            if self.coraldraw.get()!=0:
                self.txtarea.insert(END,f"\n coraldraw \t\t\t{self.coraldraw.get()}\t\t{self.s_cd_p}")
            if self.scilab.get()!=0:
                self.txtarea.insert(END,f"\n scilab \t\t\t{self.scilab.get()}\t\t{self.s_sl_p}")
            if self.i3.get()!=0:
                self.txtarea.insert(END,f"\n Intel i3 \t\t\t{self.i3.get()}\t\t{self.p_i3_p}")
            if self.i9.get()!=0:
                self.txtarea.insert(END,f"\n Intel i9 \t\t\t{self.i9.get()}\t\t{self.p_i9_p}")
            if self.i5.get()!=0:
                self.txtarea.insert(END,f"\n Intel i5 \t\t\t{self.i5.get()}\t\t{self.p_i5_p}")
            if self.i7.get()!=0:
                self.txtarea.insert(END,f"\n Intel i7 \t\t\t{self.i7.get()}\t\t{self.p_i7_p}")
            self.txtarea.insert(END,f"\n*********************************************************")
            self.txtarea.insert(END,f"\n Hardware Tax\t\t\tSoftware Tax\t\tProcessor Tax")
            self.txtarea.insert(END,f"\n {self.htax.get()}\t\t\t{self.stax.get()}\t\t{self.ptax.get()}")
            self.txtarea.insert(END,f"\n*********************************************************")
            self.txtarea.insert(END,f"\n Total Amount \t\t{self.total_price.get()}")
            self.save_bill()
    def save_bill(self):
         op=messagebox.askyesno("Save Bill","Do you want to save the bill ?")
         if op>0:
             self.bill_data=self.txtarea.get('1.0',END)
             f1=open("bills/"+str(self.bill_no.get())+".txt","w")
             f1.write(self.bill_data)
             f1.close()
             messagebox.showinfo("Saved",f"Bill no. :{self.bill_no.get()} saved Successfully")
         else:
             return

    def find_bill(self):
        present="no"
        
        for i in os.listdir("bills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f"bills/{i}","r")
                self.txtarea.delete('1.0'.END)
                for d in f1:
                    
                    self.txtarea.insert(END,d)
                f1.close()
                present="yes"
        if present=="no":
            messagebox.showerror("Error","Invalid Bill No.")
    def clear_data(self):
        self.harddisk.set(0)
        self.smartwatch.set(0)
        self.keybord.set(0)
        self.headphone.set(0)
        #####softwares#####
        self.msoffice.set(0)
        self.coraldraw.set(0)
        self.photoshop.set(0)
        self.scilab.set(0)
        ####processor###
        self.i3.set(0)
        self.i7.set(0)
        self.i5.set(0)
        self.i9.set(0)
        ########TAX$#####
        self.hprice.set("")
        self.sprice.set("")
        self.pprice.set("")

        self.htax.set("")
        self.stax.set("")
        self.ptax.set("")
        #self.total_amt=StringVar()
        ###Customer#####
        self.c_name.set("")
        self.c_phone.set("")
        
        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill.set("")
        self.welcome_bill()
    def exit_app(self):
        op=messagebox.askyesno("Exit","Do you really want to exit")
        if op>0:
            self.root.destroy()
root=Tk()
obj=Bill_App(root)
root.mainloop()
