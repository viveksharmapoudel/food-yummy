
from django.urls import path,include


from .views import (AdminPage,AdminLogin,AdminLogout,
					CategoryList,CategoryCreate,CategoryUpdate,CategoryDelete, 
					TagList,TagCreate, TagUpdate, TagDelete,
					FoodList, FoodCreate, FoodUpdate, FoodDelete,FoodDetail,
					MessageUsList,MessageUsDetail,MessageUsDelete,
					OurContactList,OurContactCreate,OurContactUpdate,
					OurContactDetail,OurContactDelete,
					FoodPictureGalleryDelete,
					)


app_name = 'food_app'

urlpatterns = [

	path('admin-panel/', AdminPage.as_view(), name='admin-page'),
	path('admin-login/', AdminLogin.as_view(),name='admin-login'),
	path('admin-logout',AdminLogout.as_view(),name='admin-logout'),

	##crud for category
	path('admin-panel/categorylist',CategoryList.as_view(), name='admin-category-list' ),
	path('admin-panel/category-create',CategoryCreate.as_view(), name='admin-category-create' ),
	path('admin-panel/category-update/<int:pk>/',CategoryUpdate.as_view(), name='admin-category-update' ),
	path('admin-panel/category-delete/<int:pk>/',CategoryDelete.as_view(), name='admin-category-delete' ),

	##crud for tag
	path('admin-panel/taglist',TagList.as_view(), name='admin-tag-list' ),
	path('admin-panel/tag-create',TagCreate.as_view(), name='admin-tag-create' ),
	path('admin-panel/tag-update/<int:pk>/',TagUpdate.as_view(), name='admin-tag-update' ),
	path('admin-panel/tag-delete/<int:pk>/',TagDelete.as_view(), name='admin-tag-delete' ),

	##crud for food
	path('admin-panel/foodlist',FoodList.as_view(), name='admin-food-list' ),
	path('admin-panel/food-create',FoodCreate.as_view(), name='admin-food-create' ),
	path('admin-panel/food-update/<int:pk>/',FoodUpdate.as_view(), name='admin-food-update' ),
	path('admin-panel/food-delete/<int:pk>/',FoodDelete.as_view(), name='admin-food-delete' ),
	path('admin-panel/food-detail/<int:pk>/',FoodDetail.as_view(), name='admin-food-detail' ),

	##crud for mszus
	path('admin-panel/messageuslist',MessageUsList.as_view(), name='admin-message-us-list' ),
	path('admin-panel/messageus-delete/<int:pk>/',MessageUsDelete.as_view(), name='admin-message-us-delete' ),
	path('admin-panel/messageus-detail/<int:pk>/',MessageUsDetail.as_view(), name='admin-message-us-detail' ),

	##crud for ourcontact
	path('admin-panel/our-contactlist',OurContactList.as_view(), name='admin-our-contact-list' ),
	path('admin-panel/our-contact-create',OurContactCreate.as_view(), name='admin-our-contact-create' ),
	path('admin-panel/our-contact-update/<int:pk>/',OurContactUpdate.as_view(), name='admin-our-contact-update' ),
	path('admin-panel/our-contact-delete/<int:pk>/',OurContactDelete.as_view(), name='admin-our-contact-delete' ),
	path('admin-panel/our-contact-detail/<int:pk>/',OurContactDetail.as_view(), name='admin-our-contact-detail' ),
	
	##for picture gallery
	path('admin-panel/food-picture-gallery-delete/<int:pk>/',FoodPictureGalleryDelete.as_view(), name='admin-food-gallery-delete' ),


	##Including all the frontend urls 
	path('',include('food.urls_frontend')),

]