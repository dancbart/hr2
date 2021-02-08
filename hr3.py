#Plot astronomical data from http://www.astro.keele.ac.uk/jkt/debcat/
import pandas as pd
import plotly.express as px
#converted ascii file to csv, then read it here
hr_data = pd.read_csv('/users/danielbarton/github/hr2/debs3.csv')
#Plotting Luminosity "log(L1)" vs. Temperature "log(Teff1)"
fig = px.scatter(hr_data, x= 'log(Teff1)', y= 'log(L1)',
            title = "DEBCat: well-studied eclipsing binaries",
            labels = {'log(Teff1)': "Temperature (K)", 'log(L1)': "Luminosity"},
            template="simple_white",
            )
fig.show()
