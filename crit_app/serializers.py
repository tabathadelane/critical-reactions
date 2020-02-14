from rest_framework import serializers
from .models import Member, Party

class PartySerializer(serializers.ModelSerializer):
    class Meta:
        model = Party
        fields = ('pk', 'title', 'who', 'what', 'why', )
        
class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('pk', 'p', 'name', 'race', 'dndclass', 'specialty', 'title', 'interests', 'bio',  )