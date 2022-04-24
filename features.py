import pandas as pd
import datetime


def get_df_from_csv(filepath):
    return pd.read_csv(filepath)  # read csv and return dataframe


def get_date_obj(date):
    return datetime.datetime.strptime(date, '%d-%b-%y')  # return datetime obj from date string


def year_from_date_obj(date):
    return date.year  # return year from datetime obj


def date_str_from_obj(date):
    return date.strftime('%d-%b-%y')  # return string date from datetime obj


def age_from_dob(dob):
    today = datetime.date.today()  # fetch today's date obj
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))  # calculate age
    return age


def percentage(x, y):
    return x * 100 / y


def players_born_after(df, year):
    df = df.dropna(subset=['DOB'])  # filter out players with no DOB
    df['DOB'] = df['DOB'].apply(get_date_obj)  # change date format from string '12-May-99' to datetime obj
    df['Year_of_Birth'] = df['DOB'].apply(year_from_date_obj)  # create a 'Year_of_Birth' col to store year of birth
    born_after_df = df[int(year) <= df['Year_of_Birth'].apply(int)]  # fetch players born after $year
    born_after_df['DOB'] = born_after_df['DOB'].apply(date_str_from_obj)  # change back date format from datetime obj
    # to string
    return born_after_df


def avg_player_age(df):
    df = df.dropna(subset=['DOB'])  # filter out players with no DOB
    df['DOB'] = df['DOB'].apply(get_date_obj)  # change date format from string '12-May-99' to datetime obj
    df['Age'] = df['DOB'].apply(age_from_dob)  # create age col from dob
    return int(df['Age'].mean())


def country_with_max_lefties(df):
    lefties_df = df[df['Batting_Hand'].str.lower() == 'Left_Hand'.lower()]  # filter records with left-handed batsmen
    count_df = lefties_df.groupby(['Country'], as_index=False).count()  # Group by Country and count the number of
    # left-handers
    max_lefties = count_df.max()['Batting_Hand']  # fetch the maximum number of left-handers in a country
    countries_with_max_lefties = count_df[count_df['Batting_Hand'] == max_lefties]['Country'].to_list()  # fetch the
    # countries having the maximum number of left-handers
    return {'country': countries_with_max_lefties, 'count': str(max_lefties)}


def players_without_country(df):
    no_country_df = df[df['Country'].isna()]  # fetch players with no country
    return no_country_df


def players_in_country(df, country):
    country_players_df = df[df['Country'].str.lower() == country.lower()]  # fetch players dataframe with given country
    return country_players_df
