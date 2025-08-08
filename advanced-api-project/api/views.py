from django.http import JsonResponse
from django.views.generic import ListView, UpdateView, DeleteView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer
import json

@method_decorator(csrf_exempt, name='dispatch')
class AuthorListView(ListView):
    model = Author

    def get(self, request, *args, **kwargs):
        authors = list(Author.objects.all())
        serializer = AuthorSerializer(authors, many=True)
        return JsonResponse(serializer.data, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class UpdateView(UpdateView):
    model = Author
    fields = ['name']

    def post(self, request, *args, **kwargs):
        author = self.get_object()
        data = json.loads(request.body)
        author.name = data.get('name', author.name)
        author.save()
        return JsonResponse({'message': 'Author updated successfully'})


@method_decorator(csrf_exempt, name='dispatch')
class DeleteView(DeleteView):
    model = Author

    def delete(self, request, *args, **kwargs):
        author = self.get_object()
        author.delete()
        return JsonResponse({'message': 'Author deleted successfully'})

