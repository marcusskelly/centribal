from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema
from src.articles.infrastructure.api.serializers import ArticleSerializer
from src.articles.infrastructure.repositories.article_repository import ORMArticleRepository
from src.articles.application.use_cases.create_article import CreateArticleUseCase
from src.articles.application.use_cases.update_article import UpdateArticleUseCase
from src.articles.application.use_cases.get_article import GetArticleUseCase
from src.articles.application.use_cases.list_articles import ListArticlesUseCase


class ArticleListCreateView(APIView):

    @extend_schema(
        responses=ArticleSerializer(many=True),
        description="List all articles"
    )
    def get(self, request):

        repository = ORMArticleRepository()
        use_case = ListArticlesUseCase(repository)

        articles = use_case.execute()

        serializer = ArticleSerializer(articles, many=True)

        return Response(serializer.data)


    @extend_schema(
        request=ArticleSerializer,
        responses=ArticleSerializer,
        description="Create a new article"
    )
    def post(self, request):

        repository = ORMArticleRepository()
        use_case = CreateArticleUseCase(repository)

        serializer = ArticleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        article = use_case.execute(**serializer.validated_data)

        return Response(ArticleSerializer(article).data)


class ArticleDetailView(APIView):

    def get(self, request, article_id):

        repository = ORMArticleRepository()
        use_case = GetArticleUseCase(repository)

        article = use_case.execute(article_id)

        serializer = ArticleSerializer(article)

        return Response(serializer.data)

    def put(self, request, article_id):

        serializer = ArticleSerializer(data=request.data)

        if serializer.is_valid():

            repository = ORMArticleRepository()
            use_case = UpdateArticleUseCase(repository)

            article = use_case.execute(article_id, **serializer.validated_data)

            response_serializer = ArticleSerializer(article)

            return Response(response_serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)