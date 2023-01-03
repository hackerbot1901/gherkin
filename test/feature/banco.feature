# language: es
Característica: Transferencia bancaria
  Como un usuario bancario quiero transferir dinero desde mi cuenta bancaria a otros

  Escenario: Transferir entre cuentas propias en el mismo banco
    #Precondicion
    Dado que tengo dos cuentas con 50, cada una,en el mismo banco
    #Eventos --> Procesos se desarrollan a partir del evento
    Cuando quiera realizar una transferencia de $50 de una cuenta origen a otra
    #Resultados
    Entonces el saldo de la cuenta destino se incrementara a $100
    Y se decrementa a $0 la cuenta origen
