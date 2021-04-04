'''
tkinter示範程式--英文字典視窗版
'''
import json
import os
import tkinter as tk
import tkinter.messagebox


def _hit22():
    if enteR21.get() in myDict:
        del myDict[enteR21.get()]
        lbL23["text"]="["+enteR21.get()+"]"+"已刪除!!"
        enteR21.delete(0,tk.END)
    else:
        lbL23["text"]="沒有這個字噢!!"
        enteR21.delete(0,tk.END)

def _hit21():
    if enteR21.get() in myDict:
        lbL23["text"]=myDict[enteR21.get()]
    else:
        lbL23["text"]="沒有這個字噢!!"
        enteR21.delete(0,tk.END)

    
def _hit11():
    myDict[enteR11.get()]=enteR12.get()
    enteR11.delete(0,tk.END)
    enteR12.delete(0,tk.END)
    enteR11.focus()

def _hit1():
    global enteR11,enteR12
    wiN1=tk.Toplevel(wiN)
    wiN1.title("新增/修改單字!!!")
    wiN1.geometry("400x300+300+200")
    lbL11 = tk.Label(wiN1,text="請輸入英文",fg="white",bg="green", font=("Arial", 16), width=15, height=2)
    lbL11.pack()
    enteR11=tk.Entry(wiN1,font=("Arial",16),bd=5)
    enteR11.pack()
    lbL12 = tk.Label(wiN1,text="請輸入中文",fg="white",bg="green", font=("Arial", 16), width=15, height=2)
    lbL12.pack()
    enteR12=tk.Entry(wiN1,font=("Arial",16),bd=5)
    enteR12.pack()
    btN11 = tk.Button(wiN1, text="新增/修改!!",bg="blue",fg="white", font=("Arial", 14), width=10, height=2, command=lambda:_hit11())
    btN11.pack() 
    btN12 = tk.Button(wiN1, text="結束!!",bg="black",fg="white", font=("Arial", 14), width=10, height=2, command=wiN1.destroy)
    btN12.pack() 

def _hit2():
    global lbL23,enteR21
    wiN2=tk.Toplevel(wiN)
    wiN2.title("查詢/刪除單字!!!")
    wiN2.geometry("400x400+300+200")
    lbL21 = tk.Label(wiN2,text="請輸入英文",fg="white",bg="green", font=("Arial", 16), width=15, height=2)
    lbL21.pack()
    enteR21=tk.Entry(wiN2,font=("Arial",16),bd=5)
    enteR21.pack()
    lbL22 = tk.Label(wiN2,text="中文是",fg="white",bg="green", font=("Arial", 16), width=15, height=2)
    lbL22.pack()
    lbL23 = tk.Label(wiN2,text="",fg="white",bg="orange", font=("Arial", 16), width=25, height=2)
    lbL23.pack()
    btN21 = tk.Button(wiN2, text="查詢!!",bg="blue" ,fg="white",font=("Arial", 14), width=10, height=2, command=lambda:_hit21())
    btN21.pack() 
    btN22 = tk.Button(wiN2, text="刪除!!",bg="red", font=("Arial", 14), width=10, height=2, command=lambda:_hit22())
    btN22.pack() 
    btN23 = tk.Button(wiN2, text="結束!!",bg="black",fg="white", font=("Arial", 14), width=10, height=2, command=wiN2.destroy)
    btN23.pack() 

def _hit3():
    wiN3=tk.Toplevel(wiN)
    wiN3.title("顯示所有單字!!!")
    wiN3.geometry("250x800+400+100")
    btN31 = tk.Button(wiN3, text="結束!!",bg="red", font=("Arial", 12), width=10, height=2, command=wiN3.destroy)
    btN31.pack() 
    sBar=tk.Scrollbar(wiN3)
    sBar.pack(side=tk.RIGHT,fill=tk.Y)
    listBox=tk.Listbox(wiN3, font=("Arial", 20),yscrollcommand=sBar.set,bg="yellow",width=850)
    listBox.pack(side=tk.RIGHT, fill=tk.BOTH)
    sBar.config(command=listBox.yview)
    for iteM in myDict.items():
        listBox.insert(tk.END, iteM)


def _hit4():
    with open("abc.json","w",encoding="utf-8") as filE:
        json.dump(myDict,filE,ensure_ascii=False,indent=4)
    qQ=tk.messagebox.askokcancel("提示","確定要結束程式嗎???")
    if qQ:
        wiN.destroy()




wiN = tk.Tk()

wiN.title("歡迎使用自製英文字典!!!")

wiN.geometry("600x350+250+150")

btN1 = tk.Button(wiN, text="新增/修改單字", font=("Arial", 20), width=20, height=2, command=_hit1,bg="blue",fg="white")
btN2 = tk.Button(wiN, text="查詢/刪除單字", font=("Arial", 20), width=20, height=2, command=_hit2,bg="blue",fg="white")
btN3 = tk.Button(wiN, text="顯示所有單字", font=("Arial", 20), width=20, height=2, command=_hit3,bg="blue",fg="white")
btN4 = tk.Button(wiN, text="結束程式", font=("Arial", 20), width=20, height=2, command=_hit4,bg="red",fg="white")

btN1.pack() 
btN2.pack() 
btN3.pack() 
btN4.pack() 


if os.path.isfile("abc.json"):
    with open("abc.json","r",encoding="utf-8") as filE:
        myDict=json.load(filE)
else:
    myDict={}        



wiN.mainloop()

