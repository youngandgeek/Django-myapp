from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

#urls mapping
urlpatterns = [
    
    path('booking/',views.form_view,name="booking"),

    path('home/',views.home,name="home"),

    path('menu/',views.menu,name="menu"),
    #path ('drinks/<str:name>',views.drinks),str:name-> that name is passed as argument in the view func in views.py
    # <str path converter to capture the URL parameter for the string "Pasta",
    # from view function menuitems (dic) 
    path('dishes/<str:dish>', views.dishesitems),
    #in link add /drinks/tea
    path('drinks/<str:drink>',views.drinksitems),

    path('about',views.about,name="about"),
    path('menu_item/<int:id>', views.display_menu_items, name="menu_item"),

]
