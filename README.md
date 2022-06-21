# calculadora_precios_fnac
Estoy haciendo una calculadora de precios de Fnac.

Utilizo Tkinter para crear la app. Cuando este funcional 100% deberia:
  1. Calcular el precio segun si eres socio o no.
  2. Calcular el precio si financias el producto dandote a escojer los 3 tipos 
     de mensualidades que hay (3 meses, 10 meses o 20 meses)
     
     
     
# TODO 
  1.No se porque si eliges que no quieres financiar pero escojes mensualidad te hace el calculo igualmente.[FIXED]
  
  2.Si selecionas que no eres socio, le das a financiar se bloquea la selecion, pero si despues le das que sí eres
  socio se mantiene bloqueado y no te deja selecionar.[NOT]
  
  3.Calcular, para la 1ª mensualidad, el 3% del valor total si selecionas 10 meses o 20 meses en la financiacion.
  Por ejemplo, si el valor total del producto es 499.99€, el precio de socio seria 474.99€. Si financias a 3 meses es tan
  sencillo como 474.99/3 = 158.33€. Pero si es en 10 meses seria: 1ª mensualidad 61,74€ y las 9 restantes 47,49€.
