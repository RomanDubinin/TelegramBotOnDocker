FROM python:3.6.7

WORKDIR /app

RUN pip install telebot && \
    pip install pyTelegramBotApi && \
    pip install bs4 && \
    pip install requests && \
    pip install lxml

COPY /bot /app

CMD ["python", "/app/bot.py"]
#CMD ["python", "--version"]

