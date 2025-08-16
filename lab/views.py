from rest_framework import generics, filters
from rest_framework.generics import ListAPIView
from rest_framework.decorators import api_view, throttle_classes
from rest_framework.throttling import AnonRateThrottle
from .models import GalleryImage, LabImage, CoverArt, NewsItem, Position
from .models import LabHead, LabMember, Alumni
from .models import JournalMetric, JournalEntry
from .models import Book, BookChapter, Patent, TradeMark
from .models import TwitterEmbed, LinkedinEmbed
from .serializers import BookSerializer, BookChapterSerializer, PatentSerializer, TradeMarkSerializer
from .serializers import JournalMetricSerializer, JournalEntrySerializer
from .serializers import GalleryImageSerializer, LabImageSerializer, CoverArtSerializer, NewsItemSerializer, PositionSerializer
from .serializers import LabHeadSerializer, LabMemberSerializer, AlumniSerializer
from .serializers import TwitterEmbedSerializer, LinkedinEmbedSerializer
from django.core.mail import send_mail
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
import os
from django.conf import settings
from .pagination import ThirtyPerPagePagination, TwentyPerPagePagination

def api_root_view(request):
    """
    A simple view for the API root.
    """
    return JsonResponse({"message": "Welcome to the NanoBack API.", "status": "ok"})

class ContactFormThrottle(AnonRateThrottle):
    rate = os.getenv("FORM_THROTTLE", "1/5min")  # 1 request every 5 minutes

@api_view(['POST'])
@throttle_classes([ContactFormThrottle])
def contact_form(request):
    name = request.data.get('name')
    email = request.data.get('email')
    subject = request.data.get('subject')
    message = request.data.get('message')

    full_message = f"From: {name} <{email}>\n\n{message}"

    try:
        send_mail(
            subject,
            full_message,
            os.getenv("EMAIL_FROM"),  # From email in .env
            [os.getenv("EMAIL_TO")],  # To email in .env
            fail_silently=False,
        )
        return JsonResponse({"success": "Message sent successfully"})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class GalleryImageListView(generics.ListAPIView):
    queryset = GalleryImage.objects.all().order_by('-uploaded_at')
    serializer_class = GalleryImageSerializer
    pagination_class = ThirtyPerPagePagination

class LabImageListView(generics.ListAPIView):
    queryset = LabImage.objects.all().order_by('-uploaded_at')
    serializer_class = LabImageSerializer
    pagination_class = ThirtyPerPagePagination

class CoverArtListView(generics.ListAPIView):
    queryset = CoverArt.objects.all().order_by('-uploaded_at')
    serializer_class = CoverArtSerializer
    pagination_class = ThirtyPerPagePagination

class NewsItemListView(ListAPIView):
    queryset = NewsItem.objects.order_by('-date')[:10]
    serializer_class = NewsItemSerializer

class PositionListView(ListAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer

class LabHeadAPIView(generics.ListAPIView):
    queryset = LabHead.objects.all()
    serializer_class = LabHeadSerializer

class LabMemberAPIView(generics.ListAPIView):
    queryset = LabMember.objects.all().order_by('idx')  # you can order by name, etc.
    serializer_class = LabMemberSerializer

class AlumniAPIView(generics.ListAPIView):
    queryset = Alumni.objects.all().order_by('idx')
    serializer_class = AlumniSerializer

class JournalMetricListView(generics.ListAPIView):
    queryset = JournalMetric.objects.all()
    serializer_class = JournalMetricSerializer

class JournalEntryListView(generics.ListAPIView):
    queryset = JournalEntry.objects.all().order_by('-idx')
    serializer_class = JournalEntrySerializer
    pagination_class = TwentyPerPagePagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['text']

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all().order_by('-idx')
    serializer_class = BookSerializer
    pagination_class = TwentyPerPagePagination

class BookChapterListView(generics.ListAPIView):
    queryset = BookChapter.objects.all().order_by('-idx')
    serializer_class = BookChapterSerializer
    pagination_class = TwentyPerPagePagination

class PatentListView(generics.ListAPIView):
    queryset = Patent.objects.all().order_by('-idx')
    serializer_class = PatentSerializer
    pagination_class = TwentyPerPagePagination

class TradeMarkListView(generics.ListAPIView):
    queryset = TradeMark.objects.all().order_by('-idx')
    serializer_class = TradeMarkSerializer
    pagination_class = TwentyPerPagePagination

class TwitterEmbedListView(ListAPIView):
    queryset = TwitterEmbed.objects.filter(active=True)
    serializer_class = TwitterEmbedSerializer

class LinkedinEmbedListView(ListAPIView):
    queryset = LinkedinEmbed.objects.filter(active=True)
    serializer_class = LinkedinEmbedSerializer
