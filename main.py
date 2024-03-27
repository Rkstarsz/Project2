import tempfile
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
from sklearn import cluster   #pip install pillow
import random,os
from tkinter import messagebox
from time import strftime



class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x800+0+0")
        self.root.title("Billing Management System")

#==================================Variables=============================================#
        self.C_name=StringVar()
        self.C_Phone=StringVar()
        self.Bill_no=StringVar()
        z=random.randint(1000,9999)
        self.Bill_no.set(z)
        self.C_Email=StringVar()
        self.Search_Bill=StringVar()
        self.Product=StringVar()
        self.prices=IntVar()
        self.Qty=IntVar()
        self.Sub_Total=StringVar()
        self.Tax_Input=StringVar()
        self.Total=StringVar()
        


        # Product Categories List
        self.Category=["Select Option","Clothes","Mobiles","Laptops","Choclates"]

        #Sub CatClothes
        self.SubCatClothes=["Select Option",'Jeans','Shirts','T-Shirts']
        self.Jeans=["Select Option","Lee Jeans","Armani Jeans","Calvin Klein"]
        self.price_LeeJeans=5000
        self.price_Armanijeans=700
        self.price_Calvinklein=8000
        
        self.Shirts=["Select Option","Louis Phillipe","Allen Solly","Levi's"]
        self.price_Louis=2100
        self.price_Allen=2700
        self.price_Levi=1740

        self.T_shirts=["Select Option","Zara","TommyHilfiger","Gucci"]
        self.price_Zara=1500
        self.price_tommy=1000
        self.price_Gucci=1700

        #SubCatMobiles
        self.SubCatMobiles=["Select Option","Iphone","Samsung","OnePlus"]
        self.Iphone=["Select Option","iphone 11","iphone 12","iphone 13"]
        self.price_iphone11=50000
        self.price_iphone12=70000
        self.price_iphone13=90000

        self.Samsung=["Select Option","Samsung Note20","Samsung A72s","Samsung s21"]
        self.price_SamsungN=65000
        self.price_SamsungA=40000
        self.price_Samsungs=75000

        self.OnePlus=["Select Option","OnePlus 6","OnePlus 7","OnePlus 9"]
        self.price_OnePlus6=30000
        self.Price_OnePlus7=45000
        self.price_OnePlus9=67000

        #SubcatLaptops
        self.SubCatLaptops=["Select Option","Lenevo","Dell","Hp"]
        self.Lenevo=["Select Option","Lenevo Ideapad","Lenevo Yoga 9i","Lenevo Legion5"]
        self.price_LenevoIp=35000
        self.price_LenevoY9i=48000
        self.price_LenevoLegion=58000

        self.Dell=["Select Option","Dell Inspiron 15","Dell Vostro","Dell Latitude 14"]
        self.price_DellI15=36000
        self.price_DellV=46000
        self.price_DellL14=56000

        self.Hp=["Select Option","Hp Pavillion","Hp Ryzen 3","Hp ChromeBook 14"]
        self.price_Hppl=32000
        self.price_HpRz3=42000
        self.price_HpCB14=62000

        #SubcatChoclate
        self.SubCatChoclate=["Select Option","Dairy_Milk","5_Star","KitKat"]
        self.Dairy_Milk=["Select Option","DM Silk","DM Bubbly","DM nuts"]
        self.price_silk=100
        self.price_bubbly=120
        self.price_nuts=150

        self.Fivestar=["Select Option","5Star 3D","5Star Chomp","5Star Bites"]
        self.price_3D=30
        self.price_Chomp=40
        self.price_Bites=60

        self.Kitkat=["Select Option","KitKat Caramel","KitKat Hazelnut","KitKat MixFruit"]
        self.price_KitCar=45
        self.price_KitHaz=35
        self.price_KitCrn=65

        # Image1
        img=Image.open("images/sem img1.jpg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        lbl_img=Label(self.root,image=self.photoimg)
        lbl_img.place(x=0,y=0,width=500,height=130)

        #Image2
        img_1=Image.open("images/sem img2.jpg")
        img_1=img_1.resize((500,130),Image.ANTIALIAS)
        self.photoimg_1=ImageTk.PhotoImage(img_1)

        lbl_img_1=Label(self.root,image=self.photoimg_1)
        lbl_img_1.place(x=500,y=0,width=500,height=130)

        #Image3
        img_2=Image.open("images/sem img3.jpg")
        img_2=img_2.resize((520,130),Image.ANTIALIAS)
        self.photoimg_2=ImageTk.PhotoImage(img_2)

        lbl_img_2=Label(self.root,image=self.photoimg_2)
        lbl_img_2.place(x=1000,y=0,width=520,height=130)

        lbl_title=Label(self.root,text="Billing System",font=("times new romain",35,"bold"),bg="Black",fg="White")
        lbl_title.place(x=0,y=130,width=1530,height=45)

        def time():
              string=strftime("%H:%M:%S %p")
              lbl.config(text=string)
              lbl.after(1000,time)

        lbl=Label(lbl_title,font=("times new roman",16,"bold"),bg="Black",fg="White")
        lbl.place(x=0,y=0,width=120,height=45)
        time()

        Main_Frame=Frame(self.root,bd=5,relief=GROOVE,bg="White")
        Main_Frame.place(x=0,y=175,width=1530,height=620)

        #Customer LabelFrame
        Cust_Frame=LabelFrame(Main_Frame,text="Customer",font=("times new romain",12,"bold"),bg="Black",fg="White")
        Cust_Frame.place(x=10,y=5,width=350,height=140)
        
        self.lbl_mob=Label(Cust_Frame,text="Mobile No.",font=("times new rain",12,"bold"),bg="White")
        self.lbl_mob.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.entry_mob=ttk.Entry(Cust_Frame,textvariable=self.C_Phone,font=("times new roman",10,"bold"),width=24)
        self.entry_mob.grid(row=0,column=1)

        self.lblCustName=Label(Cust_Frame,font=('arial',12,'bold'),bg="White",text="Customer Name",bd=4)
        self.lblCustName.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.txtCustName=ttk.Entry(Cust_Frame,textvariable=self.C_name,font=('arial',10,'bold'),width=24)
        self.txtCustName.grid(row=1,column=1,sticky=W,padx=5,pady=2)

        self.lblEmail=Label(Cust_Frame,font=('arial',12,'bold'),bg="white",text="Email",bd=4)
        self.lblEmail.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.txtEmail=ttk.Entry(Cust_Frame,textvariable=self.C_Email,font=('arial',10,'bold'),width=24)
        self.txtEmail.grid(row=2,column=1,sticky=W,padx=5,pady=2)

        # product LabelFrame
        Product_Frame=LabelFrame(Main_Frame,text="Product",font=("times new roman",12,"bold"),bg="Black",fg="White")
        Product_Frame.place(x=370,y=5,width=620,height=140)
        
        #Category
        self.lblCategory=Label(Product_Frame,font=('arial',12,'bold'),bg="white",text="Select Categories",bd=4)
        self.lblCategory.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.Combo_Category=ttk.Combobox(Product_Frame,value=self.Category,state="readonly",font=('arial',10,'bold'),width=24)
        self.Combo_Category.current(0)
        self.Combo_Category.grid(row=0,column=1,sticky=W,padx=5,pady=2)
        self.Combo_Category.bind("<<ComboboxSelected>>",self.Categories)


        # SubCategory
        self.lblSubCategory=Label(Product_Frame,font=('arial',12,'bold'),bg="white",text="SubCategory ",bd=4)
        self.lblSubCategory.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.ComboSubCategory=ttk.Combobox(Product_Frame,value=[""],state="readonly",font=('arial',10,'bold'),width=24)
        self.ComboSubCategory.grid(row=1,column=1,sticky=W,padx=5,pady=2)
        self.ComboSubCategory.bind("<<ComboboxSelected>>",self.Product_add)

        # Prodect Name
        self.lblproduct=Label(Product_Frame,font=("arial",12,"bold"),bg="White",text="Product Name",bd=4)
        self.lblproduct.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.ComboProduct=ttk.Combobox(Product_Frame,textvariable=self.Product,state="readonly",font=("arial",10,"bold"),width=24)
        self.ComboProduct.grid(row=2,column=1,sticky=W,padx=5,pady=2)
        self.ComboProduct.bind("<<ComboboxSelected>>",self.price)

        # Price
        self.lblPrice=Label(Product_Frame,font=("arial",12,"bold"),bg="White",text="Price",bd=4)
        self.lblPrice.grid(row=0,column=2,sticky=W,padx=5,pady=2)

        self.ComboPrice=ttk.Combobox(Product_Frame,state="readonly",textvariable=self.prices,font=("arial",10,"bold"),width=24)
        self.ComboPrice.grid(row=0,column=3,sticky=W,padx=5,pady=2)

        #Quantity
        self.lblQty=Label(Product_Frame,font=("arial",12,"bold"),bg="White",text="Qty",bd=4)
        self.lblQty.grid(row=1,column=2,sticky=W,padx=5,pady=2)

        self.ComboQty=ttk.Entry(Product_Frame,textvariable=self.Qty,font=("arial",10,"bold"),width=26)
        self.ComboQty.grid(row=1,column=3,sticky=W,padx=5,pady=2)

        # Middle Frame

        Middle_Frame=Frame(Main_Frame,bd=10)
        Middle_Frame.place(x=10,y=150,width=980,height=340)

         # Image3
        img_3=Image.open("images/sem img6.jpg")
        img_3=img_3.resize((490,340),Image.ANTIALIAS)
        self.photoimg_3=ImageTk.PhotoImage(img_3)

        lbl_img_3=Label(Middle_Frame,image=self.photoimg_3)
        lbl_img_3.place(x=0,y=0,width=490,height=340)

        #Image4
        img_4=Image.open("images/img sem 5.jpg")
        img_4=img_4.resize((490,340),Image.ANTIALIAS)
        self.photoimg_4=ImageTk.PhotoImage(img_4)

        lbl_img_4=Label(Middle_Frame,image=self.photoimg_4)
        lbl_img_4.place(x=490,y=0,width=500,height=340)




        # Search

        Search_Frame=Frame(Main_Frame,bd=2,bg="White")
        Search_Frame.place(x=1020,y=15,width=500,height=40)

        self.lblBill=Label(Search_Frame,font=("arial",12,"bold"),bg="Black",text="Bill No.",fg="white")
        self.lblBill.grid(row=0,column=0,sticky=W,padx=1)

        self.txt_Entry_Search=ttk.Entry(Search_Frame,textvariable=self.Search_Bill,font=("arial",10,"bold"),width=24)
        self.txt_Entry_Search.grid(row=0,column=1,sticky=W,padx=2)

        self.btnSearch=Button(Search_Frame,command=self.Find_Bill,text="Search",font=("arial",10,"bold"),bg="Black",fg="White",width=15,cursor="hand2")
        self.btnSearch.grid(row=0,column=2)





        #Right Frame For Bill Area
        RightLabelFrame=LabelFrame(Main_Frame,text="Bill Area",font=("times new roman",12,"bold"),bg="Black",fg="White")
        RightLabelFrame.place(x=1000,y=45,width=480,height=440)

        scroll_y=Scrollbar(RightLabelFrame,orient=VERTICAL)
        self.textarea=Text(RightLabelFrame,yscrollcommand=scroll_y.set,bg="Black",fg="Grey",font=("times new roman",12,"bold"))
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

        # Bill Counter LabelFrame
        Bottom_Frame=LabelFrame(Main_Frame,text="Bill Counter",font=("times new roman",12,"bold"),bg="Black",fg="White")
        Bottom_Frame.place(x=0,y=485,width=1520,height=125)

        self.SubTotal=Label(Bottom_Frame,font=("arial",12,"bold"),bg="White",text="SubTotal",bd=4)
        self.SubTotal.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.EntySubTotal=ttk.Entry(Bottom_Frame,font=("arial",10,"bold"),width=24,textvariable=self.Sub_Total)
        self.EntySubTotal.grid(row=0,column=1,sticky=W,padx=5,pady=2)

        self.lbl_Tax=Label(Bottom_Frame,font=("arial",12,"bold"),bg="White",text="Gov Tax",bd=4)
        self.lbl_Tax.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.txt_Tax=ttk.Entry(Bottom_Frame,font=("arial",10,"bold"),width=24,textvariable=self.Tax_Input)
        self.txt_Tax.grid(row=1,column=1,sticky=W,padx=5,pady=2)

        self.lblAmountTotal=Label(Bottom_Frame,font=("arial",12,"bold"),bg="White",text="Total",bd=4)
        self.lblAmountTotal.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.txtAmountTotal=ttk.Entry(Bottom_Frame,font=("arial",10,"bold"),width=24,textvariable=self.Total)
        self.txtAmountTotal.grid(row=2,column=1,sticky=W,padx=5,pady=2)

        # Button Frame

        Button_Frame=Frame(Bottom_Frame,bd=2,bg="Black")
        Button_Frame.place(x=320,y=0)

        self.btnAddToCart=Button(Button_Frame,text="Add to Cart",command=self.AddItem,font=("arial",15,"bold"),bg="Black",fg="White",width=15,cursor="hand2")
        self.btnAddToCart.grid(row=0,column=0)

        self.btnGenerate=Button(Button_Frame,text="Generate Bill",command=self.Gen_Bill,font=("arial",15,"bold"),bg="Black",fg="White",width=15,cursor="hand2")
        self.btnGenerate.grid(row=0,column=1)

        self.btnSave=Button(Button_Frame,text="Save Bill",command=self.Save_Bill,font=("arial",15,"bold"),bg="Black",fg="White",width=15,cursor="hand2")
        self.btnSave.grid(row=0,column=2)

        self.btnPrint=Button(Button_Frame,command=self.Iprint,text="Print",font=("arial",15,"bold"),bg="Black",fg="White",width=15,cursor="hand2")
        self.btnPrint.grid(row=0,column=3)

        self.btnClear=Button(Button_Frame,command=self.Clear,text="Clear",font=("arial",15,"bold"),bg="Black",fg="White",width=15,cursor="hand2")
        self.btnClear.grid(row=0,column=4)

        self.btnExit=Button(Button_Frame,command=self.root.destroy,text="Exit",font=("arial",15,"bold"),bg="Black",fg="White",width=15,cursor="hand2")
        self.btnExit.grid(row=0,column=5)
        self.Welcome()

        self.l=[]

      #=====================================Function Declaration=====================================
    def AddItem(self):
          Tax=1
          self.n=self.prices.get()
          self.m=self.Qty.get()*self.n
          self.l.append(self.m)
          if self.Product.get()=="":
                messagebox.showerror("Error","Please Select the Product Name")
          else:
                self.textarea.insert(END,f"\n {self.Product.get()}\t\t{self.Qty.get()}\t\t{self.m}")
                self.Sub_Total.set(str('Rs.%.2f'%(sum(self.l))))
                self.Tax_Input.set(str('Rs.%.2f'%((((sum(self.l)) - (self.prices.get()))*Tax)/100)))
                self.Total.set(str('Rs.%.2f'%(((sum(self.l)) + ((((sum(self.l)) - (self.prices.get()))*Tax)/100)))))

    def Gen_Bill(self):
          if self.Product.get()=="":
                messagebox.showerror("Error","Please Add to Cart product")
          else:
                text=self.textarea.get(10.0,(10.0+float(len(self.l))))
                self.Welcome()
                self.textarea.insert(END,text)
                self.textarea.insert(END,"\n================================================")
                self.textarea.insert(END,f"\n Sub Amount:\t\t\t{self.Sub_Total.get()}")
                self.textarea.insert(END,f"\n Tax Amount:\t\t\t{self.Tax_Input.get()}")
                self.textarea.insert(END,f"\n Total Amount:\t\t\t{self.Total.get()}")
                self.textarea.insert(END,"\n================================================")

    def Save_Bill(self):
          op=messagebox.askyesno("Save Bill","Do You Want to Save the Bill")
          if op>0:
                self.Bill_Data=self.textarea.get(1.0,END)
                f1=open("Bills/"+str(self.Bill_no.get())+".txt","w")
                f1.write(self.Bill_Data)
                op=messagebox.showinfo("Saved",f"Bill_no:{self.Bill_no.get()} Saved Successfully")
                f1.close() 

    def Iprint(self):
          q=self.textarea.get(1.0,"end-1c")
          filename=tempfile.mktemp(".txt")
          open(filename,"w").write(q)
          os.startfile(filename,"print")



    def Welcome(self):
          self.textarea.delete(1.0,END)
          self.textarea.insert(END,"\t MAHARASHTRA TRADERS")
          self.textarea.insert(END,f"\n Bill Number:{self.Bill_no.get()}")
          self.textarea.insert(END,f"\n Customer Name:{self.C_name.get()}")
          self.textarea.insert(END,f"\n Phone no.:{self.C_Phone.get()}")
          self.textarea.insert(END,f"\n Customer Email:{self.C_Email.get()}")
           
          self.textarea.insert(END,"\n=================================================")
          self.textarea.insert(END,f"\n Products\t\t\tQty\t\tPrice")
          self.textarea.insert(END,"\n=================================================\n")

    def Find_Bill(self):
          found="no"
          for i in os.listdir("Bills/"):
                if i.split(".")[0]==self.Search_Bill.get():
                     f1=open(f"Bills/{i}","r")
                     self.textarea.delete(1.0,END)
                     for d in f1:
                           self.textarea.insert(END,d)
                     f1.close()
                     found="Yes"
          if found=="no":
                messagebox.showerror("Error","Invalid Bill No.")
 
    def Clear(self):
          self.textarea.delete(1.0,END)
          self.C_name.set("")
          self.C_Phone.set("")
          self.C_Email.set("")
          x=random.randint(1000,9999)
          self.Bill_no.set(str(x))
          self.Search_Bill.set("")
          self.Product.set("")
          self.prices.set(0)
          self.Qty.set(0)
          self.l=[0]
          self.Total.set("")
          self.Sub_Total.set("")
          self.Tax_Input.set("")
          self.Welcome()



    def Categories(self,Event=""):
          if self.Combo_Category.get()=="Clothes":
                self.ComboSubCategory.config(value=self.SubCatClothes)
                self.ComboSubCategory.current(0)

          if self.Combo_Category.get()=="Mobiles":
                self.ComboSubCategory.config(value=self.SubCatMobiles)
                self.ComboSubCategory.current(0)

          if self.Combo_Category.get()=="Laptops":
                self.ComboSubCategory.config(value=self.SubCatLaptops)
                self.ComboSubCategory.current(0)

          if self.Combo_Category.get()=="Choclates":
                self.ComboSubCategory.config(value=self.SubCatChoclate)
                self.ComboSubCategory.current(0)

    def Product_add(self,Event=""):
          if self.ComboSubCategory.get()=="Jeans":
                self.ComboProduct.config(value=self.Jeans)
                self.ComboProduct.current(0)

          if self.ComboSubCategory.get()=="T-Shirts":
                self.ComboProduct.config(value=self.T_shirts)
                self.ComboProduct.current(0)

          if self.ComboSubCategory.get()=="Shirts":
                self.ComboProduct.config(value=self.Shirts)
                self.ComboProduct.current(0)

          # Mobiles
          if self.ComboSubCategory.get()=="Iphone":
                self.ComboProduct.config(value=self.Iphone)
                self.ComboProduct.current(0)

          if self.ComboSubCategory.get()=="Samsung":
                self.ComboProduct.config(value=self.Samsung)
                self.ComboProduct.current(0)

          if self.ComboSubCategory.get()=="OnePlus":
                self.ComboProduct.config(value=self.OnePlus)
                self.ComboProduct.current(0)

          # Laptops
          if self.ComboSubCategory.get()=="Lenevo":
                self.ComboProduct.config(value=self.Lenevo)
                self.ComboProduct.current(0)

          if self.ComboSubCategory.get()=="Dell":
                self.ComboProduct.config(value=self.Dell)
                self.ComboProduct.current(0)

          if self.ComboSubCategory.get()=="Hp":
                self.ComboProduct.config(value=self.Hp)
                self.ComboProduct.current(0)

          # Choclate
          if self.ComboSubCategory.get()=="Dairy_Milk":
                self.ComboProduct.config(value=self.Dairy_Milk)
                self.ComboProduct.current(0)

          if self.ComboSubCategory.get()=="5_Star":
                self.ComboProduct.config(value=self.Fivestar)
                self.ComboProduct.current(0)

          if self.ComboSubCategory.get()=="KitKat":
                self.ComboProduct.config(value=self.Kitkat)
                self.ComboProduct.current(0)

    def price(self,event=""):
          # Jeans
          if self.ComboProduct.get()=="Lee Jeans":
                self.ComboPrice.config(value=self.price_LeeJeans)
                self.ComboPrice.current(0)
                self.Qty.set(1)

          if self.ComboProduct.get()=="Armani Jeans":
                self.ComboPrice.config(value=self.price_Armanijeans)
                self.ComboPrice.current(0)
                self.Qty.set(1)

          if self.ComboProduct.get()=="Calvin Klein":
                self.ComboPrice.config(value=self.price_Calvinklein)
                self.ComboPrice.current(0)
                self.Qty.set(1)

          # T-Shirts
          if self.ComboProduct.get()=="Zara":
                self.ComboPrice.config(value=self.price_Zara)
                self.ComboPrice.current(0)
                self.Qty.set(1)

          if self.ComboProduct.get()=="TommyHilfiger":
                self.ComboPrice.config(value=self.price_tommy)
                self.ComboPrice.current(0)
                self.Qty.set(1)

          if self.ComboProduct.get()=="Gucci":
                self.ComboPrice.config(value=self.price_Gucci)
                self.ComboPrice.current(0)
                self.Qty.set(1)

          # Shirts
          if self.ComboProduct.get()=="Louis Phillipe":
                self.ComboPrice.config(value=self.price_Louis)
                self.ComboPrice.current(0)
                self.Qty.set(1)

          if self.ComboProduct.get()=="Allen Solly":
                self.ComboPrice.config(value=self.price_Allen)
                self.ComboPrice.current(0)
                self.Qty.set(1)

          if self.ComboProduct.get()=="Levi's":
                self.ComboPrice.config(value=self.price_Levi)
                self.ComboPrice.current(0)
                self.Qty.set(1)

          # Mobiles
          if self.ComboProduct.get()=="iphone 11":
                self.ComboPrice.config(value=self.price_iphone11)
                self.ComboPrice.current(0)
                self.Qty.set(1)

          if self.ComboProduct.get()=="iphone 12":
                self.ComboPrice.config(value=self.price_iphone12)
                self.ComboPrice.current(0)
                self.Qty.set(1)

          if self.ComboProduct.get()=="iphone 13":
                self.ComboPrice.config(value=self.price_iphone13)
                self.ComboPrice.current(0)
                self.Qty.set(1)

          # Samsung
          if self.ComboProduct.get()=="Samsung Note20":
                self.ComboPrice.config(value=self.price_SamsungN)
                self.ComboPrice.current(0)
                self.Qty.set(1)

          if self.ComboProduct.get()=="Samsung A72s":
                self.ComboPrice.config(value=self.price_SamsungA)
                self.ComboPrice.current(0)
                self.Qty.set(1)

          if self.ComboProduct.get()=="Samsung s21":
                self.ComboPrice.config(value=self.price_Samsungs)
                self.ComboPrice.current(0)
                self.Qty.set(1)

          #OnePlus
          if self.ComboProduct.get()=="OnePlus 6":
                self.ComboPrice.config(value=self.price_OnePlus6)
                self.ComboPrice.current(0)
                self.Qty.set(1)

          if self.ComboProduct.get()=="OnePlus 7":
                self.ComboPrice.config(value=self.Price_OnePlus7)
                self.ComboPrice.current(0)
                self.Qty.set(1)

          if self.ComboProduct.get()=="OnePlus 9":
                self.ComboPrice.config(value=self.price_OnePlus9)
                self.ComboPrice.current(0)
                self.Qty.set(1)

          # Laptops
          if self.ComboProduct.get()=="Lenevo Ideapad":
                self.ComboPrice.config(value=self.price_LenevoIp)
                self.ComboPrice.current(0)
                self.Qty.set(1)

          if self.ComboProduct.get()=="Lenevo Yoga 9i":
                self.ComboPrice.config(value=self.price_LenevoY9i)
                self.ComboPrice.current(0)
                self.Qty.set(1)

          if self.ComboProduct.get()=="Lenevo Legion5":
                self.ComboPrice.config(value=self.price_LenevoLegion)
                self.ComboPrice.current(0)
                self.Qty.set(1)

          # Dell
          if self.ComboProduct.get()=="Dell Inspiron 15":
                self.ComboPrice.config(value=self.price_DellI15)
                self.ComboPrice.current(0)
                self.Qty.set(1)

          if self.ComboProduct.get()=="Dell Vostro":
                self.ComboPrice.config(value=self.price_DellV)
                self.ComboPrice.current(0)
                self.Qty.set(1)

          if self.ComboProduct.get()=="Dell Latitude 14":
                self.ComboPrice.config(value=self.price_DellL14)
                self.ComboPrice.current(0)
                self.Qty.set(1)

          # Hp
          if self.ComboProduct.get()=="Hp Pavillion":
                self.ComboPrice.config(value=self.price_Hppl)
                self.ComboPrice.current(0)
                self.Qty.set(1)

          if self.ComboProduct.get()=="Hp Ryzen 3":
                self.ComboPrice.config(value=self.price_HpRz3)
                self.ComboPrice.current(0)
                self.Qty.set(1)

          if self.ComboProduct.get()=="Hp ChromeBook 14":
                self.ComboPrice.config(value=self.price_HpCB14)
                self.ComboPrice.current(0)
                self.Qty.set(1)
            
          # Choclate
          if self.ComboProduct.get()=="DM Silk":
                self.ComboPrice.config(value=self.price_silk)
                self.ComboPrice.current(0)
                self.Qty.set(1)

          if self.ComboProduct.get()=="DM Bubbly":
                self.ComboPrice.config(value=self.price_bubbly)
                self.ComboPrice.current(0)
                self.Qty.set(1)

          if self.ComboProduct.get()=="DM nuts":
                self.ComboPrice.config(value=self.price_nuts)
                self.ComboPrice.current(0)
                self.Qty.set(1)

          if self.ComboProduct.get()=="5Star 3D":
                self.ComboPrice.config(value=self.price_3D)
                self.ComboPrice.current(0)
                self.Qty.set(1)

          if self.ComboProduct.get()=="5Star Chomp":
                self.ComboPrice.config(value=self.price_Chomp)
                self.ComboPrice.current(0)
                self.Qty.set(1)

          if self.ComboProduct.get()=="5Star Bites":
                self.ComboPrice.config(value=self.price_Bites)
                self.ComboPrice.current(0)
                self.Qty.set(1)

          if self.ComboProduct.get()=="KitKat Caramel":
                self.ComboPrice.config(value=self.price_KitCar)
                self.ComboPrice.current(0)
                self.Qty.set(1)

          if self.ComboProduct.get()=="KitKat Hazelnut":
                self.ComboPrice.config(value=self.price_KitHaz)
                self.ComboPrice.current(0)
                self.Qty.set(1)

          if self.ComboProduct.get()=="KitKat MixFruit":
                self.ComboPrice.config(value=self.price_KitCrn)
                self.ComboPrice.current(0)
                self.Qty.set(1)
          
      

                 








        










        

















if __name__ == '__main__':
    root=Tk()
    object=Bill_App(root)
    root.mainloop()
