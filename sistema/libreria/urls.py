from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('libros', views.libros, name='libros'),
    path('libros/crear', views.crear, name='crear'),
    path('libros/editar/<int:id>', views.editar, name='editar'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('accounts/logout/', views.custom_logout, name='logout'),
    # categorias
    path('categorias', views.categorias, name='categorias'),
    path('categorias/crear_categoria', views.crear_categoria, name='crear_categoria'),
    path('categorias/editar_categoria/<int:id>', views.editar_categoria, name='editar_categoria'),
    path('eliminar_categorias/<int:id>', views.eliminar_categoria, name='eliminar_categoria'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)