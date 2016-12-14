from rest_framework import permissions, viewsets

from authentication.models import Account
from authentication.permissions import IsAccountOwner
from authentication.serializers import AccountSerializer

#authentication API endpoint for accounts,
#inherits from ModelViewSet, a set of views for
#listing, creating, retrieving, updating, and destroyinh
#objects of a given model
class AccountViewSet(viewsets.ModelViewSet):
    lookup_field = 'username' #overrides id for lookup in database
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    #HTTP requests of a type deemed safe by permissions
    #and POST (because any should be able to create accounts)
    #are let through, otherwise, only let them through if this is
    #the account owner and they are logged in
    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (permissions.AllowAny(),)

        return (permissions.IsAuthenticated(), IsAccountOwner(),)

    #overwrite the viewset's create method to user the Account model;s
    #create_user() method so that password is hashed. WARNING : a serializer's
    #save() method saves attributes (including passwords) IN PLAIN TEXT
    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            Account.objects.create_user(**serializer.validated_data)

            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)

        return Response({
            'status': 'Bad request',
            'message': 'Account could not be created with received data.'
        }, status=status.HTTP_400_BAD_REQUEST)