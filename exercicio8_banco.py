import sqlite3

conexao = sqlite3.connect('banco')
cursor = conexao.cursor()
# 8.Junção de Tabelas - Crie uma segunda tabela chamada "compras" com os campos: id(chave primária), cliente_id(chave estrangeira referenciando o id da tabela "clientes"), produto(texto) e valor(real).Insira algumas compras associadas a clientes existentes na tabela "clientes". Escreva uma consulta para exibir o nome do cliente,o produto e o valor de cada compra


# cursor.execute(' CREATE TABLE compras ( id INT PRIMARY KEY,  cliente_id INT, produto VARCHAR(100),  valor REAL, FOREIGN KEY (cliente_id) REFERENCES clientes(id)) ')
#cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES(1, 1, "chocolate", 12.34)')
# cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES(2, 2, "chá", 2.00)')
# cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES(3, 3, "arroz", 21.34)')
# cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES(4, 4, "milho", 5.34)')

dados = cursor.execute('SELECT * FROM clientes INNER JOIN compras ON clientes.id = compras.cliente_id')
for clientes in dados:
    print(clientes)
 
conexao.commit()
conexao.close()