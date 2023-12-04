from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from django.views import generic, View
from .models import Post, Category
from .forms import CommentForm, PostForm
from hitcount.views import HitCountDetailView, HitCountMixin
from django.core.paginator import Paginator
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib import messages

def blog(request):
    context = {}
    posts = Post.objects.filter(status=1).order_by("-hit_count_generic")
    categories = Category.objects.all()
    paginator = Paginator(posts, 4) 
    page_number = request.GET.get("page")
    posts = paginator.get_page(page_number)

    context = {
        'posts': posts,
        'categories': categories,
       
    
    }
    return render(request, 'index.html', context)


class PostDetail(HitCountDetailView):
    model = Post
    count_hit = True
 
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        comment_count = post.comments.filter(approved=True).count()
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
            
        context = {
                'post': post,
                'comments': comments,
                'commented': False,
                'liked': liked,
                'comment_form': CommentForm(),
                'comment_count': comment_count,
            }

        return render(request, 'post_detail.html', context)
        

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        context = {
                'post': post,
                'comments': comments,
                'commented': False,
                'liked': liked,
                'comment_form': CommentForm(),
            }

        return render(request, 'post_detail.html', context)
    

class PostLike(View):
    """
    Logged in user can like and unlike a post
    """
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class PostCreate(CreateView):

    model = Post
    form_class= PostForm
    template_name = 'post_create.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        success_message = "Your post is awaiting approval."
        messages.add_message(self.request, messages.SUCCESS, success_message)
        return super().form_valid(form)
        