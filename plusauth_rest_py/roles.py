import requests
from  plusauth_rest_py.base import  baseUrl
from plusauth_rest_py.bearer_token import bearerToken

base_url=baseUrl()

class RoleService():

    def getAll(self , token , page = '' , itemsPerPage = '' , sortBy = '' , sortDesc = ''  ):
        """
            Args: \n
            token:str -> You must have the access token.\n
            page -> The number of records you wish to skip before selecting records \n
            itemsPerPage -> Limit the number of results returned \n
            sortBy -> Properties that should be ordered by \n
            sortDesc -> Descending or ascending or nothing \n

            Returns: List Roles
        """
        headers = bearerToken(token)
        payload = {'page': page, 'itemsPerPage': itemsPerPage, 'sortBy': sortBy, 'sortDesc': sortDesc}
        res = requests.get(base_url + "roles", params=payload, headers=headers)
        res_j = res.json()
        return res_j

    def creat(self , token , name , description = '' , assignOnSignup = True ):
        """
            Args: \n
            token:str -> You must have the access token.\n
            name -> str \n
            description -> Description \n
            assignOnSignup -> Boolean \n

            Returns: Create new Role
        """
        headers = bearerToken(token)
        payload = {'name': name, 'description': description, 'assignOnSignup': assignOnSignup}
        res = requests.post(base_url + "roles", data=payload, headers=headers)
        res_j = res.json()
        return res_j

    def get(self , token , id ):
        """
            Args: \n
            token:str -> You must have the access token.\n
            id:str -> Role id

            Returns: Retrieve Role
        """
        headers = bearerToken(token)
        self.id = id
        res = requests.get( base_url+"roles/{}".format(self.id) , headers =headers )
        res_j = res.json()
        return res_j

    def update(self , token , id , name , description = '' , assignOnSignup = True ):
        """
            Args: \n
            token:str -> You must have the access token.\n
            name -> str \n
            description -> Description \n
            assignOnSignup -> Boolean \n

            Returns: Update Role
        """
        headers = bearerToken(token)
        self.id =id
        payload = {'name': name, 'description': description, 'assignOnSignup': assignOnSignup}
        res = requests.patch( base_url + "roles/{}".format(self.id), data = payload, headers = headers )
        res_j = res.json()
        return res_j

    def delete(self , token , id ):
        """
            Args: \n
            token:str -> You must have the access token.\n
            id:str -> Role id

            Returns: Delete Role
        """
        headers = bearerToken(token)
        self.id = id
        res = requests.delete(base_url + "roles/{}".format(self.id), headers=headers)
        return res

    def getPermissions(self , token , id ):
        """
            Args: \n
            token:str -> You must have the access token.\n
            id:str -> Role id

            Returns: Retrieve Permissions assigned to Role
        """
        headers = bearerToken(token)
        self.id = id
        res = requests.get(base_url + "roles/{}/permissions".format(self.id), headers=headers)
        res_j = res.json()
        return res_j

    def addPermission(self , token , id , *permissions_id ):
        """
            Args:  \n
            token:str -> You must have the access token.\n
            id:str -> Role id
            permissions_id -> Permission Ids


            Returns: Assign Permission to a Role
        """
        headers = bearerToken(token)
        self.id = id
        permissions_id_array =list(permissions_id)
        payload= { 'permissions_id': permissions_id_array }
        res = requests.post(base_url + "roles/{}/permissions".format(self.id), data = payload , headers=headers)
        res_j =res.json()
        return  res_j

    def removePermissions(self , token , id , *permissions_id ):
        """
            Args:  \n
            token:str -> You must have the access token.\n
            id:str -> Role id
            permissions_id -> Permission Ids

            Returns:Unassign Permissions from Role
        """
        headers = bearerToken(token)
        self.id = id
        permissions_id_array = list(permissions_id)
        payload = {'permissions_id': permissions_id_array}
        res = requests.delete(base_url + "roles/{}/permissions".format(self.id), data=payload, headers=headers)
        return res
