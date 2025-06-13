import requests

def get_top_animes(year=2024):
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
        }
      }
    }
    '''
    variables = {"year": year}
    response = requests.post(url, json={"query": query, "variables": variables})
    data = response.json()

    result = []
    for anime in data.get("data", {}).get("Page", {}).get("media", []):
        # Garantir que "genres" existe e é lista
        genres = anime.get("genres") or []
        result.append({
            "title": anime["title"]["romaji"],
            "popularity": anime["popularity"],
            "genres": genres
        })
    return result
