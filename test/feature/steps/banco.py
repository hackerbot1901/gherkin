from behave import *

from model.models import Cuenta

use_step_matcher("re")


@step("que tengo una cuenta de origen y una de destino con \$50, cada una,en el mismo banco")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.cuentaOrigen = Cuenta(50.0)
    context.cuentaDestino = Cuenta(50.0)
    # raise NotImplementedError(u'STEP: Dado que tengo una cuenta de origen y una de destino con $50, cada una,en el mismo banco')


@step("realizo una transferencia de un monto \$50 de la cuenta origen a la cuenta de destino")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.cuentaOrigen.transferir(50.0, context.cuentaDestino)
    # raise NotImplementedError(u'STEP: Cuando quiera realizar una transferencia de $50 de una cuenta origen a otra')


@step("el saldo de la cuenta destino se incrementara a \$100")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.cuentaDestino.obtenerSaldo() == 100.0
    # raise NotImplementedError(u'STEP: Entonces el saldo de la cuenta destino se incrementara a $100')


@step("se decrementa a \$0 la cuenta origen")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    # Verificacion porque no se ejecuta codigo, ademas estamos asegurando la calidad
    # Se baja las espectativas para no decepciponarse
    assert context.cuentaOrigen.obtenerSaldo() == 0.0
    # raise NotImplementedError(u'STEP: Y se decrementa a $0 la cuenta origen')
