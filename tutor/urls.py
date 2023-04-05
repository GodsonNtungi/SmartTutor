from django.urls import path
from tutor import views

urlpatterns = [
    path('', views.home, name="home"),
    path('uploadpdf/',views.upload_pdf,name="upload-pdf"),
    path('chat/',views.chat,name="chat"),
    path('retrieve/',views.retrieve_from_pdf,name="retrieve-from-pdf")
]
