import pyperclip,time
print('recoding clipboard... (ctrl-c to stop')
previous_content=''
try:
    while True:
        content=pyperclip.paste()
        if content!=previous_content:
            print(content)
            previous_content=content
        time.sleep(0.02)
except KeyboardInterrupt:
    pass