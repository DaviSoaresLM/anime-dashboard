import dash
from dash import html, dcc
import plotly.express as px
from utils.anilist_api import get_top_animes

# Busca de dados
year = 2024
animes = get_top_animes(year)
titles = [anime["title"] for anime in animes]
popularities = [anime["popularity"] for anime in animes]

# Gráfico
fig = px.bar(
    x=titles,
    y=popularities,
    labels={"x": "Anime", "y": "Popularidade"},
    title=f"Top 10 Animes de {year}"
)

# App Dash
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1(f"Top 10 Animes - {year}", style={"textAlign": "center"}),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run_server(debug=True)
