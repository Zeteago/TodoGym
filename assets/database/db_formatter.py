def formatar_treino(dados):
    """Formata resultado do banco em dicionário"""
    if not dados:
        return None

    treino = {
        "id": dados[0][0],
        "nome": dados[0][1],
        "data": dados[0][2],
        "exercicios": []
    }

    exercicio_atual = None
    for row in dados:
        if row[3] and (not exercicio_atual or exercicio_atual["id"] != row[3]):
            exercicio_atual = {
                "id": row[3],
                "nome": row[4],
                "series": []
            }
            treino["exercicios"].append(exercicio_atual)

        if row[5]:  # se tem série
            exercicio_atual["series"].append({
                "numero": row[5],
                "repeticoes": row[6],
                "peso": row[7]
            })

    return treino