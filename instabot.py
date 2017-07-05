# import requests library for working of get,post,push,delete
import requests
# import urllib library for download image
import urllib

ACCESS_TOKEN='3058343516.08021fa.52601b83bc7a4805957fdc846befcdea'
BASE_URL='https://api.instagram.com/v1/'

#function daclaration to get own info

def self_info():
    request_url= BASE_URL+"uses/self/?access_token="+ACCESS_TOKEN
    print "GET request url :%s" %(request_url)
    user_info=requests.get(request_url).json()

    if user_info['mets']['code']==200:
        if len(user_info['data']):
            print "username: %s" %(user_info['data']['username'])
            print "No. of followers: %s" %(user_info['data']['counts']['followed_by'])
            print "No of people you are following" %(user_info['data']['counts']['follows'])
            print "no of posts :%s" %(user_info['data']['counts']['media'])
        else:
            print "user does not exist"
    else:
        print "status code is other than 200 received"

#function daclaration to get the id of user by username

def get_user_id(insta_username):
    request_url= BASE_URL+"users/search?q=%s&%s"%(insta_username,ACCESS_TOKEN)
    print "get request url :%s"%(request_url)
    users_info=request_url.get(request_url).json()

    if users_info['meta']['code']==200:
        if len(users_info['data']):
            return users_info['data'][0]['id']
        else:
            return None

    else:
        print "status code is other than 200 received"
        exit()

# function get_user_info use to get the info of any user by giving user_id

def get_user_info(insta_username):
    user_id=get_user_id(insta_username)
    if user_id==None:
        exit()
    request_url=BASE_URL+"users/%s?&access_token=%s" %(user_id,ACCESS_TOKEN)
    print "get request url :%s"%(request_url)
    user_info=request_url.get(request_url).json()

    if user_info['meta']['code']==200:
        if len(user_info['data']):
            print "usersname :%s" %(user_info['data']['username'])
            print "No of followers:%s" %(user_info['data']['counts']['follows'])
            print "No. of people you are following:%s" %(user_info['data']['counts']['followed_by'])
            print "No. of posts:%s" %(user_info['data']['counts']['media'])
        else:
            print "there is no data for this user!"
    else:
        print "status code is other than 200 received"


#function get_own_post() is use to get own recent post

def get_own_post():
    request_url=BASE_URL+"users/self/media/recent/?access_token=%s" %(ACCESS_TOKEN)
    print "get request url :%s" %(request_url)
    own_media=requests.get(request_url).json()

    if own_media['meta']['code']==200:
        if len(own_media('data')):
            image_name= own_media['data'][0]['id']+".jpg"
            image_url=own_media['data'][0]['image']['standard_resolution']['url']
            urllib.urlretrieve(image_url,image_name)
            print "your image has been downloaded!"
        else:
            print "post does not exist"
    else:
        print "status code is other than 200 received"

# function get_users_posts() is use to get the user recent post by the username

def get_users_posts(insta_username):
    user_id=get_user_id(insta_username)
    if user_id==None:
        exit()

    request_url=BASE_URL+"users/%s/media/recent/?access_token=%s" %(user_id,ACCESS_TOKEN)
    print "get request url: %s" %(request_url)
    user_media=requests.get(request_url).json()

    if user_media['meta']['code']==200:
        if len(user_media['data']):
            image_name=user_media['data'][0]['id']+".jpeg"
            image_url=user_media['data'][0]['image']['standard_resolution']['url']
            urllib.urlretrieve(image_url,image_name)
            print "your image has been downloaded"
        else:
            print "post does not exist"
    else:
        print "status code is other than 200 received"


def start_bot():
    while True:
        print "\n"
        print "hey! welcome to instabot"
        print "here are your menu options"
        print "1.get your own details\n"
        print "2.get details of user by username\n"
        print "3.get your own recent post\n"
        print "4.get the recent post of user by username\n"
        print "5.exit"

        choice=int(raw_input("Enter your choice"))
        if choice == "1":
            self_info()
        elif choice == "2":
            user_name=raw_input("enter the instagram username of the user")
            get_user_info(user_name)
        elif choice == "3":
            get_own_post()
        elif choice == "4":
            user_name=raw_input("enter the instagram username of the user")
            get_users_posts(user_name)
        elif choice == "5":
            exit()


start_bot()