import dash
from dash import html, dcc, Input, Output
import plotly.express as px
from utils.anilist_api import get_top_animes_range

animes = get_top_animes_range(2015, 2024)  # só carrega uma vez na inicialização

app = dash.Dash(__name__)
app.title = "Anime Popularity Dashboard"

# Carrega todos os animes de 2015 a 2024 na inicialização
animes = get_top_animes_range(2015, 2024)

all_genres = sorted({genre for anime in animes for genre in anime["genres"]})

app.layout = html.Div(className="app-container", children=[
    html.H1("🎌 Anime Popularity Dashboard", className="logo-title"),

    # Dropdown para selecionar o ano
    html.Div([
        html.Label("Selecionar ano:"),
        dcc.Dropdown(
            id="year-dropdown",
            options=[{"label": str(y), "value": y} for y in range(2015, 2025)],
            value=2024,
            clearable=False
        )
    ], style={"marginBottom": "20px"}),

    # Dropdown para filtrar por gênero
    html.Div([
        html.Label("Filtrar por gênero:"),
        dcc.Dropdown(
            id="genre-dropdown",
            options=[{"label": g, "value": g} for g in all_genres],
            placeholder="Selecione um gênero",
            clearable=True
        ),
    ], style={"marginBottom": "20px"}),

    # Dropdown para escolher tipo do gráfico
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

    dcc.Graph(id="graph-output", className="fade-in")
])

@app.callback(
    Output("graph-output", "figure"),
    Input("year-dropdown", "value"),
    Input("genre-dropdown", "value"),
    Input("chart-type-dropdown", "value")
)
def update_graph(selected_year, selected_genre, chart_type):
    filtered = [a for a in animes if a["year"] == selected_year]

    if selected_genre:
        filtered = [a for a in filtered if selected_genre in a["genres"]]

    # Ordena pela popularidade e limita p/ top 5
    filtered = sorted(filtered, key=lambda x: x["popularity"], reverse=True)[:5]

    if chart_type == "bar":
        return px.bar(
            x=[a["title"] for a in filtered],
            y=[a["popularity"] for a in filtered],
            color=[a["title"] for a in filtered],  # cor por título
            labels={"x": "Anime", "y": "Popularidade"},
            title=f"Top 5 Animes de {selected_year} - Gênero: {selected_genre or 'Todos'}",
        )

    elif chart_type == "pie":
        # Conta gêneros nos animes filtrados
        genre_counts = {}
        for a in filtered:
            for g in a["genres"]:
                genre_counts[g] = genre_counts.get(g, 0) + 1

        return px.pie(
            names=list(genre_counts.keys()),
            values=list(genre_counts.values()),
            title=f"Distribuição dos Gêneros Lançados em {selected_year}"
        )

    elif chart_type == "scatter":
        # Se o dado 'ranking' não existir, não pode fazer scatter; vamos usar popularity no eixo y e títulos no texto
        return px.scatter(
            x=[i+1 for i in range(len(filtered))],  # índice 1..n
            y=[a["popularity"] for a in filtered],
            text=[a["title"] for a in filtered],
            labels={"x": "Posição", "y": "Popularidade"},
            title=f"Popularidade Top 10 em {selected_year}",
            size=[a["popularity"] / 1000 for a in filtered],
        )

    return {}

if __name__ == "__main__":
    app.run(debug=True)
