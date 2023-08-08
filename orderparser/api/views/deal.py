from django.core.files.uploadedfile import InMemoryUploadedFile
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response

from orderparser.api.models import Deal
from orderparser.api.serializers import DealCreateSerializer, DealSerializer
from orderparser.api.services import ParserCSVBytes

from .base import CreateViewSet


class DealViewSet(CreateViewSet):
    queryset = Deal.objects.all()
    deal_serializer_class = DealSerializer
    serializer_class = DealCreateSerializer

    def create(self, request: Request, *args: list, **kwargs: dict) -> Response:
        csv_parser = ParserCSVBytes()
        create_serializer = self.get_serializer(data=request.data)
        create_serializer.is_valid(raise_exception=True)

        deals: InMemoryUploadedFile = create_serializer.validated_data["deals"]
        if not deals.file:
            raise TypeError()
        deals_data = list(csv_parser.get_deals_data(deals.file))

        # IDK why, but drf don't validate ListValidate properly. So I don't use it.
        # TODO: Make the issue.
        for deal in deals_data:
            deal_serializer = self.deal_serializer_class(data=deal)
            deal_serializer.is_valid(raise_exception=True)
            self.perform_create(deal_serializer)
        return Response({}, status=status.HTTP_201_CREATED)
