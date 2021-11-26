import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output,Input
import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd
from collections import OrderedDict
import dash_table


card = dbc.Card(
    dbc.CardBody(
        [
            html.H4("Title", id="card-title"),
            html.H2("100", id="card-value"),
            html.P("Description", id="card-description")
        ]
    )
)

card2 = dbc.Card(
    dbc.CardBody(
        [
            html.H4("Title2", id="card-title2"),
            html.H2("100", id="card-value2"),
            html.P("Description", id="card-description2")
        ]
    )
)



df = pd.read_csv("my_stocks.csv")
df1 = pd.read_csv('df1.csv')
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP],
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}]
                )
df1['id'] = df1.index

app.layout = dbc.Container([
    dbc.Row([
    dbc.Col(html.H1("Sentiment Analytics Tool",
                    className='text-center text-primary, mb-5'),
                    width=12 )

    ]),
   dbc.Row([ 
    dbc.Col([
    dash_table.DataTable(
    page_size=20,
    style_table={'height': '800px', 'overflowY': 'auto'},
    style_data={
        'whiteSpace': 'normal',
        'height': 'auto',
    },
    style_cell = {
                'font_family': 'cursive',
                'font_size': '14px',
                'text_align': 'center',
                'overflow': 'hidden',
                'textOverflow': 'ellipsis',
            },
    data=df1.to_dict('records'),
    sort_action='native',
    columns=[
        {'name': 'review_body', 'id': 'review_body', 'type': 'text', 'editable': False},
        {'name': 'sentiment', 'id': 'sentiment', 'type': 'text', 'editable': False},
        {'name': 'condition', 'id': 'condition', 'type': 'text', 'editable': False},
        {'name': 'rating', 'id': 'rating', 'type': 'text', 'editable': False},

    ],
    editable=True,
    style_data_conditional=[
        {
            'if': {
                'filter_query': '{sentiment} = "Positive"',
                'column_id': 'sentiment'
            },
            'color': 'green'
        },
        {
            'if': {
                'filter_query': '{sentiment} = "Negative"',
                'column_id': 'sentiment'
            },
            'color': 'red'
        },
        {
            'if': {
                'filter_query': '{sentiment} = "Neutral"',
                'column_id': 'sentiment'
            },
            'color': '#FFC300'
        },
        
    ]
)
],width={'size':7,'offset':0}), #col


dbc.Col([
    dcc.Graph(id='line-fig3', figure={}),
    dcc.Graph(id='line-fig2', figure={}),

]),


]), #row1

dbc.Row([
    
    dbc.Col([
        dcc.Dropdown(id= 'my-dpdn', multi=False, value='AMZN',
        options=[{'label': x, 'value': x }
        for x in sorted(df['Symbols'].unique())]),
    
    dcc.Graph(id ='line-fig',figure={})
    ],width={'size':5,'offset':0,'order':1})

    ])



],fluid=True) #container




# Line chart - Single
@app.callback(
    Output('line-fig', 'figure'),
    Input('my-dpdn', 'value')
)
def update_graph(stock_slctd):
    dff = df[df['Symbols']==stock_slctd]
    figln = px.line(dff, x='Date', y='High')
    return figln

if __name__ =='__main__':
    app.run_server(debug=True, port=4000)