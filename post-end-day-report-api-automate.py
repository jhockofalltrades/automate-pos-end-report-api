class EndDayAPI:
    host = ''
    database = ''
    username = ''
    password = ''
    merchantId = 0
    outletId = 0
    userId = 0
    startDate = ''
    endDate = ''
    userName = 'Manager'

    def __init__(self, host, database, username, password) -> None:
        self.host = host
        self.database = database
        self.username = username
        self.password = password

    def login(self):
        import requests
        import json

        url = 'https://firstpos.online/pos2/login'

        token = False

        r = requests.post(
            url, json={"username": "manager@zippbnp.com", "password": "Bnp@k106"})

        if r.status_code != 200:
            print('Error')
            exit()

        response = r.text
        res = json.loads(response)

        if (res['status'] == 1):
            token = res['data']['token']

        return token

    def getOutlBalanceStng(self):
        pass


api = EndDayAPI('23.108.103.27', 'zippbnpc_fnb',
                'zippbnpc_fnb', 'W6e?q687J@t6')

token = api.login()
