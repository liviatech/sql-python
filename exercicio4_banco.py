import sqlite3

conexao = sqlite3.connect('banco')
cursor = conexao.cursor()

# Atualização e Remoção 
# a) Atualize a idade de um aluno específico na tabela.
cursor.execute('UPDATE alunos SET idade = "54" WHERE idade = "20"')

# b)Remova um aluno pelo seu ID. 
cursor.execute('DELETE FROM alunos where id = 3')







conexao.commit()
conexao.close()