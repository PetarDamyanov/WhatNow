from django.shortcuts import render, get_object_or_404
from users.models import UsersTasks
from users.models import Users


def list(request):
    print(request.session.get('user_id'))
    user = get_object_or_404(Users, user_id=request.session.get('user_id'))
    return render(request, 'tasks/list.html', {'tasks': UsersTasks.objects.filter(user_id=user).all()})


# def detail(request, task_id):
#     task = get_object_or_404(Tasks, id=task_id)
#     return render(request, 'tasks/detail.html', {'tasks': task})


# class TaskCreateView(CreateView):
#     model = Tasks
#     fields = ['title', 'project_id', 'date_start', 'date_end', 'status', 'description']
#     template_name = 'tasks/create.html'

#     def get_success_url(self, **kwargs):
#         return reverse_lazy('tasks:tasks:detail', kwargs={'task_id': self.object.id})


# class CourseUpdateView(UpdateView):
#     model = Course
#     fields = ['name', 'description', 'start_date', 'end_date']
#     template_name = 'courses/create.html'

#     def get_success_url(self, **kwargs):
#         return reverse_lazy('education:courses:detail', kwargs={'course_id': self.object.id})