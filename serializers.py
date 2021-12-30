from rest_framework import serializers
from .models import GithubUsersDB

class GitHubUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = GithubUsersDB
        fields = ['id', 'username', 'avatar_url', 'type', 'url', 'html_url']
        
        