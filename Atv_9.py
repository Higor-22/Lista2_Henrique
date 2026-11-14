#9. Operações Combinadas (Cadastro): Vamos criar um novo sistema para funcionarios
#contendo: ID, Nome, Cargo e Salário. Inicialize a lista vazia (funcionarios = []). Use append()
#para adicionar duas novas linhas (listas internas) de funcionários e logo após, imprima os registros
#usando um laço de repetição.

funcionarios = []

funcionarios.append([1, "João", "Vendedor", 2000])
funcionarios.append([2, "Maria", "Gerente", 3000])

for funcionario in funcionarios:
    print(funcionario)