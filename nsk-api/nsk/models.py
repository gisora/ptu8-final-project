# NSK-API funkcijos skirtos modelių apdrorojimui

import tensorflow as tf


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