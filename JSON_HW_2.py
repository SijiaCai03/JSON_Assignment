import csv

in_file = open("MODIS_C6_Australia_NewZealand_MCD14DL_NRT_2020026.csv","r")

fire_data = csv.reader(in_file, delimiter=",")

header = next(fire_data)

#create three lists
lats,lons,brights = [],[],[]

for row in fire_data:
    lats.append(float(row[0]))
    lons.append(float(row[1]))
    brights.append(float(row[2]))


from plotly.graph_objs import Layout
from plotly import offline

data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'marker':{                                              
        'size':[0.05*b for b in brights], 
        'color':brights,
        'colorscale':'Viridis',
        'reversescale':True,
        'colorbar':{'title':'Brightness'}    
    },                                                             
}]                                                                                                                          

my_layout = Layout(title="Australia Fires - January 2020")

fig = {'data':data,'layout':my_layout}

offline.plot(fig,filename='australia_fires_2020.html')