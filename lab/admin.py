from django.contrib import admin
from .models import GalleryImage,LabImage, CoverArt, NewsItem, Position
from .models import LabHead, LabMember, Alumni
from .models import JournalMetric, JournalEntry
from .models import Book, BookChapter, Patent, TradeMark
from .models import TwitterEmbed, LinkedinEmbed

# Register your models here.
@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('caption', 'uploaded_at')
    ordering = ('-uploaded_at',)

@admin.register(LabImage)
class LabImageAdmin(admin.ModelAdmin):
    list_display = ('caption', 'uploaded_at')
    ordering = ('-uploaded_at',)

@admin.register(CoverArt)
class CoverArtAdmin(admin.ModelAdmin):
    list_display = ('caption', 'uploaded_at')
    ordering = ('-uploaded_at',)

@admin.register(NewsItem)
class NewsItemAdmin(admin.ModelAdmin):
    list_display = ('date', 'description')
    search_fields = ('description',)

admin.site.register(Position)

admin.site.register(LabHead)
admin.site.register(LabMember)
admin.site.register(Alumni)

admin.site.register(JournalMetric)
admin.site.register(JournalEntry)

admin.site.register(Book)
admin.site.register(BookChapter)

admin.site.register(Patent)
admin.site.register(TradeMark)

admin.site.register(TwitterEmbed)
admin.site.register(LinkedinEmbed)