import requests

# Configuração
API_KEY = '96eedeeda512cad758924cc9fb35a2dd'
BASE_URL = 'https://v3.football.api-sports.io'
HEADERS = {
    'x-rapidapi-host': 'v3.football.api-sports.io',
    'x-rapidapi-key': API_KEY
}


def get_team_fixtures(team_id, league_id, season):
    """
    Obtém as partidas de um time específico.

    :param team_id: ID do time na API-Football
    :param league_id: ID da liga
    :param season: Temporada (ex: 2022)
    :return: Lista de partidas
    """
    url = f"{BASE_URL}/fixtures"
    params = {
        'team': team_id,
        'league': league_id,
        'season': season,
        # Removido o parâmetro 'last' para evitar erro no plano gratuito
    }

    # Requisição à API
    response = requests.get(url, headers=HEADERS, params=params)

    # Mensagens de depuração (removidas para a versão final)
    # print(f"Status Code: {response.status_code}")  # Status da requisição
    # print("Resposta da API:")
    # print(response.json())  # Mostra o JSON completo, pode ser útil para debug, mas removido aqui

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erro: {response.status_code} - {response.text}")
        return None


# Exemplo de uso
team_id = 33  # Exemplo: Manchester United
league_id = 39  # Premier League
season = 2022  # Temporada permitida no plano gratuito

fixtures = get_team_fixtures(team_id, league_id, season)
if fixtures:
    print("Partidas encontradas:")
    for match in fixtures.get('response', []):
        home_team = match['teams']['home']['name']
        away_team = match['teams']['away']['name']
        date = match['fixture']['date']
        print(f"{date}: {home_team} vs {away_team}")
else:
    print("Nenhuma partida encontrada ou erro na requisição.")
