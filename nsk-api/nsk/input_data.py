# NSK-API funkcijos skirtos duomenų apdrorojimui

import tensorflow as tf
import nltk.data

# parsisiunčiam nltk 'punkt' sakinių tokenizerį
nltk.download('punkt')

# modelio kūrimo metu gauti parametrai naudojami koduojant sakinio eilės numerį ir santraukos sakinių skaičių
line_numbers_depth = 17     # didžiausias su tf.one_hot koduojamas sakinio eilės numeris
sentences_total_depth = 22  # didžiausias su tf.one_hot koduojamas visų sakinių skaičius


def get_sentences(text: str):
    """
    Grąžinamas teksto sakinių sąrašas, naudojant NLTK 'punkt' sakinių tokenizer'į

    Args:
        text: santraukos tekstas
    """
    # paruošiam sakinių tokenizerį
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

    #skaidom tekstą į sakinių sąrašą
    sentences_list = tokenizer.tokenize(text)

    return sentences_list


def expand_sentence_chars(sentence: str):
    """
    Grąžina sakinį su išskaidytais simboliais

    Args:
        sentence: sakinio tekstas
    """
    expanded_sentence = " ".join(list(sentence))
    return expanded_sentence


