import dash
from dash import html, dcc, Input, Output
import plotly.express as px
from utils.anilist_api import get_top_animes

app = dash.Dash(__name__)
app.title = "Anime Popularity Dashboard"

# Dados
year = 2024
animes = get_top_animes(year)
all_genres = sorted({genre for anime in animes for genre in anime["genres"]})

# Layout
app.layout = html.Div(className="app-container", children=[
    html.H1("🎌 Anime Popularity Dashboard", className="logo-title"),
    html.H3(f"Dados de {year}", style={"textAlign": "center", "marginBottom": "20px"}),

    html.Div([
        html.Label("Filtrar por gênero:"),
        dcc.Dropdown(
            id="genre-dropdown",
            options=[{"label": g, "value": g} for g in all_genres],
            placeholder="Selecione um gênero"
        ),
    ], style={"marginBottom": "20px"}),

    html.Div([
        html.Label("Escolha o tipo de gráfico:"),
        dcc.Dropdown(
            id="chart-type-dropdown",
            options=[
                {"label": "Gráfico de Barras", "value": "bar"},
                {"label": "Gráfico de Pizza", "value": "pie"},
                {"label": "Gráfico de Dispersão", "value": "scatter"},
            ],
            value="bar"
        )
    ], style={"marginBottom": "20px"}),

    dcc.Graph(id="graph-output")
])

# Callback
@app.callback(
    Output("graph-output", "figure"),
    Input("genre-dropdown", "value"),
    Input("chart-type-dropdown", "value")
)
def update_graph(selected_genre, chart_type):
    if selected_genre:
        filtered = [a for a in animes if selected_genre in a["genres"]]
    else:
        filtered = animes

    filtered = sorted(filtered, key=lambda x: x["popularity"], reverse=True)[:10]

    if chart_type == "bar":
        return px.bar(
            x=[a["title"] for a in filtered],
            y=[a["popularity"] for a in filtered],
            labels={"x": "Anime", "y": "Popularidade"},
            title=f"Top 10 Animes - Gênero: {selected_genre or 'Todos'}"
        )

    elif chart_type == "pie":
        genre_counts = {}
        for a in filtered:
            for g in a["genres"]:
                genre_counts[g] = genre_counts.get(g, 0) + 1

        return px.pie(
            names=list(genre_counts.keys()),
            values=list(genre_counts.values()),
            title="Distribuição dos Gêneros"
        )

    elif chart_type == "scatter":
        return px.scatter(
            x=[a["ranking"] for a in filtered],
            y=[a["popularity"] for a in filtered],
            text=[a["title"] for a in filtered],
            labels={"x": "Ranking", "y": "Popularidade"},
            title="Popularidade vs Ranking",
            size=[a["popularity"] / 1000 for a in filtered],
        )

    return {}

# Run
if __name__ == "__main__":
    app.run(debug=True)
