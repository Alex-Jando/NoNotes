import nltk
nltk.download('punkt')

from summarizer import Summarizer

def summarize_text(input_text, num_sentences=5):
    # Initialize the BERT Extractive Summarizer
    bert_model = Summarizer()

    # Summarize the input text
    summary = bert_model(input_text, num_sentences=num_sentences)

    return summary

if __name__ == "__main__":
    with open('res/news.txt', 'r') as file:
        input_text = file.read()

    num_sentences = 5

    summarized_text = summarize_text(input_text, num_sentences=num_sentences)

    # Print the summarized text in bullet points
    summarized_text = summarized_text.replace('. ', '.\n- ')
    summarized_text = '- ' + summarized_text
    print(summarized_text)
