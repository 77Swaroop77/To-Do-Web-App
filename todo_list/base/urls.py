from django.contrib import admin
from django.urls import path, include
from base.views import Home, Login, SignUp, add_todo, delete_todo, Signout


urlpatterns = [
    path('', Home, name='Home'),
    path('Login/', Login, name='Login'),
    path('SignUp/', SignUp),
    path('Home/', Home),
    path('admin/', admin.site.urls),
    path('add-todo/', add_todo),
    path('delete-todo/<int:id>', delete_todo),
    path('logout/', Signout),
]
