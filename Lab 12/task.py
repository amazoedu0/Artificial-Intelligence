import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

dataset = pd.read_csv('D:\STUDY\1-AI\AI LAB\Code\Lab Codes\Lab 12\iris.csv')
X = dataset.iloc[:, :4].values
y = dataset['variety'].values
dataset.head(5)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

classifier = GaussianNB()
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)
y_pred

cm = confusion_matrix(y_test, y_pred)

print("Accuracy : ", accuracy_score(y_test, y_pred))
cm

df = pd.DataFrame({'Real Values': y_test, 'Predicted Values': y_pred})
df
