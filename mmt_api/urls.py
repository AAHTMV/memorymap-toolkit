# Django core
from django.urls import path, re_path

# 3rd Party Modules

# Memory Map Toolkit
from . import views

urlpatterns = [
	# V1.0 urls
	path('1.0/features/', views.feature_list, name='feature_list'),
	path('1.0/features/<str:source_layer>/<int:pk>', views.feature, name='feature'),
	path('1.0/features/search/', views.search_features, name='search_features'),
	path('1.0/features/theme/', views.get_features_by_theme, name='get_features_by_theme'),
    path('1.0/features/attachments/documents/<int:pk>', views.document, name='document'),
    path('1.0/features/<str:source_layer>/<int:pk>/attachments/', views.feature_attachments, name='attachments'),
    path('1.0/pages/<str:slug>', views.page, name='page'),
    path('1.0/pages/', views.pages, name='pages'),
]


