import json

dictionary = {
    "BarackObama":
    {
        "name": "BarackObama",
        "tweet": "What a great example of citizenship, what each of us can do to make a difference for all of us: https://t.co/YxsvONUuVl",
        "date": "2020 Feb 13"
    },
    "Cristiano":
    {
        "name": "Cristiano",
        "tweet": "👀 https://t.co/MRxEXFuthE",
        "date": "2020 Jan 11"
    },
    "TheEllenShow":
    {
        "name": "TheEllenShow",
        "tweet": "Shanell and her daughter Kinley deserve the #BestNewsEver. Good thing @Usher was here to help me deliver it. https://t.co/pVNiVsyJC4",
        "date": "2020 Mar 4"
    },
    "realDonaldTrump":
    {
        "name": "realDonaldTrump",
        "tweet": "The Mayor of Los Angeles, @ericgarcetti, is dealing with us trying to get the Federal Government to fix the terribl… https://t.co/t3asbDDxcb",
        "date": "2020 Mar 4"
    },
    "busnowtm":
    {
        "name": "busnowtm",
        "tweet": "the squad cheering on the basketball team at #rocktheroof thanks @BU_ClubSports for such an awesome night! 🏀🎉🏀🤟 https://t.co/9YvRjz80Q0",
        "date": "2018 Feb 1"
    }
}

with open("savedTweets.json", "w") as f:
    json.dump(dictionary, f)
