import numpy as np
#print(python.__version__)
import plotly.offline as pyo
import plotly.graph_objs as go

np.random.seed(42)
r_x = np.random.randint(1, 101, 100)
r_y = np.random.randint(1, 101, 100)

data = [go.Scatter(x=r_x, 
                    y=r_y, 
                    mode='markers',
                    marker=dict(
                        size=12,
                        color='rgb(51, 204, 153)',
                        symbol='pentagon',
                        line={'width':2}
                    ))]



layout = go.Layout(title='Scatter plot',
    xaxis={'title': 'X AXIS'}, 
    yaxis=dict(title='Y AXIS'),
    hovermode='closest')

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename = 'basic.html')
