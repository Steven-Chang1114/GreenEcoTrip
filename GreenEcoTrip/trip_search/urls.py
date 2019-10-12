from django.urls import include, path
import views
urlpatterns = [
    path('results/', views.result_view, name='result-view'),
]
