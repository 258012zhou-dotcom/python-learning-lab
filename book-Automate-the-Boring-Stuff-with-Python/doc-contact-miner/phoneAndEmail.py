import pyperclip,re
phone_re=re.compile(r'''(
    (\d{3}|\(\d{3}\))?  #区号
    (\s|-|\.)?
    (\d{3})             #开头三位数字
    (\s|-|\.)
    (\d{4})             #末尾四位数字
    (\s*(ext|x|ext\.)\s*(\d{2,5}))?     #分机号
)''',re.VERBOSE)

email_re=re.compile(r'''(
    [a-zA-Z0-9._%+-]+   #用户名
    @
    [a-zA-Z0-9.-]+      #域名
    (\.[a-zA-Z]{2,4})   #句号后面更2到4个字母
)''',re.VERBOSE)

text=str(pyperclip.paste())
matches=[]
for groups in phone_re.findall(text):
    phone_num='-'.join([groups[1],groups[3],groups[5]])
    if groups[6]!='':
        phone_num+=' x'+groups[6]
    matches.append(phone_num)
for groups in email_re.findall(text):
    matches.append(groups[0])

if len(matches)>0:
    pyperclip.copy('\n'.join(matches))
    print('copied to clipboard')
    print('\n'.join(matches))
else:
    print('no phone number or email addresses found.')

