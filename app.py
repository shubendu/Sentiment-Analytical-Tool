
# import plotly.express as px
# from jupyter_dash import JupyterDash
# import dash_core_components as dcc
# import dash_html_components as html
# import dash_bootstrap_components as dbc
# from dash.dependencies import Input, Output
# import plotly.express as px
# import dash

# # Iris bar figure
# def drawFigure():
#     return  html.Div([
#         dbc.Card(
#             dbc.CardBody([
#                 dcc.Graph(
#                     figure=px.bar(
#                         df, x="sepal_width", y="sepal_length", color="species"
#                     ).update_layout(
#                         template='plotly_dark',
#                         plot_bgcolor= 'rgba(0, 0, 0, 0)',
#                         paper_bgcolor= 'rgba(0, 0, 0, 0)',
#                     ),
#                     config={
#                         'displayModeBar': False
#                     }
#                 ) 
#             ])
#         ),  
#     ])

# # Text field
# def drawText():
#     return html.Div([
#         dbc.Card(
#             dbc.CardBody([
#                 html.Div([
#                     html.H2("Text"),
#                 ], style={'textAlign': 'center'}) 
#             ])
#         ),
#     ])

# # Data
# df = px.data.iris()

# # Build App
# app = dash.Dash(external_stylesheets=[dbc.themes.SLATE])

# app.layout = html.Div([
#     dbc.Card(
#         dbc.CardBody([
#             dbc.Row([
#                 dbc.Col([
#                     drawText()
#                 ], width=3),
#                 dbc.Col([
#                     drawText()
#                 ], width=3),
#                 dbc.Col([
#                     drawText()
#                 ], width=3),
#                 dbc.Col([
#                     drawText()
#                 ], width=3),
#             ], align='center'), 
#             html.Br(),
#             dbc.Row([
#                 dbc.Col([
#                     drawFigure() 
#                 ], width=3),
#                 dbc.Col([
#                     drawFigure()
#                 ], width=3),
#                 dbc.Col([
#                     drawFigure() 
#                 ], width=6),
#             ], align='center'), 
#             html.Br(),
#             dbc.Row([
#                 dbc.Col([
#                     drawFigure()
#                 ], width=9),
#                 dbc.Col([
#                     drawFigure()
#                 ], width=3),
#             ], align='center'),      
#         ]), color = 'dark'
#     )
# ])

# if __name__ == '__main__':
#     app.run_server(debug=True,port=8055)
# import dash
# import dash_core_components as dcc
# import dash_html_components as html
# import dash_table_experiments as dt
# import dash_bootstrap_components as dbc


# app = dash.Dash(external_stylesheets=[dbc.themes.CYBORG])

# app.layout = \
# dbc.Container\
# ([
#     html.Br(),
#     dbc.Row([
#     dbc.Col([dbc.Button("row 1 col 1",style={"width":"100%"})],width=3),
#     dbc.Col([dbc.Button("row 1 col 2", style={"width": "100%"})],width=3),
#     dbc.Col([dbc.Button("row 1 col 3",style={"width":"100%"})],width=3),
#     dbc.Col([dbc.Button("row 1 col 4",style={"width":"100%"})],width=3),
#     ]),
#     html.Br(),
#     dbc.Row([
#     dbc.Col([dbc.Button("row 2 col 1",style={"width":"100%"})],width=3),
#     dbc.Col([dbc.Button("row 2 col 2", style={"width": "100%"})],width=3),
#     dbc.Col([dbc.Button("row 2 col 3",style={"width":"100%"})],width=6),
#     ]),
#     html.Br(),
#     dbc.Row([
#     dbc.Col([dbc.Button("row 3 col 1",style={"width":"100%"})],width=9),
#     dbc.Col([dbc.Button("row 3 col 2", style={"width": "100%"})],width=3),
#     ])
# ])

# if __name__ == "__main__":
#     app.run_server(debug=False, port=8011)