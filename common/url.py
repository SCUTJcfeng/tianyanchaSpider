# python3.6


class UrlTool:
    @staticmethod
    def joinUrl(url, params):
        return url + '?' + '&'.join([f'{k}={v}' for k, v in params.items()])


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
    'Referer': 'https://www.tianyancha.com',
    'Cookie': 'tyc-user-info=%257B%2522claimEditPoint%2522%253A%25220%2522%252C%2522myAnswerCount%2522%253A%25220%2522%252C%2522myQuestionCount%2522%253A%25220%2522%252C%2522signUp%2522%253A%25220%2522%252C%2522explainPoint%2522%253A%25220%2522%252C%2522privateMessagePointWeb%2522%253A%25220%2522%252C%2522nickname%2522%253A%2522%25E9%25A1%25B9%25E6%25A2%2581%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522privateMessagePoint%2522%253A%25220%2522%252C%2522state%2522%253A%25220%2522%252C%2522announcementPoint%2522%253A%25220%2522%252C%2522isClaim%2522%253A%25220%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522discussCommendCount%2522%253A%25220%2522%252C%2522monitorUnreadCount%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522claimPoint%2522%253A%25220%2522%252C%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNzY2NTM4NjE5MCIsImlhdCI6MTU1ODgwMjM0NiwiZXhwIjoxNTkwMzM4MzQ2fQ.bAN8yU6tFwd_xV81I5RpEuEQilL-reNcfCNTvgMsmW_kiiNuWlWJ_5epPcumUfV9niyrS1qMKXlKEEfV00uHZg%2522%252C%2522pleaseAnswerCount%2522%253A%25220%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522bizCardUnread%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252217665386190%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNzY2NTM4NjE5MCIsImlhdCI6MTU1ODgwMjM0NiwiZXhwIjoxNTkwMzM4MzQ2fQ.bAN8yU6tFwd_xV81I5RpEuEQilL-reNcfCNTvgMsmW_kiiNuWlWJ_5epPcumUfV9niyrS1qMKXlKEEfV00uHZg'
}
