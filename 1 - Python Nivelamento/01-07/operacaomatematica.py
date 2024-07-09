#operações matemáticas

var_float = 9.0

adicao = var_float + 1              #operação de soma +
subtracao = var_float - 4           #operação de subtração -
multiplicacao = var_float * 5       #operação de multiplicação *
divisao = var_float/3               #operação de divisão /
potencia = var_float ** 2           #operação de potência **
modulo = var_float % 4              #operção de módulo %
quociente = var_float // 2          #operação de quociente //

print('Soma é: ' + str(adicao))
print('Subtração é: ' + str(subtracao))
print('Multiplicação é: ' + str(multiplicacao))
print('Divisão é: ' + str(divisao))
print('Potência é: ' + str(potencia))
print('Módulo é: ' + str(modulo))
print('Quociente é: ' + str(var_float))  #concatenação de strings

print('----------------------------------------------------')

#incremento e decremento

var_float -= 2
print('Resultado de atribuição -= 2 é: ' + str(var_float))

var_float += 5
print('Resultado de atribuição += 5 é: ' + str(var_float))