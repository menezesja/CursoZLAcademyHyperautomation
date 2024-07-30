#Exemplo prático: Gerenciamento de contatos

def criar_contato(nome, telefone, email):
    """
    Cria um dicionário representando um contato com nome, telefone e email.

    Parâmetros:
    nome (str): O nome do contato.
    telefone (str): O número de telefone do contato.
    email (str): O endereço de email do contato.

    Retorna:
    dict: Um dicionário contendo os detalhes do contato.
    """
    contato = {
        "nome": nome,
        "telefone": telefone,
        "email": email
    }
    return contato

def adicionar_contato(agenda, contato):
    """
    Adiciona um contato à agenda.

    Parâmetros:
    agenda (list): A lista de contatos.
    contato (dict): O dicionário do contato a ser adicionado.
    """
    agenda.append(contato)

def buscar_contato(agenda, nome):
    """
    Busca um contato na agenda pelo nome.

    Parâmetros:
    agenda (list): A lista de contatos.
    nome (str): O nome do contato a ser buscado.

    Retorna:
    dict ou None: O dicionário do contato encontrado ou None se não encontrar.
    """
    for contato in agenda:
        if contato["nome"] == nome:
            return contato
    return None

# Criando alguns contatos
contato1 = criar_contato("João", "123456789", "joao@email.com")
contato2 = criar_contato("Maria", "987654321", "maria@email.com")

# Criando uma agenda (uma lista de dicionários)
agenda = []
adicionar_contato(agenda, contato1)
adicionar_contato(agenda, contato2)

# Buscando um contato
contato_encontrado = buscar_contato(agenda, "João")
if contato_encontrado:
    print(f"Contato encontrado: {contato_encontrado}")
else:
    print("Contato não encontrado.")