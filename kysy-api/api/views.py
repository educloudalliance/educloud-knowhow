from rest_framework import renderers
from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from serializers import UserSerializer, PostSerializer
from models import QaUsers, QaPosts

@api_view(['GET'])
def api_root(request, format=None):
    """
    QA API root
    """
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'questions': reverse('question-list', request=request, format=format),
    })

class QuestionList(APIView):
    """
    List 10 latest feature requests.
    """
    def get(self, request, format=None):
        posts = QaPosts.objects.filter(categoryid__title='Ominaisuustoive').filter(type='Q').order_by('postid').reverse()[:10]
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def user_list(request):
    """
    List all users
    """
    if request.method == 'GET':
        users = QaUsers.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def post_list(request):
    """
    List 10 latest feature requests.
    """
    if request.method == 'GET':
        posts = QaPosts.objects.filter(categoryid__title='Ominaisuustoive').filter(type='Q').order_by('postid').reverse()[:10]
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
