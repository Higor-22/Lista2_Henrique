#7. Tratamento de "Não Encontrado": Modifique a busca do exercício anterior. Defina uma variável
#id_procurado = 99. Faça a busca por esse ID. Use uma variável de controle (booleana) para que
#o programa consiga imprimir a mensagem "Livro não encontrado" caso o ID não exista na lista.

livros = [
    [1, "Dom Casmurro", "Machado de Assis", 1899],
    [2, "O Hobbit", "J.R.R. Tolkien", 1937],
    [3, "Harry Potter", "J.K. Rowling", 1997]
]

id_procurado = 99
encontrado = False

for livro in livros:
    if livro[0] == id_procurado:
        print("Livro encontrado!")
        encontrado = True
        break

if encontrado == False:
    print("Livro não encontrado")