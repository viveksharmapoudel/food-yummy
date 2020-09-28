from django.db import models
from django.contrib.auth.models import User

from ckeditor.fields import RichTextField

AUDIT_TYPE_CHOICES = (
    (1, 'LOGIN'),
    (2, 'LOGOUT'),
    (3, 'CREATE'),
    (4, 'UPDATE'),
    (5, 'DELETE'),
)

PRIORITY_TYPE_CHOICES=(
	(1,'MOST-IMPORTANT'),
	(2,'SECOND-MOST'),
	(3,'THIRD-MOST'),
	(4,'FEATURE'),
	(5,'this_week_top'),
)

PRIORITY_CATEGORY=(
	(1,'MOST-IMPORTANT'),
	(3,'SECOND-MOST'),
	(3,'THIRD-MOST'),
	)

##date time model 
class DateTimeModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False,)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True,)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True

    def delete(self):
        self.deleted_at = timezone.now()
        super().save()


## user model
class UserModel(DateTimeModel):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
    	return "{}".format(self.created_by.username)


########################### main elements######################################
class Category(UserModel,DateTimeModel):
	name= models.CharField(max_length=100)
	priority=models.IntegerField(choices=PRIORITY_CATEGORY, default=3)

	class Meta: 
		verbose_name='category'
		verbose_name_plural='categories'
		ordering=['-created_at',]

	def __str__(self):
		return "{}".format(self.name)


class Tag(UserModel,DateTimeModel):
	name=models.CharField(max_length=100)

	class Meta: 
		verbose_name='tag'
		verbose_name_plural='tags'
		ordering=['-created_at',]
	
	def __str__(self):
		return "{}".format(self.name)


class Food(UserModel,DateTimeModel):
	name=models.CharField(max_length=100)
	description=RichTextField(max_length=10000, null=True)
	instructions=RichTextField(max_length=10000, null=True)
	notes=RichTextField(max_length=10000, null=True)
	ingredients= RichTextField(max_length=2000, null=True)
	food_tags=models.ManyToManyField(Tag)
	food_priority= models.IntegerField(choices=PRIORITY_TYPE_CHOICES,null=True, blank=True)
	food_category=models.ForeignKey(Category,
				  on_delete=models.SET_NULL,null=True,blank=True)
	cook_time=models.IntegerField(null=True,blank=True)
	prep_time=models.IntegerField(null=True,blank=True)
	is_headline=models.BooleanField(default=False)
	is_feature=models.BooleanField(default=False)
	is_sideline=models.BooleanField(default=False)
	food_main_image=models.ImageField(blank=True, upload_to='food/', default='no_img.jpg')

	class meta: 
		verbose_name='food'
		verbose_name_plural='foods'
		ordering=['-created_at',]

	def __str__(self):
		return "{}".format(self.name)


class FoodPictureGallery(UserModel,DateTimeModel):
	image=models.ImageField(blank=True,upload_to='food_gallery/')
	food_images=models.ForeignKey(Food,on_delete=models.CASCADE, related_name='picture_gallery')

	def __str__(self):
		return "{}".format(self.food_images.name)


class OurContact(UserModel,DateTimeModel):
	phone_number=models.BigIntegerField()
	email_address=models.EmailField()
	address=models.CharField(max_length=200)

	def __str__(self):
		return "{}".format(self.address)


class MessageUs(UserModel, DateTimeModel):
	name=models.CharField(max_length=200,)
	phone_number=models.BigIntegerField(null=True,blank=True)
	email_address=models.EmailField(null=True,blank=True)
	subject=models.CharField(max_length=200)
	comment=models.TextField()




