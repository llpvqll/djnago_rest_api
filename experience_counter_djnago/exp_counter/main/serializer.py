from .models import Candidate
from rest_framework import serializers


class CandidateSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100, required=True)
    total_experience = serializers.IntegerField()
    start = serializers.DateField()
    end = serializers.DateField()

    def create(self, validated_data):
        return Candidate.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.start = validated_data.get('start', instance.start)
        instance.end = validated_data.get('end', instance.end)

        instance.save()
        return instance

