import requests
from  plusauth_rest_py.base import  baseUrl
from plusauth_rest_py.bearer_token import bearerToken

base_url=baseUrl()

class UsersService():

    def getAll(self , token , page = '' , itemsPerPage = '' , sortBy = '' , sortDesc = '' ):
        """
            Args: \n
            token:str -> You must have the access token.\n
            page -> The number of records you wish to skip before selecting records \n
            itemsPerPage -> Limit the number of results returned \n
            sortBy -> Properties that should be ordered by \n
            sortDesc -> Descending or ascending or nothing \n

            Returns: List all Users

            Documentation: https://docs.plusauth.com/api/core/users/listUsers

        """
        headers = bearerToken(token)
        payload = {'page': page, 'itemsPerPage': itemsPerPage, 'sortBy': sortBy, 'sortDesc': sortDesc}
        res = requests.get(base_url + "users", params=payload, headers=headers)
        res_j = res.json()
        return res_j

    def create(self , token , username =''  , password = '' , blocked ='' , user_details ='' ):
        """
            Args:\n
            token:str -> You must have the access token.\n

            Returns: Create new User

            Documentation: https://docs.plusauth.com/api/core/users/createUser

        """
        headers = bearerToken(token)
        headers['content-type'] = 'application/json'
        payload = {'username': username, 'password': password, 'blocked': blocked , 'user_details': user_details}
        res = requests.post(base_url + "users", data=payload, headers=headers)
        res_j = res.json()
        return res_j

    def delete(self , token , id ):
        """
            Args: \n
            token:str -> You must have the access token.\n
            id:str -> User id

            Returns: Delete User

            Documentation: https://docs.plusauth.com/api/core/users/deleteUser

        """
        headers = bearerToken(token)
        self.id = id
        res = requests.delete(base_url + "users/{}".format(self.id), headers=headers)
        return res

    def get(self , token , id ):
        """
            Args: \n
            token:str -> You must have the access token.\n
            id:str -> User id

            Returns: Retrieve User

            Documentation: https://docs.plusauth.com/api/core/users/getUser

        """
        headers = bearerToken(token)
        self.id = id
        res = requests.get(base_url + "users/{}".format(self.id), headers=headers)
        res_j=res.json()
        return res_j

    def update(self , token , id , username =''  , password = '' , blocked ='' , user_details ='' ):
        """
            Args:\n
            token:str -> You must have the access token.\n
            id:str -> User id

            Returns: Update User

            Documentation: https://docs.plusauth.com/api/core/users/updateUser

        """
        headers = bearerToken(token)
        headers['content-type'] = 'application/json'
        self.id = id
        payload = {'username': username, 'password': password, 'blocked': blocked , 'user_details': user_details}
        res = requests.patch(base_url + "users/{}".format(self,id), data=payload, headers=headers)
        res_j = res.json()
        return res_j

    def unassignPermission(self , token , id , permissions_id = ''):
        """
            Args: \n
            token:str -> You must have the access token.\n
            id:str -> User id
            permissions_id -> Permission Ids


            Returns: Unassign directly assigned permission from User

            Documentation: https://docs.plusauth.com/api/core/users/unassignDirectlyAssignedPermission

        """
        headers = bearerToken(token)
        headers['content-type'] = 'application/json'
        self.id = id
        payload ={'permissions_id': permissions_id }
        res = requests.delete(base_url + "users/{}/permissions".format(self, id), data=payload, headers=headers)
        return res.text

    def getPermissions(self , token , id  ):
        """
            Args: \n
            token:str -> You must have the access token.\n
            id:str -> User id

            Returns: Get directly assigned permissions to user

            Documentation: https://docs.plusauth.com/api/core/users/getUserPermissions

        """
        headers = bearerToken(token)
        self.id = id
        res = requests.get(base_url + "users/{}/permissions".format(self, id),  headers=headers)
        res_j=res.json()
        return res_j

    def assignPermission(self , token , id , permissions_id = ''):
        """
            Args: \n
            token:str -> You must have the access token.\n
            id:str -> User id
            permissions_id -> Permission Ids


            Returns: Directly assign permission to User

            Documentation: https://docs.plusauth.com/api/core/users/directlyAssignPermissionToUser

        """
        headers = bearerToken(token)
        headers['content-type'] = 'application/json'
        self.id = id
        payload ={'permissions_id': permissions_id }
        res = requests.post(base_url + "users/{}/permissions".format(self, id), data=payload, headers=headers)
        res_j =res.json()
        return res_j

    def unassignRoleGroups(self , token , id , role_group_id = ''):
        """
            Args: \n
            token:str -> You must have the access token.\n
            id:str -> User id
            role_group_id -> Role Group Ids

            Returns: Unassign Role Groups from User

            Documentation: https://docs.plusauth.com/api/core/users/unassignRoleGroupsFromUser

        """
        headers = bearerToken(token)
        headers['content-type'] = 'application/json'
        self.id = id
        payload ={'role_group_id': role_group_id }
        res = requests.delete(base_url + "users/{}/roleGroups".format(self, id), data=payload, headers=headers)
        return res.text

    def getRoleGroups(self , token , id ):
        """
            Args: \n
            token:str -> You must have the access token.\n
            id:str -> User id

            Returns:Retrieve assigned Role Groups to User

            Documentation: https://docs.plusauth.com/api/core/users/getAssignedRoleGroupsToUser

        """
        headers = bearerToken(token)
        self.id = id
        res = requests.get(base_url + "users/{}/roleGroups".format(self, id), headers=headers)
        res_j = res.json()
        return res_j

    def assignRoleGroups(self , token , id , role_group_id = ''):
        """
            Args: \n
            token:str -> You must have the access token.\n
            id:str -> User id
            role_group_id -> Role Group Ids

            Returns: Assign Role group to User

            Documentation: https://docs.plusauth.com/api/core/users/assignRoleGroupToUser

        """
        headers = bearerToken(token)
        headers['content-type'] = 'application/json'
        self.id = id
        payload ={'role_group_id': role_group_id }
        res = requests.post(base_url + "users/{}/roles".format(self, id), data=payload, headers=headers)
        res_j = res.json()
        return res_j

    def unassignRoles(self , token , id , role_id = ''):
        """
            Args: \n
            token:str -> You must have the access token.\n
            id:str -> User id
            role_group_id -> Role  Ids

            Returns: Unassign directly assigned Roles from user

            Documentation: https://docs.plusauth.com/api/core/users/unassignDirectlyAssignedRolesFromUser

        """
        headers = bearerToken(token)
        headers['content-type'] = 'application/json'
        self.id = id
        payload ={'role_id': role_id }
        res = requests.delete(base_url + "users/{}/roles".format(self, id), data=payload, headers=headers)
        return res.text

    def getRoles(self, token , id ):
        """
            Args: \n
            token:str -> You must have the access token.\n
            id:str -> User id

            Returns: Retrieve Directly assigned Roles to User

            Documentation: https://docs.plusauth.com/api/core/users/getDirectlyAssignedRolesToUser

        """
        headers = bearerToken(token)
        self.id = id
        res = requests.get(base_url + "users/{}/roles".format(self, id), headers=headers)
        res_j = res.json()
        return res_j

    def assignRole(self , token , id , role_id = ''):
        """
            Args: \n
            token:str -> You must have the access token.\n
            id:str -> User id
            role_group_id -> Role  Ids

            Returns: Directly assign Role to User

            Documentation: https://docs.plusauth.com/api/core/users/directlyAssignRoleToUser

        """
        headers = bearerToken(token)
        headers['content-type'] = 'application/json'
        self.id = id
        payload ={'role_id': role_id }
        res = requests.post(base_url + "users/{}/roles".format(self, id), data=payload, headers=headers)
        res_j = res.json()
        return res_j

    def getTenants(self, token , id  ):
        """
            Args: \n
            token:str -> You must have the access token.\n
            id:str -> User id

            Returns: Retrieve created tenants

            Documentation: https://docs.plusauth.com/api/core/users/getCreatedTenants

        """
        headers = bearerToken(token)
        self.id = id
        res = requests.get(base_url + "users/{}/tenants".format(self, id), headers=headers)
        res_j = res.json()
        return res_j