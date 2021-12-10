from .models import Candidate
from rest_framework import serializers


class CandidateSerializers(serializers.ModelSerializer):
    total_experience = serializers.SerializerMethodField(method_name='calculate_total_exp', read_only=True)
    start = serializers.DateField(write_only=True)
    end = serializers.DateField(write_only=True)
    work_experience = serializers.SerializerMethodField(method_name='work_exp', read_only=True)


    class Meta:
        model = Candidate
        fields = ['id', 'name', 'total_experience', 'work_experience', 'start', 'end']

    def create(self, validated_data):
        return Candidate.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.start = validated_data.get('start', instance.start)
        instance.end = validated_data.get('end', instance.end)
        instance.work_experience = validated_data.get('work_experience', self.work_exp(instance))
        instance.total_experience = validated_data.get('total_experience', self.calculate_total_exp(instance))
        instance.save()
        return instance

    def calculate_total_exp(self, instance):
        start = instance.start
        end = instance.end
        months = (end.year*12) - (start.year*12)
        return int(months/12)

    def work_exp(self, instance):
        return {
            'start': instance.start,
            'end': instance.end,
        }



