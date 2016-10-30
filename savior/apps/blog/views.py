import re

from django.template.response import TemplateResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from savior.apps.blog.models import Post
from savior.lib.utils.views import get_image_url
from taggit.models import Tag


def format_post(post):
    image = get_image_url(post.image)
    author_image = get_image_url(post.author.image)

    return {
        'post': post,
        'image': image,
        'author': post.author,
        'author_image': author_image,
        'safe_text': re.sub('<.*?>', '', post.text)
    }


def get_all_posts(req):
    tag = req.GET.get('tag', '')
    posts_list = Post.objects.filter(published=True).order_by('-ctime')
    if tag:
        posts_list = posts_list.filter(tags__name__in=[tag])

    paginator = Paginator(posts_list, 5)
    page = req.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    start_page = max(1, min(posts.number - 2, posts.paginator.num_pages - 4))
    end_page = min(max(posts.number + 2, 5), posts.paginator.num_pages)
    pages = range(start_page, end_page + 1)

    context = {
        'posts': [format_post(post) for post in posts],
        'handler': posts,
        'pages': pages,
        'current_tag': tag,
        'tags': [tag.name for tag in Tag.objects.all()],
        'current': 'blog'
    }

    return TemplateResponse(req, 'blog.html', context)


def get_post(req, post_id):
    post = Post.objects.get(pk=post_id)
    tags = post.tags.all()
    return TemplateResponse(req, 'blog-single.html', {
        'post': format_post(post),
        'tags': [tag.name for tag in tags]
    })
