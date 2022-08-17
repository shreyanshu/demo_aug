from django.shortcuts import render, HttpResponse
from demo_app.models import Post

# Create your views here.
def dashboard(request):
    # friends_list = ['ram', 'sita', 'hariu', 'gita']
    list_post = Post.objects.all()
    return render(request, 'dashboard.html', context={'list_post': list_post})
