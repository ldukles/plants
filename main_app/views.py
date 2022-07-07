
from django.shortcuts import render
# Add the following import
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Plant

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
    return render(request, 'plants/detail.html', { 'plant': plant })

class PlantCreate(CreateView):
    model = Plant
    fields = '__all__'

class PlantUpdate(UpdateView):
  model = Plant
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['sciname', 'description', 'location', 'date']

class PlantDelete(DeleteView):
  model = Plant
  success_url = '/plants/'