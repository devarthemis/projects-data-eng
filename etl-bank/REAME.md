# Laboratório Prático: Aquisição e Processamento de Informações sobre os Maiores Bancos do Mundo

## Cenário

Você foi contratado como engenheiro de dados por uma organização de pesquisa. Seu chefe pediu que você criasse um código que possa ser usado para compilar a lista dos 10 maiores bancos do mundo classificados por capitalização de mercado em bilhões de USD. Além disso, os dados precisam ser transformados e armazenados em GBP, EUR e INR também, de acordo com as informações da taxa de câmbio que foram disponibilizadas para você como um arquivo CSV. A tabela de informações processadas deve ser salva localmente em formato CSV e como uma tabela de banco de dados.

Seu trabalho é criar um sistema automatizado para gerar essas informações para que o mesmo possa ser executado em cada trimestre financeiro para preparar o relatório.

## Tarefas do projeto
**Tarefa 1:** Escreva uma função log_progress() para registrar o progresso do código em diferentes estágios em um arquivo code_log.txt. Use a lista de pontos de log fornecida para criar entradas de log a cada estágio do código.

**Tarefa 2:** Extraia as informações tabulares da URL fornecida sob o título 'Por capitalização de mercado' e salve em um dataframe. a. Inspecione a página da web e identifique a posição e o padrão das informações tabulares no código HTML. b. Escreva o código para uma função extract() para realizar a extração de dados necessária. c. Execute uma chamada de função para extract() para verificar a saída.

**Tarefa 3:** Transforme o dataframe adicionando colunas para a Capitalização de Mercado em GBP, EUR e INR, arredondadas para 2 casas decimais, com base nas informações da taxa de câmbio compartilhadas como um arquivo CSV. a. Escreva o código para uma função transform() para realizar a tarefa mencionada. b. Execute uma chamada de função para transform() e verifique a saída.

**Tarefa 4:** Carregue o dataframe transformado em um arquivo CSV de saída. Escreva uma função load_to_csv(), execute uma chamada de função e verifique a saída.

**Tarefa 5:** Carregue o dataframe transformado em um servidor de banco de dados SQL como uma tabela. Escreva uma função load_to_db(), execute uma chamada de função e verifique a saída.

**Tarefa 6:** Execute consultas na tabela do banco de dados. Escreva uma função run_queries(), execute um conjunto de consultas fornecido e verifique a saída.

**Tarefa 7:** Verifique se as entradas de log foram concluídas em todas as etapas verificando o conteúdo do arquivo code_log.txt.