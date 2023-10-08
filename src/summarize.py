import nltk
from summarizer import Summarizer

def summarize_text(input_text):
    bert_model = Summarizer()

    summary = bert_model(input_text, ratio=0.5)

    bullets = []

    for bullet in summary.split('. '):
        bullets.append(bullet + '.')

    return bullets