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