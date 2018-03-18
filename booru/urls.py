from django.urls import re_path, path

import account.views
from . import views

app_name = "booru"

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^post/view/(?P<post_id>[0-9]+)/$', views.post_detail, name='post_detail'),
    re_path(r'^upload/$', views.upload, name='upload'),
    re_path(r'^post/list/$', views.post_list_detail, name='posts'),
    re_path(r'^post/list/(?P<page_number>[0-9]+)/$', views.post_list_detail, name='post_page_detail'),
    re_path(r'^tags/$', views.tags_list, name='tags_list'),
    re_path(r'^tags/list/(?P<page_number>[0-9]+)/$', views.tags_list, name='tags_page_list'),
    re_path(r'^tags/(?P<tag_id>[0-9]+)/edit/$', views.tag_edit, name='tag_edit'),
    path('tag_implications', views.ImplicationListView.as_view(), name='implication-list'),
    path('tag_implications/<int:pk>/', views.ImplicationDetailView.as_view(), name='implication-detail'),
    path('tag_aliases', views.AliasListView.as_view(), name='alias-list'),
    path('tag_aliases/<int:pk>/', views.AliasDetailView.as_view(), name='alias-detail'),

    re_path(r'^tag_alias_request/$', views.alias_create, name='alias_create'),
    re_path(r'^tag_implication_request/$', views.implication_create, name='implication_create'),

    re_path(r'^tag_aliases/(?P<alias_id>[0-9]+)/approve/$', views.alias_approve, name='alias_approve'),
    re_path(r'^tag_implications/(?P<implication_id>[0-9]+)/approve/$', views.implication_approve, name='implication_approve'),
    re_path(r'^tag_aliases/(?P<alias_id>[0-9]+)/disapprove/$', views.alias_disapprove, name='alias_disapprove'),
    re_path(r'^tag_implications/(?P<implication_id>[0-9]+)/disapprove/$', views.implication_disapprove, name='implication_disapprove'),
    re_path(r'^profile/(?P<account_slug>[\w-]+)/$', account.views.profile, name='profile'),

    re_path(r'^pool/new/$', views.pool_create, name='pool_create'),    
    re_path(r'^pool/(?P<pool_id>[0-9]+)/$', views.pool_detail, name='pool_detail'),
]
