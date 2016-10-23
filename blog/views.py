from django.shortcuts import render

# Create your views here

# La view piu' semplice puo' essere simile a questa

def post_list(request):
    return render(request, 'blog/post_list.html', {})
# abbiamo creato un metodo (def) chiamato post_list che prende request e restituisce
# un metodo render che ci fornira' (mettera' insieme) il nostro template blog/post_list.html