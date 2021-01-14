import re
from re import sub
import pytils.translit

regex = re.compile('[^а-яА-Я() ,.-]')  

def input_word(word):

    if bool(re.search('[a-zA-Z]', word)) == True:
        q = sub(r'\s+', ' ', pytils.translit.detranslify(word)).strip().lower().title()
    else:
        q = sub(r'ё', 'е', word).strip().lower().title()
        q = sub(r'\s+', ' ', q).strip().lower().title()
    fio_for_ml = regex.sub('', q).strip()
    fio_for_ml = fio_for_ml.split(' ')
    return fio_for_ml