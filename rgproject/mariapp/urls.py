from django.urls import path,include
from . import views

urlpatterns = [
  path('intro', views.show_intro, name='intro'),
  path('pass_data', views.show_pass_data, name='pass_data'),
  path('product_crud', views.show_product, name='product_crud'),
]

"""
pip install django
django-admin startproject rgproject
cd rgproject
python manage.py startapp mariapp
in mari app create urls.py file
in mari app create templates folder
in mari app create static folder

in project level add app in installed apps in settings.py
in project level add mariapp.urls in urlpatterns in urls.py
"""
