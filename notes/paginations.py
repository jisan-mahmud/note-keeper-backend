from rest_framework.pagination import PageNumberPagination
from urllib.parse import urlparse, parse_qs

class NotePagination(PageNumberPagination):
    page_size = 10

    def get_next_link(self):
        next_link = super().get_next_link()
        if next_link:
            parsed_url = urlparse(next_link)
            query_params = parse_qs(parsed_url.query)
            return query_params.get("page", [None])[0]  
        return None 

    def get_previous_link(self):
        prev_link = super().get_previous_link()
        if prev_link:
            parsed_url = urlparse(prev_link)
            query_params = parse_qs(parsed_url.query)
            return query_params.get("page", [None])[0]  
        return None 