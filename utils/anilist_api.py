import requests

def get_top_animes(year=2024):
    url = "https://graphql.anilist.co"
    query = '''
    query ($year: Int) {
      Page(perPage: 10) {
        media(type: ANIME, seasonYear: $year, sort: POPULARITY_DESC) {
          title {
            romaji
          }
          popularity
        }
      }
    }
    '''
    variables = {"year": year}
    response = requests.post(url, json={"query": query, "variables": variables})
    data = response.json()
    return [
        {
            "title": anime["title"]["romaji"],
            "popularity": anime["popularity"]
        }
        for anime in data["data"]["Page"]["media"]
    ]
