class ContaBacaria:
    """
    Cria uma conta bancária que permite realizar saques e depósitos
    """

    def __init__(self, id, titular, saldo):
        self.id = id
        self.titular = titular
        self.saldo = saldo

    def __str__(self):
        return f'A conta {self.id} de {self.titular} tem R$ {self.saldo:,.2f} de saldo'

    def depositar(self, valor):
        self.saldo += valor
        print(f"Deposito de R$ {valor:,.2f} autorizado na conta {self.id}")

    def sacar(self, valor):
        if valor > self.saldo:
            print(f"Saque de R$ {valor:,.2f} negado na conta {self.id}: SALDO INSUFICIENTE")
        else:
            self.saldo -= valor
            print(f"Saque de R$ {valor:,.2f} autorizado na conta {self.id}")


c1 = ContaBacaria(123, 'Gustavo', 3000)
c1.depositar(500)
c1.sacar(10000)
print(c1)
