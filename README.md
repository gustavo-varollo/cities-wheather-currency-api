#Cities_API

##Basic Information

API build on flask, with factory design pattern the factory method pattern creates a pattern that use factory methods 
to solve the problem of producing objects without specifying the precise class of the object to be generated. This is 
accomplished using a factory method to generate objects.

##Running the application

To rum the application perform the 3 following commands form the core directory, this will rum the flask local server
allowing accesses.

* export FLASK_APP=Metadata_Extraction_API

* export FLASK_ENV=development

* flask run

The API is deployed in Heroku the address to access is:

https://cities-wheather-currency-api.herokuapp.com/

Weather information end-point:

https://cities-wheather-currency-api.herokuapp.com/weather/<city_name>/<country_id>

Currency ratio and conversion:

https://cities-wheather-currency-api.herokuapp.com/currency/<base_currency>/<target_currency>/<amount>

##AccuWeather

AccuWeather API provides data of weather forecast for a range of countries and cities around the world. In this case
accuweather it is utilized to track and show and send json information about a specified city for 1 day.

##ExchangeRate-API
ExchangeRate-API provides methods of currency exchange for a large range of currencies around the world, In this case 
a pair of codes and an optional amount it is inputted and return the exchange rate between the codes
as well as the conversion of the optional amount if you specified it.

##Limitations
Due to the use of free licences for the development AccuWeather only allow 50 requests on daly bases and
ExchangeRate-API only allow an over all of 1500 requests.