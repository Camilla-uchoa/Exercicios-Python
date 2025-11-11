
#Lista que vai armazenar as informações
funcionarios = []

# Função calcular salario
def calcular_salario(valor_hora, quantidade_horas):
    salario_bruto = valor_hora * quantidade_horas

    #Função classificação dos  cargos
    def classifica_cargos(salario_bruto):
      if salario_bruto <= 800:
          return "Jovem Aprendiz"
      elif salario_bruto <= 1600:
          return "Funcionário Base"
      elif salario_bruto <= 2100:
          return "Auxiliar Base"
      elif salario_bruto <= 3500:
          return "Supervisor"
      elif salario_bruto <= 6000:
          return "Gerente"
      else:
          return "Gerente Geral"

    #Função de calculo do INSS
    def calculo_inss(salario_bruto):
      if salario_bruto <= 1518:
          return salario_bruto * 0.075
      elif salario_bruto <= 2793:
          return salario_bruto * 0.09
      elif salario_bruto <= 4190:
          return salario_bruto * 0.12
      else:
          return salario_bruto * 0.14

    #Função de calculo do Imposto de Renda (IR)
    def calcular_ir(salario_bruto):
        if salario_bruto <= 2112.00:
            return 0
        elif salario_bruto <= 2826.65:
           return salario_bruto * 0.075
        elif salario_bruto <= 3751.05:
           return salario_bruto * 0.15
        elif salario_bruto <= 4664.68:
            return salario_bruto * 0.22
        else:
            return salario_bruto * 0.27

    #Função de calculo do sindicato
    def calcular_sindicato(salario_bruto):
        return salario_bruto * 0.05

    #Atribuir as funções a variaveis
    cargo = classifica_cargos(salario_bruto)
    inss = calculo_inss(salario_bruto)
    ir = calcular_ir(salario_bruto)
    sindicato = calcular_sindicato(salario_bruto)
    salario_liquido = salario_bruto - inss - ir - sindicato

    return salario_bruto, cargo, inss, ir, sindicato, salario_liquido


# ---------- Funções CRUD ----------
'''
C → Create (Criar ou Cadastrar)

R → Read (Ler ou Listar)

U → Update (Atualizar ou Alterar)

D → Delete (Apagar ou Excluir)'''

'''
Create → quando você cadastra um novo funcionário.

Read → quando você lista todos os funcionários cadastrados.

Update → quando você altera os dados de um funcionário (nome, horas, valor da hora).

Delete → quando você exclui um funcionário da lista.'''

#Função da entrada de dados - Cadastro
def cadastrar():
    nome = input("Digite o nome do funcionário(a): ").strip()
    valor_hora = float(input("Digite o valor da hora trabalhada: "))
    quantidade_horas = float(input("Digite a quantidade de horas trabalhadas: "))

# descompactação - Chamar todas as funções de uma vez e atribuir
# novamente cada um
    salario_bruto, cargo, inss, ir, sindicato, salario_liquido = calcular_salario(valor_hora, quantidade_horas)

    funcionario = {
        "nome": nome,
        "valor_hora": valor_hora,
        "quantidade_horas": quantidade_horas,
        "salario_bruto": salario_bruto,
        "cargo": cargo,
        "inss": inss,
        "ir": ir,
        "sindicato": sindicato,
        "salario_liquido": salario_liquido
    }

#Adicionando as informações a um dicionário global
    funcionarios.append(funcionario)
    print(f"\n Funcionário(a) {nome} cadastrado com sucesso!\n")

#Função para
def listar():
    if not funcionarios:
        print("\n Nenhum funcionário(a) cadastrado.\n")
        return
    for i, f in enumerate(funcionarios, start=1): #dentro da lista, contar cada um a partir do 1
        print(f"\n--- Funcionário(a) {i} ---")
        print(f"Nome: {f['nome']}")
        print(f"Cargo: {f['cargo']}")
        print(f"Salário Bruto: R$ {f['salario_bruto']:.2f}")
        print(f"Salário Líquido: R$ {f['salario_liquido']:.2f}")


def alterar():
    listar()
    indice = int(input("\nDigite o número do funcionário(a) que deseja alterar: ")) - 1  #Para começar a contar realmente do 1
    if 0 <= indice < len(funcionarios): # O número escolhido não pode ser menor que o número de funcionários
        nome = input("Novo nome: ").strip()
        valor_hora = float(input("Novo valor da hora: "))
        quantidade_horas = float(input("Nova quantidade de horas: "))

        salario_bruto, cargo, inss, ir, sindicato, salario_liquido = calcular_salario(valor_hora, quantidade_horas)

        funcionarios[indice].update({ #atualizar as novas informações
            "nome": nome,
            "valor_hora": valor_hora,
            "quantidade_horas": quantidade_horas,
            "salario_bruto": salario_bruto,
            "cargo": cargo,
            "inss": inss,
            "ir": ir,
            "sindicato": sindicato,
            "salario_liquido": salario_liquido
        })
        print("\n Funcionário(a) alterado com sucesso!\n")
    else:
        print(" Funcionário(a) não encontrado.")


def excluir():
    listar()
    indice = int(input("\nDigite o número do funcionário(a) que deseja excluir: ")) - 1
    if 0 <= indice < len(funcionarios):
        removido = funcionarios.pop(indice)
        print(f"\n Funcionário(a) {removido['nome']} removido com sucesso!\n")
    else:
        print(" Funcionário(a) não encontrado.")


# ---------- Menu principal ----------
def menu():
    while True:
        print("\n++++++++ Sistema Folha de Pagamento ++++++++")
        print("1 - Cadastrar funcionário(a)")
        print("2 - Listar funcionários(a)")
        print("3 - Alterar funcionário(a)")
        print("4 - Excluir funcionário(a)")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar()
        elif opcao == "2":
            listar()
        elif opcao == "3":

            alterar()
        elif opcao == "4":
            excluir()
        elif opcao == "5":
            print("Saindo do sistema...")
            break
        else:
            print("⚠️ Opção inválida.")


# Rodar sistema
menu()
