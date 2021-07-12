import cartopy.crs as ccrs
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
import cartopy.feature as cfeature
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import numpy as np
from copy import copy

def visualize_pcolormesh(fig, axs, data_array, longitude, latitude, projection, color_scale, long_name, units, vmin, vmax, set_global=True, lonmin=-180, lonmax=180, latmin=-90, latmax=90):

    palette = copy(plt.get_cmap(color_scale))
    palette.set_under(alpha = 0)
    
    im = axs.pcolormesh(
                        longitude, latitude, data_array, 
                        cmap = palette, 
                        transform = projection,
                        vmin = vmin,
                        vmax = vmax,
                        norm = colors.Normalize(vmin = vmin, vmax = vmax),
                        shading = 'auto'
                        )
                        
    axs.add_feature(cfeature.BORDERS, edgecolor = 'black', linewidth = 1)
    axs.add_feature(cfeature.COASTLINE, edgecolor = 'black', linewidth = 1)

    if (projection == ccrs.PlateCarree()):
        axs.set_extent([lonmin, lonmax, latmin, latmax], projection)
        gl = axs.gridlines(draw_labels = True, linestyle = '--')
        gl.top_labels = False
        gl.right_labels = False
        gl.xformatter = LONGITUDE_FORMATTER
        gl.yformatter = LATITUDE_FORMATTER
        gl.xlabel_style = {'size': 16}
        gl.ylabel_style = {'size': 16}

    if(set_global):
        axs.set_global()
        axs.gridlines()

    axs.set_title(long_name, fontsize = 18, pad = 20.0)
    axs.tick_params(labelsize = 14)

    cbr = fig.colorbar(im, ax = axs, extend = 'both', orientation = 'horizontal', fraction = 0.04, pad = 0.1)   
    cbr.set_label(units, fontsize = 18)