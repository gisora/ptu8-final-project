# **NSK** - PTU8 Baigiamasis darbas
### **N**uoseklių **S**akinių **K**lasifikavimas atsitiktinių imčių medicininių tyrimų santraukose
### Sequential sentence classification in medical abstracts of randomized controlled trials
---
**Repozitorijos turinys**:
- *NSK_experiments.ipynb* - ekperimentai su modeliais
- *NSK_model.ipynb* - geriausias eksperimentų modelis ir jo apmokymas
- *nsk-api* - santraukų klasifikavimo api
---
**Įdėja:**
- Modelio pavyzdis - [Neural Networks for Joint Sentence Classification in Medical Paper Abstracts](https://arxiv.org/pdf/1612.05251)
- Duomenų rinkinio aprašas - [PubMed 200k RCT: a Dataset for Sequential Sentence Classification in Medical Abstracts](https://arxiv.org/pdf/1710.06071.pdf)
- Duomenų rinkinys - [PubMed 200k RCT](https://github.com/Franck-Dernoncourt/pubmed-rct)

**Tikslas:** sukurti **NLP** (*Natural Language Processing*) modelį, kuris klasifikuotu medicininių tyrimų santraukų tekstą į penkių etikečių grupes: **background**, **objective**, **methods**, **results**, **conclusions**.

**Metodas:** sukurti, apmokyti ir palyginti mašininio bei gilaus mokymo modelius:

| Nr. | Pavadinimas | Tipas |
|:---:|:-------------:|-------|
|0|Bazinis modelis|TF-IDF Multinomial Naive Bayes classifier|
|1|Modelis 1|Conv1D with token embedding|
|2|Modelis 2|Feature extraction with pretrained token embeddings|
|3|Modelis 3|Conv1D with characters embedding|
|4|Modelis 4|Combining pretrained token embeddings with characters embeddings|
|5|Modelis 5|Transfer learning of pretrained token embeddings with character and position embeddings|

**Rezultatas:**
- geriausias modelis apmokytas su visais pasirinkto duomenų rinkinio pavyzdžiais;
- sukurta sakinių klasifikavimo API (https://nsk-api-2plmfoaoua-lz.a.run.app/)

---
**Naudotos priemonės:** [Python](https://www.python.org/), [Miniconda](https://docs.conda.io/en/latest/miniconda.html), [NumPy](https://numpy.org/), [pandas](https://pandas.pydata.org/), [matplotlib](https://matplotlib.org/), [Jupyter Notebook](https://jupyter.org/), [Scikit-Learn](https://scikit-learn.org/stable/), [TensorFlow](https://www.tensorflow.org/), [NVIDIA CUDA Toolkit](https://developer.nvidia.com/cuda-toolkit), [NLTK](https://www.nltk.org/), [FastAPI](https://fastapi.tiangolo.com/), [Docker](https://www.docker.com/), Google Cloud [Container Registry](https://cloud.google.com/container-registry) ir [Cloud Run](https://cloud.google.com/run)

---
**Paleidimo instrukcijos:**
- *environment.yml* - conda aplinka darbui su notebooks, naudojant [TensorFlow su NVIDIA CUDA](https://www.tensorflow.org/install/pip#step-by-step_instructions)
```
conda env create -f environment.yml
conda activate tf-py38 
```
- *requirements.txt* - python venv aplinka darbui su FastAPI
```
python -m venv venv
pip install --upgrade pip
pip install -r requirements.txt
source ./venv/bin/activate
cd nsk-api
uvicorn main:app --reload
```
- *Dockerfile* - API docker konteinerio failas
```
docker build -t nsk-api .
docker run -d --name nsk_container -p 80:80 nsk-api
```
