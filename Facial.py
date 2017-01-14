#1) Learn to Use Facebook API

#2) Login Facebook

#3) Take a group of friends

#4) 




import webbrowser #needed in order to navigate to specific Facebook site













def lookup(username):
    #has to take a username and search the internet for it, bringing up the user's facebook


    link = 'https://www.facebook.com/' + username

    webbrowser.open_new(link)

    if webbrowser.open_new(link) == False:
        print('We cannot complete the request due to a username error.')








def recognize(array):
    result = ''
    for key in array:
        result += (str(key) + '\n')

    if len(array) == 1:
        print('Here is the user we matched to the photo: ')
        print(result)
        tofacebook = input("Would you like to visit the user's profile? Y/N\n")
        if tofacebook.upper() == Y:
            lookup()
            return None #check
        else:
            return result
    elif len(array) == 0:
        print('The program returned no matches. ')
        restart = input('Do you have another photo you would like to use? Y/N \n')




    else:
        sorted_list = []
        for key in array:
            entry = str(key) + ' : ' + str(array[key])
            sorted_list.append(entry)
            




    print('There were', str(len(array)), 'user_names that could be matched based on the photo.' )
    print('Here are the user_names of possible matches:')
    print(result)



























