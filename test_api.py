import json

import pytest

from config import BASE_URL, PATH_TO_CSV
from features import get_df_from_csv
from urllib import request


# GET /players
def test_api_players():
    response = request.urlopen(f'{BASE_URL}/players')
    res_dict = json.loads(response.read().decode('utf-8'))
    print(res_dict)
    df = get_df_from_csv(PATH_TO_CSV)
    assert len(res_dict['players']) == df.shape[0]


# GET /players?born-after
@pytest.mark.parametrize('year', [1991, 2000])
def test_api_born_after(year):
    response = request.urlopen(f'{BASE_URL}/players?born-after={year}')
    res_dict = json.loads(response.read().decode('utf-8'))
    print(res_dict)
    assert '%players' in res_dict
    any_born_before = False
    for player in res_dict['players']:
        if player['Year_of_Birth'] < year:
            any_born_before = True
            break
    assert not any_born_before


# GET /players?country=value
@pytest.mark.parametrize('country', ['India', 'Nigeria'])
def test_api_players_in_country(country):
    response = request.urlopen(f'{BASE_URL}/players?country={country}')
    res_dict = json.loads(response.read().decode('utf-8'))
    print(res_dict)
    assert res_dict['country'] == country
    has_diff_country = False
    has_country = True
    for player in res_dict['players']:
        if not isinstance(player['Country'], str):
            has_country = False
            break
        if player['Country'] != country:
            has_diff_country = True
            break
    assert has_country and not has_diff_country


# GET /players?country=none
@pytest.mark.parametrize('country', ['none', 'None', 'NONE'])
def test_api_players_in_country(country):
    response = request.urlopen(f'{BASE_URL}/players?country={country}')
    res_dict = json.loads(response.read().decode('utf-8'))
    print(res_dict)
    has_country = False
    for player in res_dict['players']:
        if isinstance(player['Country'], str):
            has_country = True
            break
    assert not has_country


# GET /players/average-age
def test_api_average_age():
    response = request.urlopen(f'{BASE_URL}/players/average-age')
    res_dict = json.loads(response.read().decode('utf-8'))
    print(res_dict)
    assert 'average-age' in res_dict


# GET /country/max-lefties
def test_api_max_lefties_country():
    response = request.urlopen(f'{BASE_URL}/country/max-lefties')
    res_dict = json.loads(response.read().decode('utf-8'))
    print(res_dict)
    assert 'country' in res_dict and 'count' in res_dict
