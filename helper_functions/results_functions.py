from sklearn.metrics import accuracy_score, precision_recall_fscore_support

def print_classification_results(y_true, y_pred, model_name):
    """
    Spausdina klasifikacijos įverčius accuracy, precision, recall, F1 score ir šiuos rezultatus grąžina python žodyno pavidalu

    Args:
        y_true: teisingos reikšmės
        y_pred: modelio spėtos reikšmės
        model_name: modelio pavadinimas
    """

    accuracy = accuracy_score(y_true=y_true, y_pred=y_pred)
    # accuracy = tf.keras.metrics.Accuracy()
    # accuracy.update_state(y_true, y_pred)
    # accuracy_result = float(accuracy.result().numpy())
    
    precision, recall, f1score, _ = precision_recall_fscore_support(y_true, y_pred, average="weighted")

    print(f"Modelio {model_name} klasifikacijos rezultatai:")
    print(f"\tAccuracy: {(accuracy*100):.2f}%")
    print(f"\tPrecision: {(precision*100):.2f}%")
    print(f"\tRecall: {(recall*100):.2f}%")
    print(f"\tF1 score: {(f1score*100):.2f}%")

    results = {
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall,
        "f1score": f1score,
    }
    
    return results    