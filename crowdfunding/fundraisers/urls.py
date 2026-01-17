from django.urls import path
from . import views
# . means inside this same folder

urlpatterns = [
    path('fundraisers/', views.FundraiserList.as_view()),
]
# tells it what the url path is and what view to send the path to + a special django function that helps to view it