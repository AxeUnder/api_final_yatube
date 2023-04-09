import base64

from django.core.files.base import ContentFile

from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator


from posts.models import Comment, Post, Group, Follow, User


class Base64ImageField(serializers.ImageField):
    """Serializer поля image."""
    def to_internal_value(self, data):
        if isinstance(data, str) and data.startswith('data:image'):
            img_format, img_str = data.split(';base64,')
            ext = img_format.split('/')[-1]
            data = ContentFile(base64.b64decode(img_str), name='img.' + ext)

        return super().to_internal_value(data)


class PostSerializer(serializers.ModelSerializer):
    """Serializer модели Post."""
    author = SlugRelatedField(slug_field='username', read_only=True)
    image = Base64ImageField(required=False, allow_null=True)

    class Meta:
        fields = '__all__'
        model = Post
        read_only_fields = ('pub_date',)


class CommentSerializer(serializers.ModelSerializer):
    """Serializer модели Comment."""
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Comment
        read_only_fields = ('post', 'created')


class GroupSerializer(serializers.ModelSerializer):
    """Serializer модели Group."""
    class Meta:
        fields = '__all__'
        model = Group


class FollowSerializer(serializers.ModelSerializer):
    """Serializer модели Follow."""
    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        default=serializers.CurrentUserDefault()
    )
    following = serializers.SlugRelatedField(
        slug_field='username', queryset=User.objects.all()
    )

    class Meta:
        fields = '__all__'
        model = Follow
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following')
            )
        ]

    def validate_following(self, value):
        user = self.context['request'].user
        if value == user:
            raise serializers.ValidationError('Нельзя подписываться на себя.')
        return value
