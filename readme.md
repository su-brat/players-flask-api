Steps to run the flask application:
1. Install the dependency packages to your virtual environment using requirements.txt. To do so run ```pip install requirements.txt``` after activating your virtual environment.
2. Create a folder named ```data``` and place the ```Players.csv``` file in it.
3. Run the flask application by executing ```app.py``` or by running the command ```flask run```. It runs on ```http://localhost:5000```.

API endpoints:
1. ```players```
Query args - ```born-after``` (optional), ```country``` (optional)
Patterns: 
   1. ```http://localhost:5000/players?born-after=1981```
   2. ```http://localhost:5000/players?country=India```
   3. ```http://localhost:5000/players?country=none```
   4. ```http://localhost:5000/players```
2. ```players/average-age```
Patterns:
   1. ```http://localhost:5000/players/average-age```
3. ```country/max-lefties```
Patterns:
   1. ```http://localhost:5000/country/max-lefties```
