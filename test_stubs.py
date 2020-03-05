import pytest
import savedTweets
import stubFunctions as s

def test_stubFunctions():
    assert s.getTweets() == savedTweets.dictionary
    #assert s.pickHandle() == "BarackObama" or "Cristiano" or "TheEllenShow" or "realDonaldTrump" or "busnowtm"