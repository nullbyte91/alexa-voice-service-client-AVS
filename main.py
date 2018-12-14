import settings	#Manage Env variable
import tempfile #Generate temporary files and directories

class alexaClient(object):
	def __init__(self, token=None, client_id=settings.CLIENT_ID,
                 client_secret=settings.CLIENT_SECRET,
                 refresh_token=settings.REFRESH_TOKEN, *args, **kwargs):
        	self._token = token
        	self._client_id = client_id
        	self._client_secret = client_secret
        	self._refresh_token = refresh_token
        	self.temp_dir = tempfile.mkdtemp()

if __name__ == '__main__':
	alexa = alexaClient()

