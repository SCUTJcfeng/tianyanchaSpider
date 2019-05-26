# python 3.6


from bs4 import BeautifulSoup
from common.base import strip_blank
from tyc import get_company_text, extract_company_top, extract_company_detail


def main(cid):
    html, status_code = get_company_text(cid)
    if status_code == 404:
        print(f'id {cid} company not exists')
        return
    elif status_code == 302:
        print(f'302 redirects to login page')
        return
    soup = BeautifulSoup(html, 'lxml')
    company_name, phone, email, web, addr, summary = extract_company_top(soup)
    reg_capital, found_date, status, reg_code, society_code, ogn_code, tax_code, company_type, \
        limit_date, industry, person_type, approve_date, real_capital, people_count, people_in_secure, \
        reg_ogn, old_name, eng_name, reg_addr, bussiness_range = extract_company_detail(soup)

    company_data = {
        'id': cid,
        'company_name': company_name,
        'phone': phone,
        'email': email,
        'web': web,
        'addr': strip_blank(addr),
        'summary': strip_blank(summary),
        'reg_capital': reg_capital,
        'found_date': found_date,
        'status': status,
        'reg_code': reg_code,
        'society_code': society_code,
        'ogn_code': ogn_code,
        'tax_code': tax_code,
        'company_type': company_type,
        'limit_date': limit_date,
        'industry': industry,
        'person_type': person_type,
        'approve_date': approve_date,
        'real_capital': real_capital,
        'people_count': people_count,
        'people_in_secure': people_in_secure,
        'reg_ogn': reg_ogn,
        'old_name': old_name,
        'eng_name': eng_name,
        'reg_addr': reg_addr,
        'bussiness_range': strip_blank(bussiness_range)
    }
    print(company_data)


if __name__ == "__main__":
    main(101398822)
