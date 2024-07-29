from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework import status


class FileListView(APIView):
    def get(self, request):
        files = Files.objects.all()
        serializer = FileSerializer(files, many=True)
        return Response({"status": "success", "data": serializer.data})


class HandlePublicText(APIView):

    def get(self, request):
        text = PublicText.objects.all()
        serializer = PublicTextSerializer(text, many=True)
        return Response({"status": "success", "data": serializer.data})

    def post(self, request):
        try:
            data = request.data
            serializer = PublicTextSerializer(data=data)
            if serializer.is_valid():
                result = serializer.save()
                result_serializer = PublicTextSerializer(result)
                return Response(
                    {
                        "status": status.HTTP_200_OK,
                        "message": "Text uploaded successfully",
                        "data": result_serializer.data,
                    },
                    status=status.HTTP_200_OK,
                )

            return Response(
                {
                    "status": status.HTTP_400_BAD_REQUEST,
                    "message": "Text upload failed",
                    "data": serializer.errors,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        except Exception as e:
            print(e)
            return Response(
                {
                    "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
                    "message": "An error occurred",
                    "error": str(e),
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class HandlePrivateText(APIView):

    def get(self, request, id):
        try:
            text = PrivateText.objects.get(token=id)
            serializer = PrivateTextSerializer(text)
            return Response(
                {
                    "status": status.HTTP_200_OK,
                    "message": "Text fetched successfully",
                    "data": serializer.data,
                },
            )
        except Exception as e:
            print(e)
            return Response(
                {
                    "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
                    "message": "An error occurred",
                    "error": str(e),
                },
            )

    def post(self, request):
        try:
            data = request.data
            serializer = PrivateTextSerializer(data=data)
            if serializer.is_valid():
                result = serializer.save()
                result_serializer = PrivateTextSerializer(result)
                return Response(
                    {
                        "status": status.HTTP_200_OK,
                        "message": "Text uploaded successfully",
                        "data": result_serializer.data,
                    },
                )
            return Response(
                {
                    "status": status.HTTP_400_BAD_REQUEST,
                    "message": "Text upload failed",
                    "data": serializer.errors,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        except Exception as e:
            print(e)
            return Response(
                {
                    "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
                    "message": "An error occurred",
                    "error": str(e),
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class HandlePrivateFiles(APIView):

    def get(self, request, id):
        try:
            private_file = PrivateFiles.objects.get(token=id)
            serializer = PrivateFileSerializer()
            return Response(
                {
                    "status": status.HTTP_200_OK,
                    "message": "File retrieved successfully",
                    "data": serializer.data,
                },
            )
        except Exception as e:
            return Response(
                {
                    "status": status.HTTP_404_NOT_FOUND,
                    "message": "File not found",
                    "error": str(e),
                },
            )

    def post(self, request):
        try:
            data = request.data
            serializer = PrivateFilesSerializer(data=data)
            if serializer.is_valid():
                result = serializer.save()
                result_serializer = PrivateFileSerializer(result)
                return Response(
                    {
                        "status": status.HTTP_200_OK,
                        "message": "Files uploaded successfully",
                        "data": result_serializer.data,
                    },
                )
            return Response(
                {
                    "status": status.HTTP_400_BAD_REQUEST,
                    "message": "Files upload failed",
                    "data": serializer.errors,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        except Exception as e:

            return Response(
                {
                    "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
                    "message": "An error occurred",
                    "error": str(e),
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class HandlePublicFiles(APIView):
    def get(self, request):
        try:
            files = PublicFiles.objects.all()
            serializer = PublicFileSerializer(files, many=True)
            return Response(
                {
                    "status": status.HTTP_200_OK,
                    "message": "Files retrieved successfully",
                    "data": serializer.data,
                },
            )
        except Exception as e:
            print(e)
            return Response(
                {
                    "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
                    "message": "An error occurred",
                    "error": str(e),
                },
            )

    def post(self, request):
        try:
            data = request.data
            serializer = PublicFilesSerializer(data=data)
            if serializer.is_valid():
                result = serializer.save()
                result_serializer = PublicFileSerializer(result)
                return Response(
                    {
                        "status": status.HTTP_200_OK,
                        "message": "Files uploaded successfully",
                        "data": result_serializer.data,
                    },
                )
            return Response(
                {
                    "status": status.HTTP_400_BAD_REQUEST,
                    "message": "Files upload failed",
                    "data": serializer.errors,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        except Exception as e:
            print(e)
            return Response(
                {
                    "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
                    "message": "An error occurred",
                    "error": str(e),
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
