from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from .models import Note
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


@login_required
def main(request):
    
    return render(request, 'landingpage.html')

@login_required
def create_note(request):
    user = request.user
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        Note.objects.create(title=title, content=content, user=user)
       
        return redirect("all_notes")
        
        
        
         
        # Ensure 'all_notes' is a valid URL name
    return render(request, "createnote.html")

@login_required
def all_notes(request):
    user = request.user
    notes = Note.objects.filter(user=user)  # Fetch all notes from the database
    return render(request, "all_notes.html", {"notes": notes})


def saved_notes(request):
    notes = Note.objects.all()
    return render(request, "all_notes.html", {"notes": notes})




def delete_note(request, note_id):
   
        note = Note.objects.get(id=note_id)
        note.delete()
        return redirect("all_notes")


def deleteall_note(request ):
     note = Note.objects.all()
     note.delete()
     return redirect("all_notes")


def edit_note(request,note_id):
    user = request.user
    note = get_object_or_404(Note, id=note_id)
    if request.method == "POST":
        note.title = request.POST("title")
        note.content = request.POST("content")
        note.save()
        return redirect(all_notes)
    return render(request, "edit.html", {"note": note})

def signup(request):
     if request.method == 'POST':
         username = request.POST['username']
         password1 = request.POST['password1']
         password2 = request.POST['password2']
         email = request.POST['email']
         if password1 == password2:
               user = User.objects.create(username=username, email=email )
               user.set_password(password1)
               user.save()
               login(request, user)

         else:
              return HttpResponse('Passwords do not match.')
                
         

            
         return redirect('login_user')
        
         
        
     return render(request,'signup.html')
     
def login_user(request):
    if request.method == 'POST':
        username = request.POST['login_username']
        password = request.POST['login_password']
        user = authenticate(username=username, password=password)
        if user.is_authenticated:
            login(request, user)
            return redirect('main')     
    return render (request, 'login.html', )


def logout_user(request):
     logout(request)
     return redirect('main')





# Create your views here.
