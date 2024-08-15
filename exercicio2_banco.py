import sqlite3

conexao = sqlite3.connect('banco')
cursor = conexao.cursor()

#Insira pelo menos 5 registros de alunos na tabela que você criou no exercício anterior.
#cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(100), idade INT, curso VARCHAR(100));')

cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(1, "João", 20,"Engenharia")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(2, "Maria", 21,"Medicina")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(3, "Pedro", 19,"Direito")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(4, "Ana", 22,"Ciencias da Computação")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(5, "Carlos", 23,"Economia")')






conexao.commit()
conexao.close()