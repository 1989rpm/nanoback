from django.urls import path
from .views import GalleryImageListView, LabImageListView, CoverArtListView, NewsItemListView, PositionListView
from .views import LabHeadAPIView, LabMemberAPIView, AlumniAPIView
from .views import JournalMetricListView, JournalEntryListView
from .views import BookListView, BookChapterListView
from .views import PatentListView, TradeMarkListView
from .views import LinkedinEmbedListView, TwitterEmbedListView
from .views import contact_form

urlpatterns = [
    path('gallery/', GalleryImageListView.as_view(), name='gallery-list'),
    path('lab-gallery/', LabImageListView.as_view(), name='lab-gallery-list'),
    path('cover-arts/', CoverArtListView.as_view(), name='cover-arts'),
    path('news/', NewsItemListView.as_view(), name='news-list'),
    path('positions/', PositionListView.as_view(), name='position-list'),
    path('members/lab-head/', LabHeadAPIView.as_view(), name='lab-head'),
    path('members/lab-members/', LabMemberAPIView.as_view(), name='lab-members'),
    path('members/alumni/', AlumniAPIView.as_view(), name='alumni'),
    path('journals/metrics/', JournalMetricListView.as_view(), name='journal-metrics'),
    path('journals/entries/', JournalEntryListView.as_view(), name='journal-entries'),
    path('books/', BookListView.as_view(), name='books'),
    path('book-chapters/', BookChapterListView.as_view(), name='book-chapters'),
    path('patents/', PatentListView.as_view(), name='patents'),
    path('trade-marks/', TradeMarkListView.as_view(), name='trade-marks'),
    path('twitter-embeds/', TwitterEmbedListView.as_view(), name='twitter-embed-list'),
    path('linkedin-embeds/', LinkedinEmbedListView.as_view(), name='linkedin-embed-list'),
    path('contact/', contact_form),
]
