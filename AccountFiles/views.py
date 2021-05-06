from django.shortcuts import render
from django.views import View

# Create your views here.
class AccountFilesView(View):
    def get(self, request):
        return render(request, 'accountfiles/acc_files.html')
