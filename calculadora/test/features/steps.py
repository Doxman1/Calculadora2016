# -*- coding: utf-8 -*-
from lettuce import step, world  # hacer la variable global, en este caso calc
from calculadora import Calculadora


@step(u'dado que tengo el numero "([^"]*)" y "([^"]*)"')
def dado_que_tengo_el_numero_group1_y_group1(step, num1, num2):
    cal = Calculadora()
    world.resultado = cal.suma(int(num1), int(num2))
    world.resta = cal.resta(int(num1),int(num2))
    world.mult = cal.multi(int(num1),int(num2))
    world.division = cal.div(int(num1),int(num2))
@step(u'cuando realizo la suma')
def cuando_realizo_la_suma(step):
    pass
@step(u'cuando realizo la resta')
def cuando_realizo_la_resta(step):
   	pass

@step(u'cuando realizo la multiplicacion')
def cuando_realizo_la_multiplicacion(step):
   	pass
@step(u'cuando realizo la división')
def cuando_realizo_la_division(step):
   	pass

@step(u'entonces el resultado que tengo es "([^"]*)"')
def entonces_el_resultado_que_tengo_es_group1(step, esperado):
    assert int(esperado) == world.resta, 'El res no coincide'

@step(u'entonces el resultado que obtengo es "([^"]*)"')
def entonces_el_resultado_que_obtengo_es_group1(step, esperado):
    assert int(esperado) == world.resultado, 'El res no coincide'

@step(u'entonces de la multiplicación obtengo "([^"]*)"')
def entonces_de_la_multiplicacion_obtengo_group1(step, esperado):
    assert int(esperado) == world.mult, 'El res no coincide'

@step(u'entonces de la división resulta "([^"]*)"')
def entonces_de_la_div_obtengo_group1(step, esperado):
    assert int(esperado) == world.division, 'El res no coincide'
