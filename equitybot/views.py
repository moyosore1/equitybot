from rest_framework import generics


from .models import Equity
from .serializers import EquitySerializer


class ListEquities(generics.ListAPIView):
    queryset = Equity.objects.all()
    serializer_class = EquitySerializer

