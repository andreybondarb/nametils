# Nametils
Bag-of-words classification of russian personal names.

Usage:

`from nametils import name_classifier`

`model = name_classifier()`

`model.predict_names('Антон Юрьевич Иванов')`

Output:

`{'Фамилия': 'Иванов', 'Имя': 'Антон', 'Отчество': 'Юрьевич'}`

Requirements:

pytils==0.3
