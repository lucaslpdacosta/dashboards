from dash import Dash, html, dcc, dash_table
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

app.layout = html.Div([
    html.Div(
        className="my-header",
        children=[
            html.H1(children='Análises sobre países')
        ]
    ),
    html.Hr(),
    dash_table.DataTable(data=df.to_dict("records"), page_size=10)
])

if __name__ == '__main__':
    app.run(debug=True)