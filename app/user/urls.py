from user import views

from django.urls import path


app_name = 'user'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('manage/', views.ManageUserView.as_view(), name='manage'),
    path('authtoken/', views.AuthTokenView.as_view(), name='token'),
    #path('update/<username>', views.RetrieveUpdateDeleteUser.as_view(), name='update'),
    #path('get/<username>', views.RetrieveUpdateDeleteUser.as_view(), name='get'),

]