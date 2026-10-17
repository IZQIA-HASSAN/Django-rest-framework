from rest_framework.pagination import CursorPagination

class cursorpagination(CursorPagination):
    page_size = 10
    ordering = 'name'
    cursor_query_param = 'cu'


    