from rest_framework import serializers
import shutil
from rest_framework.response import Response
from .models import *


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Files
        fields = "__all__"


class FileListSerializer(serializers.Serializer):
    files = serializers.ListField(
        child=serializers.FileField(
            max_length=1000000, allow_empty_file=False, use_url=False
        )
    )

    def zip_files(self, folder):

        shutil.make_archive(
            f"public/media/zip/{folder}", "zip", f"public/media/{folder}"
        )

    def create(self, validated_data):
        folder = Folder.objects.create()
        files = validated_data.pop("files")
        files_obj = []
        for file in files:
            file_obj = Files.objects.create(folder=folder, file=file)
            files_obj.append(file_obj)

        self.zip_files(folder.uid)
        return {"files": {}, "folder": str(folder.uid)}


class TextdataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Textdata
        fields = ["id", "text", "created_at", "set_duration"]


class PublicTextSerializer(serializers.ModelSerializer):
    text = TextdataSerializer()

    class Meta:
        model = PublicText
        fields = ["id", "text"]

    def create(self, validated_data):
        text_data = validated_data.pop("text")

        text_instance = Textdata.objects.create(**text_data)
        public_data_instance = PublicText.objects.create(
            text=text_instance, **validated_data
        )
        return public_data_instance


from rest_framework import serializers
import shutil
from .models import PublicFiles, Files, Folder
import os


class PublicFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicFiles
        fields = ["id", "files"]


class PublicFilesSerializer(serializers.ModelSerializer):
    files = serializers.ListField(
        child=serializers.FileField(
            max_length=1000000, allow_empty_file=False, use_url=False
        )
    )

    class Meta:
        model = PublicFiles
        fields = ["id", "files"]

    def zip_files(self, folder_uid):
        # Ensure the folder path exists
        folder_path = f"public/media/{folder_uid}"
        zip_path = f"public/media/zip/{folder_uid}"

        if os.path.exists(folder_path):
            shutil.make_archive(zip_path, "zip", folder_path)
        else:
            raise FileNotFoundError(f"Folder {folder_path} does not exist.")

    def create(self, validated_data):
        files = validated_data.pop("files")

        # Create a new folder instance
        folder = Folder.objects.create()
        files_obj = []
        for file in files:
            file_obj = Files.objects.create(folder=folder, file=file)
            files_obj.append(file_obj)
        # Create a zip archive of the folder
        self.zip_files(folder.uid)

        # Create PublicFiles instance
        public_files_instance = PublicFiles.objects.create(files=folder)
        return public_files_instance


class PrivateTextSerializer(serializers.ModelSerializer):
    text = TextdataSerializer()

    class Meta:
        model = PrivateText
        fields = ["id", "text", "token"]

    def create(self, validated_data):
        text_data = validated_data.pop("text")

        text_instance = Textdata.objects.create(**text_data)
        private_data_instance = PrivateText.objects.create(text=text_instance)
        return private_data_instance


class PrivateFilesSerializer(serializers.ModelSerializer):
    files = serializers.ListField(
        child=serializers.FileField(
            max_length=1000000, allow_empty_file=False, use_url=False
        )
    )

    class Meta:
        model = PrivateFiles
        fields = ["id", "files", "token"]

    def zip_files(self, folder_uid):
        # Ensure the folder path exists
        folder_path = f"public/media/{folder_uid}"
        zip_path = f"public/media/zip/{folder_uid}"

        if os.path.exists(folder_path):
            shutil.make_archive(zip_path, "zip", folder_path)
        else:
            raise FileNotFoundError(f"Folder {folder_path} does not exist.")

    def create(self, validated_data):
        files = validated_data.pop("files")

        # Create a new folder instance
        folder = Folder.objects.create()
        files_obj = []
        for file in files:
            file_obj = Files.objects.create(folder=folder, file=file)
            files_obj.append(file_obj)
        # Create a zip archive of the folder
        self.zip_files(folder.uid)

        # Create PublicFiles instance
        public_files_instance = PrivateFiles.objects.create(files=folder)
        return public_files_instance


class PrivateFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrivateFiles
        fields = ["id", "files", "token"]
