import re

def find_telephone():
    text = '''
        United States
        Apple Media Helpline 408-974-2042
        Apple Software Upgrade Center 888-840-8433
        Reseller Referral (Resellers, Trainers, Consultants) 800-538-9696
        Canada
        Apple Store (Consumer and Education Individuals) (800) MY-APPLE (800-692-7753)
        Mexico
        Apple Store (Consumer and Education Individuals) 001-800-MY-APPLE (001-800-692-7753)
        Apple Store (Small Business) 001-800-692-7753
    '''

    tel_list = re.findall(r"\d\d\d-\d\d\d-\d\d\d\d", text)
    tel_list.extend(re.findall(r"\d\d\d-\d\d\d-\d\d\d-\d\d\d\d", text))

    print(f"找电话号码：{tel_list}")


find_telephone()