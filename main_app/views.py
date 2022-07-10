
from django.shortcuts import render, redirect
# Add the following import
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Plant, Condition, Photo
from .forms import BloomForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
import boto3

S3_BASE_URL = 'https://s3.us-east-1.amazonaws.com/'
BUCKET = 'plantcollector-avatar'

# Define the home view
def home(request):
    # This is where we return a response in most cases we render a template and we'll need some data for that template
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


# Add the plant class & list and view function below the imports
# class Plant:  # Note that parens are optional if not inheriting from another class
#   def __init__(self, name, sciname, description, location, date):
#     self.name = name
#     self.sciname = sciname
#     self.description = description
#     self.location = location
#     self.date = date

# plants = [
#   Plant('Pink Ladys Slipper', 'Cypripedium acaule', 'showy wildflower from the orchid family', 'Wildflower island', '5/28/22'),
#   Plant('Eastern Bluestar', 'Amsonia tabernaemontana', 'pale blue star shaped blooms', 'Sara Stein Garden', '6/18/22'),
#   Plant('Tall Meadow Rue', 'Thalictrum dasycarpum', 'delicate white stamen that billow in the wind', 'Sara Stein Garden', '6/18/22'),

# ]
@login_required
def plants_index(request):
    # plants = Plant.objects.all()
    plants = Plant.objects.filter(user=request.user)
    return render(request, 'plants/index.html', {'plants': plants})

@login_required
def plants_detail(request, plant_id):
    plant = Plant.objects.get(id=plant_id)
    bloom_form = BloomForm()
    conditions_plant_doesnt_have = Condition.objects.exclude(id__in = plant.conditions.all().values_list('id'))
    return render(request, 'plants/detail.html', {
      'plant': plant, 'bloom_form': bloom_form,
      'conditions': conditions_plant_doesnt_have
    })

@login_required
def add_bloom(request, plant_id):
  # create the ModelForm using the data in request.POST
  form = BloomForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_bloom = form.save(commit=False)
    new_bloom.plant_id = plant_id
    new_bloom.save()
  return redirect('detail', plant_id=plant_id)

@login_required
def assoc_condition(request, plant_id, condition_id):
  # Note that you can pass a toy's id instead of the whole object
  Plant.objects.get(id=plant_id).conditions.add(condition_id)
  return redirect('detail', plant_id=plant_id)

@login_required
def assoc_condition_delete(request, plant_id, condition_id):
  # Note that you can pass a toy's id instead of the whole object
  Plant.objects.get(id=plant_id).conditions.remove(condition_id)
  return redirect('detail', plant_id=plant_id)

@login_required
def add_photo(request, plant_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full url string
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            # we can assign to cat_id or cat (if you have a cat object)
            photo = Photo(url=url, plant_id=plant_id)
            photo.save()
        except Exception as error:
            print('An error occurred uploading file to S3')
        return redirect('detail', plant_id=plant_id)
    return redirect('detail', plant_id=plant_id)


def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

class PlantCreate(LoginRequiredMixin, CreateView):
    model = Plant
    fields = ['name', 'sciname', 'description', 'location']
    def form_valid(self, form):
      form.instance.user = self.request.user
      return super().form_valid(form)

class PlantUpdate(LoginRequiredMixin, UpdateView):
  model = Plant
  # Let's disallow the renaming of a by excluding the name field!
  fields = ['name', 'sciname', 'description', 'location']

class PlantDelete(LoginRequiredMixin, DeleteView):
  model = Plant
  success_url = '/plants/'

class ConditionList(LoginRequiredMixin, ListView):
  model = Condition
  template_name = 'conditions/index.html'

class ConditionDetail(LoginRequiredMixin, DetailView):
  model = Condition
  template_name = 'conditions/detail.html'

class ConditionCreate(LoginRequiredMixin, CreateView):
    model = Condition
    fields = ['sun', 'moisture']


class ConditionUpdate(LoginRequiredMixin, UpdateView):
    model = Condition
    fields = ['sun', 'moisture']


class ConditionDelete(LoginRequiredMixin, DeleteView):
    model = Condition
    success_url = '/conditions/'