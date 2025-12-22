import pandas as pd

def analisar_notas_enem(caminho_do_arquivo, nome_da_coluna):
    """
    Lê um arquivo CSV de notas do ENEM e realiza uma análise estatística completa.
    """
    try:
        df = pd.read_csv(caminho_do_arquivo)
    except FileNotFoundError:
        return f"Erro: O arquivo '{caminho_do_arquivo}' não foi encontrado."
    except Exception as e:
        return f"Ocorreu um erro ao ler o arquivo: {e}"

    if nome_da_coluna not in df.columns:
        print("NOMES DAS COLUNAS ENCONTRADAS:", df.columns.tolist())
        return f"Erro: A coluna '{nome_da_coluna}' não foi encontrada. Verifique a lista acima."

    # Prepara a coluna de dados, removendo valores inválidos
    coluna_numerica = pd.to_numeric(df[nome_da_coluna], errors='coerce').dropna()

    if coluna_numerica.empty:
        return f"A coluna '{nome_da_coluna}' não contém valores numéricos válidos."

    #a) Média 
    media = coluna_numerica.mean()
    
    #b) Percentil 90 
    percentil_90 = coluna_numerica.quantile(0.9)
    
    #c) Probabilidade de nota < 450 
    total_alunos = len(coluna_numerica)
    alunos_menor_450 = len(coluna_numerica[coluna_numerica < 450])
    probabilidade_menor_450 = alunos_menor_450 / total_alunos if total_alunos > 0 else 0
    
    #d) Probabilidade condicional (nota > 800 | nota > 700) 
    grupo_acima_700 = coluna_numerica[coluna_numerica > 700]
    alunos_acima_800_desse_grupo = len(grupo_acima_700[grupo_acima_700 > 800])
    total_alunos_acima_700 = len(grupo_acima_700)
    
    prob_condicional = 0
    if total_alunos_acima_700 > 0:
        prob_condicional = alunos_acima_800_desse_grupo / total_alunos_acima_700
    
    # Retorna os quatro resultados
    return media, percentil_90, probabilidade_menor_450, prob_condicional


#   Programa Principal

nome_do_arquivo = 'enem_mat_amostra.csv' 
coluna_para_analise = 'NU_NT_MT' 

# Chama a função para obter os resultados
resultados = analisar_notas_enem(nome_do_arquivo, coluna_para_analise)

# Adiciona uma linha para separar o resultado
print("-" * 50) 

# Verifica se o resultado foi um sucesso ou uma mensagem de erro
if isinstance(resultados, tuple):
    media_final, p90_final, prob_450_final, prob_cond_final = resultados
    print(f"  SUCESSO! Análise completa da coluna '{coluna_para_analise}':\n")
    print(f"   a) A média das notas é: {media_final:.2f}")
    print(f"   b) A nota com 10% da amostra na frente é: {p90_final:.2f}")
    print(f"   c) A probabilidade de um aluno ter nota < 450 é: {prob_450_final:.2%}")
    print(f"   d) Dado que um aluno tirou > 700, a probabilidade de ele ter tirado > 800 é: {prob_cond_final:.2%}")
else:
    # Imprime a mensagem de erro
    print(f" {resultados}")