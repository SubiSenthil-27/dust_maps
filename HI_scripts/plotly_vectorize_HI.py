import plotly.graph_objects as go
import numpy as np
import math
from astropy.io import fits




text = 'vector_HI_full_galactic'

l_min, l_max = -180,180
b_min, b_max = -15,15

nl_new = 181
nb_new = 31

d_min = 0 #kpc
d_max = 20.0 #kpc
step = 0.4 #kpc (100 pc)


i0_new = (nl_new-1)/2
j0_new = (nb_new-1)/2    


l_array_new = np.linspace(l_min, l_max, nl_new)                             
b_array_new = np.linspace(b_min, b_max, nb_new)
d_array = np.arange(d_min, d_max + step, step)
nd = len(d_array)

p0 = (nd-1)/2
d0 = d_array[int(p0)]
l0_new =l_array_new[int(i0_new)]
b0_new = b_array_new[int(j0_new)]

del_l_new = (l_max - l_min) / (nl_new - 1)
del_b_new = (b_max - b_min) / (nb_new - 1)

# Open the FITS file
filename = f"{text}.fits"  # Replace with your file path
with fits.open(filename) as hdul:
    hdul.info()  # Print information about the FITS file
    
    # Access the data (usually in the primary HDU or extension HDU)
    data = hdul[0].data  # If data is in the primary HDU (index 0)
    header = hdul[0].header  # Access header information if needed

# Now 'data' contains the 3D array from the FITS file
print(data.shape)  # Check the shape of the data

# You can now use 'data' (your 3D array) for plotting or further processing
extinction_array = data

########

###  Creating figure and Plotting ###

X, Y, Z = np.meshgrid(l_array_new,b_array_new,d_array, indexing='ij')

fig = go.Figure(data=go.Volume(
    x=X.flatten(),
    y=Y.flatten(),
    z=Z.flatten(),
    value=extinction_array.flatten(),
    opacity=0.3,                   # needs to be small to see through all surfaces
    colorscale='hot',         
    colorbar=dict(title='density'),
    surface_count=50
    ))
    
fig.update_layout(
    scene=dict(
        xaxis_title='longitude (l)',  # Label for X axis
        yaxis_title='latitude (b)',   # Label for Y axis
        zaxis_title='distance (d)',   # Label for Z axis
        aspectratio=dict(x=2,y=1,z=1),
        camera=dict(eye=dict(x=1.5, y=1.5, z=1))
    )
)



print("figure created")
fig.write_html(f'{text}.html')


