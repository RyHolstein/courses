from django.shortcuts import render, redirect
from .models import Course
# Create your views here.
def index(request):

    courses = Course.objects.all()
    return render(request, ('add_course_app/index.html'), {'courses': courses})


def submit(request):
    if request.method == 'POST':

        Course.objects.create(name = request.POST['name'], description = request.POST['description'])
    return redirect('/')

def destroy(request, id):
    request.session['id'] = id
    thingy = Course.objects.get(id = request.session['id'])
    context = {
        'name': thingy.name,
        'description': thingy.description
    }

    return render(request, 'add_course_app/destroy.html', context)

def delete(request):
    course_id = request.session['id']
    if request.method == 'POST':
        if request.POST['destroy'] == 'yes':
            Course.objects.filter(id = course_id).delete()
            return redirect('/')
        if request.POST['destroy'] == 'no':
            return redirect('/')
