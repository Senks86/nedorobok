from django.shortcuts import render
from .models import Advertisement, Like, Comment, Notification
from django.contrib.auth.decorators import user_passes_test, login_required
from django.shortcuts import redirect
from .forms import AdvertisementForm, CommentForm
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponseForbidden

def is_moderator_or_admin(user):
    return user.is_superuser or user.groups.filter(name__in=['Moderator', 'Admin']).exists()

def ads_list(request):
    ads = Advertisement.objects.filter(is_active=True).order_by('-created_at')
    can_add = False
    if request.user.is_authenticated:
        can_add = (
            request.user.is_superuser or
            request.user.groups.filter(name__in=['Moderator', 'Admin']).exists())
        
    return render(request, 'ads/ads_list.html', {'ads': ads, 'can_add': can_add})

@login_required
@user_passes_test(is_moderator_or_admin)
def ad_create(request):
    if request.method == 'POST':
        form = AdvertisementForm(request.POST)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.author = request.user
            ad.save()
            return redirect('ads:list')
    else:
        form = AdvertisementForm()
    return render(request, 'ads/ad_form.html', {'form': form})

def ad_edit(request, pk):
    ad = get_object_or_404(Advertisement, pk=pk)
    if request.method == 'POST':
        form = AdvertisementForm(request.POST, instance=ad)
        if form.is_valid():
            form.save()
            return redirect('ads:list')
    else:
        form = AdvertisementForm(instance=ad)
    
    return render(request, 'ads/ad_form.html', {'form': form})

def ad_delete(request, pk):
    ad = get_object_or_404(Advertisement, pk=pk)
    if request.method == 'POST':
        ad.delete()
        return redirect('ads:list')
    return render(request, 'ads/ad_confirm_delete.html', {'ad': ad})

def toggle_like(request, ad_id):
    ad = get_object_or_404(Advertisement, id=ad_id)
    like = Like.objects.filter(ad=ad, user=request.user).first()
    if like:
        like.delete()
    else:
        Like.objects.create(ad=ad, user=request.user)
    return redirect('ads:list') 

def add_comment(request, pk):
    ad = get_object_or_404(Advertisement, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.ad = ad
            comment.author = request.user
            comment.save()
    if ad.author != request.user:
        Notification.objects.create(user=ad.author, message=f"Новий коментар до вашого оголошення «{ad.title}»")
    return redirect('ads:list')

def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if comment.author != request.user:
        return HttpResponseForbidden("Ви не можете видалити цей коментар")
    comment.delete()
    return redirect('ads:list')

def reply_comment(request, comment_id):
    parent = get_object_or_404(Comment, id=comment_id)
    ad = parent.ad
    if request.method == 'POST':
        text = request.POST.get("text")
    if text:
        Comment.objects.create(ad=ad, author=request.user, text=text, parent=parent)
    if parent.author != request.user:
        Notification.objects.create(user=parent.author, message="💬Хтось відповів на ваш коментар💬")
    return redirect('ads:list')

def notifications(request):
    notes = Notification.objects.filter(user=request.user).order_by("-created_at")
    return render(request, "notifications.html", {"notes": notes})

