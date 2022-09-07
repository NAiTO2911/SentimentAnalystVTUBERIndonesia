from django.apps import AppConfig
from django.conf import settings
import os
import pickle


class AisentimenanalisisvtuberConfig(AppConfig):
    path = os.path.join(settings.MODELS, 'model_b.pickle')

    #with models into separate variable

    with open (path, 'rb') as pickled:
        data = pickle.load(pickled)
    model = data ['model']
    vectorizer = data ['vectorizer']

