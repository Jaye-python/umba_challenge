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
    

class GitHubUsersApi(generics.ListAPIView):
    '''
    API URL: http://127.0.0.1:8000/api/users/profiles/
    '''
    queryset = GithubUsersDB.objects.all()
    serializer_class = GitHubUsersSerializer
    

class UserID(APIView):
    """
    API URL: http://127.0.0.1:8000/api/users/profiles/id/<id>
    """
    def get_object(self, id=None):
        try:
            return GithubUsersDB.objects.get(pk=id)
        except GithubUsersDB.DoesNotExist:
            raise Http404

    def get(self, request, id=None, format=None):
        user = self.get_object(id)
        serializer = GitHubUsersSerializer(user)
        return Response(serializer.data)


class UserName(APIView):
    """
    API URL: http://127.0.0.1:8000/api/users/profiles/username/<username>
    """
    def get_object(self, username=None):
        try:
            return GithubUsersDB.objects.get(username=username)
        except GithubUsersDB.DoesNotExist:
            raise Http404

    def get(self, request, username=None, format=None):
        user = self.get_object(username)
        serializer = GitHubUsersSerializer(user)
        return Response(serializer.data)
    
