from django.urls import path

from authentication.views import *

app_name = "auth"
urlpatterns = [
    path("authentication/", index),
    # path("profile/<slug>/", ClientProfileAddView.as_view(), name="profile"),
    # path("profile/<int:pk>/", ClientProfileDetailView.as_view(), name="profile_detail"),
    path("profile/", ClientProfile.as_view(), name="client_profile"),
    path("profile/update", ClientProfileUpdate.as_view(), name="update_profile"),
    path(
        "profile/update/information",
        ClientInformationUpdate.as_view(),
        name="update_information",
    ),
    # path("profile/update", clientedit, name="update_profile"),
    # path(
    #     "profile/<int:pk>/edit",
    #     ClientProfileEditView.as_view(),
    #     name="edit_profile",
    # ),
    # path('quiz/add/', teachers.QuizCreateView.as_view(), name='quiz_add'),
    # path('quiz/<int:pk>/', teachers.QuizUpdateView.as_view(), name='quiz_change'),
    # path('quiz/<int:pk>/delete/', teachers.QuizDeleteView.as_view(), name='quiz_delete'),
    # path('quiz/<int:pk>/results/', teachers.QuizResultsView.as_view(), name='quiz_results'),
    # path('quiz/<int:pk>/question/add/', teachers.question_add, name='question_add'),
]
