import sqlite3

conexao = sqlite3.connect('banco')
cursor = conexao.cursor()
# 7.Atualização e Remoção com Condições 
# a) Atualize o saldo de um cliente específico.
#cursor.execute('UPDATE clientes SET saldo="2500.00"  WHERE  saldo ="1900" ')
# b) Remova um cliente pelo seu ID.
#cursor.execute('DELETE FROM clientes where id = 3')





conexao.commit()
conexao.close()