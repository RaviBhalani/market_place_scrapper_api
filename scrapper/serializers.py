from rest_framework.fields import IntegerField, CharField
from rest_framework.serializers import Serializer


class ScrapperListSerializer(Serializer):
    product = CharField()
    page = IntegerField(required=False, min_value=1, default=1)
