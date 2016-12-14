from rest_framework import permissions

#if there is a user associated with the current request,
#check if that user is the same object as account
#this class, by virtue of inheriting from BasePermission,
#seems to be callable, hence its use in views
class IsAccountOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, account):
        if request.user:
            return account == request.user
        return False