from pydictionary import Dictionary as DictionaryMain
import requests
import pyautogui


def meanings(word):
    """
    Meanings of word function :-
        This function helps to find the meaning(s) of a particular word using PyDictionary.

        !!! Parameters !!!
        word -> Word of which the meaning is to be found. -> Must be str.
    """
    return DictionaryMain(word).meanings()


def synonyms(word):
    """
    Synonyms of word function :-
        This function helps to find the synonym(s) of a particular word using PyDictionary.

        !!! Parameters !!!
        word -> Word of which the synonym is to be found. -> Must be str.
    """
    return DictionaryMain(word).synonyms()


def antonyms(word):
    """
    Antonyms of word function :-
        This function helps to find the antonym(s) of a particular word using PyDictionary.

        !!! Parameters !!!
        word -> Word of which the antonym is to be found. -> Must be str.
    """
    return DictionaryMain(word).antonyms()


def location():
    """
    Get Location function :-
        This function get the location of the user using the IP address.

        # Note
            This function requires an internet connection.
    """
    try:
        ipAdd = requests.get('https://api.ipify.org').text
        url = 'https://get.geojs.io/v1/ip/geo/' + ipAdd + '.json'
        geo_request = requests.get(url)
        geo_data = geo_request.json()
        city = geo_data['city']
        state = geo_data['region']
        country = geo_data['country']
        latitude = geo_data['latitude']
        longitude = geo_data['longitude']

        l = {"city": city, "state": state, "country": country, "latitude": latitude,
             "longitude": longitude}

        return l

    except requests.exceptions.ConnectionError as e:
        raise ConnectionError(
            "Check Internet Connection. Internet Connection required.")


def screenshot(file_path=None, file_name=None, returnImage=False, saveImage=True):
    """
    Take Screenshot Function :-
        This function will take screenshot and save it in the file path you defined.

        !!! Parameters !!!
        file_path -> Path to where the screenshot will be saved
        file_name -> Name of file to be saved

        Note:-
            File_name parameter should be like below format :
                'name_of_file.png' or 'name_of_file.jpg', 'name_of_file.jpeg', 'name_of_file.tiff', 'name_of_file.gif', 'name_of_file.bmp', 'name_of_file.ppm', etc...
    """
    s = pyautogui.screenshot()
    if saveImage:
        s.save(f"{file_path}\\{file_name}")
    if returnImage:
        return s
