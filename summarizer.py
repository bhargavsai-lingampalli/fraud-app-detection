from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
import emoji
import random
import re
import ai_summary


def clean_text(text):
    return emoji.replace_emoji(text, '')


def summarize(reviews):
    return extract_fake_reviews(reviews)


def summarize_reviews(text_list):
    text = clean_text(', '.join(text_list))
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()

    summary = summarizer(parser.document, 3)  # Number of sentences in summary
    summary_text = '\n'.join([str(s) for s in summary])

    return ai_summary.make_good(summary_text.capitalize())


def extract_fake_reviews(reviews):
    keywords = ["scam", "fraud", "fake", "stole my data", "fraudulent", "malware", "phishing", "deceptive",
                "not genuine", "doesn't work", "suspicious", "waste", "cheat", "cheating"]
    fake_reviews = []
    for review in reviews:
        if any(re.search(r'\b' + keyword + r'\b', review, re.IGNORECASE) for keyword in keywords):
            fake_reviews.append(review)

    random.shuffle(fake_reviews)
    return summarize_reviews(fake_reviews)
