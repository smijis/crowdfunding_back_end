from django.urls import path
from . import views
# . means inside this same folder

urlpatterns = [
    path('fundraisers/', views.FundraiserList.as_view()), #if there isn't a number after fundraisers, then just return list of fundraisers
    path('fundraisers/<int:pk>/', views.FundraiserDetail.as_view()), #added another URL pattern to match
    path('pledges/', views.PledgeList.as_view()),
]
# tells it what the url path is and what view to send the path to + a special django function that helps to view it