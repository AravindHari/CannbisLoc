import dash
import dash_core_components as dcc
import dash_html_components as html

from dash_package import app

from dash.dependencies import Input, Output, State
from dash_package.chart_data import *

colors = {
    'background': '#9d99b0',
    'text': '#181f33s'
}

race_piechart_content = list(map(lambda c: {'country': c, 'count_data': race_count_by_country(c)}, countries()))
flavor_piechart_content = list(map(lambda c: {'country': c, 'count_data': flavor_count_by_country(c)}, countries()))
effect_piechart_content = list(map(lambda c: {'country': c, 'count_data': effect_count_by_country(c)}, countries()))

effect_map_content = list(map(lambda e: {'effect': e, 'count_data': country_count_by_effect(e)}, effects()))
flavor_map_content = list(map(lambda f: {'flavor': f, 'count_data': country_count_by_flavor(f)}, flavors()))

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[

    html.H1('Cannabis Locator', style={'font': 'Helvetica', 'textAlign': 'center', 'color': colors['text']}),

    html.H6('a data science project!!!', style={'color': '#003300', 'backgroundColor': '#ffffff', 'textAlign': 'center'}),

    html.H3('Cannabis Races by Country', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    dcc.Graph(
        id='races-by-countries',
        figure={
            'data':[
                {'x': country_race_composition['countries'], 'y': country_race_composition['sativas'], 'type': 'bar', 'name': 'sativas'},
                {'x': country_race_composition['countries'], 'y': country_race_composition['indicas'], 'type': 'bar', 'name': 'indicas'},
                {'x': country_race_composition['countries'], 'y': country_race_composition['hybrids'], 'type': 'bar', 'name': 'hybrids'}
            ],
            'layout': [{
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text']
                }
            }]
        }
    ),

    html.H3('Pie Charts by Country: Races', style={'textAlign': 'center', 'color': colors['text']}),

    html.Div([
        dcc.Dropdown(
            id='races-by-country',
            options=list(map(lambda c: {'label': c, 'value': c}, countries())),
            value="Afghanistan"
        ),
        html.Div(id='output-races')
    ]),

    html.H3('Pie Charts by Country: Flavors', style={'textAlign': 'center', 'color': colors['text']}),

    html.Div([
        dcc.Dropdown(
            id='flavors-by-country',
            options=list(map(lambda c: {'label': c, 'value': c}, countries())),
            value="Afghanistan"
        ),
        html.Div(id='output-flavors')
    ]),

    html.H3('Pie Charts by Country: Effects', style={'textAlign': 'center', 'color': colors['text']}),

    html.Div([
        dcc.Dropdown(
            id='effects-by-country',
            options=list(map(lambda c: {'label': c, 'value': c}, countries())),
            value='Afghanistan'
        ),
        html.Div(id='output-effects')
    ]),

    html.H3('So You Wanna Feel...... Where Do You Go?', style={'textAlign': 'center', 'color': colors['text']}),

    html.Div([
        dcc.Dropdown(
            id='map-by-effect',
            options=list(map(lambda e: {'label': e, 'value': e}, effects())),
            value='Happy'
        ),
        html.Div(id='effects-maps')
    ]),

    html.H3('Flavors. Where Do You Go?', style={'textAlign': 'center', 'color': colors['text']}),

    html.Div([
        dcc.Dropdown(
            id='map-by-flavor',
            options=list(map(lambda f: {'label': f, 'value': f}, flavors())),
            value='Sweet'
        ),
        html.Div(id='flavors-maps')])

])




@app.callback(Output('output-races', 'children'),
              [Input('races-by-country', 'value')])
def display_race_content(value):
    country = list(filter(lambda c: c['country'] == value, race_piechart_content))[0]
    data = [{'values': country['count_data']['y'], 'labels': country['count_data']['x'], 'type': 'pie'}]
    return html.Div([dcc.Graph(
        id='races',
        figure={
            'data': data,
            'layout': {
                'title': str(value) + ' - races of strains',
                'margin': {'l': 10,'r': 10,'b': 30,'t': 30},
                'legend': {'x': 1, 'y': 1}
            }})])

@app.callback(Output('output-flavors', 'children'),
              [Input('flavors-by-country', 'value')])
def display_flavor_content(value):
    country = list(filter(lambda c: c['country'] == value, flavor_piechart_content))[0]
    data = [{'values': country['count_data']['y'], 'labels': country['count_data']['x'], 'type': 'pie'}]
    return html.Div([dcc.Graph(
        id='flavors',
        figure={
            'data': data,
            'layout': {
                'title': str(value) + ' - flavors of strains',
                'margin': {'l': 10,'r': 10,'b': 30,'t': 30},
                'legend': {'x': 1, 'y': 1}
            }})])

@app.callback(Output('output-effects', 'children'),
              [Input('effects-by-country', 'value')])
def display_effect_content(value):
    country = list(filter(lambda c: c['country'] == value, effect_piechart_content))[0]
    data = [{'values': country['count_data']['y'], 'labels': country['count_data']['x'], 'type': 'pie'}]
    return html.Div([dcc.Graph(
        id='effects',
        figure={
            'data': data,
            'layout': {
                'title': str(value) + ' - effects of strains',
                'margin': {'l': 10,'r': 10,'b': 30,'t': 30},
                'legend': {'x': 1, 'y': 1}
            }})])

@app.callback(Output('effects-maps', 'children'),
              [Input('map-by-effect', 'value')])
def display_effect_map(value):
    effect = list(filter(lambda e: e['effect'] == value, effect_map_content))[0]
    data = [dict(
        type = 'choropleth',
        locations = effect['count_data']['x'],
        z = effect['count_data']['y'],
        text = effect['count_data']['x'],
        autocolorscale = True,
        marker = dict(
            line = dict (
                color = 'rgb(180,180,180)',
                width = 0.5
            ) ),
        colorbar = dict(
            autotick = False,
            title = 'Strainzzz'))]
    return html.Div([dcc.Graph(
        id='effect_map',
        figure={
            'data': data,
            'layout': {
                'title': 'WHERE TO GET WEED: ' + str(value),
                'margin': {'l': 10,'r': 10,'b': 30,'t': 30},
                'legend': {'x': 1, 'y': 1}
            }})])

@app.callback(Output('flavors-maps', 'children'),
              [Input('map-by-flavor', 'value')])
def display_effect_map(value):
    flavor = list(filter(lambda f: f['flavor'] == value, flavor_map_content))[0]
    data = [dict(
        type = 'choropleth',
        locations = flavor['count_data']['x'],
        z = flavor['count_data']['y'],
        text = flavor['count_data']['x'],
        autocolorscale = True,
        marker = dict(
            line = dict (
                color = 'rgb(180,180,180)',
                width = 0.5
            ) ),
        colorbar = dict(
            autotick = False,
            title = 'Strainzzz'))]
    return html.Div([dcc.Graph(
        id='flavor_map',
        figure={
            'data': data,
            'layout': {
                'title': 'WHERE TO GET WEED: ' + str(value),
                'margin': {'l': 10,'r': 10,'b': 30,'t': 30},
                'legend': {'x': 1, 'y': 1}
            }})])
