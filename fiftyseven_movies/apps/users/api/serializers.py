from rest_framework import serializers

from apps.users.models import User

import re


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'password']
    
    def validate_password(self, value):
        if len(value) < 10:
            raise serializers.ValidationError("The password must have at least 10 characters")
        
        if not re.findall('[A-Z]', value):
            raise serializers.ValidationError("The password must have at least one uppercase letter.")
        
        if not re.findall('[a-z]', value):
            raise serializers.ValidationError("The password must have at least one lowercase letter.")
        
        re_special = re.compile('[@_!#$%^&*()<>?/\|}{~:]') 
        if re_special.search(value) == None:
            raise serializers.ValidationError("The password must have at least one special character.")
        
    
    def create(self,validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    def update(self, instance, validated_data):
        print(validated_data)
        updated_user = super().update(instance, validated_data)
        updated_user.set_password(validated_data['password'])
        updated_user.save()
        return updated_user

