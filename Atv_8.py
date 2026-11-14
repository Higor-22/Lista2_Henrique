#8. Remoção de Registro: Escolha um ID válido da sua lista de livros e guarde-o na variável
#id_remover. Usando a função enumerate() em um laço for, localize a posição (índice) deste ID
#e utilize o pop(indice) para apagá-lo. Imprima a lista no final para confirmar a remoção.

livros = [
    [1, "Dom Casmurro", "Machado de Assis", 1899],
    [2, "O Hobbit", "J.R.R. Tolkien", 1937],
    [3, "Harry Potter", "J.K. Rowling", 1997]
]

id_remover = 2

for indice, livro in enumerate(livros):
    if livro[0] == id_remover:
        livros.pop(indice)
        print("Livro removido!")
        break

print("Lista depois da remoção:")
print(livros)