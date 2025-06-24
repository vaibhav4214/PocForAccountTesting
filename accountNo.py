import pandas as pd
import webbrowser

d=pd.read_excel("AccNumber.xlsx")
print(d)
getaccno=eval(input("Enter Index  For Account Number"))
accNo=d["Account Number"][getaccno]

url="http://localhost:3000/"
webbrowser.open(url+str(accNo))
 