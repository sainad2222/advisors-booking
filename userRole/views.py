from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import User, Booking
from .serializers import UserSerializer, BookingSerializer
from adminRole.serializers import AdvisorSerializer
from adminRole.models import Advisor

import hashlib, binascii, os

# helper functions to encrypt, verify password fields
def hash_password(password):
    """Hash a password for storing."""
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode("ascii")
    pwdhash = hashlib.pbkdf2_hmac("sha512", password.encode("utf-8"), salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode("ascii")


def verify_password(stored_password, provided_password):
    """Verify a stored password against one provided by user"""
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac(
        "sha512", provided_password.encode("utf-8"), salt.encode("ascii"), 100000
    )
    pwdhash = binascii.hexlify(pwdhash).decode("ascii")
    return pwdhash == stored_password


"""
request:
    name: String
    email: Email
    password: String
response:
    user_id: UserId
"""


class RegisterClassView(APIView):
    def post(self, request):
        try:
            name = request.data["name"]
            email = request.data["email"]
            password = request.data["password"]
            hashed_password = hash_password(password)
            updatedData = {"name": name, "email": email, "password": hashed_password}
            serialized_data = UserSerializer(data=updatedData)
            if not serialized_data.is_valid():
                return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
            user = serialized_data.save()
            return Response({"user_id": user.id}, status=status.HTTP_201_CREATED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


"""
request:
    email: Email
    password: String
response:
    user_id: UserId
"""


class LoginClassView(APIView):
    def post(self, request):
        try:
            user = User.objects.all().filter(email=request.data["email"])[0]
            provided_password = request.data["password"]
            if not verify_password(user.password, provided_password):
                return Response(status=status.HTTP_401_UNAUTHORIZED)
            return Response({"user_id": user.id}, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


"""
request:
    None
response:
    List of Advisors
"""


class ListAdvisorsView(APIView):
    def get(self, request, id):
        advisors = Advisor.objects.all()
        serialized_data = AdvisorSerializer(advisors, many=True)
        return Response(serialized_data.data, status=status.HTTP_200_OK)


"""
request:
    datetime: DateTime in format %d-%m-%YT%H:%M:%S
              example:  10-05-2021:16:41:46
response:
    None
"""


class BookAdvisorView(APIView):
    def post(self, request, user_id, advisor_id):
        try:
            serialized_data = BookingSerializer(
                data={
                    "user": user_id,
                    "advisor": advisor_id,
                    "datetime": request.data["datetime"],
                }
            )
            if not serialized_data.is_valid():
                return Response(
                    serialized_data.errors, status=status.HTTP_400_BAD_REQUEST
                )
            serialized_data.save()
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)


"""
request:
    None
response:
    booking_id: BookingId
    booking_time: DateTime
    advisor_id: AdvisorId
    advisor_name: AdvisorName
    advisor_profile_url: AdvisorProfile_URL
"""


class ListBookingsView(APIView):
    def get(self, request, user_id):
        try:
            booking = Booking.objects.all().filter(user=user_id)
            serialized_data = BookingSerializer(booking, many=True)
            response = []
            for obj in serialized_data.data:
                advisor = Advisor.objects.all().filter(id=obj["advisor"])[0]
                newObj = {
                    "booking_id": obj["id"],
                    "booking_time": obj["datetime"],
                    "advisor_id": advisor.id,
                    "advisor_name": advisor.name,
                    "advisor_profile_url": advisor.profile_url,
                }
                response.append(newObj)

            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)
