import requests

url = 'http://127.0.0.1:5000/iris'


labels ={
  0: "setosa",
  1: "versicolor",
  2: "virginica"
}
feature_setosa = [[5.8, 4.0, 1.2, 0.2]]
r_setosa = requests.post(url,json={'feature': feature_setosa})
print("The result is",labels[r_setosa.json()])

feature_virginica = [[6.9, 3.1, 5.1, 2.3]]
r_virginica = requests.post(url, json={'feature': feature_virginica})
print("The result is",labels[r_virginica.json()])
