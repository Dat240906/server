from django.urls import path
from . import views

app_name = 'news'
urlpatterns = [
    path('',views.Index.as_view(), name = 'index' ),
    path('add/', views.Add_post.as_view(), name = 'add'),
    path('save/', views.SaveNews.as_view(), name = 'save'),
    path('send_email/', views.Send_email.as_view(), name='send_email'),
    path('handle_email/', views.Handle_send_email.as_view(), name = "handle_email")
]