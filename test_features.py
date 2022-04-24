import datetime

from features import *


def test_get_date_obj():
    print(type(get_date_obj('24-Apr-22')))
    assert isinstance(get_date_obj('24-Apr-22'), datetime.datetime)


def test_year_from_date_obj():
    dt = get_date_obj('24-Apr-22')
    assert year_from_date_obj(dt) == 2022


def test_date_str_from_obj():
    dt = get_date_obj('24-Apr-22')
    assert date_str_from_obj(dt) == '24-Apr-22'


def test_age_from_dob():
    dob = get_date_obj('16-May-98')
    assert age_from_dob(dob) == 23


def test_percentage():
    assert percentage(3, 4) == 75
