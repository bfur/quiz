from django.db import models
from django.urls import reverse
from django_tables2.columns.base import Column
from itnet.models.models_settings import ItnetModelSettings
from itnet.mixins.itnetModelMixins import objPermissionsMixin, RelatedObjMixin, mfMixin
from itnet.decorators.inject_request import inject_request

from django.core.paginator import Paginator
import django_tables2 as tables
import sys 

class ModelSettings(ItnetModelSettings):
    def __init__(self, name, namespace='quiz', module_name=__name__, permissions = None, urls = None):
        super().__init__(name, namespace, module_name, permissions, urls)