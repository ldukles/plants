
from django.shortcuts import render

# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
    # This is where we return a response in most cases we render a template and we'll need some data for that template
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


# Add the Cat class & list and view function below the imports
class Plant:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, sciname, description, location, date):
    self.name = name
    self.sciname = sciname
    self.description = description
    self.location = location
    self.date = date

plants = [
  Plant('Pink Ladys Slipper', 'Cypripedium acaule', 'showy wildflower from the orchid family', 'Wildflower island', '5/28/22'),
  Plant('Eastern Bluestar', 'Amsonia tabernaemontana', 'pale blue star shaped blooms', 'Sara Stein Garden', '6/18/22'),
  Plant('Tall Meadow Rue', 'Thalictrum dasycarpum', 'delicate white stamen that billow in the wind', 'Sara Stein Garden', '6/18/22'),

]

def plants_index(request):
    return render(request, 'plants/index.html', {'plants': plants})