import pyttsx3
import wikipedia
import os
import webbrowser
import datetime
import pyjokes
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
import smtplib
import httpx._exceptions


def speak(audio: str, voice_no, rate=180):
    """
    Speak function :-
        This function speaks.

        !!! Parameters !!!
        audio -> The audio to be spoked out. -> Must be str.
        voice_no -> Number of voice which should be spoked out. Enter the voice number as per the voices in your computer. -> Must be int.
        rate -> The rate at which the audio will be spoked out. The default value is 180. -> Must be int.
    """
    rate = int(rate)
    voice_no = int(voice_no)
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')

    engine.setProperty('voice', voices[voice_no].id)
    engine.setProperty('rate', rate)

    engine.say(audio)
    engine.runAndWait()


def search_wiki(about):
    """
    Search in Wikipedia function:-
        Search anything in wikipedia.
        !!!Parameters!!!
        about -> What you are searching

        >> Returns about the topic you searched for when success
        >> Returns False when fail
    """
    try:
        return wikipedia.summary(about)
    except wikipedia.exceptions.DisambiguationError as e:
        print(
            f'There are many options of your search. Here are some suggestions : \n{e.options}')

    except wikipedia.exceptions.PageError:
        print("There are no pages match with your search. Check if there isn't any typo in your search.")


def open_app(path):
    """
    Open any application function:-
        You can open any application using this function.
        !!!Parameters!!!
        path -> Path of your application

        >> Opens the app when success
        >> Returns False when fail
    """
    return os.startfile(path)


def open_website(url):
    """
    Open any website function:-
        You can open any website using this function.
        !!!Parameters!!!
        url -> Url of your website

        >> Opens the url in your Web Browser when success
        >> Returns False when fail
    """
    return webbrowser.open(url)


def tell_time(format: str | None = None):
    """
    Tell the time function:-
        Tell the current time in form of:
            HH:MM:SS
        >> Returns current time when success
        >> Returns False when fail
    """
    return datetime.datetime.now().strftime(format) if format is not None else datetime.datetime.now().strftime("%H:%M:%S")


def tell_joke():
    """
    Tell a Joke function:-
        This function will take a random joke from pyjokes joke library and return it.
    """
    return pyjokes.get_joke()


def get_news():
    """
    Get Today's News Function:-
        Fetch top news of the day from "news.google.com/news/rss"

        >> You will get a list of string of news if success
        >> You will get False if fail
    """
    try:
        news_url = "https://news.google.com/news/rss"
        client = urlopen(news_url)
        xml_page = client.read()
        client.close()
        soup_page = soup(xml_page, "xml")
        news_list = soup_page.findAll("item")
        li = []

        for news in news_list[:15]:
            li.append(str(news.title.text.encode('utf-8'))[1:])
        return li

    except Exception as e:
        return None


def send_mail(email_of_sender, password_of_sender, email_of_receiver, message):
    """
    Send Email Function :-
        This function helps a user to securely connect to the gmail via python, send message and close the connection.

        ### Only Gmail is supported ###

        !!! Parameters !!!
        email_of_sender -> Email address of the sender
        password_of_sender -> Password of the sender
        email_of_receiver -> Email address of the receiver of this email
        message -> Message of the email
    """
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(email_of_sender, password_of_sender)
        server.sendmail(email_of_sender, email_of_receiver, message)
        server.close()

    except httpx._exceptions.ConnectError:
        raise httpx._exceptions.ConnectError(
            "Less secured apps not allowed. Please Allow them.")
