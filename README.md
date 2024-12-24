# Projeto BETCORNERPRO
BETCORNERPRO é um sistema de análise esportiva que tem como objetivo fornecer insights e informações sobre o desempenho de times de futebol, com foco em escanteios e outros dados relevantes para apostas esportivas.

Principal funcionalidade implementada faz consulta em uma API de futebol para obter as últimas partidas de um time, permitindo realizar análises sobre o histórico recente de jogos.

# Objetivo da Funcionalidade
A funcionalidade implementada busca as últimas partidas de futebol de um time específico, em uma liga e temporada determinadas. Esta funcionalidade é essencial para sistemas de análise esportiva, pois fornece informações sobre o desempenho recente de um time, o que pode ser utilizado para prever comportamentos futuros em jogos, como a quantidade de escanteios ou outros parâmetros de interesse.

### A funcionalidade é composta pelos seguintes passos:

1. Entrada de Dados:

    * team_id: O ID do time, usado para identificar unicamente o time na API-Football.
    * league_id: O ID da liga onde o time está competindo, como Premier League, La Liga, etc.
    * season: O ano da temporada para a qual as partidas serão consultadas (ex: 2022 - essa versão só funciona até 2022).

2. Requisição à API-Football: O sistema faz uma requisição à API-Football utilizando os parâmetros acima. A API retorna uma lista das últimas partidas do time na temporada e liga especificadas.

3. Processamento dos Dados: O sistema processa a resposta da API e extrai as informações relevantes, como:

    * Data e hora do jogo.
    * Nome do time da casa e do time visitante.
    * Resultado do jogo (quantidade de gols de cada time).

4. Saída de Dados: A funcionalidade exibe as informações das últimas partidas de forma legível, facilitando a análise dos resultados.

    ## Como Usar
    1. Requisitos:

        * Python 3.x
        * Biblioteca requests para consumir a API-Football.
        * Uma chave API da API-Football (obtenha a chave em RapidAPI).

    2. Passos para rodar:    
        * Instale a biblioteca requests:
            ``pip install requests``

    3. Atualize a chave API no arquivo app.py:
        `` API_KEY = 'SUA_CHAVE_API' ``

    4. Execute o script:
        `` python app.py ``

    5. Obter Sua Chave API:
    * Acesse https://www.api-football.com/.
    * Ao se cadastrar, você será automaticamente inscrito no plano gratuito, que oferece 100 requisições por dia e acesso a todos os endpoints e competições disponíveis.
    * Para obter sua chave API, faça login no painel de controle, vá para a seção "Minha Acesso" e copie sua chave API. Você pode começar a usá-la imediatamente para fazer requisições aos nossos serviços.
    * Caso precise de mais informações, consulte a seção de perfil em https://dashboard.api-football.com/profile?access. 

5. Exemplo de Uso: O código busca as últimas partidas do Manchester United na Premier League para a temporada de 2022, conforme o seguinte exemplo:

         `` team_id = 33  # ID do Manchester United
            league_id = 39  # Premier League
            season = 2022  # Temporada 2022

            fixtures = get_team_fixtures(team_id, league_id, season)
            if fixtures:
                for match in fixtures['response']:
                    home_team = match['teams']['home']['name']
                    away_team = match['teams']['away']['name']
                    date = match['fixture']['date']
                    print(f"{date}: {home_team} vs {away_team}")  ``

# Detalhes da API
A API utilizada é a API-Football da RapidAPI, que fornece dados detalhados sobre futebol, como partidas, estatísticas de times, jogadores e ligas.

* Endpoint: /fixtures
* Parâmetros:

     * team: ID do time.
     * league: ID da liga.
     * season: Temporada.
     * last: Número de partidas recentes a serem retornadas (não disponível no plano gratuito).
 * Resposta: A resposta contém informações como:

* Data do jogo.
    * Time da casa e time visitante.
    * Resultado do jogo (gols marcados).
    * Status da partida (finalizada, em andamento, etc.)