# Cenário do Projeto
Uma empresa internacional que busca expandir seus negócios em diferentes países do mundo recrutou você. Você foi contratado como um engenheiro de dados júnior e sua tarefa é criar um script automatizado que possa extrair a lista de todos os países em ordem de seus PIBs em bilhões de dólares (arredondados para 2 casas decimais), conforme registrado pelo Fundo Monetário Internacional (FMI). Como o FMI libera essa avaliação duas vezes por ano, esse código será usado pela organização para extrair as informações à medida que forem atualizadas.

Endereço dos dados necessários:
```
https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29
```

As informações necessárias precisam ser acessíveis como um arquivo JSON ‘Countries_by_GDP.json’ e também como uma tabela ‘Countries_by_GDP’ em um arquivo de banco de dados ‘World_Economies.db’ com os atributos ‘Country’ e ‘GDP_USD_billion’.

Seu chefe quer que você demonstre o sucesso deste código executando uma consulta na tabela do banco de dados para exibir apenas as entradas com uma economia superior a 100 bilhões de dólares. Além disso, registre todo o processo de execução em um arquivo chamado ‘etl_project_log.txt’.

Você deve criar um código Python ‘etl_project_gdp.py’ que execute todas as tarefas necessárias.