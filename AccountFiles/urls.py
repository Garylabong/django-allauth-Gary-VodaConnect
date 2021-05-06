from django.urls import path

from AccountFiles.views import AccountFilesView

app_name= 'acc_file'
urlpatterns = [
    path("account/files/", AccountFilesView.as_view(), name="acc_files")
    
]