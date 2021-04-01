from rest_framework import serializers, parsers
from funzioni_iot.models import Cliente


class ClienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cliente
        fields = ('codcli', 'descli', 'citcli', 'capcli')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Cliente.objects.create(**validated_data)
