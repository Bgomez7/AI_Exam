from django.shortcuts import render


# Create your views here.
def home(request):
    # You can add data to be passed to the template here (optional)
    context = {}
    return render(request, 'home.html', context)


