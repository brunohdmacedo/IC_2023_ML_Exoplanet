# -*- coding: utf-8 -*-
"""SKTIME - Global SIEPE 2023.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BGtOhBVWWMfnBEADMEuOxy7Ptfd8w_gC
"""

!pip install scikit-optimize
!pip install lightkurve
!pip install sklearn
!pip install numpy
!pip install pandas
!pip install xlsxwriter
!pip install sktime[all_extras]

import pandas as pd
from numpy import mean
from numpy import std
from sklearn.datasets import make_classification
from sklearn.model_selection import KFold
from sklearn.model_selection import RepeatedKFold
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import RandomizedSearchCV
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier, ExtraTreesClassifier
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis, LinearDiscriminantAnalysis
from sklearn.metrics import *
from threading import Thread
from skopt import BayesSearchCV
from skopt.space import Real, Categorical, Integer
from sklearn.base import BaseEstimator, ClassifierMixin

from sklearn.preprocessing import LabelBinarizer
from sktime.classification.kernel_based import RocketClassifier
from sktime.classification.interval_based import TimeSeriesForestClassifier
from sktime.classification.dictionary_based import WEASEL

#conectar com o drive pelo colab
from google.colab import drive
drive.mount('/content/drive')

#Nome do arquivo dataset em csv
book_name = 'global'

# Dataset google drive by colab
data_path = '/content/drive/MyDrive/Iniciacao_Cientifica/IC_22-23/SIEPE_2023/dataset/shallue_all_' + book_name +'.csv'

# Dataset local
#data_path = 'dataset/shallue_all_' + book_name +'.csv'
data = pd.read_csv(data_path, sep = ",")

#definição input e label no formato tabular exigido pelo scikit-learn
data_input = data.copy()
label = data_input.pop(data_input.columns[len(data_input.columns)-1])

X = data_input.values
y = label.values[100:500]

#normalização
norm_data = data_input.copy()
norm_data = norm_data.apply(lambda x: (x-x.min())/(x.max()-x.min()), axis=1)
X_norm = norm_data.values[100:500] #tamanho limitado para testes rápidos

#label binário
lb = LabelBinarizer()
y = lb.fit_transform(label)
y = y.reshape(-1)[100:500]  #tamanho limitado para testes rápidos

def experiment(model_name, model, params, X_train, y_train, X_test, y_test, i, results):

  # configure the cross-validation procedure
  cv_inner = StratifiedKFold(n_splits=3, shuffle=True, random_state=1)

  # define search
  search = BayesSearchCV(model, params, scoring='accuracy', cv=cv_inner, n_iter=10, refit=True, random_state=1, n_jobs=3)

  # execute search
  result = search.fit(X_train, y_train)

  # get the best performing model fit on the whole training set
  best_model = result.best_estimator_

  # evaluate model on the hold out dataset
  yhat = best_model.predict(X_test)

  # evaluate the model
  acc = accuracy_score(y_test, yhat)
  prec = precision_score(y_test, yhat)
  rec = recall_score(y_test, yhat)
  f1 = f1_score(y_test, yhat)
  mcc = matthews_corrcoef(y_test, yhat)

  # store the result
  results.append([model_name, i, acc, rec, prec, f1, mcc, result.best_score_, result.best_params_])

  # report progress
  print(f"{model_name} {i} > acc={acc:.2f}, est={result.best_score_:.2f}, cfg={result.best_params_}")

# definição dos modelos e parametros
model_params = {
    'ROCKET': {
        'model': RocketClassifier(),
        'params': {
        'num_kernels': Integer(1000, 20000)
    }},
    #'WEASEL': {
    #    'model': WEASEL(),
    #    'params': {
    #    'binning_strategy': Categorical(['equi-depth', 'equi-width', 'information-gain']),
    #    'window_inc': Integer(1, 10),
    #    'alphabet_size': Integer(2, 10),
    #    'feature_selection': Categorical(['chi2', 'none', 'random'])
    #}},
    'ComposableTSF': {
        'model': TimeSeriesForestClassifier(),
        'params': {
        'n_estimators': Integer(50, 300),
        'min_interval': Integer(2, 10)
    }}
}

# Save google drive by colab
results_file = "/content/drive/MyDrive/Iniciacao_Cientifica/IC_22-23/SIEPE_2023/resultados/global/resultado_SIEPE-2023.xlsx"

# Save local
#results_file = "resultado_SIEPE-2023.xlsx"

# enumerate splits
results = []

# configure the cross-validation procedure
cv_outer = RepeatedStratifiedKFold(n_splits=2, n_repeats=5, random_state=1)

#for train_ix, test_ix in cv_outer.split(X,y):
for i, (train_ix, test_ix) in enumerate(cv_outer.split(X_norm, y)):

  # split data
  X_train, X_test = X_norm[train_ix, :], X_norm[test_ix, :]
  y_train, y_test = y[train_ix], y[test_ix]

  #---------Usado com paralelismo:
  threads = []

  for model_name, mp in model_params.items():

    #Sem paralelismo:
    #experiment(model_name, model_params.get(model_name).get('model'), model_params.get(model_name).get('params'), X_train, y_train, X_test, y_test, i, results)

    #---------Usado com paralelismo:
    exp = Thread(target=experiment,args=[model_name, mp['model'],mp['params'], X_train, y_train, X_test, y_test, i, results])
    exp.start() #inicia thread
    threads.append(exp) #adiciona na lista para salvar a referencia da thread

  #---------Usado com paralelismo:
  for i in range (len(threads)):
    threads[i].join() #retoma o resultado para o programa chamador

# save results to file
df = pd.DataFrame(results, columns=['model', 'run', 'acc', 'rec', 'prec', 'f1', 'mcc', 'best_score', 'best_params'])
df.to_excel(results_file, index=False)
