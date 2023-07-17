from django.shortcuts import render

# Create your views here.
def user_filter(request):
    s='venkaaat'
    v='hai hall'
    f='MY name is VENKAT'
    d={'s':s,'v':v,'f':f}
    return render(request,'user_filter.html',d)
