from django.urls import path
from .views import indexPageView, azure_recommender

urlpatterns = [
    path('jobrecommendations/', azure_recommender, name='azure_recommender'),
    path('', indexPageView, name='recommender_index'),
]
