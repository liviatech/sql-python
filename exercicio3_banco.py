import sqlite3

conexao = sqlite3.connect('banco')
cursor = conexao.cursor()
#Consultas Básicas: Escreva consultas SQL para realizar as seguintes tarefas:
# a) Selecionar todos os registros da tabela "alunos"
dados = cursor.execute('SELECT * FROM alunos')
for alunos in dados:
     print(alunos)
     
# b) Selecionar o nome e a idade dos alunos com mais de 20 anos.
dados = cursor.execute('SELECT  nome, idade FROM alunos WHERE idade > 20')
for alunos in dados:
     print(alunos)

# c) Selecionar os alunos do curso de "Engenharia" em ordem alfabética.
dados = cursor.execute('SELECT  * FROM alunos ORDER BY nome')
for alunos in dados:
     print(alunos)

# d) Contar o número total de alunos na tabela 
dados = cursor.execute("SELECT COUNT(*) FROM alunos")
for alunos in dados:
      print(alunos)







conexao.commit()
conexao.close()