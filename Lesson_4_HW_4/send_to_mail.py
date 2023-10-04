import smtplib  #библиотека
from os.path import basename #чтобы прикреплять файлы к письму
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

#задаем константы. Если адрес меняется, можно вынести в config файл
fromaddr = "estgb113@mail.ru"    #от кого
toaddr = "address@mail.ru"  # кому
mypass = "gb@123gb@123"   # пароль
reportname = "report.xml"   #имя файла с отчетом


#эти данные (строки выше) заносятся в переменную msg как элементы списка
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "ПРивет от питона" #тема

# прикрепление сообения
# отчет считывается как обычный файл и передается в переменную msg
with open(reportname, "rb") as f:
    part = MIMEApplication(f.read(), Name=basename(reportname))
    part['Content-Disposition'] = f'attachment; filename="%s"% {basename(reportname)}'
    msg.attach(part)

body = "Это пробное сообщение"
msg.attach(MIMEText(body, 'plain'))

# отправка сообщения
#передаем способ шифрования (у mail.ru это ssl),
# передаем сервер smtp.mail.ru, и порт 465
server = smtplib.SMTP_SSL('smtp.mail.ru', 465)
server.login(fromaddr, mypass)

# добавляем текст
text = msg.as_string()
# отправляем
server.sendmail(fromaddr, toaddr, text)
#выходим из почтового сервера
server.quit()