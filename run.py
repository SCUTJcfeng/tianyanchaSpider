# python 3.6


from common.http import HttpTool
from common.save import SaveTool

base_url = 'https://www.tianyancha.com/company/'


def get_company_text(cid):
    url = base_url + str(cid)
    # todo add cookie
    res = HttpTool.get(url, retFormat='text')
    SaveTool.saveText(res, './temp.txt')
    pass


if __name__ == "__main__":
    get_company_text(841099016)
