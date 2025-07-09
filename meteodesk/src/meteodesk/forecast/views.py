from django.shortcuts import render


# Create your views here.
def forecast_index(request):
    """
    Render the forecast index page.
    """
    
    context = {
        "page_title": "Forecasts",
    }
    
    return render(request, 'meteodeskforecast/index.html', context)
