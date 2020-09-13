
from selenium import webdriver
import random
import time
import pyttsx3                                        #allow text-to-speech.
import wikipedia                                      #allow to access information from wikipedia.
import webbrowser                                     #allow to access websites and URL's from internet.
import datetime                                       #allows the code to access current date and time from the system.
import getpass                                        #provides secure way to handle the password prompts,(i'm still working and studing on it).
from translate import Translator                      #help in translating the input.
import smtplib
import speech_recognition as sr


engine = pyttsx3.init()
voices=engine.getProperty('voices')
# print(voices[8])
engine.setProperty('voices',voices[8].id)



def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening...')
        r.pause_threshold = 1
        r.energy_threshold = 400
        spp = r.listen(source)

    try:
        a= r.recognize_google(spp, language='en-in')
        print('You said : {}'.format(a))

    except Exception as e:
        # print(e)
        print('beg your pardon..')
        speak('beg your pardon..')
        return 'None'
    return a



# def Brow():
# browser=webdriver.Chrome('/Users/saurabhmehanti/Downloads/chromedriver')




def sendMail(to,content):
    server= smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('YOUR_EMIALID','YOUR_PASSWORD')
    server.sendmail(email_s,to,content)
    server.close()



def tran():
    print('translating..')
    speak('translating..')
    yo = Translator(from_lang=lann, to_lang=lann1)
    word = yo.translate(give)
    print(word)
    speak(word)




def Images():
    speak('images of whose?')
    ima = takeCommand()
    speak('opening photos of ' + ima)
    browser = webdriver.Chrome('/Users/saurabhmehanti/Downloads/chromedriver\ 5')
    browser.get('https://www.google.com/search?q=' + ima + '&source=lnms&tbm=isch&sa=X&ved=0ahUKEwj_xJ6Jr9njAhXGF3IKHRrFAagQ_AUIECgB&biw=1440&bih=821')
    time.sleep(2)

    speak('do you want me to close it')
    while True:
        ima1 = takeCommand()
        if ima1 in perr:
            speak('closing the tab')
            browser.quit()
            break

        elif ima1 in neg:
            speak('okay , not closing the tab')
            break

        else:
            speak('i want you to answer in yes ,or, no')
            continue



def BroClose():
    speak('shall i close the page ?')
    while True:

        anndd=takeCommand()
        if anndd in neg:
            speak('okay ,not closing this page')
            break
        elif anndd in perr:
            speak('closing this page !')
            browser.quit()
            break
        else:
            speak('i want you to answer in yes, or ,no')
            continue





def Shop():
    speak('tell me which product ?')
    shoo=takeCommand()
    speak('opening ' + shoo + ' in amazon.com')
    browser = webdriver.Chrome('/Users/saurabhmehanti/Downloads/chromedriver\ 5')
    browser.get('https://www.amazon.in/s?k=' + shoo + '&ref=nb_sb_noss_2')

    time.sleep(2)
    speak('shall i close the page ?')
    shoo1=takeCommand()
    while True:
        if shoo1 in perr:
            speak('closing this page')
            browser.quit()
            break
        elif shoo1 in neg:
            speak('okay , not closing this page')
            break
        else:
            speak('i want you to answer in yes or no')
            continue


    return 'None'






def ques():
    speak('i found something on the web about ' + a + ' , shall i open it ?')
    somm = takeCommand()
    if somm in perr:
        speak('opening web page about , ' + a)
        browser=webdriver.Chrome('/Users/saurabhmehanti/Downloads/chromedriver\ 5')
        browser.get('https://google.com/search?q=' + a)

        time.sleep(2)
        BroClose()

    elif somm in neg:
        speak('okay not opening the search page.')






def sitee():

    speak('which website?')
    web = takeCommand()
    if 'leave' in web:
        speak('okay ,not opening')
    else:
        speak('opening' + web)
        browser = webdriver.Chrome('/Users/saurabhmehanti/Downloads/chromedriver\ 5')
        browser.get('https://www.' + web)
    time.sleep(2)
    speak('shall i close the page ?')
    while True:

        anndd = takeCommand()
        if anndd in neg:
            # speak('okay ,not closing this page')
            break
        elif anndd in perr:
            speak('closing this page !')
            browser.quit()
            break
        else:
            speak('i want you to answer in yes, or ,no')
            continue


def speak(audio):
    engine.say(audio)
    engine.runAndWait()





def wishMe():
    hour=int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        speak('good morning')
    elif hour>=12 and hour<=18:
        speak('good afternoon')
    else:
        speak('good evening')





if __name__ == '__main__':
    wishMe()
    print('Type "open guide" or "guide" or "guide book to open guide book mesa"\nIf you want to skip or know the password then type "no"')
    speak('i am meesa, please enter the password , for guide , type from the following ')

    # time.sleep(0.3)

    # time.sleep(0.2)

perr=['yes','open it','open','sure','yup','yes it was','yep','good','sure why not','yea','not that bad','awesome','excellent','its was ok','ok ok','ok ok ok']


devel1=['i , meesa , was programmed by saurabh mehanti','i was designed by saurabh','developed in India by saurabh','i am programmed by saurabh']

naam=['My name is meesa, pleased to meet you','i am meesa , but you knew that already','my name is meesa , M , E , S , A']

wha=['i am listening !','go ahead !','what ?','what you want to know , just ask','dont be shy !, just tell me']

neg=['no','nope','leave it','do not open','let it go','negative','not again','no no','no no no','leave']

hel = ['hello mesa', 'hello', 'hey', 'hi', 'hie', 'hi mesa', 'hey mesa', 'hie mesa','namaste','namaskar','yo']

okaa=['Hmmmm','yep','what ok ?',"i'm not here for time pass !"]

than=['your welcome','my pleasure','no need to say thanks , it is my work','my pleasure.As always','i live to serve !','your wish is my command !']

gui1=['open guide','guide','show guide','mesa guide','guide book ','guide book of mesa']

doin=['nothing , just chilling','dealing with you','well , right now i am talking to you','i am practicing being more helpful'
      ,'just going for a round around globe']

bye=['bye mesa','quit','see you soon mesa','goodbye','bye','bye bye','tata','see you soon','ok bye','now you may leave','toodles','okay toodles']

than2=['thanks','thank you','thank you so much',"i'm thankful"]

abb=['fuck off','you bitch','get lost','shut up','keep your mouth shut','just keep quiet','keep quiet']

abb1=['you are so rude','why you are talking with me like this','i am your friend , dont talk with me like this','why are you getting rude ?'
      ,'this will make me angry']

jokk=['tell me a joke','tell a joke','make a joke','please tell me a joke',]

song=['sing for me','can you sing','do you sing','sing a song','just sing a song']

rap=['rap for me','can you rap','rap','i want to listen a rap','do some rap','do some rapping']
passs=['open it', 'point break']



while(True):
    password=takeCommand()

    if password in passs:
        speak('what is your name ?')
        passname=takeCommand()
        speak('welcome'+ passname + 'sir,what can i do')


    # elif password in gui1:
    #     book = open('mesa guide.txt')
    #     book1 = book.read()
    #     print(book1)
    #     speak('the user manual of meesa will show you ,how you can use this assistant to perform things.......please read it carefully.'
    #           'and then enter the password')
    #     continue

    else:

        speak('access denied')
        continue




    while(True):

        a=takeCommand().lower()


            #the user input.

        if 'search google' in a:
            speak('what you want to search?')
            dal1=['nothing','leave it','leave']
            dal=takeCommand()
            if dal in dal1:
                speak('okay, i will not search anything')
            else:
                speak('searching about'+ dal)
                browser=webdriver.Chrome('/Users/saurabhmehanti/Downloads/chromedriver\ 5')
                browser.get('https://www.google.com/search?q='+dal)
                time.sleep(2)
                BroClose()





        elif 'wikipedia' in a:
            speak('what you want to know ?')
            about=takeCommand()

            if 'leave' in about:
                speak('okay,not searching anything')
            else:

                speak('searching about' +about)
                result = wikipedia.summary(about, sentences=2)
                # speak(wikipedia.suggest(about))
                # print(wikipedia.suggest(about))
                print(result)
                speak(result)
                speak('shall i open the page?')

            opp=takeCommand()
            see=['yes','open it','open','sure','yup']
            if opp in see:
                speak('opening the web page about'+ about )
                webbrowser.open('https://en.wikipedia.org/wiki/'+ about)

            else:
                speak('hope you like the content')





        elif 'ask something' in a:
            speak(random.choice(wha))

        elif 'ok' in a:
            speak(random.choice(okaa))

        elif 'you doing' in a:
            speak(random.choice(doin))

        elif a in than2:
            speak(random.choice(than))

        elif 'useless' in a:
            use=['and you are so mean','you are the only one who made me , so think before you speak','but i just did what you asked !'
                 'i just tried to help you']
            speak(random.choice(use))




        elif 'how are you' in a:
            how=['i am good , what about you ?','i am healthy , thankyou' ,'awesome as always','dont you know ? i am the best !']
            speak(random.choice(how))



        elif 'fuck off' in a:
            speak(random.choice(abb1))

        elif 'bitch' in a:
            speak(random.choice(abb1))

        elif a in abb:
            speak(random.choice(abb1))






        elif 'not a good assistant' in a:
            assis=['why are you saying this ?','i just helped you','i was just helping you','okay, if you insist',"that doesn't sounds good"]
            speak(random.choice(assis))






        elif 'sleep' in a:
            speak('you want me to sleep for how much seconds ?')
            sl=takeCommand()
            try:
                speak(f'okay sleeping for ,{sl} seconds')
                time.sleep(int(sl))
                speak('hello sir i am back !')
            except Exception as e:
                speak('i cant sleep like this !')





        elif 'what is possible' in a:
            pos=['if you want , then nothing is impossible !','everything is possible .']
            speak(random.choice(pos))





        elif 'ability' in a:
            abi=['i have many ablities , just ask me to do something','i could do many task , just give me commands','if you want to know my ablities , '
                                                                                                                     'you can see it in my guide book']
            speak(random.choice(abi))






        elif 'news' in a:
            speak('here is the latest trending news on the web.')
            browser=webdriver.Chrome('/Users/saurabhmehanti/Downloads/chromedriver\ 5')
            browser.get('https://www.indiatoday.in/news.html')

            time.sleep(2)
            BroClose()





        elif 'images' in a:
            Images()

        elif 'photos' in a:
            Images()

        elif 'pics' in a:
            Images()





        elif 'gmail' in a:
            speak('opening gmail.')
            browser=webdriver.Chrome('/Users/saurabhmehanti/Downloads/chromedriver\ 5')
            browser.get('https://mail.google.com/mail/u/0/#inbox')

            time.sleep(2)
            BroClose()





        elif f'contact number' in a:
            speak('contact number of ?')
            con2=takeCommand()
            if con2 in cont:
                cont1=cont.get(con2)
                print()
                print(con2,':',cont1)
                speak(str(cont1))
            else:
                speak('no contact number found')





        elif 'meaning' in a:
            speak('meaning of which word ?')
            mean=takeCommand()
            speak('here is the meaning of , ' + mean)
            browser=webdriver.Chrome('/Users/saurabhmehanti/Downloads/chromedriver\ 5')
            browser.get('https://www.google.com/search?q=meaning%20of%20'+mean)

            time.sleep(2)
            BroClose()





        elif 'spelling' in a:
            speak('speak the word.')
            spel=takeCommand()
            for spel1 in spel:
                print(spel1.upper(),end=' '+'\n')




        elif 'online shopping' in a:
            Shop()

        elif 'online products' in a:
            Shop()

        elif 'products' in a:
            Shop()

        elif 'shopping' in a:
            Shop()





        # elif 'open camera' in a:
        #     speak('opening camera , to quit , press q')
        #
        #     video=cv2.VideoCapture(0)
        #     p=1
        #     while True:
        #         p=p+1
        #         check,frame=video.read()
        #         grey=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        #         cv2.imshow('capturing',grey)
        #         key=cv2.waitKey(1)
        #         speak('shall i close it ?')
        #         camm=takeCommand()
        #         if camm in perr:
        #             speak('closing camera !')
        #             print(p)
        #             video.release()
        #             cv2.destroyAllWindows()
        #
        #         elif neg in camm:
        #             continue


            # print(p)
            # video.release()
            # cv2.destroyAllWindows()





        elif 'youtube' in a:
            speak('what you want to search in youtube?')
            gana1=['nothing','leave it','leave']
            gana=takeCommand()
            if gana in gana1:
                speak('okay, i will not search anything')






            else:
                speak('searching '+ gana)
                browser=webdriver.Chrome('/Users/saurabhmehanti/Downloads/chromedriver\ 5')
                browser.get('https://www.youtube.com/results?search_query=' + gana )
                time.sleep(2)
                BroClose()



        elif 'made you' in a:
            speak(random.choice(devel1))

        elif 'developed' in a:
            speak(random.choice(devel1))

        elif 'develop' in a:
            speak(random.choice(devel1))

        elif 'designed' in a:
            speak(random.choice(devel1))

        elif 'design' in a:
            speak(random.choice(devel1))

        elif 'programmed' in a:
            speak(random.choice(devel1))






        elif 'lyrics' in a:
            speak('lyrics of which song')
            lyr=takeCommand()

            if 'leave' in lyr:
                speak('okay not showing you the lyrics')
            else:
                speak('who is the singer')
                singer = takeCommand()
                speak('opening the lyrics of' + lyr)
                webbrowser.open('https://www.azlyrics.com/lyrics/' + singer + '/' + lyr + '.html')






        elif 'play music' in a:
            speak('which song do you want to listen')
            song=takeCommand()
            speak('opening the song , '+song)
            browser=webdriver.Chrome('/Users/saurabhmehanti/Downloads/chromedriver\ 5')
            browser.get('https://wynk.in/music/detailsearch/'+song+'?q='+song)
            time.sleep(2)
            BroClose()





        elif 'listen a song' in a:
            speak('which song do you want to listen')
            song = takeCommand()
            speak('opening the song , ' + song)
            browser = webdriver.Chrome('/Users/saurabhmehanti/Downloads/chromedriver\ 5')
            browser.get('https://wynk.in/music/detailsearch/' + song + '?q=' + song)
            time.sleep(2)
            BroClose()




        elif 'play a song' in a:
            speak('which song do you want to listen')
            song = takeCommand()
            speak('opening the song , ' + song)
            browser = webdriver.Chrome('/Users/saurabhmehanti/Downloads/chromedriver\ 5')
            browser.get('https://wynk.in/music/detailsearch/' + song + '?q=' + song)
            time.sleep(2)
            BroClose()



        # elif ''


        elif 'website' in a:
            sitee()




        elif 'new tab' in a:
            speak('opening new tab in chrome')
            browser=webdriver.Chrome('/Users/saurabhmehanti/Downloads/chromedriver\ 5')
            browser.get('chrome-extension://clgckgfbhciacomhlchmgdnplmdiadbj/newtab.html#!/')
            time.sleep(2)
            BroClose()





        elif 'google docs' in a:
            speak('opening google documents')
            browser=webdriver.Chrome('/Users/saurabhmehanti/Downloads/chromedriver\ 5')
            browser.get('https://docs.google.com/document/u/0/')
            time.sleep(2)
            BroClose()





        elif 'google map' in a:
            speak('opening google maps')
            browser=webdriver.Chrome('/Users/saurabhmehanti/Downloads/chromedriver\ 5')
            browser.get('https://www.google.com/maps')
            time.sleep(2)
            BroClose()





        elif 'google drive' in a:
            speak('opening google drive')
            browser=webdriver.Chrome('/Users/saurabhmehanti/Downloads/chromedriver\ 5')
            browser.get('https://drive.google.com/drive/my-drive')
            time.sleep(2)
            BroClose()




        elif 'quotes' in a:
            speak('here are some quotes i found on the web')
            browser=webdriver.Chrome('/Users/saurabhmehanti/Downloads/chromedriver\ 5')
            browser.get('https://www.goodreads.com/quotes/tag/inspirational')
            time.sleep(2)
            BroClose()





        elif 'translate' in a:
            print('from which language \n')
            speak('from which language?')
            lann=takeCommand()
            if 'leave' in lann:
                speak('okay , not translating')
            else:
                print('to which language')
                speak('to which language')
                lann1 = takeCommand()
                speak('tell the word or sentance in ' + lann)
                give = takeCommand()
                tran()





        elif 'map' in a:
            speak('opening the globe')
            webbrowser.open('https://earth.google.com/web/')
            speak('Earth is the third planet from the Sun, and the only astronomical object known to harbor life.'
                  ' According to radiometric dating and other sources of evidence,'
                  ' Earth formed over 4.5 billion years ago. Earth"s gravity interacts with other objects in space, '
                  'especially the Sun and the Moon, Earth"s only natural satellite.'
                  ' Earth orbits around the Sun in 365.26 days, '
                  'a period known as an Earth year. During this time,'
                  ' Earth rotates about its axis about 366.26 times.')





        elif 'send email' in a:
            speak('send email to whome ?')
            email_s=input("sender's email id:  ")
            if 'leave' in email_s:

                speak('okay , not sending email to anybody')
            else:
                try:
                    speak('speak your message?')
                    print('your message: ')
                    content = takeCommand()
                    to = email_s
                    print('From: YOUR_NAME')
                    print('To:',email_s)
                    print('send material:',content)
                    sendMail(to, content)
                    speak('email has been send')
                except Exception as e:
                    print(e)
                    speak('sorry,problem occured while sending mail')





        elif 'guide book' in a:
            speak('the guide book tells more about mesa ')
            book = open('mesa guide.txt')
            book1 = book.read()
            print(book1)




        elif 'time' in a:
            print(time.ctime())
            speak('The time is, '+ time.ctime())







        elif 'what can you do' in a:
            un=open('wha.txt')
            uni=un.read()
            print(uni)
            un.close()

            speak('i can do many tasks, like opening gmail ,and, other websites, search in wikipedia, youtube   ,and i can also '
                  'translate into different languages , sending emails to others.')





        elif 'mimic' in a:
            speak('i will try..give me the sentence')
            while True:

                mim=takeCommand()
                if mim in neg:
                    speak('okay i am not doing now')
                    break
                else:
                    speak(mim)
                    time.sleep(0.8)
                    speak('was that good ?')
                    mim2 = takeCommand()
                    if mim2 in perr:
                        speak('thank you , lets do it again .')
                        continue
                    else:
                        speak('give me another chance !')
                        continue



        elif 'repeat after me' in a:
            speak('i will try..give me the sentence')
            while True:

                mim=takeCommand()
                if mim in neg:
                    speak('okay i am not doing now')
                    break
                else:
                    speak(mim)
                    time.sleep(0.8)
                    speak('was that good ?')
                    mim2 = takeCommand()
                    if mim2 in perr:
                        speak('thank you , lets do it again .')
                        continue
                    else:
                        speak('give me another chance !')
                        continue






        elif a in song:
            speak('okay , listen this song')
            time.sleep(0.8)

            song1=["my name's blurry face and , i care what you think , my name's blurry face and  , i care what you think , wish we could turn"
                "back time to the good old days , when the mama said us, to sleep , but now we're stressed out",
                "damn , who knew all the planes we flew good things we've been through , that i'll be standing right here talking"
                "to you about another path , i know we love to hit the road and laugh ,  it's been a long day without you my friend , "
                "and i tell you all about it when i see you again.",'you better lose yourself in the music th moments you own it you '
                                                                    'better let it go , you only get one shot do not miss your chance'
                                                                    'to blow , this opportunity comes once in a life time.'
                 ,"I . . . i've been try to fix my pride but that shit is broken . lie , lie , lie . lielielie i tried to hide but now you know it . "
                  "that i'm at an all time low low low , low lowlowlowlowlow","lately i've been hard to reach , i've been too long on my own"
                                                                              ", everybody has a private world where they cn be alone , "
                                                                              "are you calling me ? are to trying to get through ? are you reaching out"
                                                                              "for me , like i'm reaching out for you !"]

            song2=random.choice(song1)
            speak(song2)




        elif a in rap:
            rap1=["boots and cats and boots and cats and boots and cats and booms but chip and boot this bat yo give me cat and have some tat , yeah"
                  ,"chip chap chop i am a dope don't be in hope boots chick bum play that drum , dhinchak din dinchak dinchak din dinchak"]

            speak(random.choice(rap1))





        elif 'head or tail' in a:
            HT=['head','tail']
            HTT=random.choice(HT)
            print(HTT)
            speak("its , " + HTT)




        elif a in hel:
            bb=['namaste!','namaskar!','hey!','hello!','hola!','bonjour!','hello, human!']
            bb1=random.choice(bb)
            print(bb1)
            speak(bb1)




        elif 'your name' in a:
            naam2=random.choice(naam)
            speak(naam2)




            # speak('this is my favourite rap ...... meri gully mai gully gully gully mai')



 # if you have to make changes or suggest something press '#' and then start typing.
 # the further code will be written here





        elif a in bye:
            bye2=['bye ,untill we talk again!','bye ,see you soon!','okay ,i am going!','bye for now!','pleasure talking to you','have a nice day',
                  'tata, bye bye','adios amigo','']

            bye3=random.choice(bye2)
            speak(bye3)
            exit()




        elif 'calander' in a:
            speak('opening calander')
            browser=webdriver.Chrome('/Users/saurabhmehanti/Downloads/chromedriver\ 5')
            browser.get('https://calendar.google.com/calendar/r/year?pli=1')
            time.sleep(2)
            BroClose()





        elif 'who' in a:
            ques()

        elif 'what' in a:
            ques()

        elif 'how' in a:
            ques()

        elif 'where' in a:
            ques()

        elif 'when' in a:
            ques()

        elif 'why' in a:
            ques()

        elif 'which' in a:
            ques()





        elif 'universe' in a:
            webbrowser.open('https://scaleofuniverse.com/')
            speak('let me show you what is the actual size of universe.')



        # elif in a:
        #
        #     speak('are you there ?')
        #     bla=takeCommand()
        #     if 'yes' in bla:
        #         speak('then what can i do ?')
        #     elif 'no' in a:
        #         speak('okay then i am going')
        #         exit()
        #     else:
        #         speak('sorry i was not able to hear you , can you say that again ?')


        else:
            ell=['this may be not possible','this maybe beyond my abilities','i am not programmed to do this']
            speak(random.choice(ell))


                # webbrowser.open('https://www.google.com/search?q='+somm)




