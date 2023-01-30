import requests
import traceback

class Filer:

    def __init__(self,base_url):
        self.base_url = base_url

    def upload_append(self,path,file):
        try:
            files = { 'file': file }
            url = "{}/{}".format(self.base_url,path)
            r = requests.post(url,files=files,params={ "op":"append"})
            return r.json()
        except Exception as e:
            traceback.print_exc()
            raise Exception(str(e))
    
    def upload(self,path,file):
        try:
            files = { 'file': file }
            url = "{}/{}".format(self.base_url,path)
            requests.post(url,files=files)
            return self.get_metadata(path)
        except Exception as e:
            traceback.print_exc()
            raise Exception(str(e))

    def get_metadata(self,path):
        try:
            url = "{}/{}".format(self.base_url,path)
            r = requests.get(url,params={
                "metadata":"true",
                "pretty":"yes"
            })
            return r.json()
        except Exception as e:
            traceback.print_exc()
            raise Exception(str(e))
    def get(self,path):
        try:
            url = "{}/{}".format(self.base_url,path)
            r = requests.get(url)
            return r.content
        except Exception as e:
            traceback.print_exc()
            raise Exception(str(e))

    def remove(self,path,recursive=False):
        try:
            url = "{}/{}".format(self.base_url,path)
            r = requests.delete(url ,params={
                "recursive": "true" if recursive else "false"
            })
            return r.content
        except Exception as e:
            traceback.print_exc()
            raise Exception(str(e))
    
    def list(self,path):
        try:
            url = "{}/{}".format(self.base_url,path)
            r = requests.get(url,params={
                "pretty":"yes"
            },headers={
                "Accept": "application/json"
            })
            return r.json()
        except Exception as e:
            traceback.print_exc()
            raise Exception(str(e))