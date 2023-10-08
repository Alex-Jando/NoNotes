import nltk
nltk.download('punkt')

from summarizer import Summarizer

def summarize_text(input_text):
    bert_model = Summarizer()

    summary = bert_model(input_text, ratio=0.2)

    return summary

t = '''we look at the general process of mitosis. in this video in this video we are going to add in some including the names of the key stages. you may want to watch this video first to refresh your memory of how mitosis works. you should already that mitosis is a process of cell division that produces identical copies of cells and is involved in growth salary pay and reproduction. when cells divide by mitosis the number of cells increases and hence the organism grows. different organism have different numbers of chromosomes to keep it simple we are just going to look at what happens to one pair of chromosomes during cell division. before we start just a quick reminder that a chromosome is made up of two chromatids and one from the mother volume one from the father so mitosis with our special signs and names add in to this day. I just remember it meant to which order the stages go in then just take cytokinesis into the end interface the chromosomes duplicate and become it has gone from the original 46 to 92. in prophase in the nucleus the chromosomes condensed and in the cytoplasm spindle fibers form. metaphase the nuclear membrane breaks apart the spindle fibers attached to the chromosomes and the chromosomes line up at the. anaphase the spindle fibers shortened and the centromere device so that each chromosome becomes two separate chromatids telophase the nuclear membrane forms from each set of chromosomes chromosomes spread back out in the new nucleus spindle fibers breakdown in humans each nucleus has the normal 46 chromosomes again. cytokinesis the cell can you pinches into two separate sets of chromatids into two identical daughter cells with the same number of chromosomes as the parent 46 or 23 pairs in humans so there we have how cells divide by mitosis to form play identical cells with the special it meant sciency words included.'''

if __name__ == "__main__":
    with open('res/texts/news.txt', 'r') as file:
        input_text = file.read()

    input_text=t

    summarized_text = summarize_text(input_text)

    # Print the summarized text in bullet points
    summarized_text = summarized_text.replace('. ', '.\n- ')
    summarized_text = '- ' + summarized_text
    print(summarized_text)
