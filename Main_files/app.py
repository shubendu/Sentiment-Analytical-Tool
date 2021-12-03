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
import numpy as np
from plotly import tools
config = {'displayModeBar': True}
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


# dfiris = px.data.iris()  # iris is a pandas DataFrame
# figiris = px.scatter(dfiris, x="sepal_width", y="sepal_length")

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
fig_ratings['layout'].update( paper_bgcolor='rgb(255,255,255)')


temp = all_df.groupby('sentiment').count()['review_body'].reset_index().sort_values(by='review_body',ascending=False)
fig_pie = go.Figure(go.Funnelarea(
    text =temp.sentiment,
    values = temp.review_body,
    title = {"position": "top center", "text": "Funnel-Chart of Sentiment Distribution"}
    ))
fig_pie['layout'].update( paper_bgcolor='rgb(255,255,255)')


#top 10 condition
values_cond = [28788, 9069, 6145, 5904, 5588]

top_10_condition = ['Birth Control', 'Depression', 'Pain', 'Anxiety', 'Acne']
fig_top10 = px.pie(values=values_cond, names=top_10_condition)
fig_top10['layout'].update( paper_bgcolor='rgb(255,255,255)',width=300)


#top unique negative words
Unique_Negative = pd.read_csv('un_negi.csv')[:20]
fig_neg = px.treemap(Unique_Negative, path=['words'], values='count',title="Top 20 unique negative words")
fig_neg['layout'].update(title={
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'}, paper_bgcolor='rgb(255,255,255)')


Unique_Positive = pd.read_csv('un_posi.csv')[:20]
fig_posi = px.treemap(Unique_Positive, path=['words'], values='count',title="Top 20 unique positive words")
fig_posi['layout'].update(title={
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'}, paper_bgcolor='rgb(255,255,255)')


Unique_Neutral = pd.read_csv('un_neut.csv')[:40]
fig_neut = px.treemap(Unique_Neutral, path=['words'], values='count',title="Top 40 unique neutral words")
fig_neut['layout'].update(title={
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'}, paper_bgcolor='rgb(255,255,255)')






    

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
    ),
    #3rd row
   dbc.Row([ 
    dbc.Col([
    html.H3("Dataframe",
            className='text-center mt-5')
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
            className='text-center mt-5'),
    dcc.Graph(figure=fig_pie),
    dcc.Graph(figure=fig_ratings),

],width={'size':6}),

]), 
#row4
#html.Hr(className='mb-5'),
dbc.Row([
    html.H3("Distribution of top most common word used",
            className='text-center mt-5'),
    
    dbc.Col([
        dcc.Dropdown(id= '40-dropdown', 
        options=[
            {'label': i, 'value': i }
        for i in range(1,41)], 
        value=15),
    
    dcc.Graph(id ='dd-output-container',figure={},config={
			'displayModeBar':False})
    ]),
    dbc.Col([
        dcc.Dropdown(id= '40-dropdown2', 
        options=[
            {'label': i, 'value': i }
        for i in range(1,41)], 
        value=15),
    
    dcc.Graph(id ='dd-output-container2',figure={})
        ])
    ]),


#row5
#top 15 ratings and condition
#html.Hr(className='mb-5'),
dbc.Row([
    
    dbc.Col([
    html.H3("Topmost Drugs",
            className='text-center mt-5'),
    dcc.Dropdown(id= 'my-dpdn', value=10,
    options=[{'label': i, 'value': i }
    for i in range(1,11)]),

    dcc.Graph(id ='line-fig',figure={},config={
			'displayModeBar':False})

            ],width={'size':8,'offset':0}),

    dbc.Col([
    html.H3("Top Conditions",
            className='text-center mt-5'),
    dcc.Dropdown(id= 'my-dpdn2', value=10,
    options=[{'label': i, 'value': i }
    for i in range(1,21)]),

    dcc.Graph(id ='line-fig2',figure={},config={
			'displayModeBar':False})

             ])
    ]),

#row6
#ngrams
dbc.Row([

    dbc.Col([
    html.H3("Distribution of Top n-grams sentiment wise",className='text-center mt-5'),
        dcc.Dropdown(id= 'dpdn4',
        options=[
            {'label': i, 'value': i }
        for i in ['unigram', 'bigram','trigram','4-gram']], 
        value='bigram'),

    dcc.Graph(id='ngram_plot',figure={},config={
			'displayModeBar':False})

            ]),
        ]),


#row7
#unique words
dbc.Row([
 html.H3("Top unique words sentiment wise",className='text-center mt-5'),
    dbc.Col([
        dcc.Graph(figure=fig_posi,config={
			'displayModeBar':False})

            ],width={'size':6,'offset':0}),
        dbc.Col([
        dcc.Graph(figure=fig_neut,config={
			'displayModeBar':False})

            ],width={'size':6,}),
        dbc.Col([
        dcc.Graph(figure=fig_neg,config={
			'displayModeBar':False})

            ],width={'size':12}),
        ]),
    

#row8
#category wise
dbc.Row([ 
    dbc.Col([
        html.H3("Category wise sentiment analysis of drugs", className='text-center mt-5'),
        dcc.Dropdown(id= 'dpdn5',
        options=[
            {'label': i, 'value': i }
        for i in top_10_condition], 
        value='Birth Control'),
        dcc.Graph(id='condition_plot',figure={},config={
			'displayModeBar':False
		})
    ],width = 8),
    dbc.Col([
        html.H3("Top 5 most popular conditions", className='text-center mt-5'),
        dcc.Graph(figure=fig_top10),
    ]),


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
    temp = pd.DataFrame(top.most_common(int(value)))
    temp.columns = ['Common_words','count']
    fig = px.treemap(temp, path=['Common_words'], values='count',title=f' Tree of top {len(temp)} most common words')
    fig['layout'].update( paper_bgcolor='rgb(233,233,233)')
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
    temp = pd.DataFrame(top.most_common(int(value)))
    temp.columns = ['Common_words','count']
    fig = px.bar(temp, x="count", y="Common_words", title=f'Distribution of top {len(temp)} most common words', orientation='h',color='Common_words')
    fig['layout'].update( paper_bgcolor='rgb(233,233,233)')
    return fig



# Drugs according to ratings
@app.callback(
    Output('line-fig', 'figure'),
    Input('my-dpdn', 'value')
)
def rating_drug(rate):
    top_10 = all_df[all_df.rating == rate]['drugName'].value_counts()[:15]
    fig = px.bar(x=list(top_10.index), y=top_10, title=f'Top 15 drugs with {rate} ratings',color=top_10,labels=dict(x="Count", y="Drug Name", sex="Payer Gender"))
    fig['layout'].update( paper_bgcolor='rgb(233,233,233)')
    return fig


@app.callback(
    Output('line-fig2', 'figure'),
    Input('my-dpdn2', 'value')
)
def top_cond(val):
    top_conditions = ['Birth Control','Depression','Pain','Anxiety','Acne','Bipolar Disorde','Insomnia','Weight Loss',
                        'Obesity','ADHD','Diabetes, Type 2','Emergency Contraception','High Blood Pressure','Vaginal Yeast Infection','Abnormal Uterine Bleeding','Bowel Preparation',
                        'ibromyalgia',
                        'Smoking Cessation',
                        'Migraine',
                        'Anxiety and Stress']
    top_conditions_values = [28788,9069,6145,5904,5588,4224, 3673,3609,3568,3383,2554,2463,2321,2274, 2096,1859,1791,
                                1780,1694,1663]
    top_conditions = top_conditions[:val]
    top_conditions_values = top_conditions_values[:val]
    
    fig = px.bar(x=top_conditions, y=top_conditions_values, title=f'Top {val} conditions',color=top_conditions,labels=dict(x="Condition Name", y="", sex="Payer Gender"))
    fig['layout'].update( paper_bgcolor='rgb(233,233,233)')
    return fig


@app.callback(
    Output('ngram_plot', 'figure'),
    Input('dpdn4', 'value'))
def n_gram(value):
    if value=='unigram':
        #ngram
        trace0 = go.Bar({
        'marker': {'color': 'blue'},
        'orientation': 'h',
        'showlegend': False,
        'x': np.array([ 6062,  6156,  6318,  6343,  6364,  6392,  6451,  6476,  6531,  6762,
        6800,  6812,  7142,  7460,  7521,  7555,  7629,  7656,  7693,  8031,
        8340,  8358,  8552,  9116,  9338,  9398,  9527,  9627,  9632,  9698,
        9977, 10022, 10149, 10862, 11756, 12407, 13086, 13352, 13506, 13939,
        14180, 14781, 15272, 15840, 17238, 17548, 18342, 23680, 26568, 28733]),
        'y': np.array(['night', 'sleep', 'anxieti', 'cramp', 'two', 'birth', 'hour', 'made',
        'last', 'drug', 'went', 'sinc', 'even', 'bleed', 'gain', 'felt',
        'weight', 'sever', 'control', 'depress', 'help', 'still', 'bad', 'one',
        'never', 'medic', 'back', 'tri', 'got', 'mg', 'took', 'doctor', 'use',
        'stop', 'go', 'first', 'period', 'side', 'work', 'year', 'pill', 'time',
        'feel', 'effect', 'pain', 'start', 'week', 'month', 'take', 'day'],
        dtype=object)
        })

        trace1 = go.Bar({
        'marker': {'color': 'blue'},
        'orientation': 'h',
        'showlegend': False,
        'x': np.array([13924, 14123, 14647, 14887, 14915, 15016, 15033, 15504, 15656, 15666,
        15781, 15885, 15988, 16022, 16606, 16870, 16994, 17389, 17545, 17642,
        17661, 17890, 18424, 19502, 19844, 20865, 21385, 22016, 22457, 22713,
        23695, 27131, 27271, 27322, 27556, 30294, 32325, 35534, 36085, 37166,
        37600, 39387, 40170, 40205, 46138, 48009, 48517, 52082, 69062, 71003]),
        'y': np.array(['even', 'stop', 'everi', 'night', 'control', 'went', 'two', 'depress',
        'well', 'last', 'good', 'hour', 'sleep', 'still', 'bad', 'better',
        'great', 'got', 'much', 'anxieti', 'realli', 'took', 'sinc', 'medicin',
        'weight', 'life', 'doctor', 'back', 'one', 'go', 'medic', 'period',
        'pill', 'help', 'tri', 'use', 'first', 'mg', 'time', 'feel', 'pain',
        'start', 'side', 'week', 'month', 'effect', 'work', 'year', 'day',
        'take'], dtype=object)
        })
        fig = tools.make_subplots(rows=1, cols=2, vertical_spacing=0.04,
        subplot_titles=["Frequent words of rating 1 to 5 (Negative)", 
        "Frequent words of rating 6 to 10 (Positve)"])
        fig.append_trace(trace0, 1, 1)
        fig.append_trace(trace1, 1, 2)
        fig['layout'].update(height=700, paper_bgcolor='rgb(233,233,233)', title="Word Count Plots")
        return fig
    elif value=='bigram':
        #ngram
        #bi gram
        trace2 = go.Bar({
        'marker': {'color': 'orange'},
        'orientation': 'h',
        'showlegend': False,
        'x': np.array([  687,   689,   691,   705,   708,   726,   733,   735,   735,   737,
                    739,   747,   753,   768,   805,   846,   851,   885,   896,   914,
                    948,   968,   979,   986,   999,  1013,  1029,  1060,  1068,  1076,
                    1152,  1211,  1227,  1243,  1247,  1311,  1383,  1384,  1415,  1466,
                    1495,  1601,  1995,  2205,  2297,  2605,  2667,  3420,  6071, 12006]),
        'y': np.array(['much better', 'depress anxieti', 'feel better', 'went away',
                'sinc start', 'day take', 'start feel', 'take medicin', 'three month',
                'someth els', 'mg day', 'made feel', 'stomach pain', 'last week',
                'doctor prescrib', 'back pain', 'two day', 'realli bad', 'last day',
                'work well', 'week ago', 'take mg', 'next day', 'gain lbs', 'two month',
                'take medic', 'first week', 'yeast infect', 'go away', 'first time',
                'year ago', 'go back', 'first day', 'panic attack', 'everi day',
                'gain pound', 'gain weight', 'month ago', 'blood pressur', 'two week',
                'first month', 'year old', 'take pill', 'start take', 'sex drive',
                'stop take', 'weight gain', 'mood swing', 'birth control',
                'side effect'], dtype=object)
        })

        trace3 = go.Bar({
        'marker': {'color': 'orange'},
        'orientation': 'h',
        'showlegend': False,
        'x': np.array([ 1737,  1746,  1800,  1804,  1810,  1831,  1882,  1886,  1929,  1992,
                    2003,  2015,  2021,  2036,  2076,  2117,  2121,  2177,  2239,  2246,
                    2251,  2295,  2300,  2455,  2488,  2502,  2586,  2886,  2897,  3008,
                    3053,  3129,  3302,  3302,  3453,  3509,  3513,  3592,  3621,  3659,
                    3909,  4474,  4609,  4979,  5279,  5489,  6014,  6029,  9683, 36903]),
        'y': np.array(['go away', 'two month', 'lose weight', 'plan b', 'back pain',
                'work wonder', 'day take', 'per day', 'start mg', 'weight loss',
                'last day', 'twice day', 'lost pound', 'feel better', 'next day',
                'last year', 'take medic', 'time day', 'went away', 'week ago',
                'chang life', 'stop take', 'dri mouth', 'doctor prescrib',
                'high recommend', 'lost lbs', 'blood pressur', 'everi day', 'mg day',
                'gain weight', 'two week', 'first day', 'first month', 'month ago',
                'first week', 'sex drive', 'much better', 'panic attack', 'work great',
                'first time', 'take pill', 'mood swing', 'work well', 'year ago',
                'take mg', 'year old', 'start take', 'weight gain', 'birth control',
                'side effect'], dtype=object)
        })
        fig = tools.make_subplots(rows=1, cols=2, vertical_spacing=0.04,
        subplot_titles=["Frequent words of rating 1 to 5 (Negative)", 
        "Frequent words of rating 6 to 10 (Positve)"])
        fig.append_trace(trace2, 1, 1)
        fig.append_trace(trace3, 1, 2)
        fig['layout'].update(height=700, paper_bgcolor='rgb(233,233,233)', title="Word Count Plots")
        return fig
    elif value=='trigram':
        #tri-gram
        trace4 = go.Bar({
        'marker': {'color': 'green'},
        'orientation': 'h',
        'showlegend': False,
        'x': np.array([ 79,  80,  80,  82,  83,  83,  83,  84,  85,  86,  87,  88,  88,  90,
        90,  92,  92,  92,  92,  93,  93,  94,  94,  95,  97, 100, 103, 104,
        108, 113, 116, 116, 120, 120, 121, 122, 128, 132, 141, 144, 149, 151,
        151, 156, 170, 186, 204, 210, 327, 589]),
        'y': np.array(['took plan b', 'bad side effects.', 'severe side effects',
        '"i got implant', 'didn&#039;t work me.', 'ortho tri cyclen',
        'took one pill', 'horrible side effects.', 'first started taking',
        '3 months now', '2 weeks ago', '"i took medicine', 'i&#039;m going try',
        'many side effects', 'first time took', 'recommend birth control',
        '"i took one', 'birth control i&#039;ve', 'gained 10 pounds',
        'gained 15 pounds', 'first 3 months', 'lo loestrin fe',
        'took first dose', 'horrible side effects', 'first two weeks',
        '"my doctor prescribed', 'negative side effects', 'will never use',
        'gained 20 pounds', 'started birth control', 'decided stop taking',
        'started taking pill', 'first birth control', 'form birth control',
        'every single day', 'i&#039;m going back', 'worst birth control',
        '"this birth control', 'stopped taking it.', '"i birth control',
        'stop taking it.', 'high blood pressure', '"i got nexplanon',
        'side effects worth', 'birth control pill', 'bad side effects',
        'birth control pills', 'taking birth control', 'will never take',
        '"i started taking'], dtype=object)
        })

        trace5 = go.Bar({
        'marker': {'color': 'green'},
        'orientation': 'h',
        'showlegend': False,
        'x': np.array([ 184,  185,  186,  187,  188,  189,  190,  191,  191,  191,  192,  192,
        192,  195,  197,  200,  203,  206,  210,  211,  218,  225,  228,  229,
        233,  241,  242,  261,  266,  273,  276,  278,  285,  292,  292,  293,
        308,  320,  322,  334,  335,  346,  390,  405,  412,  418,  462,  482,
        533, 1441]),
        'y': np.array(['experience side effects', 'first couple days', 'tried many different',
        'first couple weeks', '2 months now', 'will go away',
        'many side effects', 'lower back pain', 'almost 2 years',
        'sexual side effects', 'side effects -', 'first 3 months',
        'small price pay', 'took first dose', 'post traumatic stress',
        'side effects experienced', 'haven&#039;t gained weight',
        'best birth control', '2 years ago', '2 years now', 'year old male',
        '"i got nexplanon', 'form birth control', '3 months now',
        'bad side effects.', 'negative side effects.', 'side effect i&#039;ve',
        'side effects first', 'year old female', '3 times day',
        '"i started using', 'birth control i&#039;ve', 'feel much better.',
        'first two weeks', 'birth control pill', 'first 2 weeks',
        'first started taking', 'taking birth control',
        'side effects i&#039;ve', 'first birth control', 'high blood pressure',
        'experienced side effects', 'feel much better', 'negative side effects',
        'side effects all.', 'side effects except', 'birth control pills',
        'bad side effects', 'took plan b', '"i started taking'], dtype=object)
        })
        fig = tools.make_subplots(rows=1, cols=2, vertical_spacing=0.04,
        subplot_titles=["Frequent words of rating 1 to 5 (Negative)", 
        "Frequent words of rating 6 to 10 (Positve)"])
        fig.append_trace(trace4, 1, 1)
        fig.append_trace(trace5, 1, 2)
        fig['layout'].update(height=700, paper_bgcolor='rgb(233,233,233)', title="Word Count Plots")
        return fig
    else:
        #ngram
        trace6 = go.Bar({
        'marker': {'color': 'red'},
        'orientation': 'h',
        'showlegend': False,
        'x': np.array([17, 17, 17, 17, 17, 17, 18, 18, 18, 18, 18, 18, 19, 19, 19, 19, 19, 19,
        20, 20, 20, 21, 21, 21, 22, 22, 23, 23, 24, 25, 25, 27, 27, 28, 28, 29,
        30, 32, 34, 34, 35, 36, 38, 40, 40, 44, 46, 47, 48, 61]),
        'y': np.array(['will never use product', 'got first depo shot',
        'side effects went away', 'will never take medication',
        'decided stop taking it.', 'taking birth control pills',
        'birth control i&#039;ve on.', 'first started taking it,',
        'first birth control i&#039;ve', 'don&#039;t know i&#039;m going',
        '"i got first shot', '"i got nexplanon put', '"i took birth control',
        'stopped taking birth control', '"i took one pill',
        '"i recommend birth control', 'side effects will go',
        '"i will never take', 'birth control side effects',
        'really bad side effects', 'first time birth control.',
        '"when first started taking', '"this birth control made',
        'will never take medicine', 'i&#039;ve gained 10 pounds',
        'i&#039;ve gained 20 pounds', '"i took first dose',
        '"i got birth control', '"this worst birth control',
        'worst birth control i&#039;ve', '"i started taking medicine',
        '"i taking birth control', '"i got depo shot', 'will never take drug',
        'side effects worth it."', 'side effects aren&#039;t worth',
        'mood swings, weight gain,', '"i got nexplanon inserted',
        '"i started taking medication', 'first birth control pill',
        'side effects go away', 'i&#039;m going stop taking',
        'started taking birth control', 'ortho tri cyclen lo',
        'will never take again."', 'will never take again.',
        '"this first birth control', 'side effects worth it.',
        '"i started taking pill', '"i started birth control'], dtype=object)
        })

        trace7 = go.Bar({
        'marker': {'color': 'red'},
        'orientation': 'h',
        'showlegend': False,
        'x': np.array([38, 38, 39, 39, 39, 40, 40, 41, 41, 41, 42, 42, 42, 42, 44, 45, 46, 47,
        47, 48, 49, 50, 50, 50, 52, 53, 54, 55, 56, 56, 56, 56, 57, 58, 58, 61,
        61, 62, 62, 69, 71, 71, 71, 71, 73, 75, 76, 78, 84, 91]),
        'y': np.array(['almost 2 years now.', 'cant remember last time',
        'first time birth control', 'havent noticed side effects',
        'remember take pill every', 'first started taking it,',
        'months now love it!', 'experienced negative side effects.',
        'say enough good things', '"i started taking pill',
        '"i got skyla inserted', '"i started taking medicine',
        'dont worry taking pill', 'took plan b one',
        'different birth control pills', 'didnt experience side effects',
        'cant say enough good', 'havent noticed weight gain',
        'dont remember take pill',
        'havent experienced side effects', 'side effects go away',
        '"i got nexplanon inserted', '"i 20 years old',
        'side effects dry mouth,', 'experienced negative side effects',
        'side effect i;ve experienced', 'best thing happened me.',
        '"i started taking adipex', 'weight gain, mood swings,',
        'side effects i;ve noticed', 'side effects weight gain',
        'side effect dry mouth', '"i love birth control.', 'plan b one step',
        'side effect i;ve noticed', 'took plan b within',
        'best birth control i ve', 'post traumatic stress disorder.',
        'mood swings, weight gain,', 'side effects i&#039;ve experienced',
        '"this first birth control', 'first birth control pill',
        '"i started taking phentermine', 'first birth control i&#039;ve',
        'side effects dry mouth', 'started taking birth control',
        '"i took plan b', '"i started taking medication',
        'side effects went away', 'post traumatic stress disorder'],
        dtype=object)
        })
        fig = tools.make_subplots(rows=1, cols=2, vertical_spacing=0.04,
        subplot_titles=["Frequent words of rating 1 to 5 (Negative)", 
        "Frequent words of rating 6 to 10 (Positve)"])
        fig.append_trace(trace6, 1, 1)
        fig.append_trace(trace7, 1, 2)
        fig['layout'].update(height=700, paper_bgcolor='rgb(233,233,233,0.7)', title="Word Count Plots")
        return fig

# Drugs according to ratings
@app.callback(
    Output('condition_plot', 'figure'),
    Input('dpdn5', 'value')
)
def category_senti(value):
    if value == 'Birth Control':
        plotdata = pd.DataFrame({
        "Positive":[1834, 1547, 3181, 1184, 1025],
        "Neutral": [1706, 1523, 1007, 1125, 987],
        "Negative":[881,  683, 742, 583, 491]
        }, index=  ["Etonogestrel", "norethindrone", "Levonorgestrel", "Nexplanon", "levonorgestrel"]
        )
        stacked_data = plotdata.apply(lambda x: x*100/sum(x), axis=1)
        stacked_data.reset_index(inplace = True)
        fig = go.Figure(go.Bar(x = stacked_data["index"],
        y = stacked_data["Positive"],name='positvie',text=stacked_data["Positive"],
        width = [0.4]*len(stacked_data),textposition='auto',texttemplate="%{y:.2f} %"))
        fig.add_bar(x = stacked_data["index"],
        y = stacked_data["Neutral"],name='Neutral',text=stacked_data["Neutral"],
        width = [0.4]*len(stacked_data),textposition='auto',texttemplate="%{y:.2f} %")

        fig.add_bar(x = stacked_data["index"],
        y = stacked_data["Negative"],name='Negative',text=stacked_data["Negative"],
        width = [0.4]*len(stacked_data),textposition='auto',texttemplate="%{y:.2f} %")

        fig.update_layout(barmode='stack',
        title = 'Category wise sentiments of drugs reviews of top 5 drugs used in Birth Control',
        xaxis_title="Drug categories",
        yaxis_title="Percentage Sentiment in each category (%)")
        fig['layout'].update( height=600,paper_bgcolor='rgb(255,255,255)')
        return fig
    elif value == 'Depression':
        plotdata = pd.DataFrame({
        "Positive":[919, 1242, 768, 502,  460],
        "Neutral": [241, 331, 336, 161, 144],
        "Negative":[209,  295, 234, 1323,126]
        }, index=  ["Bupropion", "Sertraline", "Venlafaxine", "Desvenlafaxine", "Pristiq"]
        )
        stacked_data = plotdata.apply(lambda x: x*100/sum(x), axis=1)
        stacked_data.reset_index(inplace = True)
        fig = go.Figure(go.Bar(x = stacked_data["index"],
        y = stacked_data["Positive"],name='positvie',text=stacked_data["Positive"],
        width = [0.4]*len(stacked_data),textposition='auto',texttemplate="%{y:.2f} %"))
        fig.add_bar(x = stacked_data["index"],
        y = stacked_data["Neutral"],name='Neutral',text=stacked_data["Neutral"],
        width = [0.4]*len(stacked_data),textposition='auto',texttemplate="%{y:.2f} %")

        fig.add_bar(x = stacked_data["index"],
        y = stacked_data["Negative"],name='Negative',text=stacked_data["Negative"],
        width = [0.4]*len(stacked_data),textposition='auto',texttemplate="%{y:.2f} %")

        fig.update_layout(barmode='stack',
        title = 'Category wise sentiments of drugs reviews of top 5 drugs used in Depression',
        xaxis_title="Drug categories",
        yaxis_title="Percentage Sentiment in each category (%)")
        fig['layout'].update( height=600,paper_bgcolor='rgb(255,255,255)')
        return fig

    elif value == 'Pain':
        plotdata = pd.DataFrame({
        "Positive":[722, 519, 527, 433,159],
        "Neutral": [264, 94, 70, 47, 78],
        "Negative":[152,  73, 47, 36,56]
        }, index=  ["Tramadol", "hydrocodone", "Oxycodone", "Acetaminophen", "Tapentadol"]
        )
        stacked_data = plotdata.apply(lambda x: x*100/sum(x), axis=1)
        stacked_data.reset_index(inplace = True)
        fig = go.Figure(go.Bar(x = stacked_data["index"],
        y = stacked_data["Positive"],name='positvie',text=stacked_data["Positive"],
        width = [0.4]*len(stacked_data),textposition='auto',texttemplate="%{y:.2f} %"))
        fig.add_bar(x = stacked_data["index"],
        y = stacked_data["Neutral"],name='Neutral',text=stacked_data["Neutral"],
        width = [0.4]*len(stacked_data),textposition='auto',texttemplate="%{y:.2f} %")

        fig.add_bar(x = stacked_data["index"],
        y = stacked_data["Negative"],name='Negative',text=stacked_data["Negative"],
        width = [0.4]*len(stacked_data),textposition='auto',texttemplate="%{y:.2f} %")

        fig.update_layout(barmode='stack',
        title = 'Category wise sentiments of drugs reviews of top 5 drugs used in Pain',
        xaxis_title="Drug categories",
        yaxis_title="Percentage Sentiment in each category (%)")
        fig['layout'].update( height=600,paper_bgcolor='rgb(255,255,255)')
        return fig
    elif value == "Anxiety":
        plotdata = pd.DataFrame({
        "Positive":[927, 613, 240, 613, 690],
        "Neutral": [184, 44, 160, 44, 74],
        "Negative":[176,  40, 67, 40, 58]
        }, index=  ["Escitalopram", "Alprazolam", "Buspirone", "Clonazepam", "Lexapro"]
        )
        stacked_data = plotdata.apply(lambda x: x*100/sum(x), axis=1)
        stacked_data.reset_index(inplace = True)
        fig = go.Figure(go.Bar(x = stacked_data["index"],
                        y = stacked_data["Positive"],name='positvie',text=stacked_data["Positive"],
                        width = [0.4]*len(stacked_data),textposition='auto',texttemplate="%{y:.2f} %"))
        fig.add_bar(x = stacked_data["index"],
            y = stacked_data["Neutral"],name='Neutral',text=stacked_data["Neutral"],
            width = [0.4]*len(stacked_data),textposition='auto',texttemplate="%{y:.2f} %")

        fig.add_bar(x = stacked_data["index"],
            y = stacked_data["Negative"],name='Negative',text=stacked_data["Negative"],
            width = [0.4]*len(stacked_data),textposition='auto',texttemplate="%{y:.2f} %")

        fig.update_layout(barmode='stack',
        title = 'Category wise sentiments of drugs reviews of top 5 drugs used in Anxiety',
        xaxis_title="Drug categories",
        yaxis_title="Percentage Sentiment in each category (%)")
        fig['layout'].update( height=600,paper_bgcolor='rgb(255,255,255)')
        return fig
    else:
        plotdata = pd.DataFrame({
        "Positive":[418, 272, 375, 613, 262],
        "Neutral": [58, 66, 76, 128, 35],
        "Negative":[51,  59, 59, 122, 33]
        }, index=  ["Isotretinoin", "Adapalene", "Epiduo", "Doxycycline", "Accutane"]
        )
        stacked_data = plotdata.apply(lambda x: x*100/sum(x), axis=1)
        stacked_data.reset_index(inplace = True)
        fig = go.Figure(go.Bar(x = stacked_data["index"],
                        y = stacked_data["Positive"],name='positvie',text=stacked_data["Positive"],
                        width = [0.4]*len(stacked_data),textposition='auto',texttemplate="%{y:.2f} %"))
        fig.add_bar(x = stacked_data["index"],
            y = stacked_data["Neutral"],name='Neutral',text=stacked_data["Neutral"],
            width = [0.4]*len(stacked_data),textposition='auto',texttemplate="%{y:.2f} %")

        fig.add_bar(x = stacked_data["index"],
            y = stacked_data["Negative"],name='Negative',text=stacked_data["Negative"],
            width = [0.4]*len(stacked_data),textposition='auto',texttemplate="%{y:.2f} %",
                marker=dict(
        color='rgba(119, 3, 252, 0.4)',
        line=dict(color='rgba(119, 3, 252, 1.0)', width=1)
    ))

        fig.update_layout(barmode='stack',
        title = 'Category wise sentiments of drugs reviews of top 5 drugs used in Acne',
        xaxis_title="Drug categories",
        yaxis_title="Percentage Sentiment in each category (%)")
        fig['layout'].update( height=600,paper_bgcolor='rgb(255,255,255)')
        return fig




if __name__ =='__main__':
    app.run_server(debug=True, port=4000)