import netCDF4 as nc
import matplotlib.pyplot as plt
import numpy as np
import datetime
import cartopy.crs as ccrs
from cartopy.feature import ShapelyFeature
import cartopy.feature as cfeature
import cartopy.io.shapereader as shpreader
import geopandas as gpd
from matplotlib import colors
from cartopy.io.shapereader import Reader
from matplotlib.font_manager import FontProperties


states_provinces = cfeature.NaturalEarthFeature(category='cultural',name='admin_1_states_provinces',scale='10m',facecolor='lightgray')
shpfilename = shpreader.natural_earth(resolution='10m', category='cultural', name='admin_0_countries')
fname = r'//home/joaopedro/arquivos_shp/ne_10m_bathymetry_K_200/ne_10m_bathymetry_K_200.shp'
fname_2 = r'//home/joaopedro/arquivos_shp/ne_10m_bathymetry_J_1000/ne_10m_bathymetry_J_1000.shp'

shape_feature = ShapelyFeature(Reader(fname).geometries(),ccrs.PlateCarree(), edgecolor='red',linestyle='--')
shape_feature_2 = ShapelyFeature(Reader(fname_2).geometries(),ccrs.PlateCarree(), edgecolor='black',linestyle='--')

# Abrindo os datasets
ds1 = nc.Dataset("/home/joaopedro/dados_ressurgencia/vento_era5_1994_2004.nc")
ds2 = nc.Dataset("/home/joaopedro/dados_ressurgencia/vento_era5_2004_2024.nc")

#definindo lat e lon 
lat = ds1['latitude'][:]
lon = ds1['longitude'][:]

# Concatenando os componentes do vento
u1 = ds1['u10'][:]
u2 = ds2['u10'][:]
u = np.concatenate((u1, u2), axis=0)

v1 = ds1['v10'][:]
v2 = ds2['v10'][:]
v = np.concatenate((v1, v2), axis=0)

# Concatenando tempo
t1 = ds1['valid_time'][:]  # ou 'time', se for o nome correto
t2 = ds2['valid_time'][:]
time = np.concatenate((t1, t2), axis=0)

tempo=[]
for i in range(len(time)):
    tempo.append(datetime.datetime.fromtimestamp(time[i]).date())
'''Criando medias sazonais da tensão de cisalhamento do vento'''
current_data=tempo[0]
data_final=tempo[-1]

verao_u=[]
verao_v=[]

outono_u=[]
outono_v=[]

inverno_u=[]
inverno_v=[]

primavera_u=[]
primavera_v=[]

while current_data <= data_final:
    if str(current_data.strftime('%m')) in ['01','02','12']:
        verao_u.append((1.225*0.0015*np.sqrt(u[tempo.index(current_data),:,:]**2+v[tempo.index(current_data),:,:]**2)*u[tempo.index(current_data),:,:]))
        verao_v.append((1.225*0.0015*np.sqrt(u[tempo.index(current_data),:,:]**2+v[tempo.index(current_data),:,:]**2)*v[tempo.index(current_data),:,:]))

        print(str(current_data))
        current_data = current_data + datetime.timedelta(days=1)
    elif str(current_data.strftime('%m')) in ['03','04','05']:
        outono_u.append((1.225*0.0015*np.sqrt(u[tempo.index(current_data),:,:]**2+v[tempo.index(current_data),:,:]**2)*u[tempo.index(current_data),:,:]))
        outono_v.append((1.225*0.0015*np.sqrt(u[tempo.index(current_data),:,:]**2+v[tempo.index(current_data),:,:]**2)*v[tempo.index(current_data),:,:]))

        print(str(current_data))
        current_data = current_data + datetime.timedelta(days=1)

    elif str(current_data.strftime('%m')) in ['06','07','08']:
        inverno_u.append((1.225*0.0015*np.sqrt(u[tempo.index(current_data),:,:]**2+v[tempo.index(current_data),:,:]**2)*u[tempo.index(current_data),:,:]))
        inverno_v.append((1.225*0.0015*np.sqrt(u[tempo.index(current_data),:,:]**2+v[tempo.index(current_data),:,:]**2)*v[tempo.index(current_data),:,:]))
        print(str(current_data))
        current_data = current_data + datetime.timedelta(days=1)
    elif str(current_data.strftime('%m')) in ['09','10','11']:
        primavera_u.append((1.225*0.0015*np.sqrt(u[tempo.index(current_data),:,:]**2+v[tempo.index(current_data),:,:]**2)*u[tempo.index(current_data),:,:]))
        primavera_v.append((1.225*0.0015*np.sqrt(u[tempo.index(current_data),:,:]**2+v[tempo.index(current_data),:,:]**2)*v[tempo.index(current_data),:,:]))
        print(str(current_data))
        current_data = current_data + datetime.timedelta(days=1)
    else:
        print("não tem dado - "+str(current_data))
        continue

'''calculando as medias'''
verao_u_media=np.mean(np.ma.stack(verao_u,2),axis=2)
verao_v_media=np.mean(np.ma.stack(verao_v,2),axis=2)
mag_verao=np.sqrt(verao_u_media**2+verao_v_media**2)

outono_u_media=np.mean(np.ma.stack(outono_u,2),axis=2)
outono_v_media=np.mean(np.ma.stack(outono_v,2),axis=2)
mag_outono=np.sqrt(outono_u_media**2+outono_v_media**2)

inverno_u_media=np.mean(np.ma.stack(inverno_u,2),axis=2)
inverno_v_media=np.mean(np.ma.stack(inverno_v,2),axis=2)
mag_inverno=np.sqrt(inverno_u_media**2+inverno_v_media**2)


primavera_u_media=np.mean(np.ma.stack(primavera_u,2),axis=2)
primavera_v_media=np.mean(np.ma.stack(primavera_v,2),axis=2)
mag_primavera=np.sqrt(primavera_u_media**2+primavera_v_media**2)


'''plotando'''
fig, axes=plt.subplots(2,2,subplot_kw={'projection': ccrs.PlateCarree()}, figsize=(10,6))
levels = np.linspace(0,0.1,11)
# Subplot 1: Verão
ax1 = axes[0,0]
contour1 = ax1.contourf(lon[::3],lat[::3], mag_verao[::3,::3], levels=levels, transform=ccrs.PlateCarree(), cmap="RdBu_r", vmin=0, vmax=0.1,extend='both')
quiver1=ax1.quiver(lon[::3],lat[::3],verao_u_media[::3,::3],verao_v_media[::3,::3],scale=0.55)
ax1.set_title('Verão')
ax1.add_feature(states_provinces, edgecolor='black')
ax1.add_feature(shape_feature, facecolor='none')
ax1.add_feature(shape_feature_2, facecolor='none')
g1 = ax1.gridlines(crs=ccrs.PlateCarree(), linestyle='-.',linewidth=0, color='gray', draw_labels=True)
g1.right_labels = False
g1.top_labels = False
g1.bottom_labels = False  
ax1.quiverkey(quiver1,X=-45,Y=-17,U= 0.05,label= r'$0.05 \frac{N}{m²}$',labelpos='E', coordinates='data',zorder=3,fontproperties=FontProperties(size=14))

# Subplot 2:outono
ax2=axes[0,1]
contour2 = ax2.contourf(lon[::3],lat[::3],mag_outono[::3,::3], levels=levels, transform=ccrs.PlateCarree(), cmap="RdBu_r", vmin=0, vmax=0.1)
quiver2=ax2.quiver(lon[::3],lat[::3],outono_u_media[::3,::3],outono_v_media[::3,::3],scale=0.55)
ax2.set_title('outono')
ax2.add_feature(states_provinces, edgecolor='black')
ax2.add_feature(shape_feature, facecolor='none')
ax2.add_feature(shape_feature_2, facecolor='none')
g2 = ax2.gridlines(crs=ccrs.PlateCarree(), linestyle='-.', linewidth=0,color='gray', draw_labels=False)
g2.right_labels = False
g2.top_labels = False
g2.left_labels = False  
g2.bottom_labels = False  
ax2.quiverkey(quiver2,X=-45,Y=-17,U= 0.05,label= r'$0.05 \frac{N}{m²}$',labelpos='E', coordinates='data',zorder=3,fontproperties=FontProperties(size=14))

# Subplot 3:inverno
ax3=axes[1,0]
contour3 = ax3.contourf(lon[::3],lat[::3],mag_inverno[::3,::3], levels=levels, transform=ccrs.PlateCarree(), cmap="RdBu_r", vmin=0, vmax=0.1)
quiver3=ax3.quiver(lon[::3],lat[::3],inverno_u_media[::3,::3],inverno_v_media[::3,::3],scale=0.55)
ax3.set_title('Inverno')
ax3.add_feature(states_provinces, edgecolor='black')
ax3.add_feature(shape_feature, facecolor='none')
ax3.add_feature(shape_feature_2, facecolor='none')
g3 = ax3.gridlines(crs=ccrs.PlateCarree(), linestyle='-.', linewidth=0,color='gray',draw_labels=True)
g3.right_labels = False
g3.top_labels = False
ax3.quiverkey(quiver3,X=-45,Y=-17,U= 0.05,label= r'$0.05 \frac{N}{m²}$',labelpos='E', coordinates='data',zorder=3,fontproperties=FontProperties(size=14))

# Subplot 4:primavera
ax4=axes[1,1]
contour4 = ax4.contourf(lon[::3],lat[::3],mag_primavera[::3,::3], levels=levels, transform=ccrs.PlateCarree(), cmap="RdBu_r", vmin=0, vmax=0.1,extend='both')
quiver4=ax4.quiver(lon[::3],lat[::3],primavera_u_media[::3,::3],primavera_v_media[::3,::3],scale=0.55)
ax4.set_title('primavera')
ax4.add_feature(states_provinces, edgecolor='black')
ax4.add_feature(shape_feature, facecolor='none')
ax4.add_feature(shape_feature_2, facecolor='none')
g4 = ax4.gridlines(crs=ccrs.PlateCarree(), linestyle='-.', linewidth=0,color='gray', draw_labels=True)
g4.right_labels = False
g4.top_labels = False
g4.left_labels = False
ax4.quiverkey(quiver4,X=-45,Y=-17,U= 0.05,label= r'$0.05 \frac{N}{m²}$',labelpos='E', coordinates='data',zorder=3,fontproperties=FontProperties(size=14))

plt.suptitle('Tensão de Cisalhamento do Vento (N/m²)')
params = fig.subplotpars

left_edge = params.left
right_edge = params.right
print(left_edge)
print(right_edge)
left = 0.30   
right = 0.45   
width =0.4 
cbar_bottom = 0.05  # Posição vertical da colorbar (ajuste conforme necessário)
cbar_height = 0.02  # Altura da colorbar
cbar_ax = fig.add_axes([left, cbar_bottom, right, cbar_height])
cbar=fig.colorbar(contour1,cax=cbar_ax,extend='both',orientation='horizontal',fraction=.05)
cbar.set_label('N/m²',fontsize=12,fontweight='bold')
#fig.subplots_adjust(wspace=-0.7, hspace=0.2,left=0.1,right=0.9,bottom=0.1,top=0.9)
plt.show()
