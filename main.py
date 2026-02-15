from funcoes import (
    del_data,
    list_users,
    cadastrar,
    atualizar_usuario,
    simple_list
)

print("==========================================")
print("CADASTRO BÁSICO - SCRIPT PYTHON")
print("==========================================")


print("Para cadastrar, insira: 'cadastro'\n")
print("Para ver cadastros já feitos, insira: 'listar'\n")
print("Para atualizar os dados de um usuário, basta digitar 'atualizar'\n")
print("Para deletar algum usuário já cadastro, insira: 'deletar'\n")


lista = input("Sua opção: ")

if lista.startswith('lis'):
    list_users()
    print("\n")
elif lista.startswith('atu'):
    atualizar_usuario()
elif lista.startswith('del'):
    simple_list(),
    print("\nInsira o ID do usuário a ser deletado abaixo")
    deletar = input()
    del_data(deletar)
else:
    cadastrar()

# ===================================LAÇOS=================================================

# num = int(input("Insira um número para criar sua tabuada: "))
# for i in range(1,11):
#     print(f"{num} x {i} = {num*i}")


# num =   int(input("Insira um número para criar sua tabuada: "))
# rg =    int(input("Insira até que número irá o multiplicador da tabuada: "))
# i = 1

# while i <= rg:
#     print(f"{num} x {i} = {num*i}")

#     i += 1

