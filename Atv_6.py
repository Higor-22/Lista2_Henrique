#6. Busca Simples: Crie uma variável titulo_procurado com o nome de um dos livros. Faça um
#laço for que verifique toda a lista. Se encontrar o título, imprima "Livro localizado!" e interrompa a
#busca.

livros = [
    [1, "Dom Casmurro", "Machado de Assis", 1899],
    [2, "O Hobbit", "J.R.R. Tolkien", 1937],
    [3, "Harry Potter", "J.K. Rowling", 1997]
]

titulo_procurado = "O Hobbit"

for livro in livros:
    if livro[1] == titulo_procurado:
        print("Livro localizado!")
        break