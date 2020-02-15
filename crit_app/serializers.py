from rest_framework import serializers
from .models import Member, Party


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('pk', 'party', 'name', 'race', 'dndclass', 'icon', 'theme', 'specialty', 'title', 'interests', 'bio',  )

class PartySerializer(serializers.ModelSerializer):
    m = MemberSerializer(many=True, read_only=True)
    class Meta:
        model = Party
        fields = ('pk', 'title', 'who', 'what', 'why', 'm')