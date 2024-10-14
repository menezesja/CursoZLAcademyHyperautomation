class Livro:
    def __init__(self, titulo, autor):
        self._titulo = titulo
        self._autor = autor
        self.disponivel = True  

    # Getter para o título
    @property
    def titulo(self):
        return self._titulo

    # Setter para o título
    @titulo.setter
    def titulo(self, titulo):
        self._titulo = titulo

    # Getter para o autor
    @property
    def autor(self):
        return self._autor

    # Setter para o autor
    @autor.setter
    def autor(self, autor):
        self._autor = autor

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


class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)
        print(f'O livro "{livro.titulo}" foi adicionado à biblioteca.')

    def emprestar_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo:
                livro.emprestar()
                return
        print(f'O livro "{titulo}" não foi encontrado na biblioteca.')

    def devolver_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo:
                livro.devolver()
                return
        print(f'O livro "{titulo}" não foi encontrado na biblioteca.')

    def mostrar_inventario(self):
        print("Inventário da Biblioteca:")
        for livro in self.livros:
            livro.mostrar_info()
        print('-' * 70)

livro1 = Livro("Python para Iniciantes", "Autor Maria")
livro2 = Livro("Automação com Python", "Autor João")

biblioteca = Biblioteca()
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)

biblioteca.mostrar_inventario()

biblioteca.emprestar_livro("Python para Iniciantes")
biblioteca.mostrar_inventario()

biblioteca.devolver_livro("Python para Iniciantes")
biblioteca.mostrar_inventario()
