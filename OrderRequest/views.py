from django.shortcuts import render

# Create your views here.


class VoipListView(ListView):
    model = VoIpInformation
    context_object_name = "voiplistview"
