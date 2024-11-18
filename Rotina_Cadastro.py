import os
from cadastro_clientes import main
import tkinter as tk
from tkinter import messagebox

# Dados iniciais
Restaurantes = [{'Nome': 'Burguer King', 'Tipo': 'Fast Food', 'Status': False},
                {'Nome': 'Pizza Hut', 'Tipo': 'Pizzaria', 'Status': True},
                {'Nome': 'Pizza Hut', 'Tipo': 'Pizzaria', 'Status': False}]

# Funções adaptadas para Tkinter
def cadastrar_restaurante_tk():
    def salvar_cadastro():
        nome = nome_var.get()
        tipo = tipo_var.get()
        if nome and tipo:
            Restaurantes.append({'Nome': nome, 'Tipo': tipo, 'Status': False})
            messagebox.showinfo("Cadastro", f"O restaurante '{nome}' foi cadastrado com sucesso!")
            cadastro_window.destroy()
        else:
            messagebox.showwarning("Erro", "Todos os campos devem ser preenchidos!")

    cadastro_window = tk.Toplevel(root)
    cadastro_window.title("Cadastrar Restaurante")
    
    tk.Label(cadastro_window, text="Nome do Restaurante:").grid(row=0, column=0, padx=10, pady=10)
    nome_var = tk.StringVar()
    tk.Entry(cadastro_window, textvariable=nome_var).grid(row=0, column=1, padx=10, pady=10)
    
    tk.Label(cadastro_window, text="Tipo do Restaurante:").grid(row=1, column=0, padx=10, pady=10)
    tipo_var = tk.StringVar()
    tk.Entry(cadastro_window, textvariable=tipo_var).grid(row=1, column=1, padx=10, pady=10)
    
    tk.Button(cadastro_window, text="Salvar", command=salvar_cadastro).grid(row=2, column=0, columnspan=2, pady=10)

def listar_restaurantes_tk():
    listar_window = tk.Toplevel(root)
    listar_window.title("Listar Restaurantes")
    
    tk.Label(listar_window, text=f"{'Nome'.ljust(20)} | {'Tipo'.ljust(15)} | {'Status'.ljust(10)}", font=("Courier", 10)).pack(pady=5)
    for restaurante in Restaurantes:
        status = "Ativo" if restaurante['Status'] else "Inativo"
        tk.Label(listar_window, text=f"{restaurante['Nome'].ljust(20)} | {restaurante['Tipo'].ljust(15)} | {status.ljust(10)}", font=("Courier", 10)).pack(anchor="w", padx=10)

def alterar_status_tk():
    def alterar_status():
        nome = nome_var.get()
        for restaurante in Restaurantes:
            if restaurante['Nome'] == nome:
                restaurante['Status'] = not restaurante['Status']
                status_atual = "Ativado" if restaurante['Status'] else "Desativado"
                messagebox.showinfo("Status Alterado", f"O restaurante '{nome}' foi {status_atual} com sucesso!")
                status_window.destroy()
                return
        messagebox.showwarning("Erro", "Restaurante não encontrado!")
    
    status_window = tk.Toplevel(root)
    status_window.title("Alterar Status")
    
    tk.Label(status_window, text="Nome do Restaurante:").grid(row=0, column=0, padx=10, pady=10)
    nome_var = tk.StringVar()
    tk.Entry(status_window, textvariable=nome_var).grid(row=0, column=1, padx=10, pady=10)
    
    tk.Button(status_window, text="Alterar", command=alterar_status).grid(row=1, column=0, columnspan=2, pady=10)

def alterar_cadastro_tk():
    def salvar_alteracao():
        nome = nome_var.get()
        campo = campo_var.get()
        novo_valor = novo_valor_var.get()
        for restaurante in Restaurantes:
            if restaurante['Nome'] == nome:
                if campo in restaurante:
                    restaurante[campo] = novo_valor
                    messagebox.showinfo("Alteração", f"Campo '{campo}' do restaurante '{nome}' atualizado com sucesso!")
                    alterar_window.destroy()
                    return
                else:
                    messagebox.showwarning("Erro", f"Campo '{campo}' não encontrado!")
                    return
        messagebox.showwarning("Erro", f"Restaurante '{nome}' não encontrado!")
    
    alterar_window = tk.Toplevel(root)
    alterar_window.title("Alterar Cadastro")
    
    tk.Label(alterar_window, text="Nome do Restaurante:").grid(row=0, column=0, padx=10, pady=10)
    nome_var = tk.StringVar()
    tk.Entry(alterar_window, textvariable=nome_var).grid(row=0, column=1, padx=10, pady=10)
    
    tk.Label(alterar_window, text="Campo a Alterar:").grid(row=1, column=0, padx=10, pady=10)
    campo_var = tk.StringVar()
    tk.Entry(alterar_window, textvariable=campo_var).grid(row=1, column=1, padx=10, pady=10)
    
    tk.Label(alterar_window, text="Novo Valor:").grid(row=2, column=0, padx=10, pady=10)
    novo_valor_var = tk.StringVar()
    tk.Entry(alterar_window, textvariable=novo_valor_var).grid(row=2, column=1, padx=10, pady=10)
    
    tk.Button(alterar_window, text="Salvar", command=salvar_alteracao).grid(row=3, column=0, columnspan=2, pady=10)

# Configuração da Interface Principal
root = tk.Tk()
root.title("Gerenciador de Restaurantes")

tk.Label(root, text="Gerenciador de Restaurantes", font=("Arial", 16, "bold")).pack(pady=10)

tk.Button(root, text="Cadastrar Restaurante", command=cadastrar_restaurante_tk).pack(pady=5, fill="x", padx=20)
tk.Button(root, text="Listar Restaurantes", command=listar_restaurantes_tk).pack(pady=5, fill="x", padx=20)
tk.Button(root, text="Ativar/Desativar Restaurante", command=alterar_status_tk).pack(pady=5, fill="x", padx=20)
tk.Button(root, text="Alterar Cadastro", command=alterar_cadastro_tk).pack(pady=5, fill="x", padx=20)
tk.Button(root, text="Sair", command=root.quit).pack(pady=5, fill="x", padx=20)

root.mainloop()

if __name__ == '__main__':
    main()
