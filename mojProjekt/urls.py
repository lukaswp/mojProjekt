from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def strona_glowna(request):
    return HttpResponse(
        "<h1>Witaj na mojej stronie Django!</h1>"
        "<p>Projekt dziala poprawnie na PythonAnywhere.</p>"
    )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', strona_glowna),
]
