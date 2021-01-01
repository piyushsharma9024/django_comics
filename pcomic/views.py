from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from.models import Post, PostImage, Category
from taggit.models import Tag
from .forms import PostSearchForm

def home_view(request):
    posts = Post.objects.all().order_by('-date_updated')[:4]
    # Show most common tags 
    common_tags = Post.tags.most_common()
    context = {
        'posts':posts,
        'common_tags':common_tags,
    }
    return render(request, 'home.html', context)

class Comics_view(ListView):
    model = Post
    paginate_by = 3
    template_name = 'comics.html'

def detail_view(request, slug):
    post = get_object_or_404(Post, slug=slug)
    photos = PostImage.objects.filter(post=post)
    related = Post.objects.filter(category=post.category).exclude(id=post.id)

    return render(request, 'detail.html', {
        'post':post,
        'photos':photos,
        'related': related
    })

def tagged(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    posts = Post.objects.filter(tags=tag)
    context = {
        'tag': tag,
        'posts': posts,
    }
    return render(request, 'tag.html', context)

def category(request, cats):
    category = get_object_or_404(Category, name=cats.replace('-', ' ').upper())
    posts = Post.objects.filter(category=category)
    context = {
        'posts': posts
    }
    return render(request, 'category.html', context)


def comics_search(request):
    form = PostSearchForm()
    q = '' 
    results = []

    if 'q' in request.GET:
        form = PostSearchForm(request.GET)
        if form.is_valid():
            q = form.cleaned_data['q']
            results = Post.objects.filter(title__contains=q)


    return render(request, 'search.html', 
                        {'form': form,
                        'q': q,
                        'results':results})