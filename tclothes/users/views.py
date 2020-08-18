"""Users views."""

# Django REST Framework
from rest_framework.decorators import action
from rest_framework import status, viewsets, mixins
from rest_framework.response import Response

# Models
from tclothes.users.models import User

# Serializer
from tclothes.users.serializers import (
    UserLoginSerializer,
    UserModelSerializer,
    UserSignUpSerializer
)

# Permissions
from rest_framework.permissions import AllowAny, IsAuthenticated
from tclothes.users.permissions import IsAccountOwner


class UserViewSet(viewsets.GenericViewSet,
                  mixins.RetrieveModelMixin):
    """Users view set.
    Handle users login account.
    """

    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    lookup_field = 'username'

    def get_permissions(self):
        """Assign permissions based on action."""
        if self.action in ['signup', 'login', 'verify']:
            permissions = [AllowAny]
        elif self.action in ['retrieve']:
            permissions = [IsAuthenticated, IsAccountOwner]
        else:
            permissions = [IsAuthenticated]
        return [p() for p in permissions]

    @action(detail=False, methods=['post'])
    def login(self, request):
        """User Login."""
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {
            'user': UserModelSerializer(user).data,
            'token': token
        }
        return Response(data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'])
    def signup(self, request):
        """User sign up."""
        serializer = UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UserModelSerializer(user).data
        return Response(data, status=status.HTTP_201_CREATED)
