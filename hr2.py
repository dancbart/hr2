# desired columns: V    log(Teff1)

import pandas as pd
#import matplotlib.pyplot as plt
import plotly.express as px
hr_data = pd.read_csv('/users/danielbarton/github/hr2/debs.dat')
fig = px.scatter(hr_data, x= 'V', y= 'log(Teff1)')
fig.show()
