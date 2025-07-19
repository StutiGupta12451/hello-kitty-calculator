#hello kitty calculator
import tkinter as tk
from simpleeval import simple_eval
from PIL import Image, ImageTk
calculation=""
def add_to_calculation(symbol):
    global calculation
    calculation+=str(symbol)
    textbox.delete(1.0,"end")
    textbox.insert(1.0,calculation)
def evaluate():
    try:
        global calculation
        result = simple_eval(calculation)
        calculation = str(result)
        textbox.delete(1.0, "end")
        textbox.insert(1.0, result)
    except:
        textbox.delete(1.0,"end")
        textbox.insert(1.0,"Error")
        calculation=""
def clear_screen():
    global calculation
    textbox.delete(1.0,"end")
    calculation=""

root=tk.Tk()
root.geometry("500x500")
root.configure(bg="#FFC0CB")
root.title("Hello Kitty Calculator🎀")
image_path = r"C:\Users\stuti\Downloads\wp12717365.jpg"
img = Image.open(image_path)
img = img.resize((500,75))  # resize for display
kitty_img = ImageTk.PhotoImage(img)
label=tk.Label(root,image=kitty_img, bg="#FFC0CB")
label.pack()
textbox=tk.Text(root,width=29,height=2,font=("Arial",24),bg="white", fg="hot pink")
textbox.pack(padx=5,pady=5)
buttonframe=tk.Frame(root)
buttonframe.columnconfigure(0,weight=5)
buttonframe.columnconfigure(1,weight=5)
buttonframe.columnconfigure(2,weight=5)
buttonframe.columnconfigure(3,weight=5)
buttonframe.columnconfigure(4,weight=5)
btn_clear=tk.Button(buttonframe,text="C",font=("Arial",16),width=10,height=2,bg="#FF69B4", fg="white",command=clear_screen)
btn_clear.grid(row=0,column=0)
btn_deci=tk.Button(buttonframe,text=".",font=("Arial",16),width=10,height=2,bg="#FF69B4", fg="white",command=lambda:add_to_calculation("."))
btn_deci.grid(row=0,column=1)
btn_percent=tk.Button(buttonframe,text="%",font=("Arial",16),width=10,height=2,bg="#FF69B4", fg="white",command=lambda:add_to_calculation("/100"))
btn_percent.grid(row=0,column=2)
btn_div=tk.Button(buttonframe,text="/",font=("Arial",16),width=10,height=2,bg="#FF69B4", fg="white",command=lambda:add_to_calculation("/"))
btn_div.grid(row=0,column=3)
btn_7=tk.Button(buttonframe,text="7",font=("Arial",16),width=10,height=2,bg="#FF69B4", fg="white",command=lambda:add_to_calculation(7))
btn_7.grid(row=1,column=0)
btn_8=tk.Button(buttonframe,text="8",font=("Arial",16),width=10,height=2,bg="#FF69B4", fg="white",command=lambda:add_to_calculation(8))
btn_8.grid(row=1,column=1)
btn_9=tk.Button(buttonframe,text="9",font=("Arial",16),width=10,height=2,bg="#FF69B4", fg="white",command=lambda:add_to_calculation(9))
btn_9.grid(row=1,column=2)
btn_mult=tk.Button(buttonframe,text="*",font=("Arial",16),width=10,height=2,bg="#FF69B4", fg="white",command=lambda:add_to_calculation("*"))
btn_mult.grid(row=1,column=3)
btn_4=tk.Button(buttonframe,text="4",font=("Arial",16),width=10,height=2,bg="#FF69B4", fg="white",command=lambda:add_to_calculation(4))
btn_4.grid(row=2,column=0)
btn_5=tk.Button(buttonframe,text="5",font=("Arial",16),width=10,height=2,bg="#FF69B4", fg="white",command=lambda:add_to_calculation(5))
btn_5.grid(row=2,column=1)
btn_6=tk.Button(buttonframe,text="6",font=("Arial",16),width=10,height=2,bg="#FF69B4", fg="white",command=lambda:add_to_calculation(6))
btn_6.grid(row=2,column=2)
btn_minus=tk.Button(buttonframe,text="-",font=("Arial",16),width=10,height=2,bg="#FF69B4", fg="white",command=lambda:add_to_calculation("-"))
btn_minus.grid(row=2,column=3)
btn_1=tk.Button(buttonframe,text="1",font=("Arial",16),width=10,height=2,bg="#FF69B4", fg="white",command=lambda:add_to_calculation(1))
btn_1.grid(row=3,column=0)
btn_2=tk.Button(buttonframe,text="2",font=("Arial",16),width=10,height=2,bg="#FF69B4", fg="white",command=lambda:add_to_calculation(2))
btn_2.grid(row=3,column=1)
btn_3=tk.Button(buttonframe,text="3",font=("Arial",16),width=10,height=2,bg="#FF69B4", fg="white",command=lambda:add_to_calculation(3))
btn_3.grid(row=3,column=2)
btn_plus=tk.Button(buttonframe,text="+",font=("Arial",16),width=10,height=2,bg="#FF69B4", fg="white",command=lambda:add_to_calculation("+"))
btn_plus.grid(row=3,column=3)
btn_left=tk.Button(buttonframe,text="(",font=("Arial",16),width=10,height=2,bg="#FF69B4", fg="white",command=lambda:add_to_calculation("("))
btn_left.grid(row=4,column=0)
btn_0=tk.Button(buttonframe,text="0",font=("Arial",16),width=10,height=2,bg="#FF69B4", fg="white",command=lambda:add_to_calculation(0))
btn_0.grid(row=4,column=1)
btn_right=tk.Button(buttonframe,text=")",font=("Arial",16),width=10,height=2,bg="#FF69B4", fg="white",command=lambda:add_to_calculation(")"))
btn_right.grid(row=4,column=2)
btn_equals=tk.Button(buttonframe,text="=",font=("Arial",16),width=10,height=2,bg="White",fg="#FF69B4",command=evaluate)
btn_equals.grid(row=4,column=3)
buttonframe.pack(padx=5,pady=5,fill="x")

root.mainloop() 