# desired columns: V    log(Teff1)

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
hr_data = pd.read_csv('/users/danielbarton/github/hr2/debs3.csv')
fig = px.scatter(hr_data, x= 'log(Teff1)', y= 'log(L1)',
            title = "DEBCat: well-studied eclipsing binaries",
            labels = {'log(Teff1)': "Temperature (K)", 'log(L1)': "Luminosity"},
            template="simple_white",
            )

fig.show()
