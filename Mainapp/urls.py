
from django.urls import path
from . import views

urlpatterns = [
    path(
        '',
        views.Index.as_view(),
        name='Index'
    ),

    path(
        'inicio/',
        views.Index.as_view(),
        name='Inicio'
    ),

    path(
        'registro/',
        views.Register_User.as_view(),
        name='Registro'
    ),

    path(
        'login/',
        views.LoginUser.as_view(),
        name='Login'
    ),

    path(
        'update-password/',
        views.UpdatePasswordsView.as_view(),
        name='Update_Password'
    ),

    path(
        'logout/',
        views.LogoutUser.as_view(),
        name='Logout'
    ),
]
