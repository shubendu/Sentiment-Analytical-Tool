import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output,Input
import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd
from collections import OrderedDict
import dash_table
import plotly.graph_objects as go
import plotly.express as px

card_content1 = [
    dbc.CardBody(
        [
        html.H5("Sentiment Classes", className="card-title"),
        html.P(
            "Positive, Negative and Neutral",className="card-text",
        ),
        ]
    ),
]

card_content2 = [
    dbc.CardBody(
        [
            html.H5("Total Number of Reviews", className="card-title"),
            html.P(
                "161,297",
                className="card-text",
            ),
        ]
    ),
]

card_content3 = [
    dbc.CardBody(
        [
            html.H5("Time Span of Reviews", className="card-title"),
            html.P(
                "April 1, 2008 to September 9, 2017",
                className="card-text",
            ),
        ]
    ),
]

card_content4 = [
    dbc.CardBody(
        [
            html.H5("Ratings Range ", className="card-title"),
            html.P(
                "1 to 10, where 1 is the lowest score and 10 is the highest",
                className="card-text",
            ),
        ]
    ),
]

card_content5 = [
    dbc.CardBody(
        [
            html.H5("Products ", className="card-title"),
            html.P(
                "Various Drug and their compounds",
                className="card-text",
            ),
        ]
    ),
]

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


dfiris = px.data.iris()  # iris is a pandas DataFrame
figiris = px.scatter(dfiris, x="sepal_width", y="sepal_length")

df1 = pd.read_csv('df1.csv')
all_df = pd.read_csv('train.csv')


size = [68005, 46901, 36708, 25046, 12547, 10723, 8462, 6671]
labels = "10", "1", "9", "8", "7", "5", "6", "4"
fig_ratings = px.pie(values=size, names=labels, title='Pie Chart Representation of Ratings',)
fig_ratings.update_layout(
    title={
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'})


temp = all_df.groupby('sentiment').count()['review_body'].reset_index().sort_values(by='review_body',ascending=False)
fig_pie = go.Figure(go.Funnelarea(
    text =temp.sentiment,
    values = temp.review_body,
    title = {"position": "top center", "text": "Funnel-Chart of Sentiment Distribution"}
    ))



app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP],
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}]
                )
df1['id'] = df1.index



#main_layout
app.layout = dbc.Container([

    #1st row
    dbc.Row([
    dbc.Col(html.H1("Sentiment Analytics Tool",
                    className='text-center text-primary, mb-5'),
                    width=12 )
    ,html.Br(className='mb-5') 
    ]),

    #2nd row
    dbc.Row(
    [
        dbc.Col(dbc.Card(card_content1, outline=True)),
        dbc.Col(dbc.Card(card_content2, outline=True)),
        dbc.Col(dbc.Card(card_content3, outline=True)),
        dbc.Col(dbc.Card(card_content4, outline=True)),
        dbc.Col(dbc.Card(card_content5, outline=True)),
    ],
    className="mb-4",
    ),html.Hr(className='mb-5'),
    #3rd row
   dbc.Row([ 
    dbc.Col([
    html.H3("Dataframe",
            className='text-center')
            ,
            
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
],width={'size':6,'offset':0}), #col


dbc.Col([
    html.H3("Distribution of Sentiments and Ratings",
            className='text-center'),
    dcc.Graph(figure=fig_pie),
    dcc.Graph(figure=fig_ratings),

],width={'size':6}),

]), 
#row4
html.Hr(className='mb-5'),
dbc.Row([
    html.H3("Distribution of top most common word used",
            className='text-center mb-5'),
    
    dbc.Col([
        dcc.Dropdown(id= '40-dropdown', 
        options=[
            {'label': i, 'value': i }
        for i in range(1,41)], 
        value='100'),
    
    dcc.Graph(id ='dd-output-container',figure={})
    ]),
    dbc.Col([
        dcc.Dropdown(id= '40-dropdown2', 
        options=[
            {'label': i, 'value': i }
        for i in range(1,41)], 
        value='100'),
    
    dcc.Graph(id ='dd-output-container2',figure={})
    ])
    ]),
#new row
# html.Hr(className='mb-5'),
# dbc.Row([
#     dcc.Dropdown(
#         id='demo-dropdown',
#         options=[
#             {'label': 'New York City', 'value': 'NYC'},
#             {'label': 'Montreal', 'value': 'MTL'},
#             {'label': 'San Francisco', 'value': 'SF'}
#         ],
#         value='NYC'
#     ),
#     html.Div(id='dd-output-container')
# ]),

#row5
html.Hr(className='mb-5'),
dbc.Row([
    
    dbc.Col([
        dcc.Dropdown(id= 'my-dpdn', value='10',
        options=[{'label': i, 'value': i }
        for i in range(1,11)]),
    
    dcc.Graph(id ='line-fig',figure={})

            ])
        ])

],fluid=True) #container

@app.callback(
    Output('dd-output-container2', 'figure'),
    Input('40-dropdown2', 'value')

)
def most_common_words_tree(value):
    from collections import Counter
    all_df['temp_list'] = all_df['review_body'].apply(lambda x:str(x).split())
    top = Counter([item for sublist in all_df['temp_list'] for item in sublist])
    temp = pd.DataFrame(top.most_common(value))
    temp.columns = ['Common_words','count']
    fig = px.treemap(temp, path=['Common_words'], values='count',title=f' Tree of top {len(temp)} most common words')
    return fig



#top n common words
@app.callback(
    Output('dd-output-container', 'figure'),
    Input('40-dropdown', 'value')
)
def most_common_words(value):
    from collections import Counter
    all_df['temp_list'] = all_df['review_body'].apply(lambda x:str(x).split())
    top = Counter([item for sublist in all_df['temp_list'] for item in sublist])
    temp = pd.DataFrame(top.most_common(value))
    temp.columns = ['Common_words','count']
    fig = px.bar(temp, x="count", y="Common_words", title=f'Distribution of top {len(temp)} most common words', orientation='h',color='Common_words')
    return fig

# @app.callback(
#     Output('dd-output-container', 'children'),
#     Input('demo-dropdown', 'value')
# )
# def update_output(value):
#     return 'You have selected "{}"'.format(value)




# Drugs according to ratings
@app.callback(
    Output('line-fig', 'figure'),
    Input('my-dpdn', 'value')
)
def rating_drug(rate):
    top_10 = all_df[all_df.rating == rate]['drugName'].value_counts()[:10]
    fig = go.Figure()
    fig = px.bar(x=top_10.index,y=top_10,
    title=f'Top 10 drugs with {rate} ratings',color=top_10)
    return fig


if __name__ =='__main__':
    app.run_server(debug=True, port=4000)