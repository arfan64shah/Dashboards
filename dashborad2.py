import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px

app = dash.Dash()

app.layout = html.Div([
    html.H1('My Dashboard'),
    dcc.Graph(id='plot', figure={
        'data': [{
            'x': [1, 2, 3, 4, 5],
            'y': [1, 4, 9, 16, 25]
        }],
        'layout': {
            'title': 'Plot of Y vs X'
        }
    })
])

if __name__ == '__main__':
    app.run_server()