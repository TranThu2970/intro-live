from django.db import models
from django.utils.text import slugify



# Create your models here.

class Field(models.Model):
    name = models.CharField(max_length=200)
    avatar = models.ImageField(null=True, blank=True, upload_to="images", default="/images/placeholder.png")
    content = models.TextField(null=True, blank=True)
    active = models.BooleanField(default=True)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
	    return self.name
	#create URL
    def save(self, *args, **kwargs):
	    if self.slug == None:
		    slug = slugify(self.name)

		    has_slug = Field.objects.filter(slug=slug).exists()
		    count = 1
		    while has_slug:
			    count += 1
			    slug = slugify(self.name) + '-' + str(count) 
			    has_slug = Field.objects.filter(slug=slug).exists()

		    self.slug = slug

	    super().save(*args, **kwargs)


class FieldDetail(models.Model):
    field = models.ForeignKey(Field, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=1000)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name


class TopBuilding(models.Model):
    name = models.CharField(max_length=255)
    tags = models.ManyToManyField(Tag, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    avatar = models.ImageField(null=True, blank=True, upload_to="images", default="/images/placeholder.png")
    display_stt = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
            return self.name

        
class News(models.Model):
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    avatar = models.ImageField(null=True, blank=True, upload_to="images", default="/images/placeholder.png")
    
    def __str__(self):
            return self.name


class Team(models.Model):
    STATUS = (
        ('Kiến trúc sư', 'Kiến trúc sư'),
        ('Thiết kế nội thất', 'Thiết kế nội thất'),
        ('Giám sát xây dựng','Giám sát xây dựng'),
        ('Kế toán','Kế toán')
    )
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=200, null=True, choices=STATUS)
    avatar = models.ImageField(null=True, blank=True, upload_to="images", default="/images/placeholder.png")
    
    def __str__(self):
            return self.name