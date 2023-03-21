import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay


def plot_confusion_matrix(y_true, y_pred, display_labels):
    """
    Grąžina Confusion matricos diagramą

    Args:
        y_true: teisingos reikšmės
        y_pred: modelio spėtos reikšmės
        display_labels: klasių pavadinimai
    """   

    cm = confusion_matrix(y_true, y_pred)
    cm_plot = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=display_labels)
    cm_plot.plot(xticks_rotation="vertical", cmap="Blues", colorbar=False);


def plot_confusion_matrix_comparison(y_true, model_0_y_pred, model_y_pred, display_labels, model_0_name, model_name):
    """
    Grąžina dviejų modelių Confusion matricas palyginimui

    Args:
        y_true: teisingos reikšmės
        model_0_y_pred: modelio, su kuriuo lyginam, spėtos reikšmės
        model_y_pred: modelio, kurio rezultatą lyginam, spėtos reikšmės
        display_labels: klasių pavadinimai
        model_0_name: modelio, su kurio lyginam, pavadinimas
        model_name: modelio, kuri lyginam, pavadinimas
    """
    model_0_cm = confusion_matrix(y_true, model_0_y_pred)
    model_cm = confusion_matrix(y_true, model_y_pred)

    fig, ax = plt.subplots(1, 2, figsize=(15, 5))

    fig.suptitle("Spėjimų (confusion) matricų palyginimas")
    ax[0].set_title(model_0_name)
    ax[1].set_title(model_name)

    ConfusionMatrixDisplay(confusion_matrix=model_0_cm, display_labels=display_labels).plot(ax=ax[0], xticks_rotation="vertical", cmap="BuPu", colorbar=False)
    ConfusionMatrixDisplay(confusion_matrix=model_cm, display_labels=display_labels).plot(ax=ax[1], xticks_rotation="vertical", cmap="RdPu", colorbar=False)


def plot_accuracy_loss_curves(history, model_name):
    """
    Grąžina mokymo ir įvertinimo praradimo (loss) ir tikslumo kreivių palyginimą

    Args:
        history: TensorFlow modelio History objektas, gaunamas mokinant modelį
        model_name: modelio pavadinimas
    """

    train_loss = history.history['loss']
    val_loss = history.history['val_loss']

    train_accuracy = history.history['accuracy']
    val_accuracy = history.history['val_accuracy']

    epochs = range(1, len(history.history['loss'])+1)

    fig, ax = plt.subplots(1, 2, figsize=(15, 5))
    fig.suptitle(f"Modelio {model_name} mokymosi ir įvertinimo rezultatai")

    # tikslumo (accuracy) palyginimas
    ax[0].plot(epochs, train_accuracy)
    ax[0].plot(epochs, val_accuracy)
    ax[0].legend(['mokymasis', 'įvertinimas'], loc='upper left')
    ax[0].set_title("Tikslumų (accuracy) palyginimas")
    ax[0].set_xlabel("Epochos")
    ax[0].set_ylabel("Tikslumas")
    
    # praradimų (loss) palyginimas
    ax[1].plot(epochs, train_loss, label='training_loss')
    ax[1].plot(epochs, val_loss, label='val_loss')
    ax[1].legend(['mokymasis', 'įvertinima'], loc='upper right')
    ax[1].set_title("Praradimų (loss) palyginimas")
    ax[1].set_xlabel("Epochos")
    ax[1].set_ylabel("Praradimas")

    plt.show()


def plot_hist_comparison(data, hist_2_range=None, suptitle="Duomenų pasiskirstymas"):
    """
    Grąžina duomenų histogramą ir jų dalies jistogramą nurodytame rėžyje

    Args:
        data: duomenys, kurių histograma bus sudaryta
        hist_2_range: rėžys [nuo, iki], kuriame vaizduoti antrą diagramą
        suptitle: diagramos pavadinimas
    """
    
    # atvaizduojam sakinių ilgių pasiskirstymą su histograma
    fig, ax = plt.subplots(1, 2, figsize=(15, 5))
    fig.suptitle(f"{suptitle}")

    ax[0].hist(data, bins=15)
    ax[1].hist(data, bins=15, range=hist_2_range, facecolor='green', align='mid')

    plt.show()