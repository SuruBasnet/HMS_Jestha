from rest_framework.permissions import BasePermission

class FrontDeskUserPermission(BasePermission):

    def has_permission(self, request,view):
        if request.user.user_type == 'Frontdesk':
            return True