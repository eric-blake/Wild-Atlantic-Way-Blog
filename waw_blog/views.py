from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from django.views import generic, View
from .models import Post, Categories
from .forms import CommentForm, PostForm
from django.core.paginator import Paginator
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Count
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin



def about(request):
    """ Returns about.html """
    return render(request, 'about.html')


#Source:  Learned concept of how to filter posts from tutorial https://www.youtube.com/watch?v=RfbukFYM0rM
def post_filter(request, category_slug=None):
    """
    Filters the posts by category
    """
    context = {}
    posts = Post.objects.filter(status=1)
    categories = Categories.objects.all()

    requested_category = None
    if category_slug:
        requested_category = get_object_or_404(categories, slug=category_slug)
        posts = posts.filter(category__in =[requested_category])

    paginator = Paginator(posts, 4) 
    page_number = request.GET.get("page")
    
    context = {
        'posts': posts,
        'categories': categories,
    }
    return render(request, 'categories.html', context)



def blog(request):
    """
    Lists all posts and categories on home page
    """
    context = {}
    posts = Post.objects.filter(status=1).order_by("-created_on")
    categories = Categories.objects.all()
    paginator = Paginator(posts, 4) 
    page_number = request.GET.get("page")
    posts = paginator.get_page(page_number)
    popular_posts = Post.objects.annotate(num_likes=Count('likes')).order_by('-num_likes')[:5]
 

    context = {
        'posts': posts,
        'categories': categories,
        'popular_posts' : popular_posts,
           
    }
    return render(request, 'index.html', context)


class PostDetail(View):
    """
    Lists single post details
    """
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        categories = Categories.objects.all()
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
                'categories': categories,
                'comment_count': comment_count,
            }

        return render(request, 'post_detail.html', context)
        

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        comment_count = post.comments.filter(approved=True).count()
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
                'commented': True,
                'liked': liked,
                'comment_form': CommentForm(),
                'comment_count': comment_count,
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


class PostCreate(LoginRequiredMixin, CreateView):
    """
    Logged in user can create a post
    """
    model = Post
    form_class= PostForm
    template_name = 'post_create.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        success_message = "Your post is awaiting approval."
        messages.add_message(self.request, messages.SUCCESS, success_message)
        return super().form_valid(form)
        

class PostUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    Logged in user can update their own post
    """
    model = Post
    form_class= PostForm
    template_name = 'post_update.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        success_message = "Your post has been updated successully."
        messages.add_message(self.request, messages.SUCCESS, success_message)
        return super().form_valid(form)


# Source https://stackoverflow.com/questions/48777015/djangos-successmessagemixin-not-working-with-deleteview

class PostDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Logged in user can delete their own post
    """
    model = Post
    form_class = PostForm
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
    success_message = "Your post was deleted successfully."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message, 'danger')
        return super(PostDelete, self).delete(request, *args, **kwargs)





