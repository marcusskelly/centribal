from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from src.articles.infrastructure.api.serializers import ArticleSerializer
from src.articles.infrastructure.repositories.article_repository import ORMArticleRepository
from src.articles.application.use_cases.create_article import CreateArticleUseCase
from src.articles.application.use_cases.update_article import UpdateArticleUseCase
from src.articles.application.use_cases.get_article import GetArticleUseCase
from src.articles.application.use_cases.list_articles import ListArticlesUseCase


class ArticleListCreateView(APIView):

    def get(self, request):

        repository = ORMArticleRepository()
        use_case = ListArticlesUseCase(repository)

        articles = use_case.execute()

        serializer = ArticleSerializer(articles, many=True)

        return Response(serializer.data)

    def post(self, request):

        serializer = ArticleSerializer(data=request.data)

        if serializer.is_valid():

            repository = ORMArticleRepository()
            use_case = CreateArticleUseCase(repository)

            article = use_case.execute(**serializer.validated_data)

            response_serializer = ArticleSerializer(article)

            return Response(response_serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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