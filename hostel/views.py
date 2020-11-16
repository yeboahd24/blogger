from django.shortcuts import render
from .models import Student
from django.db.models import Q

# Create your views here.
def search(request):
    query = request.GET.get('q', '')
    if query:
        qset = Q(Room__icontains=query)
        results = Student.objects.filter(qset)
    else:
        results = []
    return render(request, 'hostel/search.html', {'results':results, 'query':query})
