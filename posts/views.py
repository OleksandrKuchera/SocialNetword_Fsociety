import cloudinary.uploader
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Post, Like, Comment
from .forms import PostForm
from django.contrib.auth import get_user_model
from account.models import CustomUser
from django.db.models import Q
from django.db.models import Count
from django.core.exceptions import ObjectDoesNotExist

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            author_identifier = request.POST.get('author', '')
            author = get_user_model().objects.get(Q(email=author_identifier) | Q(name=author_identifier))  
            
            post = form.save(commit=False)
            post.author = author 
            
            upload_result = cloudinary.uploader.upload(request.FILES['image'])
            post.image_url = upload_result['secure_url'] 
            
            author.post_count += 1
            author.save()

            post.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)

def look_post_list_user(request, author_identifier):
    user = CustomUser.objects.get(Q(email=author_identifier) | Q(name=author_identifier))
    posts = Post.objects.filter(author=user)
    post_data = []
    for post in posts:
        comments_list = [] 
        for comment in post.comments.all():  
            comment_author = {
                'name': comment.user.name,
                'email': comment.user.email,
                'avatar': comment.user.avatar.url
            }
            comments_list.append({
                'id': comment.id,
                'author': comment_author, 
                'text': comment.text
            }) 
        likes_count = Like.objects.filter(post=post).count()
        is_liked = Like.objects.filter(post=post, user=user).exists()
        post_data.append({
            'id': post.id,
            'author': {
                'name': user.name,
                'email': user.email,
                'avatar': user.avatar.url
            },
            'post': {
                'image': post.image.url,
                'description': post.description,
                'likes': likes_count,
                'isLiked': is_liked,
                'comments': comments_list  
            }
        })
    return JsonResponse(post_data, safe=False)

def look_post_list_all(request, author_identifier):
    user = CustomUser.objects.get(Q(email=author_identifier) | Q(name=author_identifier))
    posts = Post.objects.all()
    post_data = []
    for post in posts:
        comments_list = [] 
        for comment in post.comments.all(): 
            comment_author = {
                'name': comment.user.name,
                'email': comment.user.email,
                'avatar': comment.user.avatar.url
            }
            comments_list.append({
                'id': comment.id,
                'author': comment_author, 
                'text': comment.text
            }) 
        likes_count = post.likes
        is_liked = Like.objects.filter(post=post, user=user).exists()
        post_data.append({
            'id': post.id,
            'author': {
                'name': post.author.name,
                'email': post.author.email,
                'avatar': post.author.avatar.url
            },
            'post': {
                'image': post.image.url,
                'description': post.description,
                'likes': likes_count,
                'isLiked': is_liked,
                'comments': comments_list  
            }
        })
    return JsonResponse(post_data, safe=False)



def like_post(request):
    if request.method == 'POST':
        name = request.POST.get('name_user')  
        post_id = request.POST.get('post_id')  
        print(name,post_id)
        user = CustomUser.objects.get(name=name)  
        post = get_object_or_404(Post, id=post_id)
        like, created = Like.objects.get_or_create(user=user, post=post)
        if created:
            post.likes += 1
            post.save()
            like.isLike = True
            like.save()
            return JsonResponse({'message': 'Post liked successfully'})
        else:
            return JsonResponse({'message': 'You already liked this post'}, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)

def comment_post(request):
    if request.method == 'POST':
        name = request.POST.get('name_user')
        post_id = request.POST.get('post_id')

        try:
            user = CustomUser.objects.get(name=name)
            post = Post.objects.get(id=post_id)

            comment_text = request.POST.get('comment', '')
            if comment_text:
                comment = Comment.objects.create(user=user, post=post, text=comment_text)
                return JsonResponse({'message': 'Comment added successfully'})
            else:
                return JsonResponse({'error': 'Comment text is empty'}, status=400)
        except (ObjectDoesNotExist, ValueError):
            return JsonResponse({'error': 'User or post not found'}, status=404)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)

def delete_post(request):
    if request.method == 'POST':
        name = request.POST.get('name_user')  
        post_id = request.POST.get('post_id')  
        user = CustomUser.objects.get(name=name)  # shykaemo user за im`yam
        post = get_object_or_404(Post, id=post_id)

        user.post_count -= 1
        user.save()

        if user == post.author:
            post.delete()
            return JsonResponse({'message': 'Post deleted successfully'})
        else:
            return JsonResponse({'error': 'You are not authorized to delete this post'}, status=403)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)

def unlike_post(request):
    if request.method == 'POST':
        name = request.POST.get('name_user')
        post_id = request.POST.get('post_id')
        user = CustomUser.objects.get(name=name)
        post = get_object_or_404(Post, id=post_id)
        try:
            like = Like.objects.get(user=user, post=post)
            post.likes -= 1
            post.save() 
            like.delete()
            return JsonResponse({'message': 'Like removed successfully'})
        except ObjectDoesNotExist:
            return JsonResponse({'message': 'You have not liked this post'}, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)

def delete_comment(request):
    if request.method == 'POST':
        comment_id = request.POST.get('comment_id') 
        try:
            comment = Comment.objects.get(id=comment_id)
            comment.delete()
            return JsonResponse({'message': 'Comment deleted successfully'})
        except :
           return JsonResponse({'error': 'Comment not found'}, status=404)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)
