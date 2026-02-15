import sqlite3

#---------------------
#
# FUNÇÕES
#
#---------------------

def cadastrar():
    print("Bem vindo(a)! Vamos realizar o seu cadastro em nosso sistema. Basta seguir as informações.\n")
    nome = input(f"Primeiro, insira seu nome: ").capitalize().strip()

    while True:
        try:
            idade = int(input(f"Excelente {nome}, agora insira a sua idade: ")) 
            break
        except ValueError:
            print("Insira somente números para a idade.")

    if idade >= 18:
        print(f"{nome}, você tem {idade} anos e é maior de idade. Vamos prosseguir com o seu cadastro")
    else:   
        tempo = 18 - idade
        print(f"{nome}, você é de menor. Não podemos prosseguir. Espere {tempo} ano(s) para se recadastrar.")
        exit()
    print("========================================")

    print("Sistema de Cadastro - Python Lessons")

    print("========================================")

    while True:
        att = input("Como gostaria de ser chamado? (Sr. ou Sra.) ").strip().lower()
        
        if att in ['sr', 'sra']:
            att = 'Sr.' if att == 'sr' else 'Sra.'
            break
        print("Por favor, preencha com sr. ou sra.")

    sobrenome = input("Insira o seu sobrenome: ").capitalize().strip()

    genero  =   'masculino' if  att ==  'Sr.'   else    'feminino'


    profissao = input("Insira a sua profissão: ").title()

    print("========================================")
    print("Cadastro Finalizado Com Sucesso!")
    print("========================================\n")
    
    quest = input("Deseja salvar os dados? (s/n)")
    if quest.startswith('s'):
        save_data(att, nome, sobrenome, idade, genero, profissao)
    else: 
        print("Dados experimentais não salvos.")

def save_data(tratamento, nome, sobrenome, idade, genero, profissao):
    conn = sqlite3.connect("portfolio2.db")
    cursor = conn.cursor()

    query = ("""
             INSERT INTO usuarios(tratamento, nome, sobrenome, idade, genero, profissao)
             VALUES(?, ?, ?, ?, ?, ?);
             """)
    
    cursor.execute(query, (tratamento, nome, sobrenome, idade, genero, profissao))

    conn.commit()
    conn.close()

    print("Excelente!\n")

    print("Gostaria de ver os usuários já cadastrados? (s/n)")
    r = input()
    if r.startswith('s'):
        list_users()
        
    else: 
        print("Ok! Até a próxima.")       

def del_data(id):
    conn = sqlite3.connect('portfolio2.db')
    cursor = conn.cursor()

    query = """
        DELETE FROM usuarios WHERE id = ? 
    """
    
    cursor.execute(query, [id])
    conn.commit()                           


    if cursor.rowcount == 0:                   
        print("ID não encontrado! Verifique novamnete!")
    else:
        print(f"Usuário com o ID {id}, apagado com sucesso!!")

    conn.close()        # quem dá commit e close é a conexão, não o cursor. CURSOR só executa.

def list_users():
    conn = sqlite3.connect('portfolio2.db')
    cursor = conn.cursor()

    query1 = """ SELECT COUNT(*) FROM usuarios  """
    cursor.execute(query1)
    total = cursor.fetchone ()[0]
    print(f"{total} cadastros")
    print("-----------------------------------")
    
    query2 = """ SELECT * FROM usuarios  """
    cursor.execute(query2)
    user_list = cursor.fetchall()

    conn.close()

    if not user_list:
        print("Nenhum usuário cadastrado!")
    else:
        print(f"\n============ Lista ============\n")
        for user in user_list:
            print("--------------------")
            print(f"ID: {user[0]:2}")
            print(f"Tratamento: {user[1]}")
            print(f"Nome: {user[2]}")
            print(f"Sobrenome: {user[3]}")
            print(f"Idade: {user[4]} anos")
            print(f"Gênero: {user[5]}")
            print(f"Profissão: {user[6]}")

def simple_list():
    conn = sqlite3.connect('portfolio2.db')
    cursor = conn.cursor()

    query="""
    SELECT id, nome, sobrenome FROM usuarios
"""
    cursor.execute(query)
    user_list = cursor.fetchall()
    for user_id, nome, ult_nome in user_list:
        print(f"ID: {user_id} | Nome: {nome} {ult_nome}")

    conn.close()