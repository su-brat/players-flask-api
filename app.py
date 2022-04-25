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
        # fetch players df born after the specified year
        res_df = features.players_born_after(df, year=born_after)
        # calculate the percentage of players born
        percentage = features.percentage(res_df.shape[0], total_records)
        # after the year
        # add percentage of players to response
        res.update({'%players': percentage})
    elif country:
        if country.lower() == 'none':
            res_df = features.players_without_country(
                df)  # fetch players df having no country
        else:
            # fetch players df for the specified country
            res_df = features.players_in_country(df, country)
        res.update({'country': country})
    else:
        res_df = df
    players = res_df.to_dict('records')
    res.update({'players': players})
    return res


@app.route('/players/average-age', methods=['GET'])
def average_age():
    country = request.args.get('country', None)
    df = features.get_df_from_csv(PATH_TO_CSV)
    res = {}
    if country == 'none':
        # filter players df with no country
        df = features.players_without_country(df)
        res.update({'country': country})
    elif country:
        # filter with respect to country
        df = features.players_in_country(df, country)
        res.update({'country': country})
    # fetch average age from filtered players dataframe
    avg_age = features.avg_player_age(df)
    res.update({'average-age': avg_age})  # update res obj with average age
    return res


@app.route('/country/max-lefties', methods=['GET'])
def max_lefties():
    df = features.get_df_from_csv(PATH_TO_CSV)
    res = features.country_with_max_lefties(df)
    return res


if __name__ == "__main__":
    app.run()
