import mysql.connector
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

#Conexão com o servidor

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="batata",
    database="teste",
)
mydb = conexao.cursor()

# CRUD

class Galpao:
    def __init__(self,id, nome,qnt,descricao):
        self.id = id
        self.nome = nome
        self.qnt = qnt
        self.descricao = descricao

    if conexao.is_connected():
        messagebox.showinfo(title="Galpao", message="Conexão online")

    def create():

        nome = entrada.get()
        if len(nome) != 0:
            qnt = 0
            mydb.execute("INSERT INTO galpao (produtos_nome, produtos_qnt) VALUES (%s, %s)" , (nome,qnt))
            conexao.commit()
            entrada.delete(0,"end")
            Galpao.read()
        else:
            messagebox.showinfo(title="Galpao", message="Nome do produto não pode ficar em branco.")

    def alt_desc():

        descricao = entrada.get()
        if len(descricao) != 0:
            id = tree.item(tree.focus(),"values")[0]
            mydb.execute("UPDATE galpao SET produtos_desc = %s WHERE idgalpao = %s", (descricao, id) )
            conexao.commit()
            entrada.delete(0,"end")
            Galpao.read()
            messagebox.showinfo(title="Galpao", message="Descrição alterada com sucesso!")

    def read():

        for i in tree.get_children():
            tree.delete(i)
        mydb.execute("SELECT * FROM galpao")
        for resultado in mydb:
            tree.insert("", "end",values=resultado)

    def update():

        quantidade = entrada.get()
        if quantidade.lstrip("-").isnumeric():
            qnt_mydb = tree.item(tree.focus(),"values")[2]
            if (int(quantidade) + int(qnt_mydb)) >= 0:
                quantidade = str(int(quantidade)+int(qnt_mydb))
                id = tree.item(tree.focus(),"values")[0]
                mydb.execute("UPDATE galpao SET produtos_qnt = %s WHERE idgalpao = %s", (quantidade, id) )
                conexao.commit()
                entrada.delete(0,"end")
                Galpao.read()
            else:
                messagebox.showinfo(title="Galpao", message="Não existem items o suficiente no Galpão para esta retirada.")
                entrada.delete(0,"end")
        else:
             messagebox.showinfo(title="Galpao", message="Para operar entrada e saída de produtos deve ser informado um número.")
             entrada.delete(0,"end")

    def delete():

        pergunta = messagebox.askyesno(title="Galpão",message="Esta ação vai apagar a linha do banco de dados. Gostaria de prosseguir?")
        if pergunta == True:
            id = tree.item(tree.focus(),"values")[0]
            mydb.execute(f"DELETE FROM galpao WHERE idgalpao = {id}")
            conexao.commit()
            Galpao.read()

#Iniciando a janela de interface

janela = Tk()
janela.title("Gerenciamento Galpão")
janela.geometry("670x370")
janela.configure(bg="#ececec")

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0,columnspan=1,ipadx=272)

style = ttk.Style(janela)
style.theme_use("clam")

janela.after(1, lambda: janela.focus_force())

#Inserindo os elementos para interação

tree = ttk.Treeview(janela, columns=("0","1","2","3"),show="headings")
tree.heading("0", text="ID")
tree.column("0",anchor="center", stretch="no", width=30)
tree.heading("1", text="Nome do Produto")
tree.column("1",anchor="center", stretch="no", width=200)
tree.heading("2", text="Qnt")
tree.column("2",anchor="center", stretch="no", width=50)
tree.heading("3", text="Descrição")
tree.column("3", stretch="no", width=320)
tree.place(x=30,y=100)

entrada = Entry(janela, width=100)
entrada.focus_set()
entrada.place(x=30, y=70)

b_create = Button(janela, text="Novo Produto", command = Galpao.create, relief="raised", overrelief=RIDGE, anchor=NW, font=("Verdana 12"), bg="#D3D4D3", fg="#080808")
b_create.place(x=30,y=20)

b_alt_desc = Button(janela, text="Alterar Descrição", command = Galpao.alt_desc, relief="raised", overrelief=RIDGE, anchor=NW, font=("Verdana 12"), bg="#D3D4D3", fg="#080808")
b_alt_desc.place(x=170,y=20)

b_update = Button(janela, text="Entrada/Saída", command = Galpao.update, relief="raised", overrelief=RIDGE, anchor=NW, font=("Verdana 12"), bg="#D3D4D3", fg="#080808")
b_update.place(x=340,y=20)

b_delete = Button(janela, text="Deletar Produto", command = Galpao.delete, relief="raised", overrelief=RIDGE, anchor=NW, font=("Verdana 12"), bg="#D3D4D3", fg="#080808")
b_delete.place(x=490,y=20)

Galpao.read()

janela.mainloop()

mydb.close()
conexao.close()