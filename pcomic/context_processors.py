from taggit.models import Tag
from .models import Category

def categories_processor(request):
    category = Category.objects.all()[:5]
    
    return {
        'category': category
    }
