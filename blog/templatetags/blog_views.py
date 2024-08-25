from django import template
from blog.models import Post

register = template.Library()


@register.inclusion_tag('blog/blog-news.html')
def get_news(cnt=4):
    posts = Post.objects.order_by('-created_at')[:cnt]
    return {"posts": posts}