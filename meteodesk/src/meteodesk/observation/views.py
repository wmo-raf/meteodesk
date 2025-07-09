from django.shortcuts import render


# Create your views here.
def obs_index(request):
    """
    Render the observation index page.
    """
    
    context = {
        "page_title": "Observations",
    }
    
    return render(request, 'meteodeskobs/index.html', context)
