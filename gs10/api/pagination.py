from rest_framework.pagination import LimitOffsetPagination

class myoffsetpagination(LimitOffsetPagination):
    # attributes for liitoffset pagination 
    # every pagination technique has different attributes 
    # default_limit = 2
    limit_query_param = 'mylist'
    offset_query_param = "myoff "
    max_limit = 6

    