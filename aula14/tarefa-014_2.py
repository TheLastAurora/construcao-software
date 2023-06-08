class Contato:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email


class Agenda:
    def __init__(self):
        self.contatos = []

    def adicionar_contato(self, nome, email):
        contato = Contato(nome, email)
        self.contatos.append(contato)
        print(f"Contato {nome} adicionado à agenda.")

    def buscar_contato(self, termo):
        for contato in self.contatos:
            if termo.lower() in contato.nome.lower() or termo.lower() in contato.email.lower():
                return contato
        return None

    def excluir_contato(self, nome):
        for contato in self.contatos:
            if contato.nome.lower() == nome.lower():
                self.contatos.remove(contato)
                print(f"Contato {nome} removido da agenda.")
                return
        print(f"Contato {nome} não encontrado na agenda.")

    def listar_contatos(self):
        if len(self.contatos) == 0:
            print("Agenda vazia.")
        else:
            print("Contatos na agenda:")
            for contato in self.contatos:
                print(f"Nome: {contato.nome}, Email: {contato.email}")


# Exemplo de uso da classe Agenda
agenda = Agenda()

agenda.adicionar_contato("João", "joao@example.com")
agenda.adicionar_contato("Maria", "maria@example.com")
agenda.adicionar_contato("Carlos", "carlos@example.com")

contato = agenda.buscar_contato("joão")
if contato:
    print(f"Contato encontrado: {contato.nome}, {contato.email}")
else:
    print("Contato não encontrado.")

agenda.excluir_contato("Maria")
agenda.listar_contatos()
