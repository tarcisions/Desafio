import json

with open('dados.json') as f:
    faturamento = json.load(f)

valores = [dia['valor'] for dia in faturamento if dia['valor'] > 0]
menor_valor = min(valores)
maior_valor = max(valores)
media_mensal = sum(valores) / len(valores)

dias_acima_da_media = sum(dia['valor'] > media_mensal for dia in faturamento if dia['valor'] > 0)

print(f'Menor valor de faturamento: R$ {menor_valor:.2f}')
print(f'Maior valor de faturamento: R$ {maior_valor:.2f}')
print(f'Número de dias com faturamento acima da média mensal: {dias_acima_da_media}')