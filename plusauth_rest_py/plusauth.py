from .apis import ApiService
from .clients import ClientService
from .connections import ConnectionService
from .permissions import PermissionServise
from .rolegroups import RoleGroupsService
from .roles import RoleService
from .tenants import TenantsService
from .users import UsersService
from .views import ViewsService

class plusauth():
    """
    Provides easy access to all endpoint classes.
    """

    def __init__(self):
        self.ApiService = ApiService()
        self.ClientService = ClientService()
        self.ConnectionService = ConnectionService()
        self.PermissionServise = PermissionServise()
        self.RoleGroupsService = RoleGroupsService()
        self.RoleService = RoleService()
        self.TenantsService = TenantsService()
        self.UsersService = UsersService()
        self.ViewsService = ViewsService()



