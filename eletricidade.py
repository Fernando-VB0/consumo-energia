# Calculadora de Consumo de Energia

print("=== Calculadora de Consumo Elétrico ===")

eletronico = input("Digite o nome do aparelho: ")
potencia = float(input("Digite a potência em watts: "))
horas_dia = float(input("Digite o uso diário em horas: "))

consumo_mensal = (potencia * horas_dia * 30) / 1000

opcao_valor = input("Quer usar valor padrão de energia (R$0.75)? (sim/não ): ")

if opcao_valor == "sim":
    custo_kwh = 0.75
else:
    custo_kwh = float(input("Digite o valor do kWh da sua cidade: "))
custo_estimado = consumo_mensal * custo_kwh

print("\n=== Resultado ===")
print(f"eletronico: {eletronico}")
print(f"Consumo estimado: {consumo_mensal:.2f} kWh/mês")
print(f"Custo estimado: R$ {custo_estimado:.2f}")