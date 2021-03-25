from django.test import TestCase
from flask import Flask
from flask import request

def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(username)
        print(password)