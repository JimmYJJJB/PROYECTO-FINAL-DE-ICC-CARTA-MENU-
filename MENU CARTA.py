from tkinter import*
from tkinter import messagebox


venNuevo = Tk()
venNuevo.geometry("1050x600+100+100")
venNuevo.title("carta")


def enviarCuenta():
    p1= ""
    p2= ""
    p3= ""
    p4= ""
    p5= ""
    p6= ""
    p7= ""
    p8= ""
    p9= ""
    p10= ""
    p11= ""
    p12= ""
    p13= ""
    p14= ""

    cuenta = open("cuenta.txt","r")
    lineas = cuenta.readlines()
    totalLista = len(lineas)
    total = int(lineas[totalLista-1])
    cuentaPedido = acantidad1.get()*15 + acantidad2.get()*20 + acantidad3.get()*18 + acantidad4.get()*14 + acantidad5.get()*10 + acantidad6.get()*10 + acantidad7.get()*13 +acantidad8.get()*18 + acantidad9.get()*7 + acantidad10.get()*6 + acantidad11.get()*6 + acantidad12.get()*6 + acantidad13.get()*7 + acantidad14.get()*3
    newTotal = total + cuentaPedido
    cuenta.close()
    cuenta = open("cuenta.txt","w")
    cuenta.write("")
    cuenta.close()
    cuenta = open("cuenta.txt","a")
    for i in range(totalLista-2):
        cuenta.write(lineas[i])

    cuenta.write(anombre.get() + "\n")
    if(acantidad1.get()!=0):
        cuenta.write(str(acantidad1.get()) + " Lomo saltado" + "  =  S/." + str(acantidad1.get()*15) + "\n")
        p1 = (str(acantidad1.get()) + " Lomo saltado" + "  =  S/." + str(acantidad1.get()*15) + "\n")
    if(acantidad2.get()!=0):
        cuenta.write(str(acantidad2.get()) + " Cuy chactado" + "  =  S/." + str(acantidad2.get()*20) + "\n")
        p2 = (str(acantidad2.get()) + " Cuy chactado" + "  =  S/." + str(acantidad2.get()*20) + "\n")
    if(acantidad3.get()!=0):
        cuenta.write(str(acantidad3.get()) + " Pato asado" + "  =  S/." + str(acantidad3.get()*18) + "\n")
        p3 = (str(acantidad3.get()) + " Pato asado" + "  =  S/." + str(acantidad3.get()*18) + "\n")
    if(acantidad4.get()!=0):
        cuenta.write(str(acantidad4.get()) + " Carapulcra" + "  =  S/." + str(acantidad4.get()*14) + "\n")
        p4 = (str(acantidad4.get()) + " Carapulcra" + "  =  S/." + str(acantidad4.get()*14) + "\n")
    if(acantidad5.get()!=0):
        cuenta.write(str(acantidad5.get()) + " Ensalada de palta" + "  =  S/." + str(acantidad5.get()*10) + "\n")
        p5 = (str(acantidad5.get()) + " Ensalada de palta" + "  =  S/." + str(acantidad5.get()*10) + "\n")
    if(acantidad6.get()!=0):
        cuenta.write(str(acantidad6.get()) + " Patacones" + "  =  S/." + str(acantidad6.get()*10) + "\n")
        p6 = (str(acantidad6.get()) + " Patacones" + "  =  S/." + str(acantidad6.get()*10) + "\n")
    if(acantidad7.get()!=0):
        cuenta.write(str(acantidad7.get()) + " Aji de gallina" + "  =  S/." + str(acantidad7.get()*13) + "\n")
        p7 = (str(acantidad7.get()) + " Aji de gallina" + "  =  S/." + str(acantidad7.get()*13) + "\n")
    if(acantidad8.get()!=0):
        cuenta.write(str(acantidad8.get()) + " Pachamanca 3 sabores" + "  =  S/." + str(acantidad8.get()*18) + "\n")
        p8 = (str(acantidad8.get()) + " Pachamanca 3 sabores" + "  =  S/." + str(acantidad8.get()*18) + "\n")
    if(acantidad9.get()!=0):
        cuenta.write(str(acantidad9.get()) + " Gaseosa 1.5L" + "  =  S/." + str(acantidad9.get()*7) + "\n")
        p9 = (str(acantidad9.get()) + " Gaseosa 1.5L" + "  =  S/." + str(acantidad9.get()*7) + "\n")
    if(acantidad10.get()!=0):
        cuenta.write(str(acantidad10.get()) + " Chicha jarra" + "  =  S/." + str(acantidad10.get()*6) + "\n")
        p10 = (str(acantidad10.get()) + " Chicha jarra" + "  =  S/." + str(acantidad10.get()*6) + "\n")
    if(acantidad11.get()!=0):
        cuenta.write(str(acantidad11.get()) + " Limonada jarra" + "  =  S/." + str(acantidad11.get()*6) + "\n")
        p11 = (str(acantidad11.get()) + " Limonada jarra" + "  =  S/." + str(acantidad11.get()*6) + "\n")
    if(acantidad12.get()!=0):
        cuenta.write(str(acantidad12.get()) + " Cerveza Pilsen" + "  =  S/." + str(acantidad12.get()*6) + "\n")
        p12 = (str(acantidad12.get()) + " Cerveza Pilsen" + "  =  S/." + str(acantidad12.get()*6) + "\n")
    if(acantidad13.get()!=0):
        cuenta.write(str(acantidad13.get()) + " Cerveza Cristal" + "  =  S/." + str(acantidad13.get()*7) + "\n")
        p13 = (str(acantidad13.get()) + " Cerveza Cristal" + "  =  S/." + str(acantidad13.get()*7) + "\n")
    if(acantidad14.get()!=0):
        cuenta.write(str(acantidad14.get()) + " Copa Anis Najar" + "  =  S/." + str(acantidad14.get()*3) + "\n")
        p14 = (str(acantidad14.get()) + " Copa Anis Najar" + "  =  S/." + str(acantidad14.get()*3) + "\n")
    cuenta.write("total de mesa = S/." + str(cuentaPedido) + "\n")
    cuenta.write("TOTAL = S/. " + "\n" + str(newTotal) + "\n")

    messagebox.showinfo("cuenta total","platos pedidos: \n" + p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9 + p10 + p11 + p12 + p13 + p14 + "\n Cuenta total = S/." + str(cuentaPedido))
    venNuevo.destroy()


anombre = StringVar()
acantidad1=IntVar()
acantidad2 = IntVar()
acantidad3 = IntVar()
acantidad4 = IntVar()
acantidad5 = IntVar()
acantidad6 = IntVar()
acantidad7 = IntVar()
acantidad8 = IntVar()
acantidad9 = IntVar()
acantidad10 = IntVar()
acantidad11 = IntVar()
acantidad12 = IntVar()
acantidad13 = IntVar()
acantidad14 = IntVar()
anombre.set("mesa N: ")

barraMenu = Menu(venNuevo)
mnuArchivo = Menu(barraMenu)
mnuArchivo.add_command(label="Nuevo")
mnuArchivo.add_separator()
mnuArchivo.add_command(label="Terminar",command=venNuevo.destroy)
barraMenu.add_cascade(label="Archivo",menu=mnuArchivo)
venNuevo.config(menu=barraMenu)

venNuevo.config(bg="gray")
imagenLogo = PhotoImage(file="logo.gif")
logo = Label(venNuevo,image=imagenLogo).place(x=580,y=50)
etiquetaNombre = Label(venNuevo,text="Nombre de mesa:",bg ="gray").place(x=30,y=10)
nombre = Entry(venNuevo,textvariable=anombre).place(x=140,y=10)
plato1 = Label(venNuevo,text="Lomo saltado .............................. S/.15",font=("Agency FB",20),bg ="gray").place(x=40,y=40)
cantidad1 = Spinbox(venNuevo,from_=0,to=100,textvariable=acantidad1).place(x=340,y=50)
plato2 = Label(venNuevo,text="Cuy chactado ..............................S/.20",font=("Agency FB",20),bg ="gray").place(x=40,y=100)
cantidad2 = Spinbox(venNuevo,from_=0,to=100,textvariable=acantidad2).place(x=340,y=110)
plato3 = Label(venNuevo,text="Pato asado .................................. S/.18",font=("Agency FB",20),bg ="gray").place(x=40,y=160)
cantidad3 = Spinbox(venNuevo,from_=0,to=100,textvariable=acantidad3).place(x=340,y=170)
plato4 = Label(venNuevo,text="Carapulcra .................................. S/.14",font=("Agency FB",20),bg ="gray").place(x=40,y=220)
cantidad4 = Spinbox(venNuevo,from_=0,to=100,textvariable=acantidad4).place(x=340,y=230)
plato5 = Label(venNuevo,text="Ensalada de palta ...................... S/.10",font=("Agency FB",20),bg ="gray").place(x=40,y=280)
cantidad5 = Spinbox(venNuevo,from_=0,to=100,textvariable=acantidad5).place(x=340,y=290)
plato6 = Label(venNuevo,text="Patacones .................................... S/.10",font=("Agency FB",20),bg ="gray").place(x=40,y=340)
cantidad6 = Spinbox(venNuevo,from_=0,to=100,textvariable=acantidad6).place(x=340,y=350)
plato7 = Label(venNuevo,text="Aji de gallina ................................ S/.13",font=("Agency FB",20),bg ="gray").place(x=40,y=400)
cantidad7 = Spinbox(venNuevo,from_=0,to=100,textvariable=acantidad7).place(x=340,y=410)
plato8 = Label(venNuevo,text="Pachamanca 3 sabores ........ S/.18",font=("Agency FB",20),bg ="gray").place(x=40,y=460)
cantidad8 = Spinbox(venNuevo,from_=0,to=100,textvariable=acantidad8).place(x=340,y=470)
bebida1 = Label(venNuevo,text="Gaseosa 1.5L ........ S/.7",font=("Agency FB",20),bg ="gray").place(x=510,y=280)
cantidad9 = Spinbox(venNuevo,from_=0,to=100,textvariable=acantidad9).place(x=530,y=330)
bebida2 = Label(venNuevo,text="Chicha jarra ........ S/.6",font=("Agency FB",20),bg ="gray").place(x=780,y=280)
cantidad10 = Spinbox(venNuevo,from_=0,to=100,textvariable=acantidad10).place(x=800,y=330)
bebida3 = Label(venNuevo,text="Limonada jarra ........ S/.6",font=("Agency FB",20),bg ="gray").place(x=510,y=370)
cantidad11 = Spinbox(venNuevo,from_=0,to=100,textvariable=acantidad11).place(x=530,y=420)
bebida4 = Label(venNuevo,text="Cerveza Pilsen ........ S/.6",font=("Agency FB",20),bg ="gray").place(x=780,y=370)
cantidad12 = Spinbox(venNuevo,from_=0,to=100,textvariable=acantidad12).place(x=800,y=420)
bebida5 = Label(venNuevo,text="Cerveza Cristal ........ S/.7",font=("Agency FB",20),bg ="gray").place(x=510,y=460)
cantidad13 = Spinbox(venNuevo,from_=0,to=100,textvariable=acantidad13).place(x=530,y=510)
bebida6 = Label(venNuevo,text="Copa Anis Najar ........ S/.3",font=("Agency FB",20),bg ="gray").place(x=780,y=460)
cantidad14 = Spinbox(venNuevo,from_=0,to=100,textvariable=acantidad14).place(x=800,y=510)
mandar = Button(venNuevo,text="TERMINAR",command=enviarCuenta,font=("Verdana",13),bg="green").place(x=180,y=530)




venNuevo.mainloop()
