from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df = pd.DataFrame({
    "Points" : ["Praca","Lanchonete","Restaurante","Praca","Lanchonete","Restaurante"],
    "Frequencia" : [500, 3000, 1200, 200, 900, 400],
    "Cidades" : ["Currais Novos", "Currais Novos", "Currais Novos", "Sao Vicente", "Sao Vicente", "Sao Vicente"],
})

fig = px.bar(df, x="Points", y="Frequencia", color="Cidades", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Meu Primeiro Dashboard'),
    dcc.Graph(
        id="CN x SV",
        figure = fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)