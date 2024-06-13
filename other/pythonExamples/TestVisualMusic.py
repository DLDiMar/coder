try:
    from importlib.metadata import entry_points
except ImportError:
    from importlib_metadata import entry_points
    
import pygal

# Input data, replace this with your actual data
frequency_values = {
    1: 10,
    2: 20,
    3: 15,
    4: 30,
    5: 25,
    6: 20,
    7: 10,
    8: 5,
    9: 15,
    10: 20
}

# Get the frequencies and decibel values
frequencies = list(frequency_values.keys())
decibels = list(frequency_values.values())

# Create a new radar chart
radar_chart = pygal.Radar(fill=True)

# Add the frequencies and decibel values to the chart
radar_chart.add('Decibels', decibels)
radar_chart.x_labels = frequencies

# Render the chart to an SVG file
radar_chart.render_to_file('decibels.svg')