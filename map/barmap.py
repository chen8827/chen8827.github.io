import folium
import pandas as pd

# read csv and make modification to match built-in color
mrtdata=pd.read_csv('basic/mrt.csv')
bardata=pd.read_csv('basic/bar.csv')
mrtdata.replace('BR','darkred',inplace=True)
mrtdata.replace('R','red',inplace=True)
mrtdata.replace('G','green',inplace=True)
mrtdata.replace('O','orange',inplace=True)
mrtdata.replace('BL','blue',inplace=True)
mrtdata.replace('Y','yellow',inplace=True)
mrtdata.replace('A','purple',inplace=True)

# for speed purposes
MAX_RECORDS=1000
  
# create empty map zoomed in
SET_COORDINATES = (25.0476226,121.5137289)
map=folium.Map(location=SET_COORDINATES,zoom_start=12,tiles="cartodbpositron",width='100%',height='100%')
 
# add mrt marker
for index,row in mrtdata[0:MAX_RECORDS].iterrows():
    folium.CircleMarker(location=[row['lat'],row['lon']],
                        tooltip=row['station_name_tw']+row['station_name_en'],
                        color=row['line_code'],
                        fill=True,
                        radius=6).add_to(map)

# add br line
folium.PolyLine(locations=(mrtdata.iloc[0:24,[9,10]]),
                color=mrtdata['line_code'][0],
                weight=3).add_to(map)
# add r line
folium.PolyLine(locations=(mrtdata.iloc[24:52,[9,10]]),
                color=mrtdata['line_code'][24],
                weight=3).add_to(map)
# add g line
folium.PolyLine(locations=(mrtdata.iloc[52:72,[9,10]]),
                color=mrtdata['line_code'][52],
                weight=3).add_to(map)
# add o line
folium.PolyLine(locations=(mrtdata.iloc[72:93,[9,10]]),
                color=mrtdata['line_code'][72],
                weight=3).add_to(map)
folium.PolyLine(locations=(mrtdata.iloc[[83,93,94,95,96,97],[9,10]]),
                color=mrtdata['line_code'][83],
                weight=3).add_to(map)
# add b line
folium.PolyLine(locations=(mrtdata.iloc[98:121,[9,10]]),
                color=mrtdata['line_code'][98],
                weight=3).add_to(map)
# add y line
folium.PolyLine(locations=(mrtdata.iloc[121:135,[9,10]]),
                color=mrtdata['line_code'][121],
                weight=3).add_to(map)
# add p line
folium.PolyLine(locations=(mrtdata.iloc[135:156,[9,10]]),
                color=mrtdata['line_code'][135],
                weight=3).add_to(map)

# add bar marker cluster
marker_cluster=folium.plugins.MarkerCluster().add_to(map)
for index,row in bardata[0:MAX_RECORDS].iterrows():
    lat=row['lat']
    lon=row['lon']
    folium.Marker((lat,lon),
                  tooltip=row['name'],
                  icon=folium.Icon(color='lightblue',icon='glyphicon-glass')).add_to(marker_cluster)
marker_cluster=folium.plugins.MarkerCluster(cursor='no-drop',).add_to(map)

#import to html
map.save('map.html')
