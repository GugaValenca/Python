# Simulações com diferentes cenários:
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
    resultados.append({
        "Cenário": cenario["nome"],
        "Meses": meses,
        "Anos e Meses": f"{meses // 12} anos e {meses % 12} meses",
        "Data Alvo": f"{(2025 + (meses // 12))}-{((meses % 12) + 1):02d}"
    })

df_resultados = pd.DataFrame(resultados)
df_resultados
