from django.shortcuts import render

# Create your views here.

# Render landing page for 8000

def index(request):
  return render(request, 'pages/index.html')