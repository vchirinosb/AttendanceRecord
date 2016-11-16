from django.shortcuts import render

# Create your views here.
def IndexView(request):
    template_name = 'attendance/index.html'
    return render(request, template_name, {})
