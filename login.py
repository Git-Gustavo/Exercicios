import tkinter as tk
from tkinter import messagebox


def fazer_login():
    # Verifica se o nome de usuário e a senha estão corretos
    if ent_usuario.get() == "usuario" and ent_senha.get() == "senha":
        messagebox.showinfo("Sucesso", "Login realizado com sucesso!")
    else:
        messagebox.showerror("Erro", "Nome de usuário ou senha incorretos.")


# Criação da janela
janela = tk.Tk()
janela.title("Painel de Login")
janela.geometry("300x200")

# Criação dos elementos de interface do usuário
lbl_usuario = tk.Label(janela, text="Nome de Usuário:")
lbl_usuario.pack()
ent_usuario = tk.Entry(janela)
ent_usuario.pack()

lbl_senha = tk.Label(janela, text="Senha:")
lbl_senha.pack()
ent_senha = tk.Entry(janela, show="*")  # Usando o show para ocultar a senha
ent_senha.pack()

btn_login = tk.Button(janela, text="Login", command=fazer_login)
btn_login.pack(pady=10)

# Inicia o loop de eventos da interface gráfica
janela.mainloop()
