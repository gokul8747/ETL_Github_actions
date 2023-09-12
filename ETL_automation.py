import requests
import sqlalchemy as db

uri = 'sqlite:///weatherdb.sqlite'

url = "https://weather.talkpython.fm/api/weather?city=Berlin&country=DE"

response = requests.get(url)

engine = db.create_engine(uri)
connection = engine.connect()

if response.status_code == 200:
    content = response.json()
    data = content["wind"]
    data['category'] = content['weather']['category']
    result = connection.execute(f"INSERT INTO weather(speed, deg,category) VALUES('{data['speed']}', '{data['deg']}','{data['category']}');")
    result.close() 