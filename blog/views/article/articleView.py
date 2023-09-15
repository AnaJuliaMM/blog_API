#Importing the module APIView
from rest_framework.views import APIView
#Import the model and the serializer class
from blog.serializers.article import ArticleSerializer
from blog.models.article import ArticleModel
#Importando a resposta
from rest_framework.response import Response
#Import status
from rest_framework import status

class ArticleView(APIView):
    """ Create and get objects from Article Table"""

    def post(self, request):
        #Receives a request
        #Post an object in the table Article
        #Returns the object created
        data = request.data
        serializer = ArticleSerializer(data=data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        #Receives a request
        #Get all objects of the table Article
        #Returns the objects found as an list of JSON
        articles = ArticleModel.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
