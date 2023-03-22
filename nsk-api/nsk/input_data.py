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


def format_input_data(abstract: str):
    """
    Grąžina TensorFlow modeliui paruoštą santraukos tekstą

    Args:
        abstract: santraukos tekstas
    """
    # sudarom santraukos sakinių sąrašą
    sentences = get_sentences(abstract)
    
    # išskaidom kiekvieno sakinio simbolius
    sentence_chars = [expand_sentence_chars(sentence) for sentence in sentences]

    # sudarom sakinių eilės numerių sąrašą
    line_numbers = [line_number for line_number in range(len(sentences))]
    # koduojam sakinių eilės numerius su tf.one_hot
    line_numebers_onehot = tf.one_hot(line_numbers, depth=line_numbers_depth)

    # sudarom santraukos sakinių skaičiaus sąrašą (kiekvienam sakiniui tas pats)
    sentences_total = [len(sentences) for _ in range(len(sentences))]
    # koduojam santraukos sakinių skaičių su tf.one_hot
    sentences_total_onehot = tf.one_hot(sentences_total, depth=sentences_total_depth)

    # paruošiam įvedimą tensorflow modeliui
    formated_input_data = (line_numebers_onehot, sentences_total_onehot, tf.constant(sentences), tf.constant(sentence_chars))

    return formated_input_data


def get_classname(classname_idx: int):
    """
    Grąžina sakinio etiketės pavadinimą

    Args:
        classname_idx: etiketes indeksas etikėčių sąraše
    """
    # etikečių pavadinimų sąrašas buvo sudarytas modelio kūrimo metu su scikit-learn LabelEncoder
    classnames = ["BACKGROUND", "CONCLUSIONS", "METHODS", "OBJECTIVE", "RESULTS"]
    
    return classnames[classname_idx]


def format_output_data(abstract: str, pred_probabilities):
    """
    Grąžina python žodynų su santraukos sakiniu ir modelio priskirta etikete sąrašą

    Args:
        abstarct: santraukos tekstas
        pred_probabilities: modelio sakinio etiketės spejimų tikimybės kiekvienam santraukos sakiniui
    """
    # sudarom santraukos sakinių sąrašą
    sentences = get_sentences(abstract)
    
    # randam didžiausios tikimybės indeksą
    predictions = tf.argmax(pred_probabilities)

    # formuojam tuščią python sąrašą
    formated_output_data = []
    
    # užpildom rezultato sąrašą
    for i, sentence in enumerate(sentences):
        formated_output_data += {
            "class": get_classname(predictions[i]),
            "text": sentence,
        }

    return formated_output_data


