# python 3.6

import re
from common.http import HttpTool
from common.url import headers

base_url = 'https://www.tianyancha.com/company/'


def get_company_text(cid):
    url = base_url + str(cid)
    html, status_code = HttpTool.get(url, headers=headers, retFormat='text')
    return html, status_code


def extract_company_top(soup):
    res = soup.find('div', {'class': re.compile(r'box -company-box')})
    company_name = res.find(class_='name').string
    detail = res.find(class_='detail')
    f0_list = detail.find_all(class_='f0')
    assert len(f0_list) == 2
    phone_email = f0_list[0]
    phone_span_list = phone_email.find(class_='in-block sup-ie-company-header-child-1').find_all('span')
    phone = phone_span_list[1].string
    email_span_list = phone_email.find(class_='in-block sup-ie-company-header-child-2').find_all('span')
    email = email_span_list[1].string
    web_addr = f0_list[1]
    web_list = web_addr.find(class_='in-block sup-ie-company-header-child-1').contents
    if len(web_list) == 2:
        web = web_list[1].string
    else:
        web = web_list[2].string
    addr_div = web_addr.find(class_='in-block sup-ie-company-header-child-2')
    if addr_div.div:
        addr = addr_div.div.div.string
    else:
        addr = addr_div.find_all('span')[1].string
    summary_div = detail.find(class_='summary')
    summary = summary_div.find_all('span')[1].string
    if summary is None:
        summary = summary_div.script.string
    return company_name, phone, email, web, addr, summary


def extract_company_detail(soup):
    container = soup.find(id='_container_baseInfo')
    if not container:
        return ['' for i in range(20)]
    tr_list = container.find_all('table')[1].find_all('tr')

    capital_date_td_list = tr_list[0].find_all('td')
    reg_capital = capital_date_td_list[1].div.string
    found_date = capital_date_td_list[3].div.string

    status_reg_code_td_list = tr_list[1].find_all('td')
    status = status_reg_code_td_list[1].get_text()
    reg_code = status_reg_code_td_list[3].string

    society_and_ogn_code_td_list = tr_list[2].find_all('td')
    society_code = society_and_ogn_code_td_list[1].string
    ogn_code = society_and_ogn_code_td_list[3].string

    tax_and_type_td_list = tr_list[3].find_all('td')
    tax_code = tax_and_type_td_list[1].string
    company_type = tax_and_type_td_list[3].string

    limit_and_industry_td_list = tr_list[4].find_all('td')
    limit_date = limit_and_industry_td_list[1].span.string
    industry = limit_and_industry_td_list[3].string

    person_type_and_approve_date_td_list = tr_list[5].find_all('td')
    person_type = person_type_and_approve_date_td_list[1].string
    approve_date = person_type_and_approve_date_td_list[3].string

    capital_and_people_td_list = tr_list[6].find_all('td')
    real_capital = capital_and_people_td_list[1].string
    people_count = capital_and_people_td_list[3].string

    people_and_reg_ogn_td_list = tr_list[7].find_all('td')
    people_in_secure = people_and_reg_ogn_td_list[1].string
    reg_ogn = people_and_reg_ogn_td_list[3].string

    old_name_and_eng_name_td_list = tr_list[8].find_all('td')
    old_name = old_name_and_eng_name_td_list[1].string
    eng_name = old_name_and_eng_name_td_list[3].string

    reg_addr_td_list = tr_list[9].find_all('td')
    reg_addr = reg_addr_td_list[1].contents[0]

    bussiness_range_td_list = tr_list[10].find_all('td')
    bussiness_range = bussiness_range_td_list[1].span.div.div.string

    return reg_capital, found_date, status, reg_code, society_code, ogn_code, tax_code, company_type, \
        limit_date, industry, person_type, approve_date, real_capital, people_count, people_in_secure, \
        reg_ogn, old_name, eng_name, reg_addr, bussiness_range
