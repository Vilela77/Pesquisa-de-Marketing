import pandas as pd
import matplotlib.pyplot as plt

# Ler os dados da planilha
df = pd.read_excel('planilha.xlsx')

# Calcular a contagem de cada opção
contagem_opcoes = df['Selecao'].explode().value_counts()

# Calcular as porcentagens correspondentes
total = contagem_opcoes.sum()
porcentagens = [(opcao, contagem / total * 100) for opcao, contagem in contagem_opcoes.items()]

# Ordenar por porcentagem em ordem decrescente
porcentagens.sort(key=lambda x: x[1], reverse=True)

# Lista de textos explicativos com porcentagens
porcentagem_por_escolha = [
    f"[{opcao:.0f}] - {porcentagem:.1f}%" for opcao, porcentagem in porcentagens
]
textos_explicativos = [
    f"[1] - Publicidade por televisão/rádio.",
    f"[2] - Publicidade online ou Pesquisa online.",
    f"[3] - Recomendação de amigos ou Familiares.",
    f"[4] - Busca boca a boca.",
    f"[5] - Eventos ou feiras.",
    f"[6] - Propagandas em lojas físicas, outdoor, anúncios móveis.",
    f"[7] - Panfletagem.",
    f"[8] - Informado por técnicos."
]

# Criar uma figura maior para acomodar o gráfico e as informações
plt.figure(figsize=(18, 8))

# Adicionar o gráfico de pizza à esquerda
plt.subplot(1, 2, 1)
plt.pie(contagem_opcoes, labels=contagem_opcoes.index, autopct='%1.1f%%', startangle=180)
plt.axis('equal')  # Para garantir que o gráfico de pizza seja um círculo
plt.text(-0.3, 1.3, 'Gráfico por porcentagem:', fontsize=13, ha='left', va='center')

# Adicionar informações à direita
plt.subplot(1, 2, 2)
texto_explicativo = '\n'.join(textos_explicativos)  # Juntar os textos com quebra de linha
plt.text(0.1, 0.37, 'Números e suas referências:', fontsize=13, ha='left', va='center')
plt.text(0.1, 0.2, texto_explicativo, fontsize=13, ha='left', va='center')
plt.axis('off')  # Para ocultar os eixos e criar espaço para o texto

# Adicionar informações à direita
plt.subplot(1, 2, 2)
texto_explicativo = '\n'.join(porcentagem_por_escolha)  # Juntar os textos com quebra de linha
plt.text(0.1, 1.1, 'Maiores porcentagens de acordo com opções marcadas:', fontsize=13, ha='left', va='center')
plt.text(0.1, 0.93, texto_explicativo, fontsize=13, ha='left', va='center')
plt.axis('off')  # Para ocultar os eixos e criar espaço para o texto

# Mostrar a figura
plt.show()
