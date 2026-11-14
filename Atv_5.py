#5. Alteração Direta: Suponha que o ano de lançamento do primeiro livro foi cadastrado errado. Sem
#recriar a lista inteira, acesse os índices correspondentes e altere o ano de lançamento desse registro
#para 2024.

livros = [
    [1, "Dom Casmurro", "Machado de Assis", 1899],
    [2, "O Hobbit", "J.R.R. Tolkien", 1937],
    [3, "Harry Potter", "J.K. Rowling", 1997]
]

livros[0][3] = 2024

print(livros)