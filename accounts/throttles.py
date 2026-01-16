from rest_framework.throttling import AnonRateThrottle, UserRateThrottle

class AuthRateThrottle(AnonRateThrottle):
    scope = 'auth'
    
    def get_cache_key(self, request, view):
        if request.user.is_authenticated:
            return None  # Only throttle unauthenticated requests
            
        return self.cache_format % {
            'scope': self.scope,
            'ident': self.get_ident(request)
        }

class RegisterThrottle(AuthRateThrottle):
    rate = '5/hour'
    
class LoginThrottle(AuthRateThrottle):
    rate = '10/hour'
