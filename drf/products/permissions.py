from rest_framework import permissions


class IsStaffEditorPermission(permissions.DjangoModelPermissions):
    # This basically just maps the HTTP methods to the permission name as
    # we can see on django admin menu under a given user.
    perms_map = {
        "GET": ["%(app_label)s.view_%(model_name)s"],
        "OPTIONS": [],
        "HEAD": [],
        "POST": ["%(app_label)s.add_%(model_name)s"],
        "PUT": ["%(app_label)s.change_%(model_name)s"],
        "PATCH": ["%(app_label)s.change_%(model_name)s"],
        "DELETE": ["%(app_label)s.delete_%(model_name)s"],
    }

    def has_permission(self, request, view):
        # if request.user.username == "staff":
        #     return False
        return super().has_permission(request, view)

    # def has_permission(self, request, view):
    #     user = request.user
    #     print(user)
    #     print(user.get_all_permissions())
    #     if user.is_staff:
    #         if user.has_perm("products.view_product"):  # app.verb_modelname
    #             return True
    #         if user.has_perm("products.add_product"):
    #             return False
    #         if user.has_perm("products.delete_product"):
    #             return False
    #         if user.has_perm("products.change_product"):
    #             return False
    #         return False
    #     return False
