from rest_framework.throttling import UserRateThrottle

class rate(UserRateThrottle):
    scope = 'rate'