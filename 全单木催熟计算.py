
def positive(x):
    if x<=0:
        x=0
    return x
def P_calculation(ripen_lst,Preripen,frag):
    E=0
    P_Preripen=(1-0.1**Preripen)/2  
    j=i=0
    for i in ripen_lst:
        j+=1
        E=(P_Preripen*(0.55**(j-1)*0.45)*(frag-1)+(1-(frag-1)*P_Preripen)*(0.55**positive(j-2)*0.2025*(j-1)))*int(i)+E  
    return E
def Dph_expectation(T_E,avrheight):
    E=[]
    E.append(1200/T_E)
    E.append(72000*avrheight/T_E)
    return E

import tkinter as tk
ripen=[]
def start_calculation():
    Avrheight = entry1_var.get()
    ripen1 = entry2_var.get()
    ripen2 = entry3_var.get()
    p_ripen = entry4_var.get()
    frag = entry5_var.get()
    ripen0=ripen1.split(" ")
    ripen_=ripen2.split("+")
    frag=int(frag)
    Avrheight=float(Avrheight)
    for i in range(len(ripen0)):
        ripen.append(int(ripen0[i]))
    r=max(ripen)
    for i in range(100):
        for j in range(int(ripen_[0])):
            ripen.append(r+4*(1+i))
        for j in range(int(ripen_[1])):
            ripen.append(r+4*(1+i)+2)
    E_T=P_calculation(ripen,int(p_ripen),frag)
    E=Dph_expectation(E_T,Avrheight)
    result="期望周期："+str(E_T)+"期望效率："+str(E[1])+"期望分钟树数："+str(E[0])
    result_text.config(text=f"计算结果: {result}")
root = tk.Tk()
root.title("trees")

label1 = tk.Label(root, text="输入树的期望高度")
label1.pack()

entry1_var = tk.StringVar()
entry1 = tk.Entry(root, textvariable=entry1_var)
entry1.pack(pady=5)

label2 = tk.Label(root, text="手动输入催熟策略（每次催熟用空格隔开）:")
label2.pack()

entry2_var = tk.StringVar()
entry2 = tk.Entry(root, textvariable=entry2_var)
entry2.pack(pady=5)

label3 = tk.Label(root, text="输入后续催熟策略:")
label3.pack()

entry3_var = tk.StringVar()
entry3 = tk.Entry(root, textvariable=entry3_var)
entry3.pack(pady=5)

label4 = tk.Label(root, text="输入预催熟次数:")
label4.pack()

entry4_var = tk.StringVar()
entry4 = tk.Entry(root, textvariable=entry4_var)
entry4.pack(pady=5)

label5 = tk.Label(root, text="输入树的生长阶段数量:")
label5.pack()

entry5_var = tk.StringVar()
entry5 = tk.Entry(root, textvariable=entry5_var)
entry5.pack(pady=5)
button = tk.Button(root, text="开始计算", command=start_calculation)
button.pack(pady=20)

result_text = tk.Label(root, text=" ")
result_text.pack(pady=10)
root.mainloop()
