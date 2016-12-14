from django.contrib.auth import update_session_auth_hash

from rest_framework import serializers

from authentication.models import Account


class AccountSerializer(serializers.ModelSerializer):
    #handled separately from fields to have write_only=True, no visibility
    #client side
    password = serializers.CharField(write_only=True, required=False)
    confirm_password = serializers.CharField(write_only=True, required=False)

    #metadata to be serialized
    class Meta:
        model = Account
        #avoid stuff like is_admin or is_superuser here for security
        fields = ('id', 'email', 'username', 'created_at', 'updated_at',
                  'first_name', 'last_name', 'tagline', 'password',
                  'confirm_password',)
        read_only_fields = ('created_at', 'updated_at',)

        #deserialization back to server side on new objects
        def create(self, validated_data):
            return Account.objects.create(**validated_data)

        #deserialization back to server side on updating existing objects
        def update(self, instance, validated_data):
            instance.username = validated_data.get('username', instance.username)
            instance.tagline = validated_data.get('tagline', instance.tagline)

            instance.save()

            password = validated_data.get('password', None)
            confirm_password = validated_data.get('confirm_password', None)

            #this is a naive implementation of password validation, research
            #something else for production
            if password and confirm_password and password == confirm_password:
                instance.set_password(password)
                instance.save()

            #explicit session authentication hash update with new password (if changed)
            #without this, user will have to relogin with their new password
            update_session_auth_hash(self.context.get('request'), instance)

            return instance