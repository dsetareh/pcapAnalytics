import json, os
import plotly.graph_objects as go

with open('raw_time_deltas.json') as f:
    data = json.load(f)
    fig = go.Figure(data=go.Bar(y=data))
    fig.write_html('time_deltas.html', auto_open=True)
