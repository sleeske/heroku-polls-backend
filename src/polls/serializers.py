from rest_framework import serializers
from . import models


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Choice
        fields = (
            'id',
            'choice_text',
            'votes',
        )


class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True)
    total_votes = serializers.SerializerMethodField()

    class Meta:
        model = models.Question
        fields = (
            'id',
            'question_text',
            'pub_date',
            'choices',
            'total_votes',
        )

    def get_total_votes(self, obj):
        return getattr(obj, 'total_votes', 0)
