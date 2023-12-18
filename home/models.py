from django.db import models

category_choices = (
    ('self-help','self-help'),
    ('Horror', 'Horror'),
    ('Romance','Romance'),
    ("Child", "Child"),
    ('History', 'History'),
    ('Health','Health'),
    ('Biography','Biography'),
    ('Fiction and Literature','Fiction and Literature'),
    ('Sprituality and philosophy','Sprituality and Philosophy'),
)
class Book(models.Model):
    book_name = models.CharField(max_length=200)
    author = models.CharField(max_length=50,blank=True)
    slug = models.SlugField(max_length=50)
    price = models.IntegerField()
    description = models.TextField(max_length=500, blank=True)
    Image = models.ImageField(upload_to="photos/books")
    is_available = models.BooleanField(default=True)
    category = models.CharField(max_length=100, choices=category_choices)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.book_name
    
