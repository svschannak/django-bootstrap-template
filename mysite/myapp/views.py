from django.shortcuts import render_to_response

def home(request):
    message = "Welcome to myapp"
    return render_to_response('index.html', {'message': message})
