from preswald import text, plotly, connect, get_df, table, query
import pandas as pd
import plotly.express as px

text("New York Air Quality 🎉")

# Load the CSV
connect()
df = get_df('AirQuality_csv')

sql = 'SELECT Start_Date, CAST("Data Value" AS INTEGER) AS "Data Value","Geo Place Name"  ' \
'FROM AirQuality_csv ' \
'WHERE CAST("Data Value" AS INT) > 100 ' \
'ORDER BY Start_Date ASC'

try:
    filtered_df = query(sql, "AirQuality_csv")
except ValueError as e:
    print(f"Configuration error: {e}")
except Exception as e:
    print(f"Query error: {e}")

# Create a scatter plot
fig = px.line(
        filtered_df,
        x="Start_Date",
        title="NO2 Levels by Neighborhood",
        labels={
            "Data Value": "Nitrogen Dioxide (NO2) Level (ppb)", 
            "Start_Date": "Start Date", 
            "Geo Place Name": "Neighborhood"
            },
        y='Data Value',
        color="Geo Place Name",
        markers=True
    )

# Show the plot
plotly(fig)

# Show the data
table(filtered_df, title="ppb Above 100")