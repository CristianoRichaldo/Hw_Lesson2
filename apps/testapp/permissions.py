from rest_framework.permissions import BasePermission


class IsAdminOnly(BasePermission):
 def has_permission(self, request, view):
    if not request.user or not request.user.is_authenticated:
      return False
    return request.user.role == request.user.Role.ADMIN


class IsUserOnly(BasePermission):
  def has_permission(self, request, view):
    if not request.user or not request.user.is_authenticated:
      return False
 
    target_role = getattr(
        request.user.Role, 'CLIENT', getattr(request.user.Role, 'USER', 'user')
    )
    return request.user.role == target_role
  