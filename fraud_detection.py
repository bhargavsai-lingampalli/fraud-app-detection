from google_play_scraper import reviews, app
from summarizer import summarize
import sqlite3
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer


def predict(app_id, n=1000):
    app_id = app_id[46:].split('&pcampaignid=')[0]

    con = sqlite3.connect('database/apps.db')
    cur = con.cursor()

    try:
        nltk.data.find('tokenizers/punkt')
        nltk.data.find('sentiment/vader_lexicon.zip')
    except LookupError:
        nltk.download('punkt')
        nltk.download('vader_lexicon')
    finally:
        cur.execute("create table if not exists app(appid, fraudulent, review);")

    app_data = cur.execute(f'select * from app where appid = "{app_id}";').fetchall()
    if app_data:
        return [app_data[0][1], app_data[0][2]]

    user_reviews = reviews(
        app_id,
        count=n,
        country='us',
        lang='en'
    )

    if len(user_reviews[0]) != n:
        about_app = app(app_id)
        details = ["title", "containsAds", "developer", "developerEmail", "developerWebsite", "free", "genre",
                   "inAppProductPrice", "realInstalls", "released", "score"]
        res = ""
        for cat in details:
            res += f'{cat.title()}: {about_app[cat]}'

        cur.execute("INSERT INTO app VALUES(?, 'Recently Created Application', ?)", (app_id, res))
        con.commit()
        con.close()
        return ["Recently Created Application", res]

    score = 0
    content = []
    sia = SentimentIntensityAnalyzer()
    for review in user_reviews[0]:
        text = review['content']
        if text is not None:
            pol = sia.polarity_scores(text)
            score += pol['compound']

            if pol['compound'] < 0:
                content.append(text)

    if score / n >= 0:
        result = app(
            app_id=app_id,
            lang='en',  # defaults to 'en'
            country='us'  # defaults to 'us'
        )
        cur.execute("INSERT INTO app VALUES(?, 'Not Fraudulent', ?)", (app_id, result["summary"]))
        return_value = ["Not Fraudulent", result["summary"]]
    else:
        res = summarize(content)
        cur.execute("INSERT INTO app VALUES(?, 'Fraudulent', ?)", (app_id, res))
        return_value = ["Fraudulent", res]

    con.commit()
    con.close()

    return return_value


if __name__ == "__main__":
    app_id = input("Enter Link: ")
    print('\n'.join(predict(app_id)))
