
import config
import requests

TARGET_MP_LIST = [mpDict['id'] for mpDict in config.TARGET_MP_DICT_LIST]

class MemberOfParliament():
	def __init__(self, mpId: int) -> None:
		self.id = mpId
		self.name = None
		self.addressAs = None
		self.website = None

		fetchedInfo = self.fetch_info()


	def __fetch_info_if_missing(func):
		
		def fetch_info_if_missing_wrapper(self, *args, **kwargs):
			if 'fetchedInfo' not in kwargs and len(args) == 0:
				kwargs['fetchedInfo'] = self.fetch_info()

			return func(self, *args, **kwargs)

		return fetch_info_if_missing_wrapper
	
	
	def fetch_info(self) -> dict:
		responseJson = requests.get(f'https://members-api.parliament.uk/api/Members/{self.id}').json()

		return responseJson['value']

	@__fetch_info_if_missing
	def refresh_name(self, fetchedInfo: dict=None) -> None:
		self.name = fetchedInfo['nameDisplayAs']
	

	@__fetch_info_if_missing
	def refresh_address_as(self, fetchedInfo: dict=None) -> None:
		self.addressAs = fetchedInfo['nameAddressAs']
	
	@__fetch_info_if_missing
	def refresh_all_info(self, fetchedInfo: dict=None) -> None:
		self.addressAs = fetchedInfo['nameAddressAs']


mp = MemberOfParliament(4000)
mp.refresh_name()
mp.refresh_name({})
mp.refresh_name(1)

