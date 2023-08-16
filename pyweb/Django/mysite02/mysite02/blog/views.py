from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages # 진행상태를 메시지로 폼에서 출력하고 싶을 때 사용 / flash처럼 내용을 적어주고 싶다..
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required
# Create your views here.

# 보기(View) 페이지 요청하게 되면 출력되는 내용을 기재한다.
def home(request):
    posts = Post.objects.all()  #전체 테이블 내용을 가져온다 = selectall _QuerySet
    context = {'posts' : posts}
    return render(request, 'blog/home.html', context)
    # return HttpResponse('<h1> Blog Home </h1>')

def about(request):
    return render(request, 'blog/about.html')
    # return HttpResponse('<h1> About page </h1>')

#=============================
@login_required
def create_post(request):
    if request.method  =='GET':
       context= {'form':PostForm()} # model 같은 폼 태그 형식을 속성으로 만들어서 클래스 안의 Meta에 지정된 값을 리턴
       return  render(request,'blog/post_form.html',context)    #context : forms.py의 Meta..
    elif request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts')
        else:
            return render(request, 'blog/post_form.html', {'form': form})

#==============================

def web01(request):
    return HttpResponse('<h1> Web01 page </h1>')

def web02(request):
    return HttpResponse('<h1> Web02 page </h1>')

#======================================8/11
@login_required
def edit_post(request,id):
    queryset = Post.objects.filter(author=request.user)# 추가
    post = get_object_or_404(queryset, id=id)

    # post = get_object_or_404(Post, id=id) #원본 : URL 패턴과 일치하지 않으면 404로 리다이렉션을 하겠다.
    if request.method == 'GET':
        context = {'form' : PostForm(instance=post), 'id' : id}
        return render(request,'blog/post_form.html', context)   #'' 주소로 템플릿을 랜더링한다.
    elif request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            #https://docs.djangoproject.com/en/4.2/ref/contrib/messages/ 내용확인 및 추가
            messages.success(request,'The post has been updated successfully')
            return redirect('posts')
        else:
            messages.error(request,'Please correct the following errors : ')
            return render(request,'blog/post_form.html',{'form':form})

@login_required
def delete_post(request,id):
    queryset = Post.objects.filter(author=request.user)  # 추가
    post = get_object_or_404(queryset, id=id)
    # post = get_object_or_404(Post, id=id)
    context={'post' : post}
    if request.method == 'GET':
        return render(request,'blog/post_confirm_delete.html', context)   #'' 주소로 템플릿을 랜더링한다.
        #request객체에 내용을 담아서 제어권을 넘긴다..
    elif request.method == 'POST':
        post.delete()
        messages.success(request,'The post has been deleted successfully')
        return redirect('posts')
        # 제어권이고 뭐고 그냥 넘어가라..