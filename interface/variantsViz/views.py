from django.shortcuts import render

# Create your views here.

def tab_list(request):
    return render(request,'variantsViz/tab_list.html', {})
