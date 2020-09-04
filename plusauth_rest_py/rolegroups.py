import requests
from  plusauth_rest_py.base import  baseUrl
from plusauth_rest_py.bearer_token import bearerToken

base_url=baseUrl()

class RoleGroupsService():

    def getAll(self , token , page = '' , itemsPerPage = '' , sortBy = '' , sortDesc = ''  ):
        """
            Args:  \n
            token:str -> You must have the access token.\n
            page -> The number of records you wish to skip before selecting records \n
            itemsPerPage -> Limit the number of results returned \n
            sortBy -> Properties that should be ordered by \n
            sortDesc -> Descending or ascending or nothing \n

            Returns: List Role GroupsList Role Groups
        """
        headers = bearerToken(token)
        payload = {'page': page, 'itemsPerPage': itemsPerPage, 'sortBy': sortBy, 'sortDesc': sortDesc}
        res = requests.get(base_url + "roleGroups", params=payload, headers=headers)
        res_j = res.json()
        return res_j

    def creat(self , token , name , description = '' , assignOnSignup = True ):
        """
            Args: \n
            token:str -> You must have the access token.\n
            name -> str \n
            description -> Description \n
            assignOnSignup -> Boolean \n

            Returns: Create new Role Group
        """
        headers = bearerToken(token)
        payload = {'name': name , 'description' : description , 'assignOnSignup' : assignOnSignup }
        res =requests.post(base_url+"roleGroups" , data= payload , headers = headers)
        res_j =res.json()
        return res_j

    def get(self , token , id ):
        """
            Args: \n
            token:str -> You must have the access token.\n
            id:str -> Role Group id

            Returns: Retrieve Role Group
        """
        headers = bearerToken(token)
        self.id = id
        res = requests.get( base_url+"roleGroups/{}".format(self.id) , headers =headers )
        res_j = res.json()
        return res_j

    def update(self , token , id , name , description = '' , assignOnSignup = True ):
        """
            Args: \n
            token:str -> You must have the access token.\n
            name -> str \n
            description -> Description \n
            assignOnSignup -> Boolean \n

            Returns: Update Role Group
        """
        headers = bearerToken(token)
        self.id =id
        payload = {'name': name, 'description': description, 'assignOnSignup': assignOnSignup}
        res = requests.patch( base_url + "roleGroups/{}".format(self.id), data = payload, headers = headers )
        res_j = res.json()
        return res_j

    def delete(self , token , id ):
        """
            Args: \n
            token:str -> You must have the access token.\n
            id:str -> Role Group id

            Returns: Delete Role Group
        """
        headers = bearerToken(token)
        self.id = id
        res = requests.delete(base_url + "roleGroups/{}".format(self.id), headers=headers)
        return res

    def getRoles(self , token , id , page = '' , itemsPerPage = '' , sortBy = '' , sortDesc = '' ):
        """
            Args: \n
            token:str -> You must have the access token.\n
            id:str -> Role Group id \n
            page -> The number of records you wish to skip before selecting records \n
            itemsPerPage -> Limit the number of results returned \n
            sortBy -> Properties that should be ordered by \n
            sortDesc -> Descending or ascending or nothing \n

            Returns:Retrieve Roles assigned to Role Group
        """
        headers = bearerToken(token)
        self.id = id
        payload = {'page': page, 'itemsPerPage': itemsPerPage, 'sortBy': sortBy, 'sortDesc': sortDesc}
        res = requests.get(base_url + "roleGroups/{}/roles".format(self.id), params=payload, headers=headers)
        res_j = res.json()
        return res_j

    def addRole(self , token , id , *role_id ):
        """
            Args: \n
            token:str -> You must have the access token.\n
            id:str -> Role Group id
            role_id -> Role Id's

            Returns: Add Role to Role Group
        """
        headers = bearerToken(token)
        self.id = id
        role_id_array =list(role_id)
        payload = {'role_id' :role_id_array }
        res = requests.post(base_url + "roleGroups/{}/roles".format(self.id), params=payload, headers=headers)
        res_j = res.json()
        return res_j

    def removeRole(self , token , id , *role_id ):
        """
            Args: \n
            token:str -> You must have the access token.\n
            id:str -> Role Group id
            role_id -> Role Id's

            Returns: Unassign Roles from Role Group
        """
        headers = bearerToken(token)
        self.id = id
        role_id_array =list(role_id)
        payload = {'role_id' :role_id_array }
        res = requests.delete(base_url + "roleGroups/{}/roles".format(self.id), params=payload, headers=headers)
        res_j = res.json()
        return res_j

