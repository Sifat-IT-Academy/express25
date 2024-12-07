from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer, LoginSerializer, VerifyCodeSerializer,PhoneVerificationSerializer
from django.contrib.auth import login
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError
from django.core.cache import cache
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils import send_sms

class PhoneVerificationView(APIView):
    def post(self, request):
        serializer = PhoneVerificationSerializer(data=request.data)
        
        if serializer.is_valid():
            phone_number = serializer.validated_data['phone_number']
            
            # Tasdiqlash kodini yaratish va yuborish
            verification_code = send_sms(phone_number)
            
            # Tasdiqlash kodini cache-ga saqlash
            cache.set(phone_number, verification_code, timeout=300)  # 5 daqiqaga amal qiladi
            
            return Response({
                "message": "Verification code sent to your phone."
            }, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RegisterView(APIView):
    def post(self, request, *args, **kwargs):
        phone_number = request.data.get('phone_number')
        
        # Telefon raqami tasdiqlanganligini tekshirish
        if not cache.get(f"verified_{phone_number}"):
            return Response({"message": "Phone number not verified."}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            
            # Tasdiqlash holatini o'chirib tashlash
            cache.delete(f"verified_{phone_number}")
            
            return Response({"message": "User registered successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VerifyPhoneView(APIView):
    def post(self, request):
        serializer = VerifyCodeSerializer(data=request.data)
        
        if serializer.is_valid():
            phone_number = serializer.validated_data['phone_number']
            verification_code = serializer.validated_data['verification_code']
            
            # Cache'dan kodni olish
            cached_code = cache.get(phone_number)
            
            if cached_code and cached_code == verification_code:
                # Kod mos keldi
                cache.delete(phone_number)  # Kodni o'chirib tashlash
                
                # Tasdiqlash holatini saqlash
                cache.set(f"verified_{phone_number}", True, timeout=3600)  # 1 soat amal qiladi
                
                return Response({"message": "Phone number verified successfully."}, status=status.HTTP_200_OK)
            
            return Response({"message": "Invalid verification code."}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            login(request, user)
            
            # Generate JWT tokens
            refresh = RefreshToken.for_user(user)
            access_token = refresh.access_token
            
            return Response({
                "access_token": str(access_token),
                "refresh_token": str(refresh),
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    def post(self, request):
        # Refresh tokenni olish
        refresh_token = request.data.get('refresh_token')
        
        if not refresh_token:
            return Response({"detail": "Refresh token is required."}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            # Refresh tokenni tekshirish
            token = RefreshToken(refresh_token)
            
            # Tokenni bloklash
            token.blacklist()
            
            return Response({"message": "Logged out successfully."}, status=status.HTTP_200_OK)
        
        except TokenError as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)