estado = int(input("Digite o codigo do estado (1 a 5): "))
peso_ton = float(input("Digite o peso em toneladas: "))
cod_carga = int(input("Digite o codigo da carga (10 a 40): "))

peso_kg = peso_ton * 1000

if cod_carga >= 10 and cod_carga <= 20:
    preco_kg = 100
elif cod_carga >= 21 and cod_carga <= 30:
    preco_kg = 250
elif cod_carga >= 31 and cod_carga <= 40:
    preco_kg = 340

preco_carga = peso_kg * preco_kg

if estado == 1:
    imposto = preco_carga * 0.35
elif estado == 2:
    imposto = preco_carga * 0.25
elif estado == 3:
    imposto = preco_carga * 0.15
elif estado == 4:
    imposto = preco_carga * 0.05
else:
    imposto = 0

valor_total = preco_carga + imposto

print(f"\nPeso em kg: {peso_kg}")
print(f"Preço da carga: R$ {preco_carga}")
print(f"Valor do imposto: R$ {imposto}")
print(f"Valor total: R$ {valor_total}")