import pickle
from inspect import getsourcefile
from os.path import abspath
import os

path = abspath(getsourcefile(lambda:0))
path = path.replace('frequencies_count.py', '')
os.chdir(path)
    
with open('frequencies.pkl', 'rb') as fo:
    (di_f, di_i, di_o) = pickle.load(fo)

def maximum_word_count(fio_words):
    
    if len(fio_words) > 3:
        fio_words = ' '.join(fio_words)
        return [fio_words]
        
    else:
        type_matrix = []
        
        for i in fio_words:
            count_for_analysis = []
            #Check in Familiya
            try:
                occurrence_in_f = di_f[i]
            except:
                occurrence_in_f = 0
                
            count_for_analysis.append(occurrence_in_f)
            
            #Check in Imya
            try:
                occurrence_in_i = di_i[i]
            except:
                occurrence_in_i = 0
            count_for_analysis.append(occurrence_in_i)
            
            #Check in Otchestvo
            try:
                occurrence_in_o = di_o[i]
            except:
                occurrence_in_o = 0
            count_for_analysis.append(occurrence_in_o)
            
            maximum = max(count_for_analysis)
            
            if maximum == occurrence_in_f:
                type_word = 'familiya'
            if maximum == occurrence_in_i:
                type_word = 'imya'
            if maximum == occurrence_in_o:
                type_word = 'otchestvo'
            if maximum == 0:
                type_matrix.append(['0', i])
            if maximum != 0:
                type_matrix.append([[type_word, maximum], i])
                
        return type_matrix
    
