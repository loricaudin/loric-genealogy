# Pour vercel
from loric_genealogy.wsgi import app

def handler(request, context):
    return app(request.environ, start_response=context["start_response"])
