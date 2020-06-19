#all
from django.shortcuts import render
#orders 
from django.shortcuts import redirect
#home
from django.core.paginator import Paginator
#orders
from django.forms import inlineformset_factory
#dashboard
from rest_framework.response  import Response
from rest_framework import status, serializers
from rest_framework.decorators import api_view
from django.views.decorators.csrf import requires_csrf_token


from ..models import *
from ..forms import *
from ..filters import OrderFilter
