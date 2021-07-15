from django.shortcuts import render
#from django.http import HttpResponse

import random
import string

# Create your views here.
def home(request):
    #return HttpResponse("Hello body!")
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')

def password(request):
    # request.GET['length'] or request.GET.get('length')

    possibilities = string.ascii_lowercase + \
                    (string.ascii_uppercase if request.GET.get('uppercase') else '') + \
                    (string.digits if request.GET.get('numbers') else '') + \
                    (string.punctuation if request.GET.get('special') else '')
    pwdresult = ''.join(random.choices(possibilities, k=int(request.GET.get('length', 8))))

    context = {'password': pwdresult}
    return render(request, 'generator/password.html', context)