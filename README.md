# 📊 Dashboard de Popularidade de Animes

Este projeto é uma aplicação web interativa desenvolvida com a biblioteca [Dash](https://dash.plotly.com/) (Plotly) em Python. O objetivo é apresentar a popularidade dos animes ao longo dos anos, com base em dados coletados da [AniList API](https://anilist.co/graphiql) via GraphQL.

---

## 🎯 Objetivo

Criar um dashboard dinâmico e visualmente atrativo para explorar e entender tendências de popularidade dos animes entre os anos de **2015 a 2024**, incluindo:

- 📅 Filtragem por ano
- 🎭 Filtragem por gênero
- 📊 Seleção entre diferentes tipos de gráficos (barras, pizza ou dispersão)
- 🏆 Visualização dos **Top 5 animes** mais populares por ano

---

## 🖼️ Funcionalidades

- **Dropdowns interativos** para ano, gênero e tipo de gráfico
- **Gráficos animados** e responsivos usando Plotly
- **Armazenamento em cache** local para evitar múltiplas requisições à API
- **Interface visual moderna**, com fundo estilizado e responsivo

---

## 🛠️ Tecnologias Utilizadas

- [Python 3.10+](https://www.python.org/)
- [Dash](https://dash.plotly.com/)
- [Plotly Express](https://plotly.com/python/plotly-express/)
- [Requests](https://docs.python-requests.org/)
- [AniList API (GraphQL)](https://anilist.co/graphiql)
- HTML + CSS (customizado com animações e Google Fonts)

---

## 📁 Estrutura do Projeto

```plaintext
anime-dashboard/
├── app.py                # Código principal da aplicação Dash
├── utils/
│   └── anilist_api.py    # Funções de busca e cache da API AniList
├── assets/
│   └── style.css         # Estilos visuais customizados para o dashboard
├── animes_cache.json     # Cache local com os dados da API
├── requirements.txt      # Dependências do projeto
└── README.md             # Documentação do projeto
