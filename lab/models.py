from django.db import models
import os

# Create your models here.
class GalleryImage(models.Model):
    image = models.ImageField(upload_to='gallery/')
    caption = models.CharField(max_length=255, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.caption:
            # Auto-generate caption from filename
            self.caption = os.path.splitext(os.path.basename(self.image.name))[0].replace('_', ' ').capitalize()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.caption
    
class LabImage(models.Model):
    image = models.ImageField(upload_to='gallery/')
    caption = models.CharField(max_length=255, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.caption:
            # Auto-generate caption from filename
            self.caption = os.path.splitext(os.path.basename(self.image.name))[0].replace('_', ' ').capitalize()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.caption
    
class CoverArt(models.Model):
    image = models.ImageField(upload_to='cover_arts/')
    caption = models.CharField(max_length=255, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.caption:
            self.caption = os.path.splitext(os.path.basename(self.image.name))[0].replace('_', ' ').capitalize()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.caption

class NewsItem(models.Model):
    date = models.DateField()
    description = models.TextField()
    image = models.ImageField(upload_to='news_images/', blank=True, null=True)
    hyperlink = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.date}: {self.description}"

class Position(models.Model):
    position = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.position

class LabHead(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    description = models.TextField(null =True)
    google_scholar = models.URLField(blank=True, null=True)
    email = models.EmailField()
    linkedin = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    orcid = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='members/lab_head/', blank=True, null=True)

    def __str__(self):
        return self.name

class LabMember(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    idx = models.IntegerField(default=0)
    description = models.TextField()
    linkedin = models.URLField(blank=True, null=True)
    email = models.EmailField()
    twitter = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='members/lab_members/', blank=True, null=True)

    def __str__(self):
        return self.name

class Alumni(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    idx = models.IntegerField(default=0)
    linkedin = models.URLField(blank=True, null=True)
    email = models.EmailField()
    twitter = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='members/alumni/', blank=True, null=True)

    def __str__(self):
        return self.name

class JournalMetric(models.Model):
    name = models.CharField(max_length=100)
    value = models.IntegerField()

    def __str__(self):
        return f"{self.name}: {self.value}"


class JournalEntry(models.Model):
    image = models.ImageField(upload_to='journal_images/')
    text = models.TextField()
    caption = models.CharField(max_length=255)
    link = models.URLField()
    idx = models.IntegerField(default=0)

    def __str__(self):
        return self.text
    
class Book(models.Model):
    idx = models.IntegerField(default=0)
    description = models.TextField()
    idx = models.IntegerField(default=0)
    def __str__(self):
        return self.description
    
class BookChapter(models.Model):
    idx = models.IntegerField(default=0)
    description = models.TextField()
    idx = models.IntegerField(default=0)

    def __str__(self):
        return self.description
    
class Patent(models.Model):
    idx = models.IntegerField(default=0)
    description = models.TextField()
    idx = models.IntegerField(default=0)

    def __str__(self):
        return self.description
    
class TradeMark(models.Model):
    idx = models.IntegerField(default=0)
    description = models.TextField()
    idx = models.IntegerField(default=0)

    def __str__(self):
        return self.description
    

class TwitterEmbed(models.Model):
    name = models.CharField(max_length=100)  # Optional: name of the feed
    embed_code = models.TextField(help_text="Paste the raw embed HTML code here")
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class LinkedinEmbed(models.Model):
    name = models.CharField(max_length=100)  # Optional: name of the feed
    embed_code = models.TextField(help_text="Paste the raw embed HTML code here")
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name