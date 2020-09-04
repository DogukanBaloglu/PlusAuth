import requests
from  plusauth_rest_py.base import  baseUrl
from plusauth_rest_py.bearer_token import bearerToken

base_url=baseUrl()

class HookService():

    def test(self , token , name , type , enabled = True , description = ''  , order = '' , content = '' , packages = '' ):
        """
            Args: \n
            token:str -> You must have the access token.\n
            name -> str \n
            type -> str \n
            enabled -> Boolean \n
            description -> str \n
            order -> number \n
            content -> str \n
            packages -> array<object> \n

            Returns: Test a hook by executing it .

            Documentation: https://docs.plusauth.com/api/core/hooks/testHook?lang=python
        """
        headers = bearerToken(token)
        headers['content-type'] = 'application/json'
        payload ={ 'name': name , 'type': type , 'enabled':enabled , 'description':description , 'order':order ,
                   'content': content , 'packages': packages }
        res = requests.post(base_url+"hook-test" , data = payload , headers = headers )
        res_j =res
        return  res_j

    def getAll(self , token , page = '' , itemsPerPage = '' , sortBy = '' , sortDesc = '' ):
        """
            Args:  \n
            token:str -> You must have the access token.\n
            page -> The number of records you wish to skip before selecting records \n
            itemsPerPage -> Limit the number of results returned \n
            sortBy -> Properties that should be ordered by \n
            sortDesc -> Descending or ascending or nothing \n

            Returns: List all Hooks.

            Documentation: https://docs.plusauth.com/api/core/hooks/listHooks?lang=python
        """
        headers = bearerToken(token)
        payload = {'page': page, 'itemsPerPage': itemsPerPage, 'sortBy': sortBy, 'sortDesc': sortDesc}
        res = requests.get(base_url + "hooks", params=payload, headers=headers)
        res_j = res.json()
        return res_j

    def updateMultiple(self ,token , *hooks ):
        """
            Args: \n
            hooks -> Array of Hooks

            Returns: Update hooks.

            Documentation: https://docs.plusauth.com/api/core/hooks/updateHooks?lang=python
        """
        headers = bearerToken(token)
        headers['content-type'] = 'application/json'
        hooks_array =list(hooks)
        payload = { 'hooks': hooks_array }
        res =requests.patch(base_url+"hooks" , data = payload , headers = headers )
        res_j =res.json()
        return res_j

    def create(self , token , name , type , enabled = True , description = ''  , order = '' , content = '' , packages = ''):
        """
            Args: \n
            token:str -> You must have the access token.\n
            name -> str \n
            type -> str \n
            enabled -> Boolean \n
            description -> str \n
            order -> number \n
            content -> str \n
            packages -> array<object> \n

            Returns: Create new Hook .

            Documentation: https://docs.plusauth.com/api/core/hooks/createHook?lang=python
        """
        headers = bearerToken(token)
        headers['content-type'] = 'application/json'
        payload = {'name': name, 'type': type, 'enabled': enabled, 'description': description, 'order': order,
                   'content': content, 'packages': packages}
        res = requests.post(base_url + "hooks", data=payload, headers=headers)
        res_j = res
        return res_j

    def delete(self ,token , id ):
        """
            Args: \n
            token:str -> You must have the access token.\n
            id:str -> Hook id

            Returns: Delete Hook

            Documentation: https://docs.plusauth.com/api/core/hooks/deleteHook?lang=python
        """
        headers = bearerToken(token)
        self.id = id
        res = requests.delete(base_url+"hooks/{}".format(self.id), headers =headers )
        return  res

    def get(self , token , id ):
        """
            Args: \n
            token:str -> You must have the access token.\n
            id:str -> Hook id

            Returns: Retrieve Hook.

            Documentation: https://docs.plusauth.com/api/core/hooks/getHook?lang=python
        """
        headers = bearerToken(token)
        self.id = id
        res =requests.get(base_url +"hooks/{}".format(self.id) , headers =headers )
        res_j =res.json()
        return  res_j

    def update(self , token , id , hook_object = ''):
        """
            Args: \n
            token:str -> You must have the access token.\n
            id:str -> Hook id \n
            hook_object -> Hook object\n

            Returns: Update Hook

            Documentation: https://docs.plusauth.com/api/core/hooks/updateHook?lang=python
        """
        headers = bearerToken(token)
        headers['content-type'] = 'application/json'
        self.id = id
        payload = {'hook_object':hook_object}
        res = requests.patch(base_url + "hooks/{}".format(self.id), data= payload , headers=headers)
        res_j = res.json()
        return res_j

    def deletePackages(self , token , id , npm = ''):
        """
            Args: \n
            token:str -> You must have the access token.\n
            id:str -> Hook id \n
            npm -> Npm packages array \n

            Returns: Delete packages from hook.

            Documentation: https://docs.plusauth.com/api/core/hooks/deleteHookPackages
        """
        headers = bearerToken(token)
        headers['content-type'] = 'application/json'
        self.id = id
        payload ={'npm': npm }
        res = requests.delete(base_url + "hooks/{}/packages".format(self.id), data = payload , headers=headers)
        return res.text

    def addPackages(self, token , id , npm = ''):
        """
            Args: \n
            token:str -> You must have the access token.\n
            id:str -> Hook id \n
            npm -> Npm packages array \n

            Returns: Delete packages from hook.

            Documentation: https://docs.plusauth.com/api/core/hooks/addHookPackages
        """
        headers = bearerToken(token)
        headers['content-type'] = 'application/json'
        self.id = id
        payload ={'npm': npm }
        res = requests.post(base_url + "hooks/{}/packages".format(self.id), data = payload , headers=headers)
        return res.text

