import dash
from dash import html, dcc, Input, Output
import plotly.express as px
from utils.anilist_api import get_top_animes

app = dash.Dash(__name__)

# Dados
year = 2024
animes = get_top_animes(year)

# Lista de gêneros únicos
all_genres = sorted({genre for anime in animes for genre in anime["genres"]})

app.layout = html.Div([
    html.H1(f"Dashboard Interativo - Animes {year}", style={"textAlign": "center"}),

    dcc.Dropdown(
        id="genre-dropdown",
        options=[{"label": g, "value": g} for g in all_genres],
        placeholder="Selecione um gênero"
    ),

    dcc.Graph(id="bar-popularity"),
    dcc.Graph(id="pie-genres"),
])


@app.callback(
    Output("bar-popularity", "figure"),
    Output("pie-genres", "figure"),
    Input("genre-dropdown", "value")
)
def update_graphs(selected_genre):
    if selected_genre:
        filtered = [a for a in animes if selected_genre in a["genres"]]
    else:
        filtered = animes

    # Gráfico de barras (top 10 por popularidade)
    filtered = sorted(filtered, key=lambda x: x["popularity"], reverse=True)[:10]
    bar_fig = px.bar(
        x=[a["title"] for a in filtered],
        y=[a["popularity"] for a in filtered],
        labels={"x": "Anime", "y": "Popularidade"},
        title=f"Top 10 Animes - Gênero: {selected_genre or 'Todos'}"
    )

    # Gráfico de pizza com distribuição dos gêneros no filtro atual
    genre_counts = {}
    for a in filtered:
        for g in a["genres"]:
            genre_counts[g] = genre_counts.get(g, 0) + 1
    pie_fig = px.pie(
        names=list(genre_counts.keys()),
        values=list(genre_counts.values()),
        title="Distribuição dos Gêneros"
    )

    return bar_fig, pie_fig


if __name__ == "__main__":
    app.run_server(debug=True)
