from .info import Info_Depart
from urllib.parse import urlencode



def start_request():
    all_start_links = []
    all_city = Info_Depart.city_info_1
    all_job = Info_Depart.industry
    base_url = 'https://m.liepin.com/zhaopin/'
    form_data = {
        'keyword': '',
        'dqs': '',#############
        'salarylow': '0',
        'salaryhigh': '999',
        'industrys': '', ##########
        'compScale': '000',
        'compKind': '000',
        'pubtime': '000',
    }

    for job_class in all_job:
        for jobs in job_class:
            for job in jobs:
                if type(job) == str:
                    continue
                job_id = job[0]
                for city in all_city:
                    if len(city[0]) == 3:
                        continue
                    city_id = city[0]
                    form_data['industrys'] = job_id
                    form_data['dqs'] = city_id
                    start_url = base_url + '?' + urlencode(form_data)
                    all_start_links.append(start_url)

    return all_start_links