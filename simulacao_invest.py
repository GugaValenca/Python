# Simula o tempo necessário para atingir R$ 10.000 em proventos mensais
# com diferentes cenários de aporte e dividend yield (DY)

import pandas as pd

# Parâmetros iniciais
total_investido = 2894.48  # Soma total da carteira atual
proventos_mensais_atuais = 34.69  # Proventos mensais atuais
meta_proventos_mensais = 10000  # Meta de proventos mensais (R$)

dy_mensal_medio = 0.0124  # DY médio atual (12.4% ao ano)

cenarios = [
    {"aporte": 3500, "dy_mensal": dy_mensal_medio, "nome": "Aporte R$ 3.500"},
    {"aporte": 3000, "dy_mensal": 0.013, "nome": "DY 1.3%"},
    {"aporte": 3000, "dy_mensal": 0.015, "nome": "DY 1.5%"},
    {"aporte": 3500, "dy_mensal": 0.013, "nome": "Aporte 3.500 + DY 1.3%"},
    {"aporte": 3500, "dy_mensal": 0.015, "nome": "Aporte 3.500 + DY 1.5%"},
]

resultados = []

for cenario in cenarios:
    total = total_investido
    proventos = proventos_mensais_atuais
    meses = 0
    while proventos < meta_proventos_mensais:
        total += cenario["aporte"] + proventos
        proventos = total * cenario["dy_mensal"]
        meses += 1

    anos = meses // 12
    resto_meses = meses % 12
    resultados.append({
        "Cenário": cenario["nome"],
        "Meses": meses,
        "Anos e Meses": f"{anos} anos e {resto_meses} meses",
        "Proventos finais (R$)": round(proventos, 2)
    })

# Exibe os resultados em tabela
resultados_df = pd.DataFrame(resultados)
print(resultados_df)
