A test for a job application which required to develop a python API, using Flask to build it and selenium to develop an RPA to access a site with a catalog of notebooks, retrive their informations and return them sorted by their prices.


To install the necessary modules to run the project, execute the command pip install -r requirements.txt

To execute the route, type the commands in CMD: set FLASK_APP=routes and then flask run or in Powershell: $env:FLASK_APP = "routes" and finally flask run

After starting the server, the route to be consumed is /informacoesNotebooks, it is a GET type route, which returns a JSON containing an array with the information of the notebooks and their prices, sorted from lowest to highest price.
