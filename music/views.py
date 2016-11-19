
from django.views.generic.edit import CreateView, UpdateView, DeleteView
#whenever you want to make a form to create, update, view a new object
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
#lets us redirect user on login
from django.contrib.auth import authenticate, login, logout
#takes username and password, verifies they are a user and they exist in the database
#login attaches session id so user doesnt have to login on every new page you visit
from django.views import generic
from django.views.generic import View
from .models import Album
from .forms import UserForm



def logout_user(request):
  logout(request)
  form = UserForm(request.POST or None)
  context = {
      "form": form,
  }
  return render(request, 'music/login.html', context)

class IndexView(generic.ListView):
  template_name = 'music/index.html'
  context_object_name = 'all_albums'
#by default when query returns object as object list
  def get_queryset(self):
    return Album.objects.all()

#displays details/properties on object
class DetailView(generic.DetailView):
  model = Album
  template_name = 'music/detail.html'

#inherits from createview
#pass in attributes you want user to be able to fill out in fields
class AlbumCreate(CreateView):
  model = Album
  fields = ['artist', 'album_title', 'genre', 'album_logo']
#next step is assign url pattern to new view

class AlbumUpdate(UpdateView):
  model = Album
  fields = ['artist', 'album_title', 'genre', 'album_logo']


class AlbumDelete(DeleteView):
  model = Album
  success_url = reverse_lazy('music:index')

#inherits from view
class UserFormView(View):
  form_class = UserForm
  template_name = 'music/registration_form.html'

  #display blank form for new user
  def get(self, request):
    #use this form (userform)
    form = self.form_class(None)
    return render(request, self.template_name, {'form' : form})
  #process form data
  def post(self,request):
    form = self.form_class(request.POST)


  #creates user object from form but does not store in database
    if form.is_valid():
      #
      user=form.save(commit=False)

      #cleaned(normalzed) data - ensures data is always formatted proper
      username = form.cleaned_data['username']
      password = form.cleaned_data['password']
      # user.set_password(password)
      #gives you ability to change user password
      user.save()

      #returns User objects if user exists
      user = authenticate(username=username, password=password)

      if user is not None:
        if user.is_active:
          #actually logs in user and attaches user to session
          login(request, user)
          #retuns user to index if user logs in successfully
          return redirect('music:index')

    #if not reload form
    return render(request, self.template_name, {'form' : form})


