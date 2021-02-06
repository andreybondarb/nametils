# Nametils
Bag-of-words classificator of russian personal names.

To install:

`pip install -e git+https://github.com/andreybondarb/Nametils.git#egg=Nametils`

Usage:

`from nametils import name_classifier`

`model = name_classifier()`

`model.predict_names('Антон Юрьевич Иванов')`

Output:

`{'Фамилия': 'Иванов', 'Имя': 'Антон', 'Отчество': 'Юрьевич'}`

Requirements:

pytils==0.3
