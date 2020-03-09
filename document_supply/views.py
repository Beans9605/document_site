from django.shortcuts import render

# Create your views here.
def propose_before (request) :
    return render(request, "document_supply/apply.html")