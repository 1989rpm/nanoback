from rest_framework import serializers
from .models import GalleryImage, LabImage, CoverArt, NewsItem, Position
from .models import LabHead, LabMember, Alumni
from .models import JournalMetric, JournalEntry
from .models import Book, BookChapter, Patent, TradeMark
from .models import TwitterEmbed, LinkedinEmbed

class GalleryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryImage
        fields = ['id', 'image', 'caption', 'uploaded_at']

class LabImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabImage
        fields = ['id', 'image', 'caption', 'uploaded_at']

class CoverArtSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoverArt
        fields = ['id', 'image', 'caption', 'uploaded_at']

class NewsItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsItem
        fields = '__all__'

class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'

class LabHeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabHead
        fields = '__all__'

class LabMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabMember
        fields = '__all__'

class AlumniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumni
        fields = '__all__'

class JournalMetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = JournalMetric
        fields = '__all__'

class JournalEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = JournalEntry
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class BookChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookChapter
        fields = '__all__'

class PatentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patent
        fields = '__all__'

class TradeMarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = TradeMark
        fields = '__all__'

class TwitterEmbedSerializer(serializers.ModelSerializer):
    class Meta:
        model = TwitterEmbed
        fields = '__all__'

class LinkedinEmbedSerializer(serializers.ModelSerializer):
    class Meta:
        model = LinkedinEmbed
        fields = '__all__'