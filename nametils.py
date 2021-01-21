from input_words import input_word
from frequencies_count import maximum_word_count
from predict import predict_personal_names


class name_classifier():
    
    def predict_names(self, per_name):
        predictions = predict_personal_names(maximum_word_count(input_word(per_name)))
        return predictions
    
    
