from flask import Flask, request

from config import PATH_TO_CSV
import features

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():
    return "<p>Players Flask API</p>"


@app.route('/players', methods=['GET'])
def get_players():
    born_after = request.args.get('born-after', None)
    country = request.args.get('country', None)
    print(born_after, country)
    df = features.get_df_from_csv(PATH_TO_CSV)  # load csv to dataframe
    total_records, *t = df.shape  # fetch number of records
    res = {}
    if born_after:
        res_df = features.players_born_after(df, year=born_after)  # fetch players df born after the specified year
        percentage = features.percentage(res_df.shape[0], total_records)  # calculate the percentage of players born
        # after the year
        res.update({'%players': percentage})  # add percentage of players to response
    elif country:
        if country.lower() == 'none':
            res_df = features.players_without_country(df)  # fetch players df having no country
        else:
            res_df = features.players_in_country(df, country)  # fetch players df for the specified country
        res.update({'country': country})
    else:
        res_df = df
    players = res_df.to_dict('records')
    res.update({'players': players})
    return res


@app.route('/players/average-age', methods=['GET'])
def average_age():
    df = features.get_df_from_csv(PATH_TO_CSV)
    avg_age = features.avg_player_age(df)
    return {'average-age': avg_age}


@app.route('/country/max-lefties', methods=['GET'])
def max_lefties():
    df = features.get_df_from_csv(PATH_TO_CSV)
    res = features.country_with_max_lefties(df)
    return res


if __name__ == "__main__":
    app.run()
