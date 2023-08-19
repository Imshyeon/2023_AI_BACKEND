from django.forms import ModelForm
from .models import Post

class PostForm(ModelForm):
    class Meta: #key-value
        model = Post
        fields = ['title', 'content', 'published_at', 'author'] #key



'''
    title = models.CharField(max_length=120)
    content = models.TextField()
    published_at = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
'''