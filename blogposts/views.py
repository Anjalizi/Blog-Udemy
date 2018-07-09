from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
def home(request):
	# -pub_date for decreasing order
	posts = Post.objects.order_by('-pub_date')
	return render(request, 'blogposts/home.html',{'posts':posts})

def post_details(request, post_id):
	posts = get_object_or_404(Post, pk=post_id)
	return render(request, 'blogposts/post_detail.html', {'posts': posts})
