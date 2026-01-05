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
