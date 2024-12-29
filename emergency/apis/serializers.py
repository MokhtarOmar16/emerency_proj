from rest_framework import serializers
from ..models import Emergency, EmergencyImage


class EmergencyImageSerializer(serializers.ModelSerializer):
    """
    Serializer for the EmergencyImage model.
    """
    class Meta:
        model = EmergencyImage
        fields = ['id', 'image']


class MinimalEmergencySerializer(serializers.ModelSerializer):
    """
    Returns only:
    - id
    - emergency_type
    - description
    - image (the first image, if any)
    """
    image = serializers.SerializerMethodField()

    class Meta:
        model = Emergency
        fields = ['id', 'emergency_type', 'description', 'image'] # name , location. time 

    def get_image(self, obj):
        """
        Return the URL of the first image associated with this Emergency, or None if no images exist.
        """
        return first_image.image.url if (first_image := obj.images.first()) else None


class EmergencyDetailSerializer(serializers.ModelSerializer):
    """
    Returns the full details of an Emergency:
    - All images
    - user first/last name
    - lat, lgt, etc.
    """
    images = EmergencyImageSerializer(many=True, read_only=True)
    user_first_name = serializers.ReadOnlyField(source='user.first_name')
    user_last_name = serializers.ReadOnlyField(source='user.last_name')

    class Meta:
        model = Emergency
        fields = [
            'id',
            'emergency_type',
            'description',
            'created_at',
            'lat',
            'lgt',
            'user_first_name',
            'user_last_name',
            'images',
        ]


class CreateEmergencySerializer(serializers.ModelSerializer):
    """
    For POST endpoint. Expects:
    - emergency_type
    - description
    - lat
    - lgt
    - images (list of file uploads, optional)
    (User is set automatically in the view, not posted by the client)
    """
    images = serializers.ListField(
        child=serializers.ImageField(),
        write_only=True,
        required=False
    )

    class Meta:
        model = Emergency
        fields = [
            'emergency_type',
            'description',
            'lat',
            'lgt',
            'images',
        ]

    def create(self, validated_data):
        images_data = validated_data.pop('images', [])
        # We'll set user in the view's perform_create
        emergency = Emergency.objects.create(**validated_data)
        for image_file in images_data:
            EmergencyImage.objects.create(emergency=emergency, image=image_file)
        return emergency
