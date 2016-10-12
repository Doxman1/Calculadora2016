Feature: Realizar suma de dos numeros
	Yo como usuario de la app calculadora 
	quiero realizar una suma de dos numeros
	para poder tener un resultado confiable.

	Scenario: sumar 2 más 2
		dado que tengo el numero "2" y "2"
		cuando realizo la suma
		entonces el resultado que obtengo es "4"
	Scenario: sumar 2 más 5
		dado que tengo el numero "2" y "5"
		cuando realizo la suma
		entonces el resultado que obtengo es "7"
	Scenario: restar 2 menos 2
		dado que tengo el numero "2" y "2"
		cuando realizo la resta
		entonces el resultado que tengo es "0"
	Scenario: restar 2 menos 5
		dado que tengo el numero "5" y "2"
		cuando realizo la resta
		entonces el resultado que tengo es "3"

	Scenario: multiplicar 2 menos 5
		dado que tengo el numero "2" y "5"
		cuando realizo la multiplicacion
		entonces de la multiplicación obtengo "10"

	Scenario: dividir 6 entre 2
		dado que tengo el numero "6" y "2"
		cuando realizo la división
		entonces de la división resulta "3"