from django.shortcuts import render
from .models import GithubUsersDB
from django.views.generic.list import ListView
from django.http import Http404
from django.utils.translation import gettext as _
from .serializers import GitHubUsersSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView

# Create your views here.

class Home(ListView):
    allow_empty = True
    model = GithubUsersDB
    template_name = "github/home.html"
    context_object_name = 'github_users'
    
    
    def get_paginate_by(self, queryset ):
        pagination = self.request.GET.get('pagination')
        if pagination:
            self.paginate_by = pagination
        else:
            self.paginate_by = 25
        return self.paginate_by
    

class Users(APIView, PageNumberPagination):
    """
    Examples:

    http://127.0.0.1:8000/api/users/profiles/?username=mojombo
    http://127.0.0.1:8000/api/users/profiles/?id=1
    http://127.0.0.1:8000/api/users/profiles/?page=2
    """
    

    def get(self, request, id=None, format=None, username=None):
        idd = self.request.GET.get('id')
        uss = self.request.GET.get('username')
        
        if idd:
            try:
                user = GithubUsersDB.objects.get(pk=idd)
                serializer = GitHubUsersSerializer(user)
            except GithubUsersDB.DoesNotExist:
                raise Http404
        elif uss:
            try:
                user = GithubUsersDB.objects.get(username=uss)
                serializer = GitHubUsersSerializer(user)
            except GithubUsersDB.DoesNotExist:
                raise Http404
        else:
            try:
                user = GithubUsersDB.objects.all()
                results = self.paginate_queryset(user, request, view = self)
            
                serializer = GitHubUsersSerializer(results, many=True)
            except GithubUsersDB.DoesNotExist:
                raise Http404
        return Response(serializer.data)
    
