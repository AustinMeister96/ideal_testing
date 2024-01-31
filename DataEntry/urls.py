from django.urls import re_path, include, path
from . import views
from accounts import views as accounts_views
from accounts.views import login_view, logout_view
from .views import add_lab_processing_with_data, add_ct_scan, add_mandatory_questionaire_c, add_mandatory_questionaire_de, add_inclusion

urlpatterns = [
]
