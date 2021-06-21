import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio
import geojson
import numpy as np

df_ind = pd.read_csv('./data_solar_energy.csv')

with open('india_states_pre2019.geojson') as f:
    geojson_ind_states = geojson.load(f)

#*******************************************************************************************************************#
# ............................................. Colors and Fonts................................................... #
#*******************************************************************************************************************#

# Colors
c_white = 'rgb(255, 255, 255)'
c_marker = 'rgb(117, 117, 117)'

#Fonts
f_titlefont_1 = 'Courier New'
f_font2 = 'Courier New'


#*******************************************************************************************************************#
# ............................................. Prepare Subplot ................................................... #
#*******************************************************************************************************************#

x = 1
y = 2
plot_titles = ['Target Solar Power Generation Capacity by 2022 (Mega-Watts)',
               'Achieved Solar Power Generation Capacity (% of Target)']
plot_features = ['Target', 'Percent Done']

fig_layout = make_subplots( rows=x, cols=y,
                            specs=[[{'type':'choropleth'} for c in np.arange(y)] for r in np.arange(x)],
                            subplot_titles=plot_titles,
                            shared_xaxes='columns', shared_yaxes='rows',
                            print_grid=True,
                            horizontal_spacing=0.0, vertical_spacing=0.0,
                            column_widths=[1, 1], row_heights=[1])

#***************************************************************************************************************#
# ............................................ Add traces ......................................................#
#***************************************************************************************************************#

# Arguments for go.Chloropleth

# - list_colorbarmode = ['fraction', 'pixels']

marker_1 = go.choropleth.Marker( opacity=1.0, line=go.choropleth.marker.Line(color=c_white, width=0.25) )

title_1 = go.choropleth.colorbar.Title(font=go.choropleth.colorbar.title.Font(color=c_white, size=10,
                                                                              family=f_font2),
                                       side='bottom', text='Colorbar')
colorbar_1 = go.choropleth.ColorBar( bgcolor=c_white, bordercolor=c_white, borderwidth=0,
                                     len=0.5, thickness=0.02, lenmode='fraction', thicknessmode='fraction',
                                     outlinecolor=c_white, outlinewidth=5,
                                     separatethousands=True,
                                     title=title_1,
                                     x=0.0, xanchor='center', xpad=0,
                                     y=0.30, yanchor='middle', ypad=0,
                                     tickfont={'family':f_titlefont_1, 'size':10, 'color':'rgb(16, 37, 51)'})

colorbar_2 = go.choropleth.ColorBar( bgcolor=c_white, bordercolor=c_white, borderwidth=0,
                                     len=0.5, thickness=0.02, lenmode='fraction', thicknessmode='fraction',
                                     outlinecolor=c_white, outlinewidth=0,
                                     separatethousands=True,
                                     title=title_1,
                                     x=1.05, xanchor='center', xpad=0,
                                     y=0.30, yanchor='middle', ypad=0,
                                     tickfont={'family':f_titlefont_1, 'size':10, 'color':'rgb(16, 37, 51)'})

list_colbar = [colorbar_1, colorbar_2]
#'rgb(112, 229, 255)'
list_colscale = [[[0, 'rgb(255, 244, 184)'], [1, 'rgb(255, 217, 0)']],
                 [[0, 'rgb(107, 107, 107)'], [1, 'rgb(255, 247, 0)']]]

r_i = 0
c_i = 0
for i in range(len(plot_titles)):

    fig_i = go.Choropleth( geojson = geojson_ind_states,
                           featureidkey='properties.NAME_1',
                           locationmode='geojson-id',
                           locations=df_ind['State'],
                           z=df_ind[plot_features[i]],
                           autocolorscale=False,
                           colorscale=list_colscale[i],
                           marker=marker_1,
                           reversescale=False,
                           showscale=True,
                           colorbar=list_colbar[i],
                           zmax=max(df_ind[plot_features[i]]),
                           zmin=0,
                           text='abc' )

    fig_layout.add_trace( fig_i,
                          row=r_i+1,
                          col=c_i+1)

    if r_i < x-1:
        if c_i is y-1:
            r_i=r_i+1
            c_i=0
        else:
            c_i=c_i+1
    else:
        c_i=c_i+1


#*********************************************************************************************************************************#
# .............................................. update_geos() and update_layout() ...............................................#
#*********************************************************************************************************************************#

c_bg_geos = 'rgb(255,210,200)'

fig_layout.update_geos( lonaxis={'range': [65, 100], 'showgrid':False, 'tick0':0, 'dtick':1,
                                  'gridcolor':'rgb(152, 237, 161)', 'gridwidth':1},
                        lataxis={'range': [6, 38], 'showgrid':False, 'tick0':0, 'dtick':1,
                                 'gridcolor':'rgb(152, 237, 161)', 'gridwidth':1},
                        bgcolor=c_white,
                        resolution=110,
                        showframe=False, framecolor=c_white, framewidth=1,
                        projection={'type':'mercator', 'scale':1},
                        center={'lon':83, 'lat':23},
                        visible=True,
                        showcoastlines=False, coastlinecolor='rgb(242, 181, 90)', coastlinewidth=1,
                        showland=False, landcolor='rgb(255, 212, 138)',
                        showocean=False, oceancolor='rgb(140, 164, 255)',
                        showlakes=False, lakecolor='rgb(163, 220, 255)',
                        showrivers=False, rivercolor='rgb(5, 179, 227)', riverwidth=1,
                        showcountries=False,
                        showsubunits=False, subunitcolor='rgb(224, 177, 110)' )

fig_layout.update_layout( title={'text':'Solar Power Generation Capacity of Each State',
                                  'font':{'family':f_titlefont_1, 'size':20, 'color':c_white},
                                  'xref':'container', 'x':0.5, 'xanchor':'auto',
                                  'yref':'paper', 'yanchor':'auto',
                                  'pad':{'t':1, 'b':1, 'l':5, 'r':5} },
                           showlegend=False,
                           legend={'bgcolor':'rgb(173, 240, 196)',
                                   'bordercolor':'rgb(74, 143, 98)', 'borderwidth':2,
                                   'font':{'family':'Times New Roman', 'size':50, 'color':'rgb(32, 69, 45)'},
                                   'traceorder':'normal'},
                           margin={'l':5, 'r':0, 't':100, 'b':5},
                           width=1280, height=720,
                           autosize=False,
                           paper_bgcolor=c_white, plot_bgcolor=c_white,
                           grid={'rows':1, 'roworder':'top to bottom', 'columns':2, 'subplots':[],
                                 'xgap':0.1, 'ygap':0.1,
                                 'xside':'bottom plot', 'yside':'left plot'},
                           font={'family':f_titlefont_1, 'size':18, 'color':'rgb(16, 37, 51)'})

fig_layout.show()
