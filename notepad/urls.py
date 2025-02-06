from django.urls import path
from . import views

urlpatterns = [
    path("", views.main, name= "main"),
    path("create/", views.create_note, name="create_note"),
    path("savednotes/", views.saved_notes, name="saved_notes"),
    path("all_notes/", views.all_notes, name="all_notes"),
    path("delete_note/<int:note_id>/", views.delete_note, name="delete_note"),
    path("deleteall_note/", views.deleteall_note, name="deleteall_note"),
    path("edit_note/<int:note_id>/", views.edit_note , name="edit_note"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    
   

]