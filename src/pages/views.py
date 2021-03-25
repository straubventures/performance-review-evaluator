from django.shortcuts import render
from .tests import *


from django.http import HttpResponse
from django.shortcuts import render
from .ML_Script import prediction_model
from json import dumps


def home_view(request, *args, **kwargs):
    return render(request, "home.html", {
    })

def home(request, *args, **kwargs):
    return HttpResponse("This page is working!")

def result(request):
    user_input_text = str(request.POST)
    text_array = user_input_text.split(':')
    print(text_array)
    text_array[3] = text_array[3].replace('>', "", -1)
    text_array[3] = text_array[3].replace(']', "", -1)
    text_array[3] = text_array[3].replace('[', "", -1)
    text_array[3] = text_array[3].replace('\'', "", -1)
    text_array[3] = text_array[3].replace('}', "", -1)

    prediction_result = prediction_model(user_input_text)
    prediction = prediction_result[0]
    graph_data = prediction_result[1]
    data_dictionary = {}
    for word, value in graph_data:
        data_dictionary.__setitem__(word,value)
    print(data_dictionary)
    dataJSON = dumps(data_dictionary)
    return render(request, 'result.html', {'data': dataJSON, 'hello': text_array[3], 'prediction': prediction})


def index(request, *args, **kwargs):
    return render(request, "index.html", {
    })

def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {
    })


def about_view(request, *args, **kwargs):
    my_context = {
        "my_text": "this is about us.",
    }
    return render(request, "about.html", my_context)


def social_view(request, *args, **kwargs):
    return render(request, "social.html", {})
