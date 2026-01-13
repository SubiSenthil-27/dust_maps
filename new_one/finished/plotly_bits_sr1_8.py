import plotly.graph_objects as go
import numpy as np
import math
from astropy.io import fits

text = 'vector_226_216'

l_min, l_max = 216, 226.02
b_min, b_max = -5, 5.02

nl_new = 76
nb_new = 9

d_min = 0 #kpc
d_max = 12.0 #kpc
step = 0.1 #kpc (100 pc)


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


# --- Parameters  for the cube---


# Box 1
# --- Parameters  for the cube---

l_max = 226
l_min = 223
b_max = 4
b_min = -4
d_near = 0.3  # front face (near)
d_far  = 0.7  # back face (far)


# Rectangle corners (for near and far planes)
rect_l = [l_min, l_max, l_max, l_min, l_min]
rect_b = [b_min, b_min, b_max, b_max, b_min]
rect_d_near = [d_near]*len(rect_l)
rect_d_far  = [d_far]*len(rect_l)

# --- Create Plotly traces ---

# Front (near) face
rect_near = go.Scatter3d(
    x=rect_l, y=rect_b, z=rect_d_near,
    mode='lines',
    line=dict(color='lime', width=5),
    showlegend=False
)

# Back (far) face
rect_far = go.Scatter3d(
    x=rect_l, y=rect_b, z=rect_d_far,
    mode='lines',
    line=dict(color='lime', width=5),
    showlegend=False
)

# Connect corresponding corners (vertical edges)
edges = []
for i in range(4):  # 4 corners
    edge = go.Scatter3d(
        x=[rect_l[i], rect_l[i]],
        y=[rect_b[i], rect_b[i]],
        z=[d_near, d_far],
        mode='lines',
        line=dict(color='lime', width=5),
        showlegend=False
    )
    edges.append(edge)

# --- Add all to figure ---
fig.add_trace(rect_near)
fig.add_trace(rect_far)
for edge in edges:
    fig.add_trace(edge)

# Box 2
# --- Parameters  for the cube---

l_max = 226
l_min = 223
b_max = 1.2
b_min = -2.7
d_near = 1.5  # front face (near)
d_far  = 2.1  # back face (far)


# Rectangle corners (for near and far planes)
rect_l = [l_min, l_max, l_max, l_min, l_min]
rect_b = [b_min, b_min, b_max, b_max, b_min]
rect_d_near = [d_near]*len(rect_l)
rect_d_far  = [d_far]*len(rect_l)

# --- Create Plotly traces ---

# Front (near) face
rect_near = go.Scatter3d(
    x=rect_l, y=rect_b, z=rect_d_near,
    mode='lines',
    line=dict(color='lime', width=5),
    showlegend=False
)

# Back (far) face
rect_far = go.Scatter3d(
    x=rect_l, y=rect_b, z=rect_d_far,
    mode='lines',
    line=dict(color='lime', width=5),
    showlegend=False
)

# Connect corresponding corners (vertical edges)
edges = []
for i in range(4):  # 4 corners
    edge = go.Scatter3d(
        x=[rect_l[i], rect_l[i]],
        y=[rect_b[i], rect_b[i]],
        z=[d_near, d_far],
        mode='lines',
        line=dict(color='lime', width=5),
        showlegend=False
    )
    edges.append(edge)

# --- Add all to figure ---
fig.add_trace(rect_near)
fig.add_trace(rect_far)
for edge in edges:
    fig.add_trace(edge)

# Box 3
# --- Parameters  for the cube---

l_max = 226
l_min = 223
b_max = 0.8
b_min = -1.5
d_near = 3.5  # front face (near)
d_far  = 4.2  # back face (far)


# Rectangle corners (for near and far planes)
rect_l = [l_min, l_max, l_max, l_min, l_min]
rect_b = [b_min, b_min, b_max, b_max, b_min]
rect_d_near = [d_near]*len(rect_l)
rect_d_far  = [d_far]*len(rect_l)

# --- Create Plotly traces ---

# Front (near) face
rect_near = go.Scatter3d(
    x=rect_l, y=rect_b, z=rect_d_near,
    mode='lines',
    line=dict(color='lime', width=5),
    showlegend=False
)

# Back (far) face
rect_far = go.Scatter3d(
    x=rect_l, y=rect_b, z=rect_d_far,
    mode='lines',
    line=dict(color='lime', width=5),
    showlegend=False
)

# Connect corresponding corners (vertical edges)
edges = []
for i in range(4):  # 4 corners
    edge = go.Scatter3d(
        x=[rect_l[i], rect_l[i]],
        y=[rect_b[i], rect_b[i]],
        z=[d_near, d_far],
        mode='lines',
        line=dict(color='lime', width=5),
        showlegend=False
    )
    edges.append(edge)

# --- Add all to figure ---
fig.add_trace(rect_near)
fig.add_trace(rect_far)
for edge in edges:
    fig.add_trace(edge)

# Box 4
# --- Parameters  for the cube---

l_max = 226
l_min = 223
b_max = 1
b_min = -2
d_near = 4.6  # front face (near)
d_far  = 5.7  # back face (far)


# Rectangle corners (for near and far planes)
rect_l = [l_min, l_max, l_max, l_min, l_min]
rect_b = [b_min, b_min, b_max, b_max, b_min]
rect_d_near = [d_near]*len(rect_l)
rect_d_far  = [d_far]*len(rect_l)

# --- Create Plotly traces ---

# Front (near) face
rect_near = go.Scatter3d(
    x=rect_l, y=rect_b, z=rect_d_near,
    mode='lines',
    line=dict(color='lime', width=5),
    showlegend=False
)

# Back (far) face
rect_far = go.Scatter3d(
    x=rect_l, y=rect_b, z=rect_d_far,
    mode='lines',
    line=dict(color='lime', width=5),
    showlegend=False
)

# Connect corresponding corners (vertical edges)
edges = []
for i in range(4):  # 4 corners
    edge = go.Scatter3d(
        x=[rect_l[i], rect_l[i]],
        y=[rect_b[i], rect_b[i]],
        z=[d_near, d_far],
        mode='lines',
        line=dict(color='lime', width=5),
        showlegend=False
    )
    edges.append(edge)

# --- Add all to figure ---
fig.add_trace(rect_near)
fig.add_trace(rect_far)
for edge in edges:
    fig.add_trace(edge)

# Box 5
# --- Parameters  for the cube---

l_max = 226
l_min = 223
b_max = 1
b_min = -2.1
d_near = 5.7  # front face (near)
d_far  = 6.9 # back face (far)


# Rectangle corners (for near and far planes)
rect_l = [l_min, l_max, l_max, l_min, l_min]
rect_b = [b_min, b_min, b_max, b_max, b_min]
rect_d_near = [d_near]*len(rect_l)
rect_d_far  = [d_far]*len(rect_l)

# --- Create Plotly traces ---

# Front (near) face
rect_near = go.Scatter3d(
    x=rect_l, y=rect_b, z=rect_d_near,
    mode='lines',
    line=dict(color='lime', width=5),
    showlegend=False
)

# Back (far) face
rect_far = go.Scatter3d(
    x=rect_l, y=rect_b, z=rect_d_far,
    mode='lines',
    line=dict(color='lime', width=5),
    showlegend=False
)

# Connect corresponding corners (vertical edges)
edges = []
for i in range(4):  # 4 corners
    edge = go.Scatter3d(
        x=[rect_l[i], rect_l[i]],
        y=[rect_b[i], rect_b[i]],
        z=[d_near, d_far],
        mode='lines',
        line=dict(color='lime', width=5),
        showlegend=False
    )
    edges.append(edge)

# --- Add all to figure ---
fig.add_trace(rect_near)
fig.add_trace(rect_far)
for edge in edges:
    fig.add_trace(edge)

# Box 6
# --- Parameters  for the cube---

l_max = 226
l_min = 223
b_max = 0.8
b_min = -0.8
d_near = 6.9  # front face (near)
d_far  = 8.1  # back face (far)


# Rectangle corners (for near and far planes)
rect_l = [l_min, l_max, l_max, l_min, l_min]
rect_b = [b_min, b_min, b_max, b_max, b_min]
rect_d_near = [d_near]*len(rect_l)
rect_d_far  = [d_far]*len(rect_l)

# --- Create Plotly traces ---

# Front (near) face
rect_near = go.Scatter3d(
    x=rect_l, y=rect_b, z=rect_d_near,
    mode='lines',
    line=dict(color='lime', width=5),
    showlegend=False
)

# Back (far) face
rect_far = go.Scatter3d(
    x=rect_l, y=rect_b, z=rect_d_far,
    mode='lines',
    line=dict(color='lime', width=5),
    showlegend=False
)

# Connect corresponding corners (vertical edges)
edges = []
for i in range(4):  # 4 corners
    edge = go.Scatter3d(
        x=[rect_l[i], rect_l[i]],
        y=[rect_b[i], rect_b[i]],
        z=[d_near, d_far],
        mode='lines',
        line=dict(color='lime', width=5),
        showlegend=False
    )
    edges.append(edge)

# --- Add all to figure ---
fig.add_trace(rect_near)
fig.add_trace(rect_far)
for edge in edges:
    fig.add_trace(edge)

# Box 7
# --- Parameters  for the cube---

l_max = 226
l_min = 223
b_max = 0.8
b_min = -0.8
d_near = 8.1  # front face (near)
d_far  = 9.5  # back face (far)


# Rectangle corners (for near and far planes)
rect_l = [l_min, l_max, l_max, l_min, l_min]
rect_b = [b_min, b_min, b_max, b_max, b_min]
rect_d_near = [d_near]*len(rect_l)
rect_d_far  = [d_far]*len(rect_l)

# --- Create Plotly traces ---

# Front (near) face
rect_near = go.Scatter3d(
    x=rect_l, y=rect_b, z=rect_d_near,
    mode='lines',
    line=dict(color='lime', width=5),
    showlegend=False
)

# Back (far) face
rect_far = go.Scatter3d(
    x=rect_l, y=rect_b, z=rect_d_far,
    mode='lines',
    line=dict(color='lime', width=5),
    showlegend=False
)

# Connect corresponding corners (vertical edges)
edges = []
for i in range(4):  # 4 corners
    edge = go.Scatter3d(
        x=[rect_l[i], rect_l[i]],
        y=[rect_b[i], rect_b[i]],
        z=[d_near, d_far],
        mode='lines',
        line=dict(color='lime', width=5),
        showlegend=False
    )
    edges.append(edge)

# --- Add all to figure ---
fig.add_trace(rect_near)
fig.add_trace(rect_far)
for edge in edges:
    fig.add_trace(edge)

#############################
### Next set ### 


# Box 1
# --- Parameters  for the cube---

l_max = 223
l_min = 220
b_max = 4
b_min = -4
d_near = 0.3  # front face (near)
d_far  = 0.7  # back face (far)


# Rectangle corners (for near and far planes)
rect_l = [l_min, l_max, l_max, l_min, l_min]
rect_b = [b_min, b_min, b_max, b_max, b_min]
rect_d_near = [d_near]*len(rect_l)
rect_d_far  = [d_far]*len(rect_l)

# --- Create Plotly traces ---

# Front (near) face
rect_near = go.Scatter3d(
    x=rect_l, y=rect_b, z=rect_d_near,
    mode='lines',
    line=dict(color='lime', width=5),
    showlegend=False
)

# Back (far) face
rect_far = go.Scatter3d(
    x=rect_l, y=rect_b, z=rect_d_far,
    mode='lines',
    line=dict(color='lime', width=5),
    showlegend=False
)

# Connect corresponding corners (vertical edges)
edges = []
for i in range(4):  # 4 corners
    edge = go.Scatter3d(
        x=[rect_l[i], rect_l[i]],
        y=[rect_b[i], rect_b[i]],
        z=[d_near, d_far],
        mode='lines',
        line=dict(color='lime', width=5),
        showlegend=False
    )
    edges.append(edge)

# --- Add all to figure ---
fig.add_trace(rect_near)
fig.add_trace(rect_far)
for edge in edges:
    fig.add_trace(edge)

# Box 2
# --- Parameters  for the cube---

l_max = 223
l_min = 220
b_max = 1.2
b_min = -2.7
d_near = 1.5  # front face (near)
d_far  = 2.1  # back face (far)


# Rectangle corners (for near and far planes)
rect_l = [l_min, l_max, l_max, l_min, l_min]
rect_b = [b_min, b_min, b_max, b_max, b_min]
rect_d_near = [d_near]*len(rect_l)
rect_d_far  = [d_far]*len(rect_l)

# --- Create Plotly traces ---

# Front (near) face
rect_near = go.Scatter3d(
    x=rect_l, y=rect_b, z=rect_d_near,
    mode='lines',
    line=dict(color='lime', width=5),
    showlegend=False
)

# Back (far) face
rect_far = go.Scatter3d(
    x=rect_l, y=rect_b, z=rect_d_far,
    mode='lines',
    line=dict(color='lime', width=5),
    showlegend=False
)

# Connect corresponding corners (vertical edges)
edges = []
for i in range(4):  # 4 corners
    edge = go.Scatter3d(
        x=[rect_l[i], rect_l[i]],
        y=[rect_b[i], rect_b[i]],
        z=[d_near, d_far],
        mode='lines',
        line=dict(color='lime', width=5),
        showlegend=False
    )
    edges.append(edge)

# --- Add all to figure ---
fig.add_trace(rect_near)
fig.add_trace(rect_far)
for edge in edges:
    fig.add_trace(edge)

# Box 3
# --- Parameters  for the cube---

l_max = 223
l_min = 220
b_max = 0.8
b_min = -1.5
d_near = 3.5  # front face (near)
d_far  = 4.2  # back face (far)


# Rectangle corners (for near and far planes)
rect_l = [l_min, l_max, l_max, l_min, l_min]
rect_b = [b_min, b_min, b_max, b_max, b_min]
rect_d_near = [d_near]*len(rect_l)
rect_d_far  = [d_far]*len(rect_l)

# --- Create Plotly traces ---

# Front (near) face
rect_near = go.Scatter3d(
    x=rect_l, y=rect_b, z=rect_d_near,
    mode='lines',
    line=dict(color='lime', width=5),
    showlegend=False
)

# Back (far) face
rect_far = go.Scatter3d(
    x=rect_l, y=rect_b, z=rect_d_far,
    mode='lines',
    line=dict(color='lime', width=5),
    showlegend=False
)

# Connect corresponding corners (vertical edges)
edges = []
for i in range(4):  # 4 corners
    edge = go.Scatter3d(
        x=[rect_l[i], rect_l[i]],
        y=[rect_b[i], rect_b[i]],
        z=[d_near, d_far],
        mode='lines',
        line=dict(color='lime', width=5),
        showlegend=False
    )
    edges.append(edge)

# --- Add all to figure ---
fig.add_trace(rect_near)
fig.add_trace(rect_far)
for edge in edges:
    fig.add_trace(edge)

# Box 4
# --- Parameters  for the cube---

l_max = 223
l_min = 220
b_max = 1
b_min = -2
d_near = 4.6  # front face (near)
d_far  = 5.7  # back face (far)


# Rectangle corners (for near and far planes)
rect_l = [l_min, l_max, l_max, l_min, l_min]
rect_b = [b_min, b_min, b_max, b_max, b_min]
rect_d_near = [d_near]*len(rect_l)
rect_d_far  = [d_far]*len(rect_l)

# --- Create Plotly traces ---

# Front (near) face
rect_near = go.Scatter3d(
    x=rect_l, y=rect_b, z=rect_d_near,
    mode='lines',
    line=dict(color='lime', width=5),
    showlegend=False
)

# Back (far) face
rect_far = go.Scatter3d(
    x=rect_l, y=rect_b, z=rect_d_far,
    mode='lines',
    line=dict(color='lime', width=5),
    showlegend=False
)

# Connect corresponding corners (vertical edges)
edges = []
for i in range(4):  # 4 corners
    edge = go.Scatter3d(
        x=[rect_l[i], rect_l[i]],
        y=[rect_b[i], rect_b[i]],
        z=[d_near, d_far],
        mode='lines',
        line=dict(color='lime', width=5),
        showlegend=False
    )
    edges.append(edge)

# --- Add all to figure ---
fig.add_trace(rect_near)
fig.add_trace(rect_far)
for edge in edges:
    fig.add_trace(edge)

# Box 5
# --- Parameters  for the cube---

l_max = 223
l_min = 220
b_max = 1
b_min = -2.1
d_near = 5.7  # front face (near)
d_far  = 6.9 # back face (far)


# Rectangle corners (for near and far planes)
rect_l = [l_min, l_max, l_max, l_min, l_min]
rect_b = [b_min, b_min, b_max, b_max, b_min]
rect_d_near = [d_near]*len(rect_l)
rect_d_far  = [d_far]*len(rect_l)

# --- Create Plotly traces ---

# Front (near) face
rect_near = go.Scatter3d(
    x=rect_l, y=rect_b, z=rect_d_near,
    mode='lines',
    line=dict(color='lime', width=5),
    showlegend=False
)

# Back (far) face
rect_far = go.Scatter3d(
    x=rect_l, y=rect_b, z=rect_d_far,
    mode='lines',
    line=dict(color='lime', width=5),
    showlegend=False
)

# Connect corresponding corners (vertical edges)
edges = []
for i in range(4):  # 4 corners
    edge = go.Scatter3d(
        x=[rect_l[i], rect_l[i]],
        y=[rect_b[i], rect_b[i]],
        z=[d_near, d_far],
        mode='lines',
        line=dict(color='lime', width=5),
        showlegend=False
    )
    edges.append(edge)

# --- Add all to figure ---
fig.add_trace(rect_near)
fig.add_trace(rect_far)
for edge in edges:
    fig.add_trace(edge)

# Box 6
# --- Parameters  for the cube---

l_max = 223
l_min = 220
b_max = 0.8
b_min = -0.8
d_near = 6.9  # front face (near)
d_far  = 8.1  # back face (far)


# Rectangle corners (for near and far planes)
rect_l = [l_min, l_max, l_max, l_min, l_min]
rect_b = [b_min, b_min, b_max, b_max, b_min]
rect_d_near = [d_near]*len(rect_l)
rect_d_far  = [d_far]*len(rect_l)

# --- Create Plotly traces ---

# Front (near) face
rect_near = go.Scatter3d(
    x=rect_l, y=rect_b, z=rect_d_near,
    mode='lines',
    line=dict(color='lime', width=5),
    showlegend=False
)

# Back (far) face
rect_far = go.Scatter3d(
    x=rect_l, y=rect_b, z=rect_d_far,
    mode='lines',
    line=dict(color='lime', width=5),
    showlegend=False
)

# Connect corresponding corners (vertical edges)
edges = []
for i in range(4):  # 4 corners
    edge = go.Scatter3d(
        x=[rect_l[i], rect_l[i]],
        y=[rect_b[i], rect_b[i]],
        z=[d_near, d_far],
        mode='lines',
        line=dict(color='lime', width=5),
        showlegend=False
    )
    edges.append(edge)

# --- Add all to figure ---
fig.add_trace(rect_near)
fig.add_trace(rect_far)
for edge in edges:
    fig.add_trace(edge)

# Box 7
# --- Parameters  for the cube---

l_max = 223
l_min = 220
b_max = 0.8
b_min = -0.8
d_near = 8.1  # front face (near)
d_far  = 9.3  # back face (far)


# Rectangle corners (for near and far planes)
rect_l = [l_min, l_max, l_max, l_min, l_min]
rect_b = [b_min, b_min, b_max, b_max, b_min]
rect_d_near = [d_near]*len(rect_l)
rect_d_far  = [d_far]*len(rect_l)

# --- Create Plotly traces ---

# Front (near) face
rect_near = go.Scatter3d(
    x=rect_l, y=rect_b, z=rect_d_near,
    mode='lines',
    line=dict(color='lime', width=5),
    showlegend=False
)

# Back (far) face
rect_far = go.Scatter3d(
    x=rect_l, y=rect_b, z=rect_d_far,
    mode='lines',
    line=dict(color='lime', width=5),
    showlegend=False
)

# Connect corresponding corners (vertical edges)
edges = []
for i in range(4):  # 4 corners
    edge = go.Scatter3d(
        x=[rect_l[i], rect_l[i]],
        y=[rect_b[i], rect_b[i]],
        z=[d_near, d_far],
        mode='lines',
        line=dict(color='lime', width=5),
        showlegend=False
    )
    edges.append(edge)

# --- Add all to figure ---
fig.add_trace(rect_near)
fig.add_trace(rect_far)
for edge in edges:
    fig.add_trace(edge)

# Box 8
# --- Parameters  for the cube---

l_max = 223
l_min = 220
b_max = 0.8
b_min = -0.8
d_near = 9.3  # front face (near)
d_far  = 10.2  # back face (far)


# Rectangle corners (for near and far planes)
rect_l = [l_min, l_max, l_max, l_min, l_min]
rect_b = [b_min, b_min, b_max, b_max, b_min]
rect_d_near = [d_near]*len(rect_l)
rect_d_far  = [d_far]*len(rect_l)

# --- Create Plotly traces ---

# Front (near) face
rect_near = go.Scatter3d(
    x=rect_l, y=rect_b, z=rect_d_near,
    mode='lines',
    line=dict(color='lime', width=5),
    showlegend=False
)

# Back (far) face
rect_far = go.Scatter3d(
    x=rect_l, y=rect_b, z=rect_d_far,
    mode='lines',
    line=dict(color='lime', width=5),
    showlegend=False
)

# Connect corresponding corners (vertical edges)
edges = []
for i in range(4):  # 4 corners
    edge = go.Scatter3d(
        x=[rect_l[i], rect_l[i]],
        y=[rect_b[i], rect_b[i]],
        z=[d_near, d_far],
        mode='lines',
        line=dict(color='lime', width=5),
        showlegend=False
    )
    edges.append(edge)

# --- Add all to figure ---
fig.add_trace(rect_near)
fig.add_trace(rect_far)
for edge in edges:
    fig.add_trace(edge)

#############################
### Next set ### 


# Box 1
# --- Parameters  for the cube---

l_max = 220
l_min = 216
b_max = 4
b_min = -4
d_near = 0.3  # front face (near)
d_far  = 0.7  # back face (far)


# Rectangle corners (for near and far planes)
rect_l = [l_min, l_max, l_max, l_min, l_min]
rect_b = [b_min, b_min, b_max, b_max, b_min]
rect_d_near = [d_near]*len(rect_l)
rect_d_far  = [d_far]*len(rect_l)

# --- Create Plotly traces ---

# Front (near) face
rect_near = go.Scatter3d(
    x=rect_l, y=rect_b, z=rect_d_near,
    mode='lines',
    line=dict(color='lime', width=5),
    showlegend=False
)

# Back (far) face
rect_far = go.Scatter3d(
    x=rect_l, y=rect_b, z=rect_d_far,
    mode='lines',
    line=dict(color='lime', width=5),
    showlegend=False
)

# Connect corresponding corners (vertical edges)
edges = []
for i in range(4):  # 4 corners
    edge = go.Scatter3d(
        x=[rect_l[i], rect_l[i]],
        y=[rect_b[i], rect_b[i]],
        z=[d_near, d_far],
        mode='lines',
        line=dict(color='lime', width=5),
        showlegend=False
    )
    edges.append(edge)

# --- Add all to figure ---
fig.add_trace(rect_near)
fig.add_trace(rect_far)
for edge in edges:
    fig.add_trace(edge)

# Box 2
# --- Parameters  for the cube---

l_max = 220
l_min = 216
b_max = 1.2
b_min = -2.7
d_near = 1.5  # front face (near)
d_far  = 2.1  # back face (far)


# Rectangle corners (for near and far planes)
rect_l = [l_min, l_max, l_max, l_min, l_min]
rect_b = [b_min, b_min, b_max, b_max, b_min]
rect_d_near = [d_near]*len(rect_l)
rect_d_far  = [d_far]*len(rect_l)

# --- Create Plotly traces ---

# Front (near) face
rect_near = go.Scatter3d(
    x=rect_l, y=rect_b, z=rect_d_near,
    mode='lines',
    line=dict(color='lime', width=5),
    showlegend=False
)

# Back (far) face
rect_far = go.Scatter3d(
    x=rect_l, y=rect_b, z=rect_d_far,
    mode='lines',
    line=dict(color='lime', width=5),
    showlegend=False
)

# Connect corresponding corners (vertical edges)
edges = []
for i in range(4):  # 4 corners
    edge = go.Scatter3d(
        x=[rect_l[i], rect_l[i]],
        y=[rect_b[i], rect_b[i]],
        z=[d_near, d_far],
        mode='lines',
        line=dict(color='lime', width=5),
        showlegend=False
    )
    edges.append(edge)

# --- Add all to figure ---
fig.add_trace(rect_near)
fig.add_trace(rect_far)
for edge in edges:
    fig.add_trace(edge)

# Box 3
# --- Parameters  for the cube---

l_max = 220
l_min = 216
b_max = 0.8
b_min = -1.5
d_near = 3.5  # front face (near)
d_far  = 4.2  # back face (far)


# Rectangle corners (for near and far planes)
rect_l = [l_min, l_max, l_max, l_min, l_min]
rect_b = [b_min, b_min, b_max, b_max, b_min]
rect_d_near = [d_near]*len(rect_l)
rect_d_far  = [d_far]*len(rect_l)

# --- Create Plotly traces ---

# Front (near) face
rect_near = go.Scatter3d(
    x=rect_l, y=rect_b, z=rect_d_near,
    mode='lines',
    line=dict(color='lime', width=5),
    showlegend=False
)

# Back (far) face
rect_far = go.Scatter3d(
    x=rect_l, y=rect_b, z=rect_d_far,
    mode='lines',
    line=dict(color='lime', width=5),
    showlegend=False
)

# Connect corresponding corners (vertical edges)
edges = []
for i in range(4):  # 4 corners
    edge = go.Scatter3d(
        x=[rect_l[i], rect_l[i]],
        y=[rect_b[i], rect_b[i]],
        z=[d_near, d_far],
        mode='lines',
        line=dict(color='lime', width=5),
        showlegend=False
    )
    edges.append(edge)

# --- Add all to figure ---
fig.add_trace(rect_near)
fig.add_trace(rect_far)
for edge in edges:
    fig.add_trace(edge)

# Box 4
# --- Parameters  for the cube---

l_max = 220
l_min = 216
b_max = 1
b_min = -2
d_near = 4.6  # front face (near)
d_far  = 5.7  # back face (far)


# Rectangle corners (for near and far planes)
rect_l = [l_min, l_max, l_max, l_min, l_min]
rect_b = [b_min, b_min, b_max, b_max, b_min]
rect_d_near = [d_near]*len(rect_l)
rect_d_far  = [d_far]*len(rect_l)

# --- Create Plotly traces ---

# Front (near) face
rect_near = go.Scatter3d(
    x=rect_l, y=rect_b, z=rect_d_near,
    mode='lines',
    line=dict(color='lime', width=5),
    showlegend=False
)

# Back (far) face
rect_far = go.Scatter3d(
    x=rect_l, y=rect_b, z=rect_d_far,
    mode='lines',
    line=dict(color='lime', width=5),
    showlegend=False
)

# Connect corresponding corners (vertical edges)
edges = []
for i in range(4):  # 4 corners
    edge = go.Scatter3d(
        x=[rect_l[i], rect_l[i]],
        y=[rect_b[i], rect_b[i]],
        z=[d_near, d_far],
        mode='lines',
        line=dict(color='lime', width=5),
        showlegend=False
    )
    edges.append(edge)

# --- Add all to figure ---
fig.add_trace(rect_near)
fig.add_trace(rect_far)
for edge in edges:
    fig.add_trace(edge)

# Box 5
# --- Parameters  for the cube---

l_max = 220
l_min = 216
b_max = 1
b_min = -2.1
d_near = 5.7  # front face (near)
d_far  = 6.9 # back face (far)


# Rectangle corners (for near and far planes)
rect_l = [l_min, l_max, l_max, l_min, l_min]
rect_b = [b_min, b_min, b_max, b_max, b_min]
rect_d_near = [d_near]*len(rect_l)
rect_d_far  = [d_far]*len(rect_l)

# --- Create Plotly traces ---

# Front (near) face
rect_near = go.Scatter3d(
    x=rect_l, y=rect_b, z=rect_d_near,
    mode='lines',
    line=dict(color='lime', width=5),
    showlegend=False
)

# Back (far) face
rect_far = go.Scatter3d(
    x=rect_l, y=rect_b, z=rect_d_far,
    mode='lines',
    line=dict(color='lime', width=5),
    showlegend=False
)

# Connect corresponding corners (vertical edges)
edges = []
for i in range(4):  # 4 corners
    edge = go.Scatter3d(
        x=[rect_l[i], rect_l[i]],
        y=[rect_b[i], rect_b[i]],
        z=[d_near, d_far],
        mode='lines',
        line=dict(color='lime', width=5),
        showlegend=False
    )
    edges.append(edge)

# --- Add all to figure ---
fig.add_trace(rect_near)
fig.add_trace(rect_far)
for edge in edges:
    fig.add_trace(edge)

# Box 6
# --- Parameters  for the cube---

l_max = 220
l_min = 216
b_max = 0.8
b_min = -0.8
d_near = 6.9  # front face (near)
d_far  = 8.1  # back face (far)


# Rectangle corners (for near and far planes)
rect_l = [l_min, l_max, l_max, l_min, l_min]
rect_b = [b_min, b_min, b_max, b_max, b_min]
rect_d_near = [d_near]*len(rect_l)
rect_d_far  = [d_far]*len(rect_l)

# --- Create Plotly traces ---

# Front (near) face
rect_near = go.Scatter3d(
    x=rect_l, y=rect_b, z=rect_d_near,
    mode='lines',
    line=dict(color='lime', width=5),
    showlegend=False
)

# Back (far) face
rect_far = go.Scatter3d(
    x=rect_l, y=rect_b, z=rect_d_far,
    mode='lines',
    line=dict(color='lime', width=5),
    showlegend=False
)

# Connect corresponding corners (vertical edges)
edges = []
for i in range(4):  # 4 corners
    edge = go.Scatter3d(
        x=[rect_l[i], rect_l[i]],
        y=[rect_b[i], rect_b[i]],
        z=[d_near, d_far],
        mode='lines',
        line=dict(color='lime', width=5),
        showlegend=False
    )
    edges.append(edge)

# --- Add all to figure ---
fig.add_trace(rect_near)
fig.add_trace(rect_far)
for edge in edges:
    fig.add_trace(edge)

# Box 7
# --- Parameters  for the cube---

l_max = 220
l_min = 216
b_max = 0.8
b_min = -0.8
d_near = 8.1  # front face (near)
d_far  = 9.3  # back face (far)


# Rectangle corners (for near and far planes)
rect_l = [l_min, l_max, l_max, l_min, l_min]
rect_b = [b_min, b_min, b_max, b_max, b_min]
rect_d_near = [d_near]*len(rect_l)
rect_d_far  = [d_far]*len(rect_l)

# --- Create Plotly traces ---

# Front (near) face
rect_near = go.Scatter3d(
    x=rect_l, y=rect_b, z=rect_d_near,
    mode='lines',
    line=dict(color='lime', width=5),
    showlegend=False
)

# Back (far) face
rect_far = go.Scatter3d(
    x=rect_l, y=rect_b, z=rect_d_far,
    mode='lines',
    line=dict(color='lime', width=5),
    showlegend=False
)

# Connect corresponding corners (vertical edges)
edges = []
for i in range(4):  # 4 corners
    edge = go.Scatter3d(
        x=[rect_l[i], rect_l[i]],
        y=[rect_b[i], rect_b[i]],
        z=[d_near, d_far],
        mode='lines',
        line=dict(color='lime', width=5),
        showlegend=False
    )
    edges.append(edge)

# --- Add all to figure ---
fig.add_trace(rect_near)
fig.add_trace(rect_far)
for edge in edges:
    fig.add_trace(edge)

# Box 8
# --- Parameters  for the cube---

l_max = 220
l_min = 216
b_max = 0.8
b_min = -0.8
d_near = 9.3  # front face (near)
d_far  = 10.5  # back face (far)


# Rectangle corners (for near and far planes)
rect_l = [l_min, l_max, l_max, l_min, l_min]
rect_b = [b_min, b_min, b_max, b_max, b_min]
rect_d_near = [d_near]*len(rect_l)
rect_d_far  = [d_far]*len(rect_l)

# --- Create Plotly traces ---

# Front (near) face
rect_near = go.Scatter3d(
    x=rect_l, y=rect_b, z=rect_d_near,
    mode='lines',
    line=dict(color='lime', width=5),
    showlegend=False
)

# Back (far) face
rect_far = go.Scatter3d(
    x=rect_l, y=rect_b, z=rect_d_far,
    mode='lines',
    line=dict(color='lime', width=5),
    showlegend=False
)

# Connect corresponding corners (vertical edges)
edges = []
for i in range(4):  # 4 corners
    edge = go.Scatter3d(
        x=[rect_l[i], rect_l[i]],
        y=[rect_b[i], rect_b[i]],
        z=[d_near, d_far],
        mode='lines',
        line=dict(color='lime', width=5),
        showlegend=False
    )
    edges.append(edge)

# --- Add all to figure ---
fig.add_trace(rect_near)
fig.add_trace(rect_far)
for edge in edges:
    fig.add_trace(edge)

# Box 9
# --- Parameters  for the cube---

l_max = 220
l_min = 216
b_max = 0.4
b_min = -0.4
d_near = 10.5  # front face (near)
d_far  = 11.2  # back face (far)


# Rectangle corners (for near and far planes)
rect_l = [l_min, l_max, l_max, l_min, l_min]
rect_b = [b_min, b_min, b_max, b_max, b_min]
rect_d_near = [d_near]*len(rect_l)
rect_d_far  = [d_far]*len(rect_l)

# --- Create Plotly traces ---

# Front (near) face
rect_near = go.Scatter3d(
    x=rect_l, y=rect_b, z=rect_d_near,
    mode='lines',
    line=dict(color='lime', width=5),
    showlegend=False
)

# Back (far) face
rect_far = go.Scatter3d(
    x=rect_l, y=rect_b, z=rect_d_far,
    mode='lines',
    line=dict(color='lime', width=5),
    showlegend=False
)

# Connect corresponding corners (vertical edges)
edges = []
for i in range(4):  # 4 corners
    edge = go.Scatter3d(
        x=[rect_l[i], rect_l[i]],
        y=[rect_b[i], rect_b[i]],
        z=[d_near, d_far],
        mode='lines',
        line=dict(color='lime', width=5),
        showlegend=False
    )
    edges.append(edge)

# --- Add all to figure ---
fig.add_trace(rect_near)
fig.add_trace(rect_far)
for edge in edges:
    fig.add_trace(edge)

print("figure created")
fig.write_html(f'{text}.html')


