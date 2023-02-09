# language: es
Característica: Transferencia bancaria
  Como un usuario bancario quiero transferir dinero desde mi cuenta bancaria a otros

  Escenario: Transferir entre cuentas propias en el mismo banco
    #Precondicion
    Dado que tengo una cuenta de origen y una de destino con '50.0', cada una,en el mismo banco
    #Eventos --> Procesos se desarrollan a partir del evento
    Cuando realizo una transferencia de un monto '50.0' de la cuenta origen a la cuenta de destino
    #Resultados
    Entonces el saldo de la cuenta destino se incrementara a '100.0'
    Y se decrementa a '0.0' la cuenta origen

  Escenario: Transferir entre cuentas propias en el mismo banco
    #Precondicion
    Dado que tengo una cuenta de origen y una de destino con '50.0', cada una,en el mismo banco
    #Eventos --> Procesos se desarrollan a partir del evento
    Cuando realizo una transferencia de un monto '100.0' de la cuenta origen a la cuenta de destino
    #Resultados
    Entonces el saldo de la cuenta destino se incrementara a '50.0'
    Y se decrementa a '50.0' la cuenta origen








