# 📊 Dashboard de Popularidade de Animes

Este projeto consiste em uma aplicação web interativa desenvolvida com a biblioteca [Dash (Plotly)](https://dash.plotly.com/) em Python. O objetivo é apresentar a popularidade de animes ao longo dos anos utilizando visualizações de dados baseadas em informações coletadas de fontes como **AniList** e **MyAnimeList**.

## 🎯 Objetivo

Criar um dashboard interativo para contar histórias com dados (**data storytelling**) sobre a popularidade de animes em diferentes contextos, como:

- Evolução da popularidade ao longo dos anos
- Gêneros de anime mais populares
- Top 10 animes por ano ou temporada
- Plataformas de streaming mais influentes
- Destaques recentes no crescimento de popularidade

## 🛠️ Tecnologias Utilizadas

- [Python 3.10+](https://www.python.org/)
- [Dash](https://dash.plotly.com/)
- [Plotly](https://plotly.com/python/)
- [Pandas](https://pandas.pydata.org/)
- [Requests](https://docs.python-requests.org/)
- [AniList API (GraphQL)](https://anilist.gitbook.io/anilist-apiv2-docs/)

## 📁 Estrutura do Projeto
📦 anime-dashboard
┣ 📊 assets/
┣ 📄 app.py
┣ 📄 requirements.txt
┣ 📄 dataset.csv (opcional)
┗ 📄 README.md

## 📈 Funcionalidades

- Filtro interativo por ano, gênero ou estúdio
- Visualização de rankings e avaliações
- Gráficos de linha, barras e pizza para análise
- Interface simples e responsiva
- Conexão com API externa (AniList) para dados em tempo real (opcional)

🔍 Fontes de Dados
- AniList — Dados de animes, rankings e avaliações via API GraphQL
- MyAnimeList — Informações detalhadas de animes populares, notas e popularidade
- Kitsu.io — Base de dados alternativa com dados similares aos anteriores
- Reddit /r/anime — Tendências e discussões da comunidade sobre animes populares

👨‍💻 Autores
DaviSoaresLM (@DaviSoaresLM)