from preswald import connect, get_df

connect()  # Initialize connection to preswald.toml data sources
df = get_df("my_dataset")  # Load data

from preswald import query

sql = "SELECT * FROM my_dataset"
filtered_df = query(sql, "my_dataset")

from preswald import table, text

text("# My Data Analysis App")
table(filtered_df, title="Filtered Data")

from preswald import plotly
import plotly.express as px

fig = px.scatter(df, x="Age", y="BMI", color="Gender")
plotly(fig)