class Categoria:
    def __init__(self, nome):
        self.nome = nome
        self.__livro = ""  

    def aceita(self, paginas):
        return True

    def regra(self):
        return "qualquer livro"

    def cumprir(self, titulo):
        self.__livro = titulo

    def cumprida(self):
        return self.__livro != ""

    def livro_que_cumpriu(self):
        return self.__livro


class CategoriaLonga(Categoria):

    def aceita(self, paginas):
        return paginas >= 400

    def regra(self):
        return "400 páginas ou mais"


class CategoriaCurta(Categoria):

    def aceita(self, paginas):
        return paginas <= 150

    def regra(self):
        return "até 150 páginas"


class Desafio:
    def __init__(self, meta):
        self.meta = meta
        self.__lidos = []  
        self.categorias = [
            Categoria("Um clássico"),
            Categoria("Um romance"),
            Categoria("Uma ficção científica"),
            Categoria("Uma fantasia"),
            CategoriaLonga("Um livro longo"),
            CategoriaCurta("Um livro curto"),
            
        ]

    def listar_categorias(self):
        for i in range(len(self.categorias)):
            categoria = self.categorias[i]
            print(f"  {i + 1} - {categoria.nome} ({categoria.regra()})")

    def registrar(self, titulo, paginas, numero):
        """Registra um livro lido. numero = 0 significa 'nenhuma categoria'."""
        if numero < 0 or numero > len(self.categorias):
            print("Categoria inválida. Nada foi registrado.")
        elif numero > 0 and self.categorias[numero - 1].cumprida():
            print("Essa categoria já foi cumprida. Nada foi registrado.")
        elif numero > 0 and not self.categorias[numero - 1].aceita(paginas):
            regra = self.categorias[numero - 1].regra()
            print(f"Esse livro não serve para a categoria ({regra}). Nada foi registrado.")
        else:
            self.__lidos.append(titulo)
            if numero > 0:
                self.categorias[numero - 1].cumprir(titulo)
            print(f"'{titulo}' registrado!")

    def ver(self):
        lidos = len(self.__lidos)
        print(f"Meta: {lidos}/{self.meta} livros ({lidos * 100 // self.meta}%)")
        print("Categorias:")
        for categoria in self.categorias:
            if categoria.cumprida():
                print(f"  [x] {categoria.nome} -> {categoria.livro_que_cumpriu()}")
            else:
                print(f"  [ ] {categoria.nome} ({categoria.regra()})")
        print("Livros lidos:")
        for titulo in self.__lidos:
            print(f"  - {titulo}")

    def ritmo(self, mes_atual):
        lidos = len(self.__lidos)
        esperado = self.meta * mes_atual // 12
        print(f"Você leu {lidos} livro(s). Até o mês {mes_atual}, o esperado era {esperado}.")
        if lidos >= self.meta:
            print("Meta batida! Parabéns!")
        elif lidos >= esperado:
            print("Você está no ritmo!")
        else:
            print(f"Faltam {esperado - lidos} livro(s) para voltar ao ritmo.")


meta = int(input("Meta de livros para o ano: "))
mes_atual = int(input("Mês atual (1 a 12): "))
desafio = Desafio(meta)

opcao = ""
while opcao != "0":
    print("\n===== DESAFIO DE LEITURA =====")
    print("1 - Registrar livro lido")
    print("2 - Ver desafio")
    print("3 - Ver ritmo")
    print("0 - Sair")
    opcao = input("Escolha: ")

    if opcao == "1":
        titulo = input("Título: ")
        paginas = int(input("Número de páginas: "))
        print("Categorias (0 = nenhuma):")
        desafio.listar_categorias()
        numero = int(input("Qual categoria esse livro cumpriu? "))
        desafio.registrar(titulo, paginas, numero)
    elif opcao == "2":
        desafio.ver()
    elif opcao == "3":
        desafio.ritmo(mes_atual)
    elif opcao == "0":
        print("Boas leituras!")
    else:
        print("Opção inválida.")