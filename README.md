# Automating the ETL process with Github Actions   
In order to create a model, we first need to get data. Besides, as we want to create an MLOps pipeline, we will need to create an ETL process that extracts the data, transforms it, and loads it somewhere, like a data lake, data warehouse, or database. By doing so, we will be able to retrain the model with fresh new data anytime and put it into production.          


In our example we will be using a [Weather api](https://weather.talkpython.fm/api/weather?city=Berlin&country=DE), that show the hourly weather and forecast.       


Our ETL pipline consists of the following:            


* **Extraction**: read the information from the API.
* **Transform**: Get the hourly weather data.
*  **Load**:  upload the information to a database to store all the historical information.
