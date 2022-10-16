from django import forms
from . models import post, Category, Comment

#choices = [('coding', 'coding'), ('sports', 'sports'), ('entertainment', 'entertainment'),]
choices = Category.objects.all().values_list('name','name')

choice_list = []

for item in choices:
	choice_list.append(item)


class PostForm(forms.ModelForm):
	class Meta:
		model = post
		fields = ('title', 'title_tag', 'author', 'category', 'body', 'snippet','header_image')

		widgets = {

			'title': forms.TextInput(attrs={'class': 'form-control'}),
			'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
			'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id':'tani', 'type':'hidden'}),
			#'author': forms.Select(attrs={'class': 'form-control'}),
			'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
			'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Please Discribe Your Post Here'}),
			'snippet' : forms.Textarea(attrs={'class': 'form-control'}),

		}


class EditForm(forms.ModelForm):
	class Meta:
		model = post
		fields = ('title', 'title_tag', 'body', 'snippet')

		widgets = {

			'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'This is Title Placeholder Stuff'}),
			'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'This is Title_Tag Placeholder Stuff'}),
			#'author': forms.Select(attrs={'class': 'form-control'}),
			'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Please Discribe Your Post Here'}),
			'snippet': forms.Textarea(attrs={'class': 'form-control'}),

		}

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('name', 'body')

		widgets = {

			'name': forms.TextInput(attrs={'class': 'form-control'}),
			'body': forms.Textarea(attrs={'class': 'form-control'}),

		}
