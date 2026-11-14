#10. Desafio de Atualização Condicional: No sistema de funcionarios, um deles recebeu um
#aumento. Crie um laço for que procure pelo funcionário de ID número 2. Quando encontrá-lo,
#aumente o valor do seu salário em 500. Se encontrar, faça também um print de confirmação
#mostrando seu novo salário. (Dica: como você vai alterar a lista original dentro do for, você precisará
#usar enumerate() ou acessar o elemento original da iteração).

funcionarios = []

funcionarios.append([1, "Pedro", "Vendedor", 2000])
funcionarios.append([2, "Maria", "Gerente", 3000])

for funcionario in funcionarios:
    if funcionario[0] == 2:
        funcionario[3] = funcionario[3] + 500

        print("Aumento realizado!")
        print("Novo salário:", funcionario[3])