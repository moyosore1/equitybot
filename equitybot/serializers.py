from rest_framework import serializers


from .models import Equity


class EquitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Equity
        fields = "__all__"
