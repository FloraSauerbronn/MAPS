from tokenize import PlainToken
from matplotlib.offsetbox import AnchoredText
import matplotlib.pyplot as plt

import cartopy.crs as ccrs
import cartopy.feature as cfeature
import geopandas as gpd
##COLOCAR O CHAPE FILE ESTA DESFORMATANDO O MAPA##

# ___Load the shapefile or GeoJSON containing state boundaries and names__
shapefile_path = 'C:/Users/flora/OneDrive/Documentos/MESTRADO_UFSC/rotinas/python/BR_UF_2022/BR_UF_2022.shp'
gdf = gpd.read_file(shapefile_path)

def main():
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())

    #CORDENADAS
    ax.set_extent([-40, -34, -8, -2], crs=ccrs.PlateCarree())
    # Plot state names at centroid of each state
    for idx, row in gdf.iterrows():
        state_name = row['SIGLA_UF']  # Replace with the actual column name
        centroid = row['geometry'].centroid
        plt.text(centroid.x, centroid.y, state_name, fontsize=12, fontweight='bold', ha='center', va='center')

    # Put a background image on for nice sea rendering.
    ax.stock_img()

    # Create a feature for States/Admin 1 regions at 1:50m from Natural Earth
    states_provinces = cfeature.NaturalEarthFeature(
        category='cultural',
        name='admin_1_states_provinces_lines',
        scale='50m',
        facecolor='none')



    #ax.add_feature(cfeature.LAND)

    ax.add_feature(cfeature.COASTLINE, edgecolor='black')
    #Add states borders
    ax.add_feature(states_provinces , edgecolor='gray', linestyle=':') #
    #Add countrys borders
    ax.add_feature(cfeature.BORDERS, linestyle=':')

 # Add gridlines with labels on the left and bottom
    gl = ax.gridlines(draw_labels=False, dms=True, x_inline=False, y_inline=False)
    gl.right_labels = True 
    gl.bottom_labels = True 
    gl.xlabel_style = {'fontsize': 16}  # Adjust the fontsize as needed
    gl.ylabel_style = {'fontsize': 16}  # Adjust the fontsize as needed

    # Set gridline locators to show every 5 degrees
    #gl.xlocator = plt.FixedLocator(range(-0, -30, 5))
    #gl.ylocator = plt.FixedLocator(range(-10, 0 ,2))


# Add title to the map
    ax.set_title('Área de Estudo', fontsize=20)


    # Save the figure with transparent background
    plt.savefig('C:/Users/flora/OneDrive/Documentos/MESTRADO_UFSC/rotinas/python/Ares_estudo.png')


    plt.show()


if __name__ == '__main__':
    main()