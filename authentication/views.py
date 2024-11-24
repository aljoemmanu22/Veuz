from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from .serializers import RegisterSerializer


class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  

class LoginView(APIView):
  def post(self, request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not User.objects.filter(username=username).exists():
      return Response({'error': 'Username not exists'}, status=status.HTTP_400_BAD_REQUEST)
    
    user = authenticate(username=username, password=password)

    if not user:
      return Response({'error': 'invalid password'}, status=status.HTTP_401_UNAUTHORIZED)
    
    refresh = RefreshToken.for_user(user)
    return Response({
      'refresh': str(refresh),
      'access': str(refresh.access_token),
    })

class ProfileView(APIView):
  permission_classes = [IsAuthenticated]

  def get(self, request):
    user = request.user
    return Response({'username': user.username, 'email': user.email})

from .models import Profile
from .serializers import ProfileSerializer

class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        profile = user.profile  # OneToOne relation
        profile_data = ProfileSerializer(profile).data
        return Response({
            'username': user.username,
            'email': user.email,
            'profile': profile_data
        })

    def put(self, request):
        user = request.user
        data = request.data
        profile = user.profile

        # Update user info
        user.username = data.get("username", user.username)
        user.email = data.get("email", user.email)
        user.save()

        # Update profile info
        profile_serializer = ProfileSerializer(profile, data=data.get("profile", {}), partial=True)
        if profile_serializer.is_valid():
            profile_serializer.save()
        else:
            return Response(profile_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response({'message': 'Profile updated successfully'})



class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        user = request.user
        old_password = request.data.get('old_password')
        new_password = request.data.get('new_password')
        confirm_password = request.data.get('confirm_password')

        if not user.check_password(old_password):
            return Response({'error': 'Old password is incorrect'}, status=status.HTTP_400_BAD_REQUEST)

        if new_password != confirm_password:
            return Response({'error': "Passwords don't match"}, status=status.HTTP_400_BAD_REQUEST)

        user.set_password(new_password)
        user.save()
        return Response({'message': 'Password changed successfully'}, status=status.HTTP_200_OK)
