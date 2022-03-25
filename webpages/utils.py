from django.utils.text import slugify 

import string
import random


def generate_random_string(N): 
    res = ''.join(random.choices(
                             string.digits, k = N))
    return res
  

def generate_slug(text):
    new_slug = slugify(text)
    from webpages.models import BlogModel
    
    if BlogModel.objects.filter(slug = new_slug).first():
        return generate_slug(text +'-rand'+ generate_random_string(3))
    return new_slug