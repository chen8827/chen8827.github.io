import folium
import pandas as pd
import folium.plugins
#import sys
#sys.setrecursionlimit(10000)

mrtdata=pd.read_csv('basic/mrt.csv')
bardata=pd.read_csv('basic/bar.csv')

SET_COORDINATES = (25.0476226,121.5137289)
mrtdata.replace('BR','darkred',inplace=True)
mrtdata.replace('R','red',inplace=True)
mrtdata.replace('G','green',inplace=True)
mrtdata.replace('O','orange',inplace=True)
mrtdata.replace('BL','blue',inplace=True)
mrtdata.replace('Y','yellow',inplace=True)
mrtdata.replace('A','purple',inplace=True)

# for speed purposes
MAX_RECORDS=1000
  
#create empty map zoomed in
map=folium.Map(location=SET_COORDINATES,zoom_start=12,tiles="cartodbpositron",width='100%',height='100%')
 
#add mrt marker
for index,row in mrtdata[0:MAX_RECORDS].iterrows():
    folium.CircleMarker(location=[row['lat'],row['lon']],
                        #popup=row['station_name_tw'],
                        tooltip=row['station_name_tw']+row['station_name_en'],
                        color=row['line_code'],
                        fill=True,
                        #fill_color=row['line_code'],
                        #fill_opacity=0.5,
                        radius=6).add_to(map)

#add br lines
folium.PolyLine(locations=(mrtdata.iloc[0:24,[9,10]]),
                color=mrtdata['line_code'][0],
                weight=3).add_to(map)
#add r lines
folium.PolyLine(locations=(mrtdata.iloc[24:52,[9,10]]),
                color=mrtdata['line_code'][24],
                weight=3).add_to(map)
#add g lines
folium.PolyLine(locations=(mrtdata.iloc[52:72,[9,10]]),
                color=mrtdata['line_code'][52],
                weight=3).add_to(map)
#add o lines
folium.PolyLine(locations=(mrtdata.iloc[72:93,[9,10]]),
                color=mrtdata['line_code'][72],
                weight=3).add_to(map)
folium.PolyLine(locations=(mrtdata.iloc[[83,93,94,95,96,97],[9,10]]),
                color=mrtdata['line_code'][83],
                weight=3).add_to(map)
#add b lines
folium.PolyLine(locations=(mrtdata.iloc[98:121,[9,10]]),
                color=mrtdata['line_code'][98],
                weight=3).add_to(map)
#add y lines
folium.PolyLine(locations=(mrtdata.iloc[121:135,[9,10]]),
                color=mrtdata['line_code'][121],
                weight=3).add_to(map)
#add p lines
folium.PolyLine(locations=(mrtdata.iloc[135:156,[9,10]]),
                color=mrtdata['line_code'][135],
                weight=3).add_to(map)


'''# Define html inside marker pop-up
pub_html=folium.Html(f"""<p style="text-align: center;"><span style="font-family: Didot, serif; font-size: 21px;">{name}</span></p>
<p style="text-align: center;"><iframe src={insta_post}embed width="240" height="290" frameborder="0" scrolling="auto" allowtransparency="true"></iframe>
<p style="text-align: center;"><a href={website} target="_blank" title="{name} Website"><span style="font-family: Didot, serif; font-size: 17px;">{name} Website</span></a></p>
<p style="text-align: center;"><a href={directions} target="_blank" title="Directions to {name}"><span style="font-family: Didot, serif; font-size: 17px;">Directions to {name}</span></a></p>
""", script=True)
# Create pop-up with html content
popup=folium.Popup(pub_html,max_width=500)'''

marker_cluster=folium.plugins.MarkerCluster().add_to(map)
for index,row in bardata[0:MAX_RECORDS].iterrows():
    lat=row['lat']
    lon=row['lon']
    folium.Marker((lat,lon),
                  tooltip=row['name'],
                  #popup=popup,
                  icon=folium.Icon(color='lightblue',icon='glyphicon-glass')).add_to(marker_cluster)
marker_cluster=folium.plugins.MarkerCluster(cursor='no-drop',).add_to(map)

#import
map.save('map.html')

'''
#api key
api_file=opem('api-key.txt','r')
api_key=api_file.read()
api_file.close()
'<a href=https://fr.wikipedia.org/wiki/Place_Guillaume_II>Place Guillaume II</a>'
'''
