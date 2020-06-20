from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
  return render(request, 'index.html')

def create(request):
  # print(request.POST['name'])
  print(request.POST['dojo'])
  boxes = request.POST.getlist('good')
  context = {
    'name': request.POST['name'],
    'location': request.POST['dojo'],
    'language': request.POST['location'],
    'comment': request.POST['comment'],
    'gender': request.POST['gender'],
    'exp': boxes
  }
  return render(request, 'result.html', context)
def result(request):
  return render(request, 'result.html')
