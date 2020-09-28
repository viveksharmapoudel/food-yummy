
from django.urls import path,include

from .views_frontend import (Index,Recipe, 
							FrontendContactUs,CategoryView,
							category_data,
							)

urlpatterns =[

	path('',Index.as_view(), name='index' ),
    path('recipe/<int:pk>/',Recipe.as_view(),name='frontend-recipe'),
    path('contact-us/',FrontendContactUs.as_view(),name='contact'),
    path('category/<int:pk>/',CategoryView.as_view(),name='frontend-category'),
    
	### for index ajax call category specific food
    path('category-data/',category_data,name='frontend-category-single'),
	
]