

class Conta:
    """
    Classe para representar uma conta bancária.

    Atributos:
        numero_conta (int): O número da conta.
        titular (str): O nome do titular da conta.
        saldo (float): O saldo atual da conta.
    """

    def __init__(self, numero_conta, titular, saldo=0.0):
        """
        Inicializa uma nova conta bancária.

        Args:
            numero_conta (int): O número da conta.
            titular (str): O nome do titular da conta.
            saldo (float, opcional): O saldo inicial da conta. Padrão é 0.0.
        """
        self.numero_conta = numero_conta
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        """
        Realiza um depósito na conta.

        Args:
            valor (float): O valor a ser depositado.

        Raises:
            ValueError: Se o valor do depósito for não positivo.
        """
        if valor <= 0:
            raise ValueError("O valor do depósito deve ser positivo.")
        self.saldo += valor
        print(f"Depósito de R${valor:.2f} realizado com sucesso.")

    def sacar(self, valor):
        """
        Realiza um saque da conta.

        Args:
            valor (float): O valor a ser sacado.

        Raises:
            ValueError: Se o valor do saque for não positivo ou se o saldo for insuficiente.
        """
        if valor <= 0:
            raise ValueError("O valor do saque deve ser positivo.")
        if valor > self.saldo:
            raise ValueError("Saldo insuficiente.")
        self.saldo -= valor
        print(f"Saque de R${valor:.2f} realizado com sucesso.")

    def verificar_saldo(self):
        """Exibe o saldo atual da conta."""
        print(f"Saldo atual: R${self.saldo:.2f}")

def exibir_menu():
    """Exibe o menu de operações e retorna a opção escolhida pelo usuário."""
    print("\n--- Sistema Bancário ---")
    print("1. Verificar Saldo")
    print("2. Depositar")
    print("3. Sacar")
    print("4. Sair")
    return input("Escolha uma opção: ")

def tratar_opcao(opcao, conta):
    """Trata a opção escolhida pelo usuário no menu.

    Args:
        opcao (str): A opção escolhida pelo usuário.
        conta (Conta): A instância da conta bancária.
    """
    if opcao == '1':
        conta.verificar_saldo()
    elif opcao == '2':
        try:
            valor = float(input("Digite o valor para depósito: R$"))
            conta.depositar(valor)
        except ValueError as ve:
            print(f"Erro: {ve}")
    elif opcao == '3':
        try:
            valor = float(input("Digite o valor para saque: R$"))
            conta.sacar(valor)
        except ValueError as ve:
            print(f"Erro: {ve}")
    elif opcao == '4':
        print("Saindo do sistema. Até logo!")
        return False
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
    return True

def main():
    """Função principal que controla o fluxo do sistema bancário."""
    conta = Conta(12345, "Jonatas Dias", 1000.0)

    while True:
        opcao = exibir_menu()
        if not tratar_opcao(opcao, conta):
            break

if __name__ == "__main__":
    main()
