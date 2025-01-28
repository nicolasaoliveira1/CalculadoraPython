import tkinter as tk

ultimo_operador = False
tem_ponto = False

def inserirNumero(num):
    global ultimo_operador, tem_ponto

    if entrada_var.get() == "Erro":
        limparCampo()

    texto_atual = entrada_var.get()

    if texto_atual == "" and num == ".":
        return  

    if texto_atual != "" and texto_atual[-1] in "+-×÷":
        
        if num == "0" and texto_atual[-2:] != "0":  
            entrada_var.set(texto_atual + num)
            return
        if num == "0":  
            return

  
    if num == ".":
        
        if tem_ponto:
            return  
        tem_ponto = True  
        
        if texto_atual == "" or texto_atual[-1] in "+-×÷":
            entrada_var.set(texto_atual + "0.")
        else:
            entrada_var.set(texto_atual + num)
        return

    
    if texto_atual == "0" and num == "0":
        return
    
    if texto_atual == "0" and num != ".":
        entrada_var.set(num)
        tem_ponto = False
    else:
        
        if ultimo_operador:
            tem_ponto = False

        entrada_var.set(texto_atual + num)

    ultimo_operador = False

def inserirOperador(op):
    global ultimo_operador, tem_ponto

    if entrada_var.get() == "Erro":
        limparCampo()

    texto_atual = entrada_var.get()

    if texto_atual != "" and not ultimo_operador:
        entrada_var.set(texto_atual + op)
        ultimo_operador = True

def limparCampo():
    global tem_ponto
    entrada_var.set("")
    tem_ponto = False  

def apagarUltimo():
    global tem_ponto
    texto_atual = entrada_var.get()

    if texto_atual == "Erro":
        limparCampo()
        return
    
    if texto_atual.endswith("."):
        tem_ponto = False  

    entrada_var.set(texto_atual[:-1])

def calcularResultado():
    texto_atual = entrada_var.get()
    if texto_atual == "":
        return
    
    try:
        expressao = entrada_var.get()
        expressao = expressao.replace("×", "*").replace("÷", "/")  
        expressao = expressao.replace(",", ".")  
        resultado = eval(expressao)  # calcula a expressão
        entrada_var.set(str(resultado))  
    except Exception as e:
        entrada_var.set("Erro")
        print(f"Erro ao calcular: {e}")

# Interface gráfica permanece a mesma
janela = tk.Tk()
janela.title("Calculadora Python")
janela.geometry("500x700")
janela.configure(background="#213738")
janela.resizable(False, False)

for i in range(4):
    janela.grid_columnconfigure(i, weight=1)

entrada_var = tk.StringVar()

entrada = tk.Entry(janela, font=("Arial", 36), justify="right", textvariable=entrada_var, state="readonly", bg="#213738", fg="white", readonlybackground="#213738", borderwidth=0, highlightthickness=0)
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="ew")

botoes = [
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2),
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2),
    (".", 5, 2)
]

operacoes = [
    ("÷", 1, 3), ("×", 2, 3), ("+", 3, 3), ("-", 4, 3)  
]

for (texto, linha, coluna) in botoes:
    tk.Button(janela, borderwidth=0.5, text=texto, font=("Arial", 18), command=lambda t=texto: inserirNumero(t)).grid(row=linha, column=coluna, padx=0, pady=0, sticky="nsew")
tk.Button(janela, borderwidth=0.5, text="0", font=("Arial", 18), command=lambda: inserirNumero("0")).grid(row=5, column=0, columnspan=2, padx=0, pady=0, sticky="nsew")

for (texto, linha, coluna) in operacoes:
    tk.Button(janela, borderwidth=0.5, highlightthickness=0, text=texto, font=("Arial", 18), bg= "#e87a2c", command=lambda t=texto: inserirOperador(t)).grid(row=linha, column=coluna, padx=0, pady=0, sticky="nsew")

tk.Button(janela, borderwidth=0.5, text="C", font=("Arial", 18), command=limparCampo).grid(row=1, column=0, columnspan=2, padx=0, pady=0, sticky="nsew")
tk.Button(janela, borderwidth=0.5, text="⌫", font=("Arial", 18), command=apagarUltimo).grid(row=1, column=2, padx=0, pady=0, sticky="nsew")
tk.Button(janela, borderwidth=0.5, text="=", font=("Arial", 18), bg= "#e87a2c", command=calcularResultado).grid(row=5, column=3, padx=0, pady=0, sticky="nsew")

for i in range(6):
    janela.grid_rowconfigure(i, weight=1)

janela.mainloop()
