#Import class APIView
from rest_framework.views import APIView
#Import exception Http4o4
from django.http import Http404
#Import Response class
from rest_framework.response import Response
#Import status
from rest_framework import status
#Import the model class and its Serializer for this view
from blog.models.article import ArticleModel
from blog.serializers.article import ArticleSerializer


class ArticleDetailView(APIView):
    """
    Retrieve, update or delete a category instance.
    """

    def get_object(self, request, pk, model):
        #Receives a http request, a key "pk" included in the URL and a model class
        #Searches the object whose primary key is equal to the field "pk"
        #Returns the object found or an exception "Http404" in case the object was not found
        try:
            return model.objects.get(pk=pk)

        except ArticleModel.DoesNotExist:
            raise Http404


    def get(self, request,pk):
        #Receives a request and a primary key
        #Searches the object whose primary key is equal to the field "pk" and serialize it as a JSON
        # Returns a JSON of the object found
        article = self.get_object(pk, ArticleModel)
        serialized = ArticleSerializer(article)
        return Response(serialized.data, status=status.HTTP_200_OK)
    
    