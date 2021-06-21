import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio
import geojson

df_ind_fmch = pd.read_csv('./data_fm_channels.csv')

with open('indian_states_pre2019.geojson') as f:
    geojson_ind_states = geojson.load(f)

#***************************************************************************************************************#
# ............................................. go.Figure() ................................................... #
#***************************************************************************************************************#

# Colors
c_white = 'rgb(255, 255, 255)'



# Arguments

title_1 = go.choropleth.colorbar.Title( font=go.choropleth.colorbar.title.Font(color=c_white, size=15,
                                                                               family='Times New Roman'),
                                        side='bottom', text='Colorbar')
marker_1 = go.choropleth.Marker( opacity=1.0, line=go.choropleth.marker.Line(color='mintcream', width=0.4) )
colorbar_1 = go.choropleth.ColorBar( bgcolor=c_white, bordercolor=c_white, borderwidth=0.8,
                                     len=0.5, thickness=20.0, lenmode='fraction', thicknessmode='pixels',
                                     outlinecolor=c_white, outlinewidth=0.8,
                                     separatethousands=True,
                                     title=title_1,
                                     x=0.2, xanchor='left', xpad=15,
                                     y=0.25, yanchor='middle', ypad=10)


# Method

fig = go.Figure( data = go.Choropleth(
    geojson = geojson_ind_states,
    featureidkey='properties.ST_NM',
    locationmode='geojson-id',
    locations=df_ind_fmch['State'],
    z=df_ind_fmch['No Of Channels'],

    ids=[df_ind_fmch['State']],

    autocolorscale=False,
    colorscale=[[0, 'rgb(184, 231, 252)'], [1, 'rgb(3, 173, 252)']],
    marker=marker_1,
    reversescale=False,
    showscale=True,

    colorbar=colorbar_1,

    text='FM Channels',

    zmax=max(df_ind_fmch['No Of Channels']),
    zmin=min(df_ind_fmch['No Of Channels'])
) )

#***************************************************************************************************************#
# ............................................. update_geos() ................................................... #
#***************************************************************************************************************#

fig.update_geos( lonaxis={'range': [68, 98], 'showgrid':False, 'tick0':0, 'dtick':1,
                                  'gridcolor':'rgb(152, 237, 161)', 'gridwidth':1},
                         lataxis={'range': [6, 38], 'showgrid':False, 'tick0':0, 'dtick':1,
                                  'gridcolor':'rgb(152, 237, 161)', 'gridwidth':1},
                         bgcolor='rgb(255, 255, 255)',
                         resolution=110,
                         showframe=False, framecolor='rgb(105, 181, 94)', framewidth=2,
                         projection={'type':'mercator', 'scale':1},
                         center={'lon':83, 'lat':23},
                         visible=False,
                         showcoastlines=False, coastlinecolor='rgb(242, 181, 90)', coastlinewidth=1,
                         showland=False, landcolor='rgb(255, 212, 138)',
                         showocean=False, oceancolor='rgb(140, 164, 255)',
                         showlakes=False, lakecolor='rgb(163, 220, 255)',
                         showrivers=False, rivercolor='rgb(5, 179, 227)', riverwidth=1,
                         showcountries=False,
                         showsubunits=False, subunitcolor='rgb(224, 177, 110)')

#***************************************************************************************************************#
# .......................................... update_layout() ...................................................#
#***************************************************************************************************************#

fig.update_layout( title={'text':'Number of Private FM Radio Stations',
                                  'font':{'family':'Courier New', 'size':18, 'color':'rgb(10, 85, 120)'},
                                  'xref':'container', 'x':0.5, 'xanchor':'auto',
                                  'yref':'paper', 'yanchor':'auto',
                                  'pad':{'t':1, 'b':1, 'l':5, 'r':5} },
                           showlegend=True,
                           legend={'bgcolor':'rgb(173, 240, 196)',
                                   'bordercolor':'rgb(74, 143, 98)', 'borderwidth':2,
                                   'font':{'family':'Times New Roman', 'size':50, 'color':'rgb(32, 69, 45)'},
                                   'traceorder':'normal', 'tracegroupgap':10, 'itemsizing':'trace', 'itemwidth':30,
                                   'x':0, 'xanchor':'auto', 'y':0.5, 'yanchor':'auto', 'valign':'middle',
                                   'title':{'text':'Legend',
                                            'font':{'family':'Arial','size':1, 'color':'rgb(16, 37, 51)'},
                                            'side':'top left'}},
                           margin={'l':10, 'r':10, 't':100, 'b':80},
                           width=1280, height=720,
                           paper_bgcolor='rgb(255, 255, 255)', plot_bgcolor='rgb(255, 255, 255)',
                           hoverlabel={'bgcolor':'rgb(252, 255, 79)', 'bordercolor':'rgb(3, 64, 138)',
                                       'font':{'family':'Arial, sans-serif', 'size':13,'color':'rgb(3, 64, 138)'},
                                       'align':'auto', 'namelength':-1} )


#***************************************************************************************************************#
# .......................................... add_scattergeo() ...................................................#
#***************************************************************************************************************#
list_st = ['AN', 'AP', 'AR', 'AS', 'BR', 'CH', 'CT', 'DN', 'DL', 'GA', 'GJ', 'HR', 'HP', 'JK', 'JH',
           'KA', 'KL', 'LD', 'MP', 'MH', 'MN', 'ML', 'MZ', 'NL', 'OR', 'PY', 'PB', 'RJ', 'SK', 'TN',
           'TG', 'TR', 'UP', 'UK', 'WB']

c_textfont = 'rgb(12, 39, 71)'
tfont_1 = go.scattergeo.Textfont(color=c_textfont, size=8, family='Courier New')
tfont_2 = go.scattergeo.Textfont(color=c_textfont, size=9, family='Courier New')

fig.add_scattergeo(geojson=geojson_ind_states, locations=df_ind_fmch['State'],
                   text=df_ind_fmch['State'],
                   textfont=tfont_1,
                   textposition='top center',
                   featureidkey='properties.ST_NM', mode='text',
                   showlegend=False)
fig.add_scattergeo(geojson=geojson_ind_states, locations=df_ind_fmch['State'],
                   text=df_ind_fmch['No Of Channels'],
                   textfont=tfont_2,
                   textposition='bottom center',
                   featureidkey='properties.ST_NM', mode='text',
                   showlegend=False)



fig.show()

# pio.write_image(fig_ind_lit,'ind_literacy_2011',format='png', engine='kaleido')