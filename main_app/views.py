from django.shortcuts import render



def index(request, *args, **kwargs):
    return render(request, 'main_app/index.html', context={})

def show_selected(request, *args, **kwargs):
    context = {
        'selected_name': kwargs['selected']
    }

    return render(request, 'main_app/index.html', context=context)