from django.shortcuts import render


# Create your views here.
def bulletin_index(request):
    """
    Render the bulletin index page.
    """
    
    context = {
        "page_title": "Bulletins",
    }
    return render(request, 'meteodeskbulletin/index.html', context)
