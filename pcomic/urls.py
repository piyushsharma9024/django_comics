from django.urls import path
from .views import home_view, tagged, detail_view, category, Comics_view, comics_search

app_name = 'pcomics'

urlpatterns=[
    path('', home_view, name='home'),
    path('search/', comics_search, name='comics-search'),
    path('comics/', Comics_view.as_view() , name='comics'),
    path('gallary/<slug>/', detail_view, name='detail'),
    path('gallary/tag/<slug>/', tagged, name='tags'),
    path('gallary/category/<str:cats>/', category, name='category')
]
