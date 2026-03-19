from django.urls import path
from .views import ad_delete,  ads_list, ad_create, ad_edit, toggle_like, add_comment, delete_comment, reply_comment, notifications

app_name = 'ads'
urlpatterns = [
    path('', ads_list, name='list'),
    path('create/', ad_create, name='create'),
    path('<int:pk>/edit/', ad_edit, name='edit'),
    path('<int:pk>/delete/', ad_delete, name='delete'),
    path('like/<int:ad_id>/', toggle_like, name='toggle_like'),
    path("comment/<int:pk>/", add_comment, name="comment"),
    path("comment/delete/<int:comment_id>/", delete_comment, name="delete_comment"),
    path("comment/reply/<int:comment_id>/", reply_comment, name="reply_comment"),
    path("notifications/", notifications, name="notifications"),
]