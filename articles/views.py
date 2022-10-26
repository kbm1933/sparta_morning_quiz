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
        serializer = ArticleSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            print(serializer.errors)
            #개발할땐 상관 없지만 보안상의 이유로 서비스할 때는 비추
            return Response(serializer.errors) 
        