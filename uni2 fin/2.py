livros = []

def cadastrar_livro(titulo,autor,ano,genero,disponibilidade):
    for livro in livros:
        if livro['titulo'] == autor and livro['autor'] == autor:
           livro['autor'] = autor
           livro['ano'] = ano
           livro['genero'] = genero
           livro['disponibilidade'] = disponibilidade
           return livro
    novo_livro = {
        'titulo':titulo,
        'autor':autor,
        'ano':ano,
        'genero':genero,
        'disponibilidade':disponibilidade,
        'emprestimos': 0
    }
    livros.append(novo_livro)
    return novo_livro



def consultar_livro(titulo=None, autor=None,ano=None):
    resultados = []
    for livro in livros:
        if (titulo is None or livro['titulo'] == titulo) and \
           (autor is None or livro['autor'] == autor) and \
           (ano is None or livro['ano'] == ano):
            resultados.append(livro)
    return resultados

def emprestimo_de_livro(titulo):
    for livro in livros:
        if livro['titulo'] == titulo and livro['disponibilidade'] == True:
            livro['disponibilidade'] = False
            livro['emprestimos'] += 1
            print("Emprestimo feito com sucesso")
            return livro
    print("livro nao indentificado")

def devolver_livro(titulo):
    for livro in livros:
        if livro['titulo'] == titulo and livro['disponibilidade'] == False:
            livro['disponibilidade'] = True
            print("Livro devolcido com sucesso")
            return livro
    print("livro nao indentificado")


def gerar_relatorio():
    total_livros = len(livros)
    livros_disponiveis = sum(1 for livro in livros if livro['disponibilidade'])
    livros_emprestados = total_livros - livros_disponiveis

    # Ordena os livros por número de empréstimos, em ordem decrescente
    livros_ordenados = sorted(livros, key=lambda x: x['emprestimos'], reverse=True)
    livros_mais_emprestados = livros_ordenados[:5]  # Pega os 5 livros mais emprestados

    print(f"Quantidade total de livros: {total_livros}")
    print(f"Quantidade de livros disponíveis: {livros_disponiveis}")
    print(f"Quantidade de livros emprestados: {livros_emprestados}")

    print("Livros mais emprestados:")
    for livro in livros_mais_emprestados:
        print(f"{livro['titulo']} (Empréstimos: {livro['emprestimos']})")




cadastrar_livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1954, "Fantasia", True)
cadastrar_livro("1984", "George Orwell", 1949, "Distopia", False)
cadastrar_livro("A Revolta dos Bichos", "George Orwell", 1945, "Distopia", False)
cadastrar_livro("Dom Casmurro", "Machado de Assis", 1899, "Literatura Brasileira", False)
cadastrar_livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943, "Infantil", True)

# Testar o empréstimo de alguns livros
emprestimo_de_livro("1984")
emprestimo_de_livro("O Pequeno Príncipe")
emprestimo_de_livro("O Pequeno Príncipe")

# Gerar o relatório
gerar_relatorio()