from django.db.models import F, Sum
from django.shortcuts import get_object_or_404
from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from . import models, serializers


class QuestionViewSet(
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet):

    permission_classes = (AllowAny, )
    serializer_class = serializers.QuestionSerializer
    queryset = (
        models.Question.objects
        .prefetch_related('choices')
        .annotate(total_votes=Sum('choices__votes'))
    )

    @action(detail=True, methods=['post'])
    def vote(self, request, pk=None):
        choice = get_object_or_404(models.Choice, question=pk, id=request.data.get('choice'))
        choice.votes = F('votes') + 1
        choice.save(update_fields=('votes', ))

        return Response(
            data=self.get_serializer(self.get_object()).data
        )
