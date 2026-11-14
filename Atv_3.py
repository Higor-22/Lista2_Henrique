#3. Acesso a Índices: Usando a lista livros criada no exercício anterior, faça um print() que
#mostre exclusivamente o nome do autor do segundo livro cadastrado.

livros = [
    [1, "Dom Casmurro", "Machado de Assis", 1899],
    [2, "O Hobbit", "J.R.R. Tolkien", 1937],
    [3, "Harry Potter", "J.K. Rowling", 1997]
]

autor = livros[1][2]

print("Autor do segundo livro:", autor)