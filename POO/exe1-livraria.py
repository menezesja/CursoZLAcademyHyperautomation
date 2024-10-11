# Classe Livro
class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True  # Inicia o livro como disponível

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            print(f'O livro "{self.titulo}" foi emprestado.')
        else:
            print(f'O livro "{self.titulo}" não está disponível.')

    def devolver(self):
        if not self.disponivel:
            self.disponivel = True
            print(f'O livro "{self.titulo}" foi devolvido.')
        else:
            print(f'O livro "{self.titulo}" já está disponível na biblioteca.')

    def mostrar_info(self):
        status = "Disponível" if self.disponivel else "Indisponível"
        print(f'Título: {self.titulo}, Autor: {self.autor}, Status: {status}')

class Livraria:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)
        print(f'O livro "{livro.titulo}" foi adicionado à livraria.')

    def emprestar_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo:
                livro.emprestar()
                return
        print(f'O livro "{titulo}" não foi encontrado na livraria.')

    def mostrar_inventario(self):
        print("Inventário da Livraria:")
        for livro in self.livros:
            livro.mostrar_info()

    def devolver_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo:
                livro.devolver()
                return
        print(f'O livro "{titulo}" devolvido.')


livro1 = Livro("Python para Iniciantes", "Autor A")
livro2 = Livro("Automação com Python", "Autor B")

livraria = Livraria()
livraria.adicionar_livro(livro1)
livraria.adicionar_livro(livro2)

livraria.mostrar_inventario()

livraria.emprestar_livro("Python para Iniciantes")
livraria.mostrar_inventario()

livraria.emprestar_livro("Python para Iniciantes")
livraria.devolver_livro("Python para Iniciantes")

livraria.mostrar_inventario()