from behave import *

from model.models import Cuenta

use_step_matcher("parse")


@step("que tengo una cuenta de origen y una de destino con '{monto:f}', cada una,en el mismo banco")
def step_impl(context, monto):
    """
    :type context: behave.runner.Context
    """
    context.cuentaOrigen = Cuenta(monto)
    context.cuentaDestino = Cuenta(monto)
    # raise NotImplementedError(u'STEP: Dado que tengo una cuenta de origen y una de destino con $50, cada una,en el mismo banco')


@step("realizo una transferencia de un monto '{monto:f}' de la cuenta origen a la cuenta de destino")
def step_impl(context, monto):
    """
    :type context: behave.runner.Context
    """
    context.cuentaOrigen.transferir(monto, context.cuentaDestino)
    # raise NotImplementedError(u'STEP: Cuando quiera realizar una transferencia de $50 de una cuenta origen a otra')


@step("el saldo de la cuenta destino se incrementara a '{saldo:f}'")
def step_impl(context, saldo):
    """
    :type context: behave.runner.Context
    """
    print('Saldo: ', context.cuentaDestino.obtenerSaldo())
    assert context.cuentaDestino.obtenerSaldo() == saldo
    # raise NotImplementedError(u'STEP: Entonces el saldo de la cuenta destino se incrementara a $100')


@step("se decrementa a '{saldo:f}' la cuenta origen")
def step_impl(context, saldo):
    """
    :type context: behave.runner.Context
    """
    # Verificacion porque no se ejecuta codigo, ademas estamos asegurando la calidad
    # Se baja las espectativas para no decepciponarse
    assert context.cuentaOrigen.obtenerSaldo() == saldo
    # raise NotImplementedError(u'STEP: Y se decrementa a $0 la cuenta origen')


@step("que tengo una cuenta de origen y una de destino con {saldoInicial:f}, cada una,en el mismo banco")
def step_impl(context, saldoInicial):
    """
    :type context: behave.runner.Context
    :type saldoInicial: str
    """
    context.cuentaOrigen = Cuenta(saldoInicial)
    context.cuentaDestino = Cuenta(saldoInicial)
    # raise NotImplementedError(u'STEP: Dado que tengo una cuenta de origen y una de destino con <saldoInicial>, cada una,en el mismo banco')


@step("realizo una transferencia de un monto {monto:f} de la cuenta origen a la cuenta de destino")
def step_impl(context, monto):
    """
    :type context: behave.runner.Context
    :type monto: str
    """
    context.cuentaOrigen.transferir(monto, context.cuentaDestino)
    # raise NotImplementedError(u'STEP: Cuando realizo una transferencia de un monto <monto> de la cuenta origen a la cuenta de destino')


@step("el saldo de la cuenta destino se incrementara a {saldoFinalOrigen:f}")
def step_impl(context, saldoFinalOrigen):
    """
    :type context: behave.runner.Context
    :type saldoFinalOrigen: str
    """
    print('Saldo: ', context.cuentaDestino.obtenerSaldo())
    assert context.cuentaDestino.obtenerSaldo() == saldoFinalOrigen
    # raise NotImplementedError(u'STEP: Entonces el saldo de la cuenta destino se incrementara a <saldoFinalOrigen>')


@step("se decrementa a {saldoFinalDestino:f} la cuenta origen")
def step_impl(context, saldoFinalDestino):
    """
    :type context: behave.runner.Context
    :type saldoFinalDestino: str
    """
    assert context.cuentaOrigen.obtenerSaldo() == saldoFinalDestino
    # raise NotImplementedError(u'STEP: Y se decrementa a \'<saldoFinalDestino> la cuenta origen')
