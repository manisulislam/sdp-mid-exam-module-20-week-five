from django.shortcuts import redirect,render
from django.views import View

class homeView(View):
    def get(self,request):
        return render(request,'home.html')
