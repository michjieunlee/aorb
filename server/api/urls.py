from django.urls import path
from . import views

urlpatterns = [
    path('aorb/', views.AorbsView.as_view()),
    path('aorb/<int:id>', views.AorbView.as_view())
]
