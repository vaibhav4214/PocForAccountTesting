import pandas as pd
l=[{"Name":"vaibhav","AccNo":123456789,"Status":"not ok","Balance":"$1400"},
   {"Name":"Rahul","AccNo":65325986586,"Status":"not ok","Balance":"$5333"}
   ]
d=pd.DataFrame(l)
d.to_excel("data.xlsx",index=False)
