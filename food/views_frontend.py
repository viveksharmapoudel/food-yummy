from django.utils import timezone
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView, FormView, UpdateView, ListView, CreateView, DetailView)
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.http import HttpResponseRedirect, HttpResponse

from .models import (Food,Category,
					 MessageUs,OurContact,
					 )

from .forms import MessageUsForm


class Index(TemplateView):
	template_name='food/frontend/frontend_home.html'

	def get_context_data(self, **kwargs):
		context=super(Index,self).get_context_data(**kwargs)
		headline_recipe=(Food.objects.filter(deleted_at__isnull=True,is_headline=True)
									.order_by('-created_at')[0]
									)
		context['headline_recipe']=headline_recipe
		sideline_recipe= (Food.objects.filter(deleted_at__isnull=True,is_sideline=True)
								 	.order_by('-created_at')
									.exclude(id=headline_recipe.id)
								   	)[:4]
		context['sideline_recipe']=sideline_recipe
		featured_recipes=(Food.objects.filter(deleted_at__isnull=True,is_feature=True)
								   	.exclude(id__in=[object.id for object in sideline_recipe]+[headline_recipe.id])
								   	.order_by('-created_at')
								   	)[:10]
		print(featured_recipes)
		context['featured_recipes']=featured_recipes
		categories=(Category.objects.filter(deleted_at__isnull=True,)
								.order_by('priority')[:5]
								)
		context['categories']=categories
		first_category_data=Food.objects.filter(deleted_at__isnull=True,food_category=categories[0])
		context['first_category_data']=first_category_data

		return context


class Recipe(DetailView):
	template_name='food/frontend/recipe.html'
	model= Food

	def get_context_data(self,**kwargs):
		context=super(Recipe,self).get_context_data(**kwargs)
		try:
			food_images=Food.objects.get(pk=self.kwargs['pk'])
			context['food_gallery']=FoodPictureGallery.objects.filter(deleted_at__isnull=True,food_images=food_images)
			context['similar_posts']=Food.objects.filter(food_category=food_images.food_category)[:5]
		except:
			pass

		return context


class CategoryView(ListView):
	template_name='food/frontend/frontend_category.html'
	paginate_by=5

	def get_queryset(self):
		self.category= get_object_or_404(Category,pk=self.kwargs['pk'])
		return Food.objects.filter(deleted_at__isnull=True,food_category=self.category)


class FrontendContactUs(CreateView):
	template_name='food/frontend/contact.html'
	model=MessageUs
	form_class = MessageUsForm
	success_url = reverse_lazy('food_app:index')	

	def get_context_data(self, **kwargs):
	    context = super(FrontendContactUs, self).get_context_data(**kwargs)
	    context['our_contact']=(OurContact.objects.filter(deleted_at__isnull=True)
	    										.order_by('-created_at'))[0]

	    return context


###Ajax call for sending data
def category_data(request):

	if request.method == 'GET':
		food_id=request.GET['food_id']
		print(food_id)
		category=get_object_or_404(Category,pk=food_id)
		food_data=Food.objects.filter(deleted_at__isnull=True,food_category=category)
		template_name='food/frontend/category_section.html'
		context={'category_foods': food_data}
		return render(request, template_name,context)

	else: 
		return HttpResponse("page not found")








