from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm, EmailPostForm, SignupForm, EditPost, PasswordChange
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import update_session_auth_hash
# , login_required

# Home page view


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

# post detail view


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


# post creation view
@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/post_create.html', {'form': form})


@login_required
def edit(request, pk):
    post = get_object_or_404(Post, pk=pk, author=request.user)
    post.save()
    if request.method == 'POST':
        form = EditPost(request.POST, instance=post)
        if form.is_valid():
            post.save()
            messages.success(request, "Updated succesfully")
            return redirect('post_list')
    else:
        form = EditPost(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


@login_required
def delete(request, pk):
    post = get_object_or_404(Post, pk=pk, author=request.user)
    post.delete()
    messages.success(request, "Item deleted Succesfully")
    return redirect('/')

# post share view


def post_share(request, pk):
    post = Post.objects.get(pk=pk)
    sent = False
    if request.method == "POST":
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(subject=f"{cd['name']} recommends you to read a post",
                      message=f"{post.title}" + "\n\n" + cd['message'],
                      from_email=settings.EMAIL_HOST_USER,
                      recipient_list=[cd['email']],
                      auth_user=settings.EMAIL_HOST_USER,
                      auth_password=settings.EMAIL_HOST_PASSWORD)
            sent = True
            messages.success(request, "Email Sent successfullly")
            return redirect('/')
    else:
        form = EmailPostForm()
    return render(request, 'blog/share.html', {'post': post, 'form': form})

# Sign up view


def register(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User created successfullly")
            return redirect('/')

    else:
        form = SignupForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChange(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            # Important to update the session with the new password hash
            update_session_auth_hash(request, user)
            messages.success(
                request, 'Your password was successfully updated!')
            return redirect('/')  # Redirect to a success page
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChange(request.user)
    return render(request, 'registration/passwordChange.html', {'form': form})


# def passwordReset(request):
#     if request.method == 'POST':
#         form = PasswordReset(request.POST)
#         if form.is_valid():
#             messages.success(request, 'Check your Mail')
#             return redirect('/')  # Redirect to a success page
#         else:
#             messages.error(request, 'Please correct the error below.')
#     else:
#         form = PasswordReset()
#     return render(request, 'registration/reset_password.html', {'form': form})
