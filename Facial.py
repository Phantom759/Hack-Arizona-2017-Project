#1) Learn to Use Facebook API

#2) Login Facebook

#3) Take a group of friends

#4) 



'''
import webbrowser, os #needed in order to navigate to specific Facebook site

'''


from fbrecog import recognize #imports 



cookies = 'datr=v94jV6FYsoDjcXtJA07NI3CW; lu=gAAhKMppCH_jMiD0DSUmuRXg; sb=yd4jVwqrv56caCxPhbFx3x9V; c_user=100001140458819; xs=119%3A8DKsSWTSPKCXig%3A2%3A1461968585%3A19449; fr=0gYKbsXA1zk19JSnp.AWWq093dzb-xUjsEZ_rkwdTAn5I.BXI97J._m.FhZ.0.0.BYenWj.AWWDpFyP; csm=2; s=Aa6UTgwLvMVHappN.BYedDW; p=-2; presence=EDvF3EtimeF1484420880EuserFA21B01140458819A2EstateFDutF1484420880314CEchFDp_5f1B01140458819F5CC; act=1484420905734%2F3'

fb_dtsg = 'AQHf6f1fB-2V:AQHscGuQOiPK'

path = '/home/rysterman34/Desktop/Hackathons/FamiliarFaceProject/TestPhoto3' #Insert your image file path here
access_token = '' #Insert your access token obtained from Graph API explorer here




print(recognize(path,access_token,cookies,fb_dtsg))

#print(recognizer)





#print(recognize(path,access_token,cookie,fb_dtsg))

'''







def lookup(username):
    #has to take a username and search the internet for it, bringing up the user's facebook
    link = 'https://www.facebook.com/' + username
    if webbrowser.open_new(link) == False:
        print('We cannot complete the request due to a username error.')
        return None

    else:
        webbrowser.open_new(link)




def recognize(array):
    result = ''
    for key in array:
        result += (str(key) + '\n')

    if len(array) == 1:
        print('Here is the user we matched to the photo: ')
        print(result)
        visit_user = input("Would you like to visit the user's profile? Y/N\n")
        if visit_user.upper() == Y:
            lookup(key) #needs winning username
            #return None **********************************************check
        else:
            restart = input('Do you have another photo you would like to use? Y/N \n')
            if restart.upper() == 'Y':
                recognize() #need to restart Facebook API

    elif len(array) == 0:
        print('The program returned no matches. ')
        restart = input('Do you have another photo you would like to use? Y/N \n')

    else:
        ranked_list = []
        sorted_array = sorted(array.items(), key=operator.itemgetter(1))
        i = 1
        for key in sorted_array:
            ranked_list.append(str(key))
        print('The list below is sorted by matching relevance.')
        if len(ranked_list) < 3:
            print('These are the', str(len(ranked_list)), 'matches we have, listed in groups of 3.')
            for i in range(len(ranked_list) - 2):
                print(ranked_list[i:i+2])
                choose = input('Do any of these profiles match the picture? If yes, which one? \n')










    print('There were', str(len(array)), 'user_names that could be matched based on the photo.' )
    print('Here are the user_names of possible matches:')
    print(result)
'''