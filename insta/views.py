from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from .models import Image, Profile, Like
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from .forms import ImageForm, ProfileForm, CommentForm
from django.contrib.auth import logout
from .email import send_welcome_email

# Create your views here.

@login_required(login_url='/accounts/login/')
def index(request):
    current_user = request.user
    images = Image.objects.all().order_by('-posted_at')
    profiles = Profile.objects.filter(user_id = current_user.id).all()
    
    if request.method == 'POST':  
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            com = form.save(commit=False)
            com.user = request.user
            com.save()
            return redirect('index')
    
    else:
        form = CommentForm()
        
    return render(request, 'index.html',{"current_user": current_user, "images":images, "profiles":profiles, "form":form})


@login_required(login_url='/accounts/login/')
def post(request):
    
    if request.method == 'POST':  
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('index')
    
    else:
        form = ImageForm()
        return render(request, 'post.html', {'form':form})
    

@login_required(login_url='/accounts/login/')
def userprofile(request):
    current_user = request.user
    images =Image.objects.filter(user_id = current_user.id).all()
    profiles = Profile.objects.filter(user_id = current_user.id).all()
    return render(request, 'user-profile.html',{"current_user": current_user, "images":images, "profiles":profiles})
 

@login_required(login_url='/accounts/login/')
def updateprofile(request):
    current_user = request.user
    form = ProfileForm(request.POST, request.FILES)
    if request.method == 'POST':  
        
        
        if form.is_valid():
            prof = form.save(commit=False)
            prof.user = request.user
            prof.save()
            return redirect ('userprofile')
        
        else:
            form = ProfileForm()
                        
    return render(request, 'update-profile.html', {'form':form})  


@login_required
def search_results(request):
  if 'search_user' in request.GET and request.GET["search_user"]:
    search_term = request.GET.get('search_user')
    searched_users = Profile.search_profile(search_term)
    message = f"{search_term}"
    return render(request,'search.html',{"message":message,"users":searched_users})
  else:
    message="You haven't searched for any term."  
    return render(request,'search.html',{"message":message,"users":searched_users})

@login_required(login_url='/accounts/login/')
def profile(request,pk):
    
    user = User.objects.get(pk = pk)
    images = Image.objects.filter(user = user).all()
    current_user = request.user
    profiles = Profile.objects.filter(user = user).all()
    return render(request,'profile.html',{"current_user":current_user,"images":images, "user":user, "profiles":profiles})  

@login_required
def comments(request,image_id):
  form = CommentForm()
  image = Image.objects.filter(pk = image_id).first()
  if request.method == 'POST':
    form = CommentForm(request.POST)
    if form.is_valid():
      comment = form.save(commit = False)
      comment.user = request.user
      comment.image = image
      comment.save() 
  return redirect('index')

def like(request, image_id):
    current_user = request.user
    image=Image.objects.get(id=image_id)
    new_like,created= Like.objects.get_or_create(liker=current_user,image=image)
    new_like.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])
