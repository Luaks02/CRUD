import mysql.connector
from tkinter import *
from tkinter import ttk

#Conexão com o servidor

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="batata",
    database="teste",
)
mydb = conexao.cursor()

# CRUD

# CREATE

def create():
    nome = entrada.get()
    qnt = 0
    mydb.execute("INSERT INTO galpao (produtos_nome, produtos_qnt) VALUES (%s, %s)" , (nome,qnt))
    conexao.commit()
    entrada.delete(0,"end")

# READ

def read():

    mydb.execute("SELECT * FROM galpao")
    tree = ttk.Treeview(janela, columns=("ID","Nome_Produto","Qnt","Descrição"),show="headings")
    tree.heading("ID", text="ID")
    tree.column("ID",anchor="center", stretch="no", width=30)
    tree.heading("Nome_Produto", text="Nome do Produto")
    tree.column("Nome_Produto",anchor="center", stretch="no", width=200)
    tree.heading("Qnt", text="Qnt")
    tree.column("Qnt",anchor="center", stretch="no", width=50)
    tree.heading("Descrição", text="Descrição")
    tree.column("Descrição", stretch="no", width=400)
    for resultado in mydb:
        tree.insert("", "end",values=resultado)
    tree.place(x=30,y=100)


# UPDATE

def update():

    mydb.execute("UPDATE galpao SET produtos_qnt = %s WHERE produtos_nome = %s", (quantidade, nome) )
    conexao.commit()

# DELETE

def delete():

    mydb.execute(f"DELETE FROM galpao WHERE idgalpao = {id}")
    conexao.commit()

#Iniciando a janela de interface

janela = Tk()
janela.title("Gerenciamento Galpão")
janela.geometry("800x400")
janela.configure(bg="#ececec")

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0,columnspan=1,ipadx=272)

style = ttk.Style(janela)
style.theme_use("clam")

#Inserindo os botões para interação

entrada = Entry(janela, width=100)
entrada.focus_set()
entrada.place(x=30, y=70)

b_create = Button(janela, text="Novo Produto", command = create, relief="raised", overrelief=RIDGE, anchor=NW, font=("Verdana 12"), bg="#D3D4D3", fg="#080808")
b_create.place(x=30,y=20)

b_read = Button(janela, text="Listar Produtos", command = read, relief="raised", overrelief=RIDGE, anchor=NW, font=("Verdana 12"), bg="#D3D4D3", fg="#080808")
b_read.place(x=180,y=20)

b_update = Button(janela, text="Entrada/Saída",relief="raised", overrelief=RIDGE, anchor=NW, font=("Verdana 12"), bg="#D3D4D3", fg="#080808")
b_update.place(x=340,y=20)

b_delete = Button(janela, text="Deletar Produto",relief="raised", overrelief=RIDGE, anchor=NW, font=("Verdana 12"), bg="#D3D4D3", fg="#080808")
b_delete.place(x=490,y=20)

janela.mainloop()

mydb.close()
conexao.close()