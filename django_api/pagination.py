from rest_framework.pagination import PageNumberPagination

class ProductPagination(PageNumberPagination):
    page_size = 2
    page_query_params = 'page'
    page_size_query_params = 'size'
    max_page_size = 4