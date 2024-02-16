# Conexao do python com o MySQL

!["Imagem Python com MySQL"](https://miro.medium.com/v2/resize:fit:720/format:webp/1*OnDVcS17HTWZ2L2vPaaQ1A.png)

## Drive de comunicação com o mysql 
Para estabelecer a comunicação entre o Python e 
o banco de dados  mysql, iremos usar o seguinte drive:
<a href="https://pypi.org/project/mysql-connector-python/#description"> https://pypi.org/project/mysql-connector-python/#description </a>

### Comando para instalar o drive
```python 
    python -m pip install mysql-connector-python
``` 
### Configuração do banco de dados MySQL
O nosso banco de dados está em um container de docker.
Para acessá-lo será nessesário criar o conteiner, então faremos os seguintes comandos em um servidor Fedora com o docker instalado:

#### Criação do volume 
```shell
mkdir dadosclientes
```

#### Criação do conteiner
<center>
<img src="https://d1.awsstatic.com/acs/characters/Logos/Docker-Logo_Horizontel_279x131.b8a5c41e56b77706656d61080f6a0217a3ba356d.png"height" "100"></center>

```shell 
docker run --name srv-mysql -v ~/dadosclientes:/var/lib/mysql -p 3784:3306 -e MYSQL_ROOT_PASSWORD-SENAC@123 -d mysql

```
# Importando a a biblioteca de conexão com o banco 
# de dados mysql
 
# Vamos adicionar um alias a biblioteca
 
import mysql.connector as mc
 
# Vamos estabelecer a conexao com o banco 
# de dados e para tal, iremos passar os seguintes dados:
# servidor, porta, usuário, senha, banco 
 
conexao = mc.connect(
    host="127.0.0.1",
    port="3784",
    user="root",
    password="SENAC@123",
    database="banco"
)    
 # Estamos c
print(conexao)

#para se movimentar dentro da estrutura de 
# banco de dados e retornar dos dados necessário
# iremos criar um cursor
cursor = conexao.cursor()

# Vamos executar um comando usando  o cursor 
cursor.execute("Create database Ola")

# vamos executar um comando usando o cursor 
# cursor.execute("Create database Ola")

# Vamos selecionar todos os bancos de dados na tabela cliente
cursor.execute("Insert into clientes(nome_cliente,email,telefone)values('Amanda','amanda@oul.com.br','(11)95487-6512')")
print(cursor)
for c in cursor:
    print(f"Id do cliente: {c [0]}")
    print(f"Nome do cliente: {c [1]}")
    print(f"Email: {c [2]}")

   