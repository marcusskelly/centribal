from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from src.orders.infrastructure.api.serializers import OrderSerializer
from src.orders.infrastructure.repositories.order_repository import ORMOrderRepository
from src.articles.infrastructure.repositories.article_repository import ORMArticleRepository
from src.orders.application.use_cases.create_order import CreateOrderUseCase
from src.orders.application.use_cases.update_order import UpdateOrderUseCase
from src.orders.application.use_cases.get_order import GetOrderUseCase
from src.orders.application.use_cases.list_orders import ListOrdersUseCase


class OrderListCreateView(APIView):

    def get(self, request):

        repository = ORMOrderRepository()
        use_case = ListOrdersUseCase(repository)

        orders = use_case.execute()

        serializer = OrderSerializer(orders, many=True)

        return Response(serializer.data)

    def post(self, request):

        serializer = OrderSerializer(data=request.data)

        if serializer.is_valid():

            order_repository = ORMOrderRepository()
            article_repository = ORMArticleRepository()

            use_case = CreateOrderUseCase(order_repository, article_repository)

            order = use_case.execute(serializer.validated_data["items"])

            response_serializer = OrderSerializer(order)

            return Response(response_serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderDetailView(APIView):

    def get(self, request, order_id):

        repository = ORMOrderRepository()
        use_case = GetOrderUseCase(repository)

        order = use_case.execute(order_id)

        serializer = OrderSerializer(order)

        return Response(serializer.data)

    def put(self, request, order_id):

        serializer = OrderSerializer(data=request.data)

        if serializer.is_valid():

            order_repository = ORMOrderRepository()
            article_repository = ORMArticleRepository()

            use_case = UpdateOrderUseCase(order_repository, article_repository)

            order = use_case.execute(order_id, serializer.validated_data["items"])

            response_serializer = OrderSerializer(order)

            return Response(response_serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)