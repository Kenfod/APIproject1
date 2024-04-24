import requests
from django.shortcuts import render

def home(request):
  # USING APIS => Example 1
  response = requests.get('https://api.github.com/events')
  data = response.json()
  result = data[0]["repo"]

  # Example 2
  reponse2 = requests.get('https://dog.ceo/api/breeds/image/random')
  data2 = reponse2.json()
  result2 = data2["message"]

  r1 = requests.get('https://uselessfacts.jsph.pl/random.json?language=en')
  data3 = r1.json()
  fact = data3['text']

  return render(request, 'templates/index.html', {'result': result, 'result2': result2, 'fact': fact})