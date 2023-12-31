class EndDayAPI:
    host = '23.108.103.27'
    database = 'zippbnpc_fnb'
    username = 'zippbnpc_fnb'
    password = 'W6e?q687J@t6'
    merchantId = 478
    outletId = 6
    userId = 482
    startDate = '2023-07-31 10:16:59'
    endDate = '2023-07-31 20:37:34'
    name = 'Manager'

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
        import requests
        import json

        token = '169129403863067'

        if token == False:
            return False
        url = 'https://firstpos.online/pos2/generate_GTO_test'
        r = requests.get(url, params={
            'token': token,
            'manualgto': 1,
            'host': self.host,
            'database': self.database,
            'username': self.username,
            'password': self.password,
            'merchantId': self.merchantId,
            'outletId': self.outletId,
            'userId': self.userId,
            'endDate': self.endDate,
            'startDate': self.startDate,
            'name': self.name
        })

        print(r.text.replace(
            '{"status":0,"msg":"wrong api id"}{"status":0,"msg":"wrong api id"}', ''))


api = EndDayAPI('23.108.103.27', 'zippbnpc_fnb',
                'zippbnpc_fnb', 'W6e?q687J@t6')

api.getOutlBalanceStng()
