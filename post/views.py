from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import PostSerializer
from .models import Post
from rest_framework.decorators import action

from django.db.models import Func, F

import logging

logger = logging.getLogger(__name__)

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        queryset = Post.objects.all()
        tags = self.request.GET.getlist('tags')
        if tags is not None:
            queryset = queryset.filter(tags__contains=tags)
        return queryset

    @action(detail=False, methods=['get'])
    def get_all_tags(self, request):
        all_tags = Post.objects.annotate(tag=Func(F('tags'), function='unnest')).values_list('tag').distinct()
        return Response({
            "tags": [tag[0] for tag in all_tags]
        })