import requests
from flask import Flask
import json


app = Flask(__name__)

@app.route('/<country_name>')
def countrey(country_name):
    
    
    url1 = "https://restcountries.eu/rest/v2/name/" +country_name+"?fullText=true"
    response = requests.get(url1)
    if response.status_code != 200:
        return ""+country_name +" not found in countrey list!"
    info= ''
    dic = (response.json())
    info+= "<b>Country’s Full Name:" +dic[0]['name']+ '<br/>'
   # print("Country’s Full Name:", dic[0]['name'])

    info +="Country’s Capital :"+ dic[0]['capital']+'<br/>'
    info +="Country’s Common Language:" + dic[0]["languages"][0]["name"] + '<br/>'

   # print("Country’s Common Language:", dic[0]['languages'][0]['name'])
    info+="Country’s Currency Name:"+ dic[0]["currencies"][0]["name"]+ '<br/>'
   
   # print("Country’s Currency Name:", dic[0]['currencies'][0]['name'])

    curcode = dic[0]['currencies'][0]["code"]

    url2 = "http://data.fixer.io/api/latest?access_key=0f74f9e3e64cb0c2ce6ec5230dc7592d&format=1&symbols=" + curcode 
    response1 = requests.get(url2)
    dic2 = (response1.json())
    info+="Country’s Currency rate (Base currency is EURO)  :"+str(dic2['rates'][curcode])+'<br/>'

    #print("Country’s Currency rate (Base currency is EURO)  :", dic2['rates'][curcode])

    return (info)

    if __name__ == "__main__":
        app.run(host='0.0.0.0' , debug=True)
    

   

