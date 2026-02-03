from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission): #must inherit the BasePermission class
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user
#is the owner of the fundraiser the same as the user who is making this request? if yes, allow 


#WRITE ALL YOUR PERMISSION CLASSES HERE THEN REFER TO IN THE VIEW FILE
#example
#class CustomPermissionCheck(permission.BasePermission): EVERY CLASS YOU CREATE MUST INHERIT BASEPERMISSION CLASS
    #def has_object_permission (self, request, view, obj):
        #.....

class IsSupporterOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.supporter == request.user
    
    