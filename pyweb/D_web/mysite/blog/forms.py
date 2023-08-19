from django.forms import ModelForm
from .models import Post

class PostForm(ModelForm):
    class Meta:
        model=Post
        field=['title','content','published_at','author']