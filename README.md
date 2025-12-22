# 📊 Análise Estatística de Notas do ENEM

Projeto de análise estatística aplicada a dados reais do ENEM (Exame Nacional do Ensino Médio), desenvolvido em Python com Pandas.

## 📋 Sobre o Projeto

Este projeto realiza análise estatística completa das notas de Matemática do ENEM, calculando:

- **Média** das notas
- **Percentil 90** (nota que deixa 10% dos alunos acima)
- **Probabilidade** de um aluno ter nota inferior a 450
- **Probabilidade condicional** de nota superior a 800, dado que a nota é superior a 700

## 🎯 Enunciado do Problema

**Contexto:** Você é um analista de dados trabalhando para o Ministério da Educação e precisa analisar o desempenho dos estudantes na prova de Matemática do ENEM.

**Tarefa:** Desenvolver um programa que:

a) Calcule a **média** das notas de Matemática  
b) Determine o **percentil 90** (a nota que deixa apenas 10% dos alunos acima dela)  
c) Calcule a **probabilidade** de um aluno escolhido aleatoriamente ter nota inferior a 450  
d) Calcule a **probabilidade condicional**: P(nota > 800 | nota > 700)  

**Dados:** Arquivo CSV contendo notas reais de Matemática do ENEM (`NU_NT_MT`)

## 🚀 Como Executar

### Pré-requisitos

- Python 3.7 ou superior
- Pandas

### Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/analise-enem-estatistica.git
cd analise-enem-estatistica
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Execute o programa:
```bash
python Main.py
```

## 📊 Exemplo de Saída

```
--------------------------------------------------
  SUCESSO! Análise completa da coluna 'NU_NT_MT':

   a) A média das notas é: 535.67
   b) A nota com 10% da amostra na frente é: 698.40
   c) A probabilidade de um aluno ter nota < 450 é: 28.45%
   d) Dado que um aluno tirou > 700, a probabilidade de ele ter tirado > 800 é: 15.32%
```

## 🛠️ Tecnologias Utilizadas

- **Python 3.12**
- **Pandas** - Análise e manipulação de dados
- **CSV** - Formato dos dados do ENEM

## 📁 Estrutura do Projeto

```
analise-enem-estatistica/
├── README.md                    # Documentação do projeto
├── Main.py                      # Código principal
├── requirements.txt             # Dependências
└── media/
    └── enem_mat_amostra.csv    # Dados de amostra do ENEM
```

## 💡 Conceitos Aplicados

- Estatística descritiva (média, percentis)
- Probabilidade básica
- Probabilidade condicional
- Análise de dados com Pandas
- Tratamento de dados ausentes/inválidos

## 👤 Autor

Desenvolvido como projeto de análise estatística aplicada.

## 📝 Licença

Este projeto está sob a licença MIT. Sinta-se livre para usar e modificar.

---

⭐ Se este projeto foi útil, considere dar uma estrela no GitHub!
