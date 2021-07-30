import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
from tool import *

# create dash application
app = dash.Dash(__name__)
server = app.server

# convert csv data to dataframe
mrtdata=pd.read_csv('mrt.csv',header=0)
bardata=pd.read_csv('bar.csv',header=0)
mrt=pd.DataFrame(mrtdata)
bar=pd.DataFrame(bardata)

# create web layout
app.layout = html.Div([
    dcc.Location(id='url'),
    dcc.Link('T A I P E I', href='/', style=tab_styleb),
    html.Div(html.Br(),),
    dcc.Link('BR own', href='/BR', style=tab_style),
    dcc.Link('R ed', href='/R', style=tab_style),
    dcc.Link('G reen', href='/G', style=tab_style),
    dcc.Link('O range', href='/O', style=tab_style),
    dcc.Link('BL ue', href='/BL', style=tab_style),
    dcc.Link('Y ellow', href='/Y', style=tab_style),
    dcc.Link('A irport', href='/A', style=tab_style),
    html.Div(bargod),
    html.Div([

        # Tab main
        html.Div(
            id='TAIPEI',
            children=[
                html.H1('B A R M A P'),
                html.Iframe(id='map',srcDoc=open('map.html','r',encoding='utf-8').read(),width='600px',height='600px')
            ]
        ),

        # Tab BR
        html.Div(
            id='BR',
            style={'display': 'none'},
            children=[
                html.H1('B R L I N E'),
                dcc.Dropdown(
                    id='dropdown-BR',
                    options=[
                        {'label': row['station_name_tw'], 'value': row['index']}
                        for index, row in mrt[0:24].iterrows()
                    ]
                ),
                html.Div(id='display-BR'),
                html.Br(),
                html.Iframe(id='BRmap',srcDoc=open('BRmap.html','r',encoding='utf-8').read(),width='600px',height='600px')
            ]
        ),

        # Tab R
        html.Div(
            id='R',
            style={'display': 'none'},
            children=[
                html.H1('R L I N E'),
                dcc.Dropdown(
                    id='dropdown-R',
                    options=[
                        {'label': row['station_name_tw'], 'value': row['index']}
                        for index, row in mrt[24:52].iterrows()
                    ]
                ),
                html.Div(id='display-R'),
                html.Br(),
                html.Iframe(id='Rmap',srcDoc=open('Rmap.html','r',encoding='utf-8').read(),width='600px',height='600px')
            ]
        ),

        # Tab G
        html.Div(
            id='G',
            style={'display': 'none'},
            children=[
                html.H1('G L I N E'),
                dcc.Dropdown(
                    id='dropdown-G',
                    options=[
                        {'label': row['station_name_tw'], 'value': row['index']}
                        for index, row in mrt[52:72].iterrows()
                    ]
                ),
                html.Div(id='display-G'),
                html.Br(),
                html.Iframe(id='Gmap',srcDoc=open('Gmap.html','r',encoding='utf-8').read(),width='600px',height='600px')
            ]
        ),

        # Tab O
        html.Div(
            id='O',
            style={'display': 'none'},
            children=[
                html.H1('O L I N E'),
                dcc.Dropdown(
                    id='dropdown-O',
                    options=[
                        {'label': row['station_name_tw'], 'value': row['index']}
                        for index, row in mrt[72:98].iterrows()
                    ]
                ),
                html.Div(id='display-O'),
                html.Br(),
                html.Iframe(id='Omap',srcDoc=open('Omap.html','r',encoding='utf-8').read(),width='600px',height='600px')
            ]
        ),

        # Tab BL
        html.Div(
            id='BL',
            style={'display': 'none'},
            children=[
                html.H1('B L L I N E'),
                dcc.Dropdown(
                    id='dropdown-BL',
                    options=[
                        {'label': row['station_name_tw'], 'value': row['index']}
                        for index, row in mrt[98:121].iterrows()
                    ]
                ),
                html.Div(id='display-BL'),
                html.Br(),
                html.Iframe(id='BLmap',srcDoc=open('BLmap.html','r',encoding='utf-8').read(),width='600px',height='600px')
            ]
        ),

        # Tab Y
        html.Div(
            id='Y',
            style={'display': 'none'},
            children=[
                html.H1('Y L I N E'),
                dcc.Dropdown(
                    id='dropdown-Y',
                    options=[
                        {'label': row['station_name_tw'], 'value': row['index']}
                        for index, row in mrt[121:135].iterrows()
                    ]
                ),
                html.Div(id='display-Y'),
                html.Br(),
                html.Iframe(id='Ymap',srcDoc=open('Ymap.html','r',encoding='utf-8').read(),width='600px',height='600px')
            ]
        ),

        # Tab A
        html.Div(
            id='A',
            style={'display': 'none'},
            children=[
                html.H1('A L I N E'),
                dcc.Dropdown(
                    id='dropdown-A',
                    options=[
                        {'label': row['station_name_tw'], 'value': row['index']}
                        for index, row in mrt[135:156].iterrows()
                    ]
                ),
                html.Div(id='display-A'),
                html.Br(),
                html.Iframe(id='Amap',srcDoc=open('Amap.html','r',encoding='utf-8').read(),width='600px',height='600px')
            ]
        ),

    ])
],style={'width':'100%','display':'inline-block','textAlign':'center'})

# add callback
def generate_display_tab(tab):
    def display_tab(pathname):
        if tab == 'TAIPEI' and (pathname is None or pathname == '/'):
            return {'display': 'block'}
        elif pathname == '/{}'.format(tab):
            return {'display': 'block'}
        else:
            return {'display': 'none'}
    return display_tab

for tab in ['TAIPEI', 'BR', 'R', 'G', 'O', 'BL', 'Y', 'A']:
    app.callback(Output(tab, 'style'), [Input('url', 'pathname')])(
        generate_display_tab(tab)
    )

def generate_display_tab(idd):
    def display_tab(pathname):
        if pathname == '/{}'.format(idd):
            return {'display': 'block'}
        else:
            return {'display': 'none'}
    return display_tab

for idd in noo:
    app.callback(Output(idd, 'style'), [Input('url', 'pathname')])(
        generate_display_tab(idd)
    )

# Tab BR
@app.callback(
    Output('display-BR', 'children'),
    [Input('dropdown-BR', 'value')])
def display_value(value):
    mrt_lon=mrt['lon'][value]
    mrt_lat=mrt['lat'][value]
    godname=[]
    godindex=[]
    god=[]
    god+=[html.Br(),]
    mrt_name=mrt['station_name_tw'][value]
    url1='https://www.instagram.com/explore/tags/'+str(mrt_name)+'酒吧/' #ig hashtag
    url2='https://www.google.com/search?q='+str(mrt_name)+'酒吧' #google search
    c=html.A('Explore More Nearby Bars on Ins', href=url1, style=tab_style0, target='_blank')
    d=html.A('Explore More Nearby Bars on Google', href=url2, style=tab_style0, target='_blank')
    for index,row in bar[0:MAX_RECORDS].iterrows():
        barindex=row['index']
        distance=dis(mrt_lon,mrt_lat,row['lon'],row['lat'])
        if distance<=1:
            godname+=[bar.iloc[barindex,2],]
            godindex+=[barindex,]
    for i,j in zip(godname,godindex):
        a=dcc.Link(i, href='/{}'.format(j))
        b=html.Br()
        god+=[b,a,b,]
    god+=[html.Br(),html.Br(),d,c,html.Br(),html.Br(),]
    return (god)

# Tab R
@app.callback(
    Output('display-R', 'children'),
    [Input('dropdown-R', 'value')])
def display_value(value):
    mrt_lon=mrt['lon'][value]
    mrt_lat=mrt['lat'][value]
    godname=[]
    godindex=[]
    god=[]
    god+=[html.Br(),]
    mrt_name=mrt['station_name_tw'][value]
    url1='https://www.instagram.com/explore/tags/'+str(mrt_name)+'酒吧/' #ig hashtag
    url2='https://www.google.com/search?q='+str(mrt_name)+'酒吧' #google search
    c=html.A('Explore More Nearby Bars on Ins', href=url1, style=tab_style0, target='_blank')
    d=html.A('Explore More Nearby Bars on Google', href=url2, style=tab_style0, target='_blank')
    for index,row in bar[0:MAX_RECORDS].iterrows():
        barindex=row['index']
        distance=dis(mrt_lon,mrt_lat,row['lon'],row['lat'])
        if distance<=1:
            godname+=[bar.iloc[barindex,2],]
            godindex+=[barindex,]
    for i,j in zip(godname,godindex):
        a=dcc.Link(i, href='/{}'.format(j))
        b=html.Br()
        god+=[b,a,b,]
    god+=[html.Br(),html.Br(),d,c,html.Br(),html.Br(),]
    return (god)

# Tab G
@app.callback(
    Output('display-G', 'children'),
    [Input('dropdown-G', 'value')])
def display_value(value):
    mrt_lon=mrt['lon'][value]
    mrt_lat=mrt['lat'][value]
    godname=[]
    godindex=[]
    god=[]
    god+=[html.Br(),]
    mrt_name=mrt['station_name_tw'][value]
    url1='https://www.instagram.com/explore/tags/'+str(mrt_name)+'酒吧/' #ig hashtag
    url2='https://www.google.com/search?q='+str(mrt_name)+'酒吧' #google search
    c=html.A('Explore More Nearby Bars on Ins', href=url1, style=tab_style0, target='_blank')
    d=html.A('Explore More Nearby Bars on Google', href=url2, style=tab_style0, target='_blank')
    for index,row in bar[0:MAX_RECORDS].iterrows():
        barindex=row['index']
        distance=dis(mrt_lon,mrt_lat,row['lon'],row['lat'])
        if distance<=1:
            godname+=[bar.iloc[barindex,2],]
            godindex+=[barindex,]
    for i,j in zip(godname,godindex):
        a=dcc.Link(i, href='/{}'.format(j))
        b=html.Br()
        god+=[b,a,b,]
    god+=[html.Br(),html.Br(),d,c,html.Br(),html.Br(),]
    return (god)

# Tab O
@app.callback(
    Output('display-O', 'children'),
    [Input('dropdown-O', 'value')])
def display_value(value):
    mrt_lon=mrt['lon'][value]
    mrt_lat=mrt['lat'][value]
    godname=[]
    godindex=[]
    god=[]
    god+=[html.Br(),]
    mrt_name=mrt['station_name_tw'][value]
    url1='https://www.instagram.com/explore/tags/'+str(mrt_name)+'酒吧/' #ig hashtag
    url2='https://www.google.com/search?q='+str(mrt_name)+'酒吧' #google search
    c=html.A('Explore More Nearby Bars on Ins', href=url1, style=tab_style0, target='_blank')
    d=html.A('Explore More Nearby Bars on Google', href=url2, style=tab_style0, target='_blank')
    for index,row in bar[0:MAX_RECORDS].iterrows():
        barindex=row['index']
        distance=dis(mrt_lon,mrt_lat,row['lon'],row['lat'])
        if distance<=1:
            godname+=[bar.iloc[barindex,2],]
            godindex+=[barindex,]
    for i,j in zip(godname,godindex):
        a=dcc.Link(i, href='/{}'.format(j))
        b=html.Br()
        god+=[b,a,b,]
    god+=[html.Br(),html.Br(),d,c,html.Br(),html.Br(),]
    return (god)

# Tab BL
@app.callback(
    Output('display-BL', 'children'),
    [Input('dropdown-BL', 'value')])
def display_value(value):
    mrt_lon=mrt['lon'][value]
    mrt_lat=mrt['lat'][value]
    godname=[]
    godindex=[]
    god=[]
    god+=[html.Br(),]
    mrt_name=mrt['station_name_tw'][value]
    url1='https://www.instagram.com/explore/tags/'+str(mrt_name)+'酒吧/' #ig hashtag
    url2='https://www.google.com/search?q='+str(mrt_name)+'酒吧' #google search
    c=html.A('Explore More Nearby Bars on Ins', href=url1, style=tab_style0, target='_blank')
    d=html.A('Explore More Nearby Bars on Google', href=url2, style=tab_style0, target='_blank')
    for index,row in bar[0:MAX_RECORDS].iterrows():
        barindex=row['index']
        distance=dis(mrt_lon,mrt_lat,row['lon'],row['lat'])
        if distance<=1:
            godname+=[bar.iloc[barindex,2],]
            godindex+=[barindex,]
    for i,j in zip(godname,godindex):
        a=dcc.Link(i, href='/{}'.format(j))
        b=html.Br()
        god+=[b,a,b,]
    god+=[html.Br(),html.Br(),d,c,html.Br(),html.Br(),]
    return (god)

# Tab Y
@app.callback(
    Output('display-Y', 'children'),
    [Input('dropdown-Y', 'value')])
def display_value(value):
    mrt_lon=mrt['lon'][value]
    mrt_lat=mrt['lat'][value]
    godname=[]
    godindex=[]
    god=[]
    god+=[html.Br(),]
    mrt_name=mrt['station_name_tw'][value]
    url1='https://www.instagram.com/explore/tags/'+str(mrt_name)+'酒吧/' #ig hashtag
    url2='https://www.google.com/search?q='+str(mrt_name)+'酒吧' #google search
    c=html.A('Explore More Nearby Bars on Ins', href=url1, style=tab_style0, target='_blank')
    d=html.A('Explore More Nearby Bars on Google', href=url2, style=tab_style0, target='_blank')
    for index,row in bar[0:MAX_RECORDS].iterrows():
        barindex=row['index']
        distance=dis(mrt_lon,mrt_lat,row['lon'],row['lat'])
        if distance<=1:
            godname+=[bar.iloc[barindex,2],]
            godindex+=[barindex,]
    for i,j in zip(godname,godindex):
        a=dcc.Link(i, href='/{}'.format(j))
        b=html.Br()
        god+=[b,a,b,]
    god+=[html.Br(),html.Br(),d,c,html.Br(),html.Br(),]
    return (god)

# Tab A
@app.callback(
    Output('display-A', 'children'),
    [Input('dropdown-A', 'value')])
def display_value(value):
    mrt_lon=mrt['lon'][value]
    mrt_lat=mrt['lat'][value]
    godname=[]
    godindex=[]
    god=[]
    god+=[html.Br(),]
    mrt_name=mrt['station_name_tw'][value]
    url1='https://www.instagram.com/explore/tags/'+str(mrt_name)+'酒吧/' #ig hashtag
    url2='https://www.google.com/search?q='+str(mrt_name)+'酒吧' #google search
    c=html.A('Explore More Nearby Bars on Ins', href=url1, style=tab_style0, target='_blank')
    d=html.A('Explore More Nearby Bars on Google', href=url2, style=tab_style0, target='_blank')
    for index,row in bar[0:MAX_RECORDS].iterrows():
        barindex=row['index']
        distance=dis(mrt_lon,mrt_lat,row['lon'],row['lat'])
        if distance<=1:
            godname+=[bar.iloc[barindex,2],]
            godindex+=[barindex,]
    for i,j in zip(godname,godindex):
        a=dcc.Link(i, href='/{}'.format(j))
        b=html.Br()
        god+=[b,a,b,]
    god+=[html.Br(),html.Br(),d,c,html.Br(),html.Br(),]
    return (god)

if __name__ == '__main__':
    app.run_server(debug=False)
