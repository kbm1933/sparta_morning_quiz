from rest_framework.response import Response
from rest_framework.decorators import api_view
from articles.serializers import ArticleSerializer
from articles.models import Article

# Create your views here.
@api_view(['GET','POST'])
def index(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles,many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = ArticleSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)
        return Response(serializer)