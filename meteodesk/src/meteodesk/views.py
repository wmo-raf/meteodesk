from django.shortcuts import render


# Create your views here.
def weather_variables_settings(request):
    """
    Render the forecast index page.
    """
    return render(request, 'meteodesk/index.html')
