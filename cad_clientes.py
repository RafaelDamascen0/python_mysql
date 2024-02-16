import mysql.connector as mc

# estabelecer a conexao com o banco 
cx = mc.connect(
    host="127.0.0.1",
    port="3784",
    user="root",
    password="SENAC@123",
    database="banco"
)
# verificar  se a conexao foi estabelecida 
print(cx)

#criação de variáveis para o usuário para os dados do cliente
# para cadastrar
nome = input("Digite o nome do cliente: ")
email = input("Digite o email do cliente: ")
telefone = input("Digite o telefone do cliente: ")

cursor = cx.cursor()
cursor.execute("insert into clientes(nome_cliente,email,telefone)values('"+nome+"','"+email+"','"+telefone+"')")
# confirmar a inserção dos dados na tabela
cx.commit()