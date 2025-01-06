from rest_framework import viewsets, filters
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet

from advertisement.filters import IsAuthorFilterBackend, PriceFilterBackend, CategoryFilterBackend
from advertisement.models import Advertisement, Category, Report
from advertisement.permissions import IsAuthorOrAdmin
from advertisement.serializers import AdvertisementSummarySerializer, AdvertisementSerializer, CategorySerializer, \
    ReportSerializer


class AdvertisementViewSet(viewsets.ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = [IsAuthorOrAdmin]
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        IsAuthorFilterBackend,
        PriceFilterBackend,
        CategoryFilterBackend,
    ]
    search_fields = ['title', 'description']
    ordering_fields = ['created', 'price']

    def get_serializer_class(self):
        if self.action == 'list':
            return AdvertisementSummarySerializer
        return AdvertisementSerializer

    def get_permissions(self):
        if self.action in ['retrieve', 'list']:
            return [AllowAny()]
        return [IsAuthorOrAdmin()]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CategoryViewSet(ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        if self.request.user.is_staff:
            return Report.objects.all()
        return Report.objects.filter(user=self.request.user)
