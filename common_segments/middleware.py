from django.shortcuts import redirect


class SitemapMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if request.path == '/sitemap.xml':
            response['Content-Type'] = 'application/xml; charset=UTF-8'
        return response


class URLMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = request.path
        if "/person/month_day_description/" in path:
            new_path = path.replace("month_day_description", "month-day-description")
            return redirect(new_path)

        response = self.get_response(request)
        return response
