from pickle import GET
from urllib import response
from django.shortcuts import render

from .apps import AisentimenanalisisvtuberConfig
from django.http import JsonResponse
from rest_framework.views import APIview

class call_model(APIview):
    def get(self, request):
        if request.method == 'GET':
            #gettext from request
            text = request.GET.get('text')
            
            #vectorized text
            vector = AisentimenanalisisvtuberConfig.vectorizer.transform([text])

            #build response
            response = {'text_sentiment' : prediction}

            #retuen response
            return JsonResponse(response)