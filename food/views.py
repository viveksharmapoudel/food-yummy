from django.utils import timezone
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView, FormView, UpdateView, ListView, CreateView, DetailView)
from django.views.generic.base import View
from django.contrib.auth.models import User
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse



from .models import (Category, Tag, Food,FoodPictureGallery,
					MessageUs, OurContact
					)
from .forms import (CategoryForm, CategoryDeleteForm, 
					TagForm, TagDeleteForm,
					FoodForm,FoodDeleteForm,
					MessageUsForm,MessageUsDeleteForm,
					OurContactForm, OurContactDeleteForm,
					FoodPictureGalleryDeleteForm,
					LoginForm,
					)


########################## Mixim #####################################

#*****************mixims****************************************# 
class UserRequiredMixin(UserPassesTestMixin,View):

	def test_func(self):
		return self.request.user.is_superuser


class DeleteMixin(UserRequiredMixin, UpdateView):
    
    def form_valid(self, form):
        form.instance.deleted_at = timezone.now()
        form.save()
        return super(DeleteMixin, self).form_valid(form)


########################## Admin panel ################################
class AdminPage(UserRequiredMixin,TemplateView):
	template_name='food/home.html'


class AdminLogin(TemplateView):
    template_name='account/login.html'

    def get_context_data(self):
        context=super(AdminLogin, self).get_context_data()
        form = LoginForm()
        context['form'] = form
        return context

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            form = LoginForm()
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/admin-panel/')
            else:
                print('else')

                return HttpResponseRedirect('/admin-login')


class AdminLogout(TemplateView):
    template_name='account/logout.html'

    def post(self, request):
        logout(request)
        return HttpResponseRedirect('/admin-login/')    # simply for logout only


########################## category CRUD ##############################
class CategoryList(UserRequiredMixin,ListView):
	template_name='food/categorylist.html'
	queryset=Category.objects.filter(
        deleted_at__isnull=True).order_by(
        '-created_at')


class CategoryCreate(UserRequiredMixin,CreateView):
	template_name='food/categoryform.html'
	model = Category
	form_class = CategoryForm
	success_url = reverse_lazy('food_app:admin-category-list')	

	def form_valid(self,form):
		creator = User.objects.get(username=self.request.user)
		form.instance.created_by = creator
		return super(CategoryCreate, self).form_valid(form)


class CategoryUpdate(UserRequiredMixin,UpdateView):
	template_name='food/categoryform.html'
	model = Category
	form_class = CategoryForm
	success_url = reverse_lazy('food_app:admin-category-list')


class CategoryDelete(DeleteMixin):
	'''
		soft deletion
	'''
	template_name = 'food/categorydelete.html'
	model = Category
	form_class = CategoryDeleteForm
	success_url = reverse_lazy('food_app:admin-category-list')


########################## Food CRUD ##############################
class FoodList(UserRequiredMixin,ListView):
	template_name='food/foodlist.html'
	queryset=Food.objects.filter(
        deleted_at__isnull=True).order_by(
        '-created_at')


class FoodCreate(UserRequiredMixin,CreateView):
	template_name='food/foodform.html'
	model = Food
	form_class = FoodForm
	success_url = reverse_lazy('food_app:admin-food-list')	

	def form_valid(self,form):
		creator = User.objects.get(username=self.request.user)
		form.instance.created_by = creator
		obj=form.save()
		for afile in self.request.FILES.getlist('files'):
			pic=FoodPictureGallery(created_by=creator,image=afile,food_images=obj)
			pic.save()
		
		return super().form_valid(form)


class FoodUpdate(UserRequiredMixin,UpdateView):
	template_name='food/foodform.html'
	model = Food
	form_class = FoodForm
	success_url = reverse_lazy('food_app:admin-food-list')

	def form_valid(self, form):
		prev_obj = self.get_object()
		obj = form.save()
		for afile in self.request.FILES.getlist('files'):
			creator=User.objects.get(username=self.request.user)
			pic = FoodPictureGallery( created_by=creator,image=afile,food_images=prev_obj)
			pic.save()
		
		return super().form_valid(form)


class FoodDelete(DeleteMixin):
	'''
		soft deletion
	'''
	template_name = 'food/fooddelete.html'
	model = Food
	form_class = FoodDeleteForm
	success_url = reverse_lazy('food_app:admin-food-list')


class FoodDetail(UserRequiredMixin,DetailView):
	model= Food
	template_name='food/fooddetail.html'

	def get_context_data(self,**kwargs):
		context=super(FoodDetail,self).get_context_data(**kwargs)
		try:
			food_images=Food.objects.get(pk=self.kwargs['pk'])
			context['food_gallery']=FoodPictureGallery.objects.filter(deleted_at__isnull=True,food_images=food_images)
		except:
			pass
		return context


########################## Tag CRUD ##############################
class TagList(UserRequiredMixin,ListView):
	template_name='food/taglist.html'
	queryset=Tag.objects.filter(
        deleted_at__isnull=True).order_by(
        '-created_at')


class TagCreate(UserRequiredMixin,CreateView):
	template_name='food/tagform.html'
	model = Tag
	form_class = TagForm
	success_url = reverse_lazy('food_app:admin-tag-list')	

	def form_valid(self,form):
		creator = User.objects.get(username=self.request.user)
		form.instance.created_by = creator
		return super(TagCreate, self).form_valid(form)


class TagUpdate(UserRequiredMixin,UpdateView):
	template_name='food/tagform.html'
	model = Tag
	form_class = TagForm
	success_url = reverse_lazy('food_app:admin-tag-list')


class TagDelete(DeleteMixin):
	'''
		soft deletion
	'''
	template_name = 'food/tagdelete.html'
	model = Tag
	form_class = TagDeleteForm
	success_url = reverse_lazy('food_app:admin-tag-list')


###################################################################
class FoodPictureGalleryDelete(DeleteMixin):
	'''
		soft deletion
	'''
	template_name = 'food/foodgallerydelete.html'
	model = FoodPictureGallery
	form_class = FoodPictureGalleryDeleteForm
	success_url = reverse_lazy('food_app:admin-tag-list')


###################################################################
class MessageUsList(UserRequiredMixin,ListView):
	template_name='food/message-us-list.html'
	queryset=MessageUs.objects.filter(
        deleted_at__isnull=True).order_by(
        '-created_at')


class MessageUsDetail(UserRequiredMixin,DetailView):
	model= MessageUs
	template_name='food/message-us-detail.html'


class MessageUsDelete(DeleteMixin):
	'''
		soft deletion
	'''
	template_name = 'food/message-us-delete.html'
	model = MessageUs
	form_class = MessageUsDeleteForm
	success_url = reverse_lazy('food_app:admin-message-us-list')


###################################################################
class OurContactList(UserRequiredMixin,ListView):
	template_name='food/our-contact-list.html'
	queryset=OurContact.objects.filter(
        deleted_at__isnull=True).order_by(
        '-created_at')


class OurContactCreate(UserRequiredMixin,CreateView):
	template_name='food/our-contact-form.html'
	model = OurContact
	form_class = OurContactForm
	success_url = reverse_lazy('food_app:admin-our-contact-list')	

	def form_valid(self,form):
		creator = User.objects.get(username=self.request.user)
		form.instance.created_by = creator
		return super(OurContactCreate, self).form_valid(form)


class OurContactUpdate(UserRequiredMixin,UpdateView):
	template_name='food/our-contact-form.html'
	model = OurContact
	form_class = OurContactForm
	success_url = reverse_lazy('food_app:admin-our-contact-list')


class OurContactDetail(UserRequiredMixin,DetailView):
	model= OurContact
	template_name='food/our-contact-detail.html'


class OurContactDelete(DeleteMixin):
	'''
		soft deletion
	'''
	template_name = 'food/our-contact-delete.html'
	model = OurContact
	form_class = OurContactDeleteForm
	success_url = reverse_lazy('food_app:admin-our-contact-list')








