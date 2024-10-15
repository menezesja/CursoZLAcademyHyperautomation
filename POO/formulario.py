from datetime import datetime

class FormularioBase:
    def __init__(self, cpf, nome, dataNascimento):
        self.__cpf = cpf
        self.__nome = nome
        self.__dataNascimento = dataNascimento

    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def dataNascimento(self):
        return self.__dataNascimento
    
    @dataNascimento.setter
    def dataNascimento(self, dataNascimento):
        self.__dataNascimento = dataNascimento

    def mostrar_informacoes(self):
        return f"CPF: {self.__cpf}, Nome: {self.__nome}, Data de Nascimento: {self.__dataNascimento}"

class FormularioLogin(FormularioBase):
    def __init__(self, cpf, nome, dataNascimento, usuario, senha):
        super().__init__(cpf, nome, dataNascimento)
        self.__usuario = usuario
        self.__senha = senha

    @property
    def usuario(self):
        return self.__usuario
    
    @usuario.setter
    def usuario(self, usuario):
        self.__usuario = usuario

    @property
    def senha(self):
        return self.__senha
    
    @senha.setter
    def senha(self, senha):
        self.__senha = senha

    def mostrar_informacoes(self):
        base_info = super().mostrar_informacoes()
        return f"{base_info}\nUsuário: {self.__usuario}\nSenha: {self.__senha}"

class FormularioEndereco(FormularioBase):
    def __init__(self, cpf, nome, dataNascimento, cep, rua, numero, bairro, cidade, estado):
        super().__init__(cpf, nome, dataNascimento)
        self.__cep =  cep
        self.__rua =  rua
        self.__numero =  numero
        self.__bairro =  bairro
        self.__cidade = cidade
        self.__estado = estado

    @property
    def cep(self):
        return self.__cep
    
    @cep.setter
    def cep(self, cep):
        self.__cep = cep

    @property
    def rua(self):
        return self.__rua
    
    @rua.setter
    def rua(self, rua):
        self.__rua = rua

    @property
    def numero(self):
        return self.__numero
    
    @numero.setter
    def numero(self, numero):
        self.__numero = numero

    @property
    def bairro(self):
        return self.__bairro
    
    @bairro.setter
    def bairro(self, bairro):
        self.__bairro = bairro

    @property
    def cidade(self):
        return self.__cidade
    
    @cidade.setter
    def cidade(self, cidade):
        self.__cidade = cidade

    @property
    def estado(self):
        return self.__estado
    
    @estado.setter
    def estado(self, estado):
        self.__estado = estado

    def mostrar_informacoes(self):
        return (f"Rua: {self.__rua}, {self.__numero}, "
                f"{self.__bairro}, {self.__cep}, {self.__cidade}, {self.__estado}")

class FormularioContato(FormularioBase):
    def __init__(self, cpf, nome, dataNascimento, telefone, celular, email):
        super().__init__(cpf, nome, dataNascimento)
        self.__telefone = telefone
        self.__celular = celular
        self.__email = email

    @property
    def telefone(self):
        return self.__telefone
    
    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone

    @property
    def celular(self):
        return self.__celular
    
    @celular.setter
    def celular(self, celular):
        self.__celular = celular

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, email):
        self.__email = email

    def mostrar_informacoes(self):
        return (f"Telefone: {self.__telefone}, Celular: {self.__celular}, "
                f"Email: {self.__email}")

# Exemplo de uso
form_login = FormularioLogin("12345678900", "Jade Santos", "1995-06-15", "jades", "senha123")
print(form_login.mostrar_informacoes())

form_endereco = FormularioEndereco("12345678900", "Jade Santos", "1995-06-15", "69000000", "Rua Exemplo", 123, "Centro", "Manaus", "AM")
print(form_endereco.mostrar_informacoes())

form_contato = FormularioContato("12345678900", "Jade Santos", "1995-06-15", "921234567", "991234567", "jade@email.com")
print(form_contato.mostrar_informacoes())
