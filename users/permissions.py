from rest_framework import permissions
from rest_framework.views import APIView, Response, Request, status


class UserPermission(permissions.BasePermission):
  def has_permission(self, request: Request, view):
    path_request = str(request.get_full_path()) 

    index = path_request.find(str(request.user.id))

    if not bool(request.user and request.user.is_authenticated):
      return False
    
    if request.user.is_employee:
      return True
    
    if index != -1:
      return True
    
    if not request.user.is_employee:
      return False