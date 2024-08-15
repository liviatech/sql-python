import sqlite3

conexao = sqlite3.connect('banco')
cursor = conexao.cursor()

# cursor.execute('CREATE TABLE usuarios(id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR(100));')

# cursor.execute('ALTER TABLE usuarios RENAME TO usuario ')

# cursor.execute('ALTER TABLE usuario ADD COLUMN telefoni INT')

# cursor.execute('ALTER TABLE  usuario RENAME COLUMN telefoni TO telephone')

# cursor.execute('CREATE TABLE produtos(id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR(100));')

# cursor.execute('DROP TABLE  produtos')

# cursor.execute('INSERT INTO usuario(id, nome, endereco, email, telefone) VALUES(1, "Isadora", "França","isddll@gmail.com", 123456)')
# cursor.execute('INSERT INTO usuario(id, nome, endereco, email, telefone) VALUES(2, "Maria", "França","isddll@gmail.com", 123456)')
# cursor.execute('INSERT INTO usuario(id, nome, endereco, email, telefone) VALUES(3, "Orlando", "França","isddll@gmail.com", 123456)')
# cursor.execute('INSERT INTO usuario(id, nome, endereco, email, telefone) VALUES(4, "Queiroz", "França","isddll@gmail.com", 123456)')

# cursor.execute('DELETE FROM usuario where id = 1')

# visualizar = cursor.execute('SELECT * FROM  usuario') 
# for  usuario in visualizar: 
#     print (usuario)

# visualizar = cursor.execute('SELECT nome, telefone FROM  usuario') 
# for  usuario in visualizar: 
#     print (usuario)

# visualizar = cursor.execute('SELECT nome usuario FROM  usuario WHERE id >=2') 
# for  usuario in visualizar: 
#     print (usuario)

# cursor.execute('UPDATE usuario SET telefone = "987654" WHERE nome = "Maria"')

# visualizar = cursor.execute('SELECT * FROM  usuario ORDER BY nome') 
# for  usuario in visualizar: 
#     print (usuario)

# visualizar = cursor.execute('SELECT * FROM  usuario ORDER BY nome DESC') 
# for  usuario in visualizar: 
#     print (usuario)


# visualizar = cursor.execute('SELECT * FROM  usuario LIMIT 2') 
# for  usuario in visualizar: 
#     print (usuario)

# visualizar = cursor.execute('SELECT DISTINCT * FROM  usuario LIMIT 2') 
# for  usuario in visualizar: 
#     print (usuario)

# COMANDOS JOIN : INNER JOIN, LEFT JOIN, RIGHT JOIN, FULL JOIN.

# SUB-CONSULTAS : SUB-QUERYS, OU SUB-SELECT são consultas aninhadas




conexao.commit()
conexao.close