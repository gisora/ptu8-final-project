# NSK-API funkcijos skirtos modelių apdrorojimui

import tensorflow as tf
from .data import format_input_data, format_output_data


# TensorFlow modelių saugojimo aplankas
MODELS_PATH = "models/"


def get_model(model_name="nsk_model_v1"):
    """
    Grąžina išsaugotą TensorFlow modelį

    Args:
        model_name: modelio pavadinimas, pagal nutylėjima "nsk_model_v1"
    """
    # iškviečiam išsaugota TensorFlow išsaugota modelį
    model = tf.keras.models.load_model(MODELS_PATH + model_name)

    return model


def get_result(abstract: str, model, group=False):
    """
    Grąžina suklasifikuotų santraukos sakinių python žodynų sąrašą

    Args:
        abstract: santraukos tekstas
        model: TesorFlow modelis
        group:
            False - grąžina etiketę prie kiekvieno sakinio
            True - grąžina sakinius sugrupuotus pagal etiketes
    """
    # formuojam įvedimo duomenys
    inputs = format_input_data(abstract)
    
    # gaunam kiekvieno sakinio klasifikavimo tikimybes 
    pred_probs = model.predict(x=inputs)

    # formuojam rezultatus
    outputs = format_output_data(abstract, pred_probs, group)

    return outputs