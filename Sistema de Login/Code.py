import tkinter as tk # Importa a biblioteca padrão para gerar interface gráfica

def verificar_login():
    usuario = entry_usuario.get()
    senha = entry_senha.get()

    # Verificação de usuário e senha (exemplo simples)
    if usuario == "Usuario" and senha == "123":
        label_resultado["text"] = "Login bem-sucedido!"
    else:
        label_resultado["text"] = "Usuário ou senha incorretos."

# Criando a janela principal
root = tk.Tk()
root.title("Tela de Login")

# Criando os widgets
label_usuario = tk.Label(root, text="Usuário:")
label_usuario.pack()

entry_usuario = tk.Entry(root)
entry_usuario.pack()

label_senha = tk.Label(root, text="Senha:")
label_senha.pack()

entry_senha = tk.Entry(root, show="*")  # 'show' esconde a senha
entry_senha.pack()

botao_login = tk.Button(root, text="Login", command=verificar_login)
botao_login.pack()

label_resultado = tk.Label(root, text="")
label_resultado.pack()

# Iniciar o loop principal da aplicação
root.mainloop()
