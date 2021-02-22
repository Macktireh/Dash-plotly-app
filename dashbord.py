import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


import plotly.express as px


import dash
import dash_core_components as dcc
import dash_html_components as html


## Creating dataframe of total data
url = "https://raw.githubusercontent.com/pycaret/pycaret/master/datasets/insurance.csv"
data = pd.read_csv(url)
df = data.copy()

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

header1 = html.H2(children="Medical insurance Analysis")
header2 = html.H6(children="Macktireh ABDI SOUBANEH")

chart1 = px.scatter(data_frame=df,
           x="charges",
           y="age",
           color="sex",
           #size=[1]*1338,
           title="charges vs âge couleur par sexe")


graph1 = dcc.Graph(
        id='graph1',
        figure=chart1,
        className="six columns"
    )

chart2 = px.scatter(data_frame=df,
           x="charges",
           y="bmi",
           color="sex",
           #size=[1]*1338,
           title="charges vs IMC couleur par sexe")


graph2 = dcc.Graph(
        id='graph2',
        figure=chart2,
        className="six columns"
    )

chart3 = px.scatter(data_frame=df,
           x="charges",
           y="age",
           color="smoker",
           #size=[1]*1338,
           title="charges vs âge couleur par fumeur")

graph3 = dcc.Graph(
        id='graph3',
        figure=chart3,
        className="six columns"
    )



chart4 = px.histogram(data_frame=df,
             x="charges",
             color="smoker",
             title="Distributions de la charge par couleur selon le fumeur")

graph4 = dcc.Graph(
        id='graph4',
        figure=chart4,
        className="six columns"
    )


chart5 = px.histogram(data_frame=df,
             x="charges",
             color="sex",
             title="Distributions de la charge par couleur selon le sexe")

graph5 = dcc.Graph(
        id='graph5',
        figure=chart5,
        className="six columns"
    )



chart6 = px.box(data_frame=df,
           x="region",
           y="charges",
           color="smoker",
           title="Boxplot région vs charges par couleur selon le fumeur")

graph6 = dcc.Graph(
        id='graph6',
        figure=chart6,
        className="six columns"
    )



chart7 = px.box(data_frame=df,
           x="region",
           y="charges",
           color="sex",
           title="Boxplot région vs charges par couleur selon le sexe")

graph7 = dcc.Graph(
        id='graph7',
        figure=chart7,
        className="six columns"
    )




# chart8 = sns.pairplot(df)

# graph8 = dcc.Graph(
#         id='graph8',
#         figure=chart8,
#         className="six columns"
#     )



# chart9 = sns.heatmap(df.corr(), annot=True, cmap='Greens')

# graph9 = dcc.Graph(
#         id='graph9',
#         figure=chart9,
#         className="six columns"
#     )


row1 = html.Div(children=[graph1, graph2, graph3, graph4],)

row2 = html.Div(children=[graph5, graph6, graph7])

# row3 = html.Div(children=[graph3, graph6, graph9])

layout = html.Div(children=[header1, header2, row1, row2], style={"text-align": "center"})

app.layout = layout

if __name__ == "__main__":
    app.run_server(debug=True)