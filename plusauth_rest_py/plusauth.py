from plusauth_rest_py.apis import ApiService
from plusauth_rest_py.clients import ClientService
from plusauth_rest_py.connections import ConnectionService
from plusauth_rest_py.permissions import PermissionServise
from plusauth_rest_py.rolegroups import RoleGroupsService
from plusauth_rest_py.roles import RoleService
from plusauth_rest_py.tenants import TenantsService
from plusauth_rest_py.users import UsersService
from plusauth_rest_py.views import ViewsService

class plusAuth():

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



