import time
from django.http import HttpResponseForbidden

class LogRequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # process before when browser sends request - before reaching url patterns.
        print(f"[Middleware] Request Path: {request.path}") 

        # process after vies sends back response - after view before web server response.
        response = self.get_response(request)
        print(f"[Middleware] Response Status: {response.status_code}")
        return response

class TimerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start = time.time()
        response = self.get_response(request)
        duration = time.time() - start
        print(f"[Middleware] Request took {duration:.2f} seconds")
        return response
    

class BlockIPMiddleware:
    BLOCKED_IPS = []
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        ip = request.META.get("REMOTE_ADDR")
        if ip in self.BLOCKED_IPS:
            return HttpResponseForbidden("Your IP is blocked")

        return self.get_response(request)
