import json
import csv
import pickle
from functools import reduce

# Classe Livro, representando os atributos principais de um livro
class Livro:
    def __init__(self, titulo, autor, ano, genero):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.genero = genero

    def __repr__(self):
        return f"Livro(titulo='{self.titulo}', autor='{self.autor}', ano={self.ano}, genero='{self.genero}')"

# Classe Biblioteca, gerenciando uma coleção de livros
class Biblioteca:
    def __init__(self):
        self.livros = []

    # Adicionar livro à biblioteca
    def adicionar_livro(self, livro):
        self.livros.append(livro)

    # Listar livros por autor
    def listar_livros_por_autor(self, autor):
        return list(filter(lambda livro: livro.autor == autor, self.livros))

    # Exportar dados em formato texto
    def exportar_texto(self, arquivo):
        with open(arquivo, 'w') as f:
            for livro in self.livros:
                f.write(f"{livro.titulo},{livro.autor},{livro.ano},{livro.genero}\n")

    # Exportar dados em formato JSON
    def exportar_json(self, arquivo):
        with open(arquivo, 'w') as f:
            json.dump([livro.__dict__ for livro in self.livros], f)

    # Exportar dados em formato CSV
    def exportar_csv(self, arquivo):
        with open(arquivo, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['titulo', 'autor', 'ano', 'genero'])
            for livro in self.livros:
                writer.writerow([livro.titulo, livro.autor, livro.ano, livro.genero])

    # Exportar dados em formato binário com pickle
    def exportar_binario(self, arquivo):
        with open(arquivo, 'wb') as f:
            pickle.dump(self.livros, f)

    # Importar dados do formato texto
    def importar_texto(self, arquivo):
        with open(arquivo, 'r') as f:
            for linha in f:
                titulo, autor, ano, genero = linha.strip().split(',')
                self.adicionar_livro(Livro(titulo, autor, int(ano), genero))

    # Importar dados do formato JSON
    def importar_json(self, arquivo):
        with open(arquivo, 'r') as f:
            livros = json.load(f)
            for livro_data in livros:
                self.adicionar_livro(Livro(**livro_data))

    # Importar dados do formato CSV
    def importar_csv(self, arquivo):
        with open(arquivo, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                self.adicionar_livro(Livro(row['titulo'], row['autor'], int(row['ano']), row['genero']))

    # Importar dados do formato binário com pickle
    def importar_binario(self, arquivo):
        with open(arquivo, 'rb') as f:
            self.livros = pickle.load(f)

    # Listar todos os títulos de livros usando map
    def listar_titulos(self):
        return list(map(lambda livro: livro.titulo, self.livros))

    # Contar número de livros por gênero usando reduce
    def contar_livros_por_genero(self, genero):
        return reduce(lambda contador, livro: contador + 1 if livro.genero == genero else contador, self.livros, 0)

    # Filtrar livros por ano e/ou gênero usando filter
    def filtrar_livros(self, ano=None, genero=None):
        return list(filter(lambda livro: 
                           (ano is None or livro.ano == ano) and
                           (genero is None or livro.genero == genero), 
                           self.livros))

    # Backup dos dados em JSON ou binário
    def backup(self, arquivo='backup.json', formato='json'):
        if formato == 'json':
            self.exportar_json(arquivo)
        elif formato == 'binario':
            self.exportar_binario(arquivo)

# Teste das funcionalidades
if __name__ == "__main__":
    # Criação de instâncias de livros
    livro1 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1954, "Fantasia")
    livro2 = Livro("1984", "George Orwell", 1949, "Distopia")
    livro3 = Livro("O Hobbit", "J.R.R. Tolkien", 1937, "Fantasia")
    livro4 = Livro("A Revolução dos Bichos", "George Orwell", 1945, "Distopia")
    livro5 = Livro("Dom Quixote", "Miguel de Cervantes", 1605, "Clássico")

    # Instância da biblioteca
    biblioteca = Biblioteca()

    # Adicionar livros à biblioteca
    biblioteca.adicionar_livro(livro1)
    biblioteca.adicionar_livro(livro2)
    biblioteca.adicionar_livro(livro3)
    biblioteca.adicionar_livro(livro4)
    biblioteca.adicionar_livro(livro5)

    # Consultar livros por autor
    print("Livros por J.R.R. Tolkien:", biblioteca.listar_livros_por_autor("J.R.R. Tolkien"))

    # Contar livros por gênero
    print("Número de livros de Distopia:", biblioteca.contar_livros_por_genero("Distopia"))

    # Listar todos os títulos de livros
    print("Títulos de todos os livros:", biblioteca.listar_titulos())

    # Filtrar livros por ano e gênero
    print("Filtrar livros de 1945, gênero Distopia:", biblioteca.filtrar_livros(ano=1945, genero="Distopia"))

    # Exportar dados em todos os formatos
    biblioteca.exportar_texto("biblioteca.txt")
    biblioteca.exportar_json("biblioteca.json")
    biblioteca.exportar_csv("biblioteca.csv")
    biblioteca.exportar_binario("biblioteca.pkl")

    # Importar dados em todos os formatos para verificar consistência
    nova_biblioteca = Biblioteca()

    nova_biblioteca.importar_texto("biblioteca.txt")
    print("Livros importados do TXT:", nova_biblioteca.livros)

    nova_biblioteca = Biblioteca()
    nova_biblioteca.importar_json("biblioteca.json")
    print("Livros importados do JSON:", nova_biblioteca.livros)

    nova_biblioteca = Biblioteca()
    nova_biblioteca.importar_csv("biblioteca.csv")
    print("Livros importados do CSV:", nova_biblioteca.livros)

    nova_biblioteca = Biblioteca()
    nova_biblioteca.importar_binario("biblioteca.pkl")
    print("Livros importados do binário (pickle):", nova_biblioteca.livros)

    # Backup dos dados
    biblioteca.backup("backup.json", "json")
    biblioteca.backup("backup.pkl", "binario")