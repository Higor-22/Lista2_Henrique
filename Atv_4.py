#4. Iteração e f-strings: Crie um laço for para percorrer a lista de livros. Para cada linha, exiba uma
#frase usando f-strings no seguinte formato:
#ID: 1 | O livro "Título" foi escrito por Autor em Ano.

livros = [
    [1, "Dom Casmurro", "Machado de Assis", 1899],
    [2, "O Hobbit", "J.R.R. Tolkien", 1937],
    [3, "Harry Potter", "J.K. Rowling", 1997]
]

for livro in livros:
    print(f"ID: {livro[0]} | O livro {livro[1]} foi escrito por {livro[2]} em {livro[3]}.")