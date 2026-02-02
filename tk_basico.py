import tkinter as tk


janela = tk.Tk()

janela.title("Minha primeira interface")
janela.geometry("720x380")



def mostrar_nome():
    nome = entrada.get()  # <--- Referencia a entrada que vem depois da função!
    print("Nome digitado:", nome)

entrada = tk.Entry(janela,) # <---- Entry = caixa de texto, usando .get() seria a mesma coisa do imput()
entrada.pack(pady=10) 

botao = tk.Button(janela, text="Enviar", command=mostrar_nome)
botao.pack()

janela.mainloop()