Steps to run the flask application:

1. Install the dependency packages to your virtual environment using requirements.txt. To do so run `pip install requirements.txt` after activating your virtual environment.
2. Create a folder named `data` and place the `Players.csv` file in it.
3. Run the flask application by executing `app.py` or by running the command `flask run`. It runs on `http://localhost:5000`.

API endpoints:

1. `players`\
   Query args: `born-after` (optional), `country` (optional)\
   Request patterns:
   1. `http://localhost:5000/players?born-after=1981`\
      Response:
   ```
   {
      "%players": 64.31095406360424,
      "players": [
         {
            "Batting_Hand": "Right_Hand",
            "Bowling_Skill": "Right-arm medium",
            "Country": "India",
            "DOB": "24-Feb-91",
            "Player_Name": "A Ashish Reddy",
            "Year_of_Birth": 1991
         }, ...
      ]
   }
   ```
   2. `http://localhost:5000/players?country=India`\
      Response:
   ```
   {
      "country": "India",
      "players": [
         {
            "Batting_Hand": "Right_Hand",
            "Bowling_Skill": "Right-arm medium",
            "Country": "India",
            "DOB": "24-Feb-91",
            "Player_Name": "A Ashish Reddy",
         }, ...
      ]
   }
   ```
   3. `http://localhost:5000/players?country=none`\
      Response:
   ```
   {
      "country": "none",
      "players": [
         {
            "Batting_Hand": "Right_hand",
            "Bowling_Skill": "Left-arm fast-medium",
            "Country":NaN,
            "DOB":NaN,
            "Player_Name": "A Choudhary"
         }, ...
      ]
   }
   ```
   4. `http://localhost:5000/players`\
      Response:
   ```
   {
      "players": [
         {
            "Batting_Hand": "Right_Hand",
            "Bowling_Skill": "Right-arm medium",
            "Country": "India",
            "DOB": "24-Feb-91",
            "Player_Name": "A Ashish Reddy"
         }, ...
      ]
   }
   ```
2. `players/average-age`\
   Request patterns:
   1. `http://localhost:5000/players/average-age`\
      Response:
   ```
   {
      "average-age": 36
   }
   ```
   2. `http://localhost:5000/players/average-age?country=Australia`\
      Response:
   ```
   {
      "average-age": 39,
      "country": "Australia"
   }
   ```
3. `country/max-lefties`\
    Request patterns:
   1. `http://localhost:5000/country/max-lefties`\
      Response:
   ```
   {
      "count": "58",
      "country": [
         "India"
      ]
   }
   ```

Pytest files:

```
test_features.py
test_api.py
```

**Note:** Run `test_api.py` test file only while running the flask app.
