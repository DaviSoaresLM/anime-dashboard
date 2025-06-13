import requests
import time
import json
import os

CACHE_FILE = "animes_cache.json"

def fetch_animes_by_year(year):
    url = "https://graphql.anilist.co"
    query = '''
    query ($year: Int) {
      Page(perPage: 50) {
        media(type: ANIME, seasonYear: $year, sort: POPULARITY_DESC) {
          title {
            romaji
          }
          popularity
          genres
          seasonYear
        }
      }
    }
    '''
    variables = {"year": year}

    try:
        response = requests.post(url, json={"query": query, "variables": variables}, timeout=10)
        response.raise_for_status()
        json_data = response.json()
        return [
            {
                "title": anime["title"]["romaji"],
                "popularity": anime["popularity"],
                "genres": anime["genres"],
                "year": anime.get("seasonYear", year),
            }
            for anime in json_data["data"]["Page"]["media"]
        ]
    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar dados do ano {year}: {e}")
        return []

def get_top_animes_range(start_year, end_year):
    # Tenta carregar cache
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r", encoding="utf-8") as f:
            print("Carregando dados do cache...")
            return json.load(f)

    print("Buscando dados da API AniList, aguarde...")
    all_animes = []
    for y in range(start_year, end_year + 1):
        print(f"Buscando ano: {y}")
        animes_year = fetch_animes_by_year(y)
        all_animes.extend(animes_year)
        time.sleep(1.5)  # pausa para evitar 429 Too Many Requests

    # Salva cache
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(all_animes, f, ensure_ascii=False, indent=2)

    return all_animes
