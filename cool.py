import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np
from math import radians, cos, sin, asin, sqrt

bardata=pd.read_csv('basic/bar.csv')
bar=pd.DataFrame(bardata)
MAX_RECORDS=1000

# Create a dash application
app = dash.Dash(__name__)

tab_stylei = {
    'font-style':'italic',
    'font-weight':'normal',
    'font-family': 'Brush Script MT, Brush Script Std, cursive',
    'color': 'whitesmoke',
    'margin': 15,
    'cursor': 'crosshair',
    'text-decoration': 'none',
    'align-items': 'center',
    'justify-content': 'center',
    'font-size':'30px',
    'text-shadow': 'rgb(250, 200, 250) 0px 0px 5px,rgb(250, 200, 250) 0px 0px 10px,rgb(255, 45, 150) 0px 0px 20px,rgb(255, 45, 150) 0px 0px 30px'
}

tab_styleb = {
    'font-style':'italic',
    'color': 'whitesmoke',
    'cursor': 'crosshair',
    'text-decoration': 'none',
    'align-items': 'center',
    'justify-content': 'center',
    'font-size':'50px',
    'text-shadow': 'rgb(255, 240, 175) 0px 0px 5px,rgb(255, 240, 175) 0px 0px 15px,rgb(255,200, 0) 0px 0px 20px,rgb(255,200, 0) 0px 0px 30px,rgb(255,200, 0) 0px 0px 40px'
}

tab_style = {
    'font-style':'italic',
    'color': 'whitesmoke',
    'margin': 17.5,
    'cursor': 'crosshair',
    'text-decoration': 'none',
    'align-items': 'center',
    'justify-content': 'center',
    'font-size':'30px',
    'text-shadow': 'rgb(255, 240, 175) 0px 0px 5px,rgb(255, 240, 175) 0px 0px 15px,rgb(255,200, 0) 0px 0px 20px,rgb(255,200, 0) 0px 0px 30px,rgb(255,200, 0) 0px 0px 40px'
}

tab_style0 = {
    'color': 'whitesmoke',
    'margin': 20,
    'cursor': 'crosshair',
    'text-decoration': 'underline',
    'align-items': 'center',
    'justify-content': 'center',
    'font-size':'20px',
    'font-weight':'bold',
    'font-style':'italic',
    'font-family':'sans-serif',
    'text-shadow':'rgb(225, 175, 250) 0px 0px 5px,rgb(225, 175, 250) 0px 0px 5px,rgb(150, 45, 225) 0px 0px 10px,rgb(150, 45, 225) 0px 0px 10px,rgb(150, 45, 225) 0px 0px 10px'
}

no=np.linspace(0,110,num=111,endpoint=True,retstep=False,dtype=int)
noo=[]
for i in no:
    noo += [str(i), ]

bargod = []
for index, row in bar[0:MAX_RECORDS].iterrows():
    i=row['index']
    name = row['name']
    a=name.replace( ' ' , '+' )
    url='https://www.google.com/search?q='+a+'+營業時間'
    abar = html.Div(
        id=str(i),
        style={'display':'none'},
        children=[
            html.H2(name, style={'textAlign': 'center'}),
            dcc.Link('Business Hours', href=url, target='_blank',style=tab_stylei),
            dcc.Link('Instagram Official', href=row['insof'], target='_blank', style=tab_stylei),
            dcc.Link('Instagram Gallery', href=row['insplace'], target='_blank', style=tab_stylei),
            html.Div(html.Br(),),
            html.Iframe(src=row['map'],style={'height':'600px','width':'600px'}),
            html.Div(id='display{}'.format(i))
        ]
    )
    bargod += [abar, ]

def dis(lon1, lat1, lon2, lat2):
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371
    return c * r