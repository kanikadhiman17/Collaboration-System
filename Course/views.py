from django.shortcuts import render
from .models import Course, Topics




def create_course(request):
	name = request.POST['name']
	desc = request.POST['desc']
	course = Course.objects.create(name=name, desc=desc)
	return course


def create_topics(request, pk):

	if request.user.is_authenticated:
		if request.method == 'POST':
			name = request.POST['name']
			parentid = request.POST['parentid']
			if Topics.objects.filter(pk=parentid).exist():
				parent = Topics.objects.get(pk=parentid)
			else:
				parent = None
			course = Course.objects.get(pk=pk)
			topic = Topics.objects.create(name = name, parent=parent, course = course )
			return topic
		else:
			course = Course.objects.get(pk=pk)
			topics = Topics.object.filter(course=course)
			return render(request, 'signup.html', {'course': course, 'topics':topics})




