import tkinter as tk
import customtkinter
root = customtkinter.CTk()
root.title("Calculator")
root.title("Calculator")
root.geometry("500x600+300+100")
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("dark-blue")
root.resizable(0,0)
signs = ['*','+','%','-','/']   
var=customtkinter.StringVar()
def clicked(val):
    global var 
    
    if val == "=":
        try:
            if var.get()!="":
                last_character = var.get()[-1]
                if last_character in signs:
                    txt = var.get()[:-1]
                    result = eval(txt)
                    var.set(result)
                else:
                    txt = var.get()
                    result = eval(txt)
                    var.set(result)
                        
            else:
                var.set(result)    
        except Exception as e:
            var.set("Error")
    elif var.get()=='Error':
        var.set("")
        var.set(var.get()+val)
                
    elif val =="C":
            var.set("")
            calc.update() 
    elif val == "DEL":
            val = var.get()
            val = val[:len(val)-1]
            var.set(val)
            calc.update()   
    elif val == ".":
            if "." not in var.get():
                var.set(var.get() + ".")
                calc.update()
            elif "."in var.get():
                sp = var.get().split(".")
                if "%" in sp[len(sp)-1] or "*"in sp[len(sp)-1] or "-" in sp[len(sp)-1] or "+" in sp[len(sp)-1]:
                    var.set(var.get()+".")
                    calc.update()
                        
    else:
        if var.get()!="":
            last_ch = var.get()[-1]
            if val in signs and last_ch in signs:
                pass
            else:
                var.set(var.get()+val)  
                
        else:
            var.set(var.get()+val)    
       

mainframe = customtkinter.CTkFrame(root,fg_color="gray11",width=500,height=600)
top_frame = customtkinter.CTkFrame(mainframe, width=450, height=200,fg_color='black')
bottom = customtkinter.CTkFrame(mainframe, width=500, height=400,fg_color="transparent")
calc = customtkinter.CTkEntry(top_frame, font=('american', 70), justify='right',textvariable=var,width=450, height=180)
calc.place(x=0, y=10)
top_frame.place(x=23, y=2)
btns_frame = customtkinter.CTkFrame(bottom,width=480,height=360,border_width=2,border_color="gray15",fg_color="gray13")
# Button Clear
btnC = customtkinter.CTkButton(btns_frame, text="C",fg_color="red"  ,font=('american',40,"bold"),height=60,cursor="hand2",width=110,command= lambda x="C":clicked(x))
btnC.place(x = 5, y = 10)
# Button DEL
btnDEL = customtkinter.CTkButton(btns_frame, text="DEL",fg_color="darkgreen" ,font=('american',40,"bold"),height=60,cursor="hand2",width=110,command= lambda x="DEL":clicked(x))
btnDEL.place(x = 125, y = 10)
# Button %
btnmod = customtkinter.CTkButton(btns_frame, text="%",  font=('american',40,"bold"),height=60,cursor="hand2",width=110,command= lambda x="%":clicked(x))
btnmod.place(x = 245, y = 10)
# Button divide
btndiv = customtkinter.CTkButton(btns_frame, text="/",  font=('american',40,"bold"),height=60,cursor="hand2",width=110,command= lambda x="/":clicked(x))
btndiv.place(x = 365, y = 10)
# Button 7
btn7 = customtkinter.CTkButton(btns_frame, text="7",  font=('american',40,"bold"),height=60,cursor="hand2",width=110,command= lambda x="7":clicked(x))
btn7.place(x = 5, y = 80)
# Button 8
btn8 = customtkinter.CTkButton(btns_frame, text="8",  font=('american',40,"bold"),height=60,cursor="hand2",width=110,command= lambda x="8":clicked(x))
btn8.place(x = 125, y = 80)
# Button 9
btn9 = customtkinter.CTkButton(btns_frame, text="9",  font=('american',40,"bold"),height=60,cursor="hand2",width=110,command= lambda x="9":clicked(x))
btn9.place(x = 245, y = 80)
# Button x
btnmul = customtkinter.CTkButton(btns_frame, text="*",  font=('american',40,"bold"),height=60,cursor="hand2",width=110,command= lambda x="*":clicked(x))
btnmul.place(x = 365, y = 80)
# Button 4
btn4 = customtkinter.CTkButton(btns_frame, text="4",  font=('american',40,"bold"),height=60,cursor="hand2",width=110,command= lambda x="4":clicked(x))
btn4.place(x = 5, y = 150)
# Button 5
btn5 = customtkinter.CTkButton(btns_frame, text="5",  font=('american',40,"bold"),height=60,cursor="hand2",width=110,command= lambda x="5":clicked(x))
btn5.place(x = 125, y = 150)
# Button 6
btn6 = customtkinter.CTkButton(btns_frame, text="6",  font=('american',40,"bold"),height=60,cursor="hand2",width=110,command= lambda x="6":clicked(x))
btn6.place(x = 245, y = 150)
# Button -
btnminus = customtkinter.CTkButton(btns_frame, text="-",  font=('american',40,"bold"),height=60,cursor="hand2",width=110,command= lambda x="-":clicked(x))
btnminus.place(x = 365, y = 150)
# Button 1
btn1 = customtkinter.CTkButton(btns_frame, text="1",  font=('american',40,"bold"),height=60,cursor="hand2",width=110,command= lambda x="1":clicked(x))
btn1.place(x = 5, y = 220)
# Button 2
btn2 = customtkinter.CTkButton(btns_frame, text="2",  font=('american',40,"bold"),height=60,cursor="hand2",width=110,command= lambda x="2":clicked(x))
btn2.place(x = 125, y = 220)
# Button 3
btn3 = customtkinter.CTkButton(btns_frame, text="3",  font=('american',40,"bold"),height=60,cursor="hand2",width=110,command= lambda x="3":clicked(x))
btn3.place(x = 245, y = 220)
btnplus = customtkinter.CTkButton(btns_frame, text="+",  font=('american',40,"bold"),height=60,cursor="hand2",width=110,command= lambda x="+":clicked(x))
btnplus.place(x = 365, y = 220)
# Button 0
btn0 = customtkinter.CTkButton(btns_frame, text="0", font=('american',40),cursor="hand2",height=60,width=230,command= lambda x="0":clicked(x))
btn0.place(x = 5, y = 290)
# Button .
btndot = customtkinter.CTkButton(btns_frame, text=".",  font=('american',40,"bold"),height=60,cursor="hand2",width=110,command= lambda x=".":clicked(x))
btndot.place(x = 245, y = 290)
# Button =
btnequal = customtkinter.CTkButton(btns_frame, text="=",  font=('american',40,"bold"),height=60,cursor="hand2",width=110,command= lambda x="=":clicked(x))
btnequal.place(x = 365, y = 290)
btns_frame.place(relx=0.017,rely=0.03)
bottom.place(rely=0.35, x=0.2)
mainframe.pack()
root.mainloop()
