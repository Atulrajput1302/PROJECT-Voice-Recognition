#import
import speech_recognition as sr
import webbrowser

#check Microphone list
#print(sr.Microphone.list_microphone_names())
#list of all the list_microphone_names
#'Microsoft Sound Mapper - Input', 'Microphone (Realtek High Defini', 'Microsoft Sound Mapper - Output', 'Speakers / Headphones (Realtek ', 'Primary Sound Capture Driver', 'Microphone (Realtek High Definition Audio)', 'Primary Sound Driver', 'Speakers / Headphones (Realtek High Definition Audio)', 'Speakers / Headphones (Realtek High Definition Audio)', 'Microphone (Realtek High Definition Audio)', 'Stereo Mix (Realtek HD Audio Stereo input)', 'Speakers (Realtek HD Audio output)', 'Microphone (Realtek HD Audio Mic input)']


##for giving input we need --->    [Microsoft Sound Mapper - Input']  ---> which is at index 1

sr.Microphone(device_index = 1)

r = sr.Recognizer()


#any energy below the energy_threshold will be discarded || only enery above the energy_threshold will be taken in as an input
r.energy_threshold = 5000


url = 'https://www.google.com/search?client=firefox-b-d&q='



with sr.Microphone() as source:
    print('Hey Alexa is Online.\nWhat Do you wanna Search?!')
    audio = r.listen(source)
    try:
        #the input audio can be recognized by many ways || recognize_google is one best way to do so
        text = r.recognize_google(audio)
        print('You Said : \n' + text)
        print('\n')
        print('Opening your search with Google................')
        search_url = url + text
        webbrowser.open(search_url)

    except Exception as e:
        print('Voice not recognized \n Please retry!')
