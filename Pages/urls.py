
from django.urls import path
from . import views


urlpatterns = [

    path(
        'blog/',
        views.Blog.as_view(),
        name='Blog'
    ),

    path(
        'blog/<str:slug>',
        views.ArticleIndividual.as_view(),
        name='Article_Individual'
    ),


    path('categoria/<int:category_id>',
         views.Category_new.as_view(),
         name='Category'
         ),

    path('crear-articulo/',
         views.CreateArticle.as_view(),
         name='Crear-articulo'
         ),

    path(
        'editar-articulo/<str:slug>',
        views.EditarArticle.as_view(),
        name='Editar-articulo'
    ),
    
    path('editar/<str:slug>',
         views.UpdateArticle.as_view(),
         name='Editar'
         ),


    path('eliminar-articulo/<slug>',
         views.DeleteArticle.as_view(),
         name='Eliminar-articulo'
         ),

]




# -----------------------------------------------------------

"""

    path('editar/<str:slug>',
         views.editado.as_view(),
         name='Editar'
         ),


]
 """
