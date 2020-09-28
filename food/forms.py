##order of import system, django, 3rd party, local
from django import forms 
from django.contrib.auth.models import User

from ckeditor.widgets import CKEditorWidget
from django_select2.forms import Select2Widget,Select2MultipleWidget

from .models import (Category,Tag,Food,FoodPictureGallery,
					OurContact, MessageUs,
					)


#################### Category ##################################
class CategoryForm(forms.ModelForm):
	class Meta: 
		model =Category
		fields= ('name','priority')
		
		widgets={
        	'name':forms.TextInput(attrs={'class':'form-control'}),
        	'priority':forms.NumberInput(attrs={'class':'form-control'}),

        }	


class CategoryDeleteForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('deleted_at', )


#################### Tag ######################################
class TagForm(forms.ModelForm):
	class Meta: 
		model =Tag
		fields= ('name',)
		
		widgets={
        	'name':forms.TextInput(attrs={'class':'form-control'}),
        }	


class TagDeleteForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ('deleted_at', )


#################### Food ######################################
class FoodForm(forms.ModelForm):
	class Meta: 
		model =Food
		fields= ('name','description','instructions','notes','food_tags',
			    'food_priority','food_category','prep_time','cook_time','is_feature',
			    'is_headline','is_sideline',
		        'ingredients','food_main_image')
		
		widgets={
        	'name':forms.TextInput(attrs={'class':'form-control'}),
        	'description':CKEditorWidget(attrs={'class':'form-control',}),
        	'instructions':CKEditorWidget(attrs={'class':'form-control',}),
        	'notes':CKEditorWidget(attrs={'class':'form-control',}),
        	'food_tags':Select2MultipleWidget(attrs={'class':'form-control ',
        									  'placeholder':'Select here'}),
        	'food_priority':forms.NumberInput(attrs={'class':'form-control'}),
   			'food_category':forms.Select(attrs={'class':'form-control glyphicon glyphicon-plus',
   											'placeholder':'Select here'}),
        	'prep_time':forms.NumberInput(attrs={'class':'form-control'}),
        	'cook_time':forms.NumberInput(attrs={'class':'form-control'}),
        	'is_feature':forms.NullBooleanSelect(attrs={'class':'form-control'}),
        	'is_headline':forms.NullBooleanSelect(attrs={'class':'form-control'}),
        	'is_sideline':forms.NullBooleanSelect(attrs={'class':'form-control'}),
        	'ingredients':CKEditorWidget(attrs={'class':'form-control',}),
   			'food_main_image':forms.FileInput(attrs={'class':'form-control'}),
        }	


class FoodDeleteForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ('deleted_at', )


class FoodPictureGalleryDeleteForm(forms.ModelForm):
    class Meta:
        model = FoodPictureGallery
        fields = ('deleted_at', )


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control ',
                    'placeholder':'username',
                    }))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control',
            		'placeholder':'password'}))


class MessageUsForm(forms.ModelForm):

	class Meta: 
		model =MessageUs
		fields= ('name','phone_number','email_address','subject','comment')
		labels={
			'name':'',
			'phone_number':'',
			'email_address':'',
			'subject':'',
			'comment':'',

		}
		widgets={
        	'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Your Name',}),
        	'phone_number':forms.NumberInput(attrs={'class':'form-control','placeholder':'Your Phone Number',}),
        	'email_address':forms.EmailInput(attrs={'class':'form-control','placeholder':'Your email address',}),
        	'subject':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your subject'}),
        	'comment':forms.Textarea(attrs={'class':'form-control','placeholder':'Comments'},),

        }	


class MessageUsDeleteForm(forms.ModelForm):
    class Meta:
        model = MessageUs
        fields = ('deleted_at', )


class OurContactForm(forms.ModelForm):

	class Meta: 
		model =OurContact
		fields= ('address','phone_number','email_address',)
		
		widgets={
        	'address':forms.TextInput(attrs={'class':'form-control',}),
        	'phone_number':forms.NumberInput(attrs={'class':'form-control'}),
        	'email_address':forms.EmailInput(attrs={'class':'form-control'}),
        }	
	

class OurContactDeleteForm(forms.ModelForm):
    class Meta:
        model = OurContact
        fields = ('deleted_at', )



