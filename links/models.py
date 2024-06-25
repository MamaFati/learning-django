from django.db import models
from django.utils.text  import slugify
# slugify : It take in a string and all spaces between them it returns them with a "-" to make then url frendly

# Create your models here.
# save a shortened link => name, urls,slug
class Link(models.Model):
    name = models.CharField(max_length=50, unique=True)
    url = models.URLField(max_length=200) 
    # example of urls mysite.com/links/1
    slug = models.SlugField(unique=True, blank=True)
    clicks = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.name} | {self.clicks}"
    
    def click(self):
        self.clicks += 1
        self.save()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        return super().save(*args, **kwargs)