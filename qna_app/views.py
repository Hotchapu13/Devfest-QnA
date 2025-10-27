from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from .models import User
from .serializers import AudienceRegistrationSerializer
from rest_framework.permissions import IsAuthenticated

class AudienceRegistrationView(APIView):
    """
    Handles passwordless registration of audience members
    Takes a nickname, creates a user and issues a token
    """

    # Anyone can access this view
    permission_classes = []

    def post(self, request):
        serializer = AudienceRegistrationSerializer(data=request.data)

        if serializer.is_valid():
            nickname = serializer.validated_data['nickname']

            # create passwordless user using the nickname as username
            user = User.objects.create(
                username=nickname,
                display_name=nickname,
                is_speaker=False
            )

            token, created = Token.objects.get_or_create(user=user)

            return Response({
                'token': token.key,
                'nickname': user.display_name
            }, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        

class LogoutView(APIView):
    """
    Delete the auth token for authenticated user, thus logging them out
    Works for both speakers and audience members
    """

    # Require only logged in users to access this view
    permission_classes = [IsAuthenticated] 

    def post(self, request):
        if request.auth:
            request.auth.delete()
            return Response(
                {"detail: Successfully Logged Out."},
                status = status.HTTP_200_OK
            )

        return Response(
            {"No active token found for user."},
            status=status.HTTP_400_BAD_REQUEST
        )