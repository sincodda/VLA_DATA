import sweetviz as sv
import pandas as pd


# Load your data into a Pandas DataFrame
df = pd.read_csv(f'../goldendata/files/goldens/g_c_bb.csv')
# Drop columns from the DataFrame
df = df.drop(columns=['Ciudad', 'Latitud', 'Longitud'])
# Create an analysis report for your data
report = sv.analyze(df)

# Display the report
report.show_html()