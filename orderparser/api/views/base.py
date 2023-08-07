from typing import TypeVar

from rest_framework import mixins, viewsets

Model = TypeVar("Model")


class CreateViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    pass


class ListViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    pass
