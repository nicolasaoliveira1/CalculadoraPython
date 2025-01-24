import tkinter as tk

ultimo_operador = False
tem_ponto = False

def inserirNumero(num):
    global ultimo_operador, tem_ponto

    if entrada_var.get() == "Erro":
        limparCampo()

    texto_atual = entrada_var.get()

    # Impede adicionar ponto quando a entrada está vazia
    if texto_atual == "" and num == ".":
        return  

    # Verifica se o zero está sendo adicionado após um operador
    if texto_atual != "" and texto_atual[-1] in "+-×÷":
        # Permite apenas um único zero após o operador
        if num == "0" and texto_atual[-2:] != "0":  # Permite um zero após o operador
            entrada_var.set(texto_atual + num)
            return
        elif num == "0":  # Bloqueia múltiplos zeros após o operador
            return

    # Impede adicionar múltiplos pontos
    if num == ".":
        # Verifica se já existe um ponto no número atual
        if tem_ponto:
            return  # Se já existe um ponto, não permite adicionar outro
        tem_ponto = True  # Marca que o número atual agora tem um ponto
        # Se o número estiver vazio ou acabar em um operador, insere "0."
        if texto_atual == "" or texto_atual[-1] in "+-×÷":
            entrada_var.set(texto_atual + "0.")
        else:
            entrada_var.set(texto_atual + num)
        return

    # Permite apenas um zero inicial se for o primeiro número e não for seguido por ponto
    if texto_atual == "0" and num == "0":
        return

    # Substitui o zero inicial por outro número se não for um número decimal
    if texto_atual == "0" and num != ".":
        entrada_var.set(num)
        tem_ponto = False
    else:
        # Reseta o ponto quando um operador foi o último caractere inserido
        if ultimo_operador:
            tem_ponto = False

        entrada_var.set(texto_atual + num)

    ultimo_operador = False  # Quando um número é inserido, o último operador é "resetado"


def inserirOperador(op):
    global ultimo_operador, tem_ponto

    if entrada_var.get() == "Erro":
        limparCampo()

    texto_atual = entrada_var.get()

    # Permite inserir um operador apenas se não houver outro operador consecutivo
    if texto_atual != "" and not ultimo_operador:
        entrada_var.set(texto_atual + op)
        ultimo_operador = True

def limparCampo():
    global tem_ponto
    entrada_var.set("")
    tem_ponto = False  # Reseta a condição do ponto ao limpar o campo

def apagarUltimo():
    global tem_ponto
    texto_atual = entrada_var.get()

    if texto_atual == "Erro":
        limparCampo()
        return
    
    if texto_atual.endswith("."):
        tem_ponto = False  # Se o ponto for apagado, atualiza a flag

    entrada_var.set(texto_atual[:-1])

def calcularResultado():
    texto_atual = entrada_var.get()
    if texto_atual == "":
        return
    
    try:
        expressao = entrada_var.get()
        expressao = expressao.replace("×", "*").replace("÷", "/")  # Corrige os sinais
        expressao = expressao.replace(",", ".")  # Substitui vírgula por ponto
        resultado = eval(expressao)  # Calcula a expressão
        entrada_var.set(str(resultado))  # Exibe o resultado
    except Exception as e:
        entrada_var.set("Erro")
        print(f"Erro ao calcular: {e}")

# Interface gráfica permanece a mesma
janela = tk.Tk()
janela.title("Calculadora Python")
janela.geometry("590x800")
janela.resizable(False, False)

for i in range(4):
    janela.grid_columnconfigure(i, weight=1)

entrada_var = tk.StringVar()

entrada = tk.Entry(janela, font=("Arial", 36), justify="right", textvariable=entrada_var, state="readonly")
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
    tk.Button(janela, text=texto, font=("Arial", 18), command=lambda t=texto: inserirNumero(t)).grid(row=linha, column=coluna, padx=2, pady=2, sticky="nsew")
tk.Button(janela, text="0", font=("Arial", 18), command=lambda: inserirNumero("0")).grid(row=5, column=0, columnspan=2, padx=2, pady=2, sticky="nsew")

for (texto, linha, coluna) in operacoes:
    tk.Button(janela, text=texto, font=("Arial", 18), command=lambda t=texto: inserirOperador(t)).grid(row=linha, column=coluna, padx=2, pady=2, sticky="nsew")

tk.Button(janela, text="C", font=("Arial", 18), command=limparCampo).grid(row=1, column=0, columnspan=2, padx=2, pady=2, sticky="nsew")
tk.Button(janela, text="⌫", font=("Arial", 18), command=apagarUltimo).grid(row=1, column=2, padx=2, pady=2, sticky="nsew")
tk.Button(janela, text="=", font=("Arial", 18), command=calcularResultado).grid(row=5, column=3, padx=2, pady=2, sticky="nsew")

for i in range(6):
    janela.grid_rowconfigure(i, weight=1)

janela.mainloop()
