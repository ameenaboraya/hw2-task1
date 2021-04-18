# hw2-task1
python code that receives a country , and return :
Country’s Full Name
Country’s Capital
Country’s Common Language
Country’s Currency Name
Country’s Currency rate (Base currency is EURO)


Installation:
git clone https://github.com/ameenaboraya/hw2-task1.git

docker build --tag hw2-task1 .

docker run hw2-task1

docker run --publish 5000:5000 hw2-task1



then open http://127.0.0.1:5000/country_name
and enter the country name in the url

if we enter wrong country name , you get "ountry  name is not found in country list !" , so check the country name.
