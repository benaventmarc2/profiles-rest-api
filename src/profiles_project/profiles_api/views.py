from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class HelloApiView(APIView):
    """ Test API View."""
    
    def get(self, request, fromat=None):
        """ Returns a list of APIViews features."""
        
        an_apiview = [
            "Uses HTTP methos as functions (get, post, patch, put, delete)",
            "It is similar to a traditional Django view",
            "Gives you the most control over your logic",
            "Is mapped manually to URLs"    
        ]
        
        return Response({"message": "Hello!", "an_apiview": an_apiview})