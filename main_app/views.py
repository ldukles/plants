
from django.shortcuts import render, redirect
# Add the following import
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Plant, Condition
from .forms import BloomForm
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

def plants_index(request):
    plants = Plant.objects.all()
    return render(request, 'plants/index.html', {'plants': plants})

def plants_detail(request, plant_id):
    plant = Plant.objects.get(id=plant_id)
    bloom_form = BloomForm()
    conditions_plant_doesnt_have = Condition.objects.exclude(id__in = plant.conditions.all().values_list('id'))
    return render(request, 'plants/detail.html', {
      'plant': plant, 'bloom_form': bloom_form,
      'conditions': conditions_plant_doesnt_have
    })

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

def assoc_condition(request, plant_id, condition_id):
  # Note that you can pass a toy's id instead of the whole object
  Plant.objects.get(id=plant_id).conditions.add(condition_id)
  return redirect('detail', plant_id=plant_id)

def assoc_condition_delete(request, plant_id, condition_id):
  # Note that you can pass a toy's id instead of the whole object
  Plant.objects.get(id=plant_id).conditions.remove(condition_id)
  return redirect('detail', plant_id=plant_id)

class PlantCreate(CreateView):
    model = Plant
    fields = ['name', 'sciname', 'description', 'location']
    success_url = '/plants/'

class PlantUpdate(UpdateView):
  model = Plant
  # Let's disallow the renaming of a by excluding the name field!
  fields = ['name', 'sciname', 'description', 'location']

class PlantDelete(DeleteView):
  model = Plant
  success_url = '/plants/'

class ConditionList(ListView):
  model = Condition
  template_name = 'conditions/index.html'

class ConditionDetail(DetailView):
  model = Condition
  template_name = 'conditions/detail.html'

class ConditionCreate(CreateView):
    model = Condition
    fields = ['sun', 'moisture']


class ConditionUpdate(UpdateView):
    model = Condition
    fields = ['sun', 'moisture']


class ConditionDelete(DeleteView):
    model = Condition
    success_url = '/conditions/'