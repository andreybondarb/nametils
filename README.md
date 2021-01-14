# nametils
Bag of words classification of personal names

Usage:

`from nametils import name_classifier`
`model = name_classifier()`
`model.predict_names('Антон Юрьевич Иванов')`

Output:

`{'Фамилия': 'Иванов', 'Имя': 'Антон', 'Отчество': 'Юрьевич'}`
