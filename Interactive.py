#John Paul Lee
#Analysis of Iris Data Set

#Creation of Interactive Report of the Iris Data Set

#Import Pandas for Data Management 
import pandas as pd

#Import Pandas Profiling to run Interactive Report
from pandas_profiling import ProfileReport

#Import the Data and 
f =pd.read_csv("IrisData.csv")

#Create a DataFrame from the Csv file to allow for easier analysis
df = pd.DataFrame(f)

profile = ProfileReport(df, title="Iris Data Interactive Report", html={'style':{'full_width':True}})

#Run the Report
df.profile_report()

#Save the Report as a HTML Document
profile.to_file(output_file="Iris Data Interactive Report.html")