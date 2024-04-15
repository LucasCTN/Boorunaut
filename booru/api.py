from datetime import datetime, timedelta

from django.apps import apps
from django.shortcuts import get_object_or_404
from django.db.models import Q, F, Value
from django.utils import timezone
from django.db.models.functions import Concat

from .models import Post, Comment
from .auth import OptionalJWTAuth

from ninja import ModelSchema, Router
from ninja import Query
from ninja.errors import HttpError
from ninja_jwt.authentication import JWTAuth

from typing import List, Optional
from pydantic import BaseModel, Field

router = Router()

class PostSchema(ModelSchema):
    url: str = Field(...)

    class Config:
        model           = Post
        model_fields    = ['parent', 'preview', 'sample', 'media', 'score']

@router.get('posts/list', response={200: List[PostSchema]})
def list_posts(request):
    posts = Post.objects.all()
    return list(posts)
