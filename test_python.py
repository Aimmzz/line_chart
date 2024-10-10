from bokeh.plotting import figure, show
from bokeh.io import output_file
from bokeh.models import ColumnDataSource
import pandas as pd

with open('soal_chart_bokeh.txt', 'r') as file:
    lines = file.readlines()

timestamps = []
speed_sender = []

for line in lines:
    if "Timestamp" in line:
        current_timestamp = line.split(": ")[1].strip()
    elif "sec" in line and "Mbits/sec" in line:
        parts = line.split()
        if len(parts) >= 5:
            speed = float(parts[4])
            timestamps.append(current_timestamp)
            speed_sender.append(speed)

df = pd.DataFrame({
    'timestamp': pd.to_datetime(timestamps),
    'speed_sender': speed_sender
})

source = ColumnDataSource(df)

output_file("line_chart.html")

p = figure(title="Grafik Kecepatan Pengiriman Data (Sender)",
           x_axis_label='Waktu',
           y_axis_label='Speed (Mbits/sec)',
           x_axis_type='datetime')

p.line('timestamp', 'speed_sender', source=source, legend_label="Speed Sender", line_width=2)

show(p)