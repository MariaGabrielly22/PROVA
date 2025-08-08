salario = int(input("Informe seu salário mensal: R$ "))

salario_anual = salario * 12

if salario > 5000:
    imposto_anual = salario_anual * 0.12
    imposto_mensal = salario * 0.12
elif salario >= 2000:
    imposto_anual = salario_anual * 0.07
    imposto_mensal = salario * 0.07
else:
    imposto_anual = salario_anual * 0.03
    imposto_mensal = salario * 0.03

print("Salário mensal: R$", salario)
print("Salário anual: R$", salario_anual)
print("Imposto mensal: R$", round(imposto_mensal, 2))
print("Imposto anual: R$", round(imposto_anual, 2))