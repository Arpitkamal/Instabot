# import requests library for working of get,post,push,delete
import requests
# import urllib library for download image
import urllib
# textblob library is use to show that how much the text is negative and positive (nlp)
# NaiveBayesAnalyzer is analyzer which analyze the text
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer

# daclaration of global variable
ACCESS_TOKEN='3058343516.08021fa.52601b83bc7a4805957fdc846befcdea'
BASE_URL='https://api.instagram.com/v1/'

#function daclaration to get own info

def self_info():
    # fromalise the request url using the instagram API and attaching access token with it
    request_url= (BASE_URL+"users/self/?access_token=%s") %(ACCESS_TOKEN)
    print "GET request url :%s" %(request_url)
    # hitting the url using get() and using the json function to decode the object and storing it in own_media
    user_info=requests.get(request_url).json()
    if user_info['meta']['code']==200:
        if len(user_info['data']):
            print "username: %s" %(user_info['data']['username'])
            print "No. of followers: %s" %(user_info['data']['counts']['followed_by'])
            print "No of people you are following:%s" %(user_info['data']['counts']['follows'])
            print "no of posts :%s" %(user_info['data']['counts']['media'])
        else:
            print "user does not exist"
    else:
        print "status code is other than 200 received"

# function is use to get the media_id of recent post
def get_post_id(insta_username):
    user_id=get_user_id(insta_username)
    if user_id==None:
        print "user does not exist"
        exit()
     # fromalise the request url using the instagram API and attaching access token with it
    request_url=(BASE_URL+"users/%s/media/recent/?access_token=%s") %(user_id,ACCESS_TOKEN)
    print "GET request url =%s" %(request_url)
    # hitting the url using get() and using the json function to decode the object and storing it in post_id
    post_id=requests.get(request_url).json()

    if post_id['meta']['code']==200:
        if len(post_id['data']):
            return post_id['data'][0]['id']
        else:
            print "there is no recent post of user"
    else:
        print "status code is other than 200 received"
        exit()


#function daclaration to get the user_id of user by username

def get_user_id(insta_username):
    # fromalise the request url using the instagram API and attaching access token with it
    request_url= (BASE_URL+"users/search?q=%s &access_token=%s") %(insta_username,ACCESS_TOKEN)
    print "get request url :%s"%(request_url)
    # hitting the url using get() and using the json function to decode the object and storing it in user_info
    users_info=requests.get(request_url).json()

    if users_info['meta']['code']==200:
        if len(users_info['data']):
            return users_info['data'][0]['id']
        else:
            print "Invalid name!... Enter instagram username"
            return None
    else:
        print "status code is other than 200 received"
        exit()

# function get_user_info use to get the info of any user by giving user_id

def get_user_info(insta_username):
    user_id=get_user_id(insta_username)
    if user_id==None:
        exit()
    # fromalise the request url using the instagram API and attaching access token with it
    request_url=(BASE_URL+"users/%s?&access_token=%s")%(user_id,ACCESS_TOKEN)
    print "get request url :%s"%(request_url)
    # hitting the url using get() and using the json function to decode the object and storing it in user_info
    user_info=requests.get(request_url).json()

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
    # fromalise the request url using the instagram API and attaching access token with it
    request_url=(BASE_URL+"users/self/media/recent/?access_token=%s") %(ACCESS_TOKEN)
    print "get request url :%s" %(request_url)
    # hitting the url using get() and using the json function to decode the object and storing it in media_info
    media_info=requests.get(request_url).json()

    if media_info['meta']['code']==200:
        if len(media_info['data']):
            image_name= media_info['data'][0]['id']+".jpg"
            image_url=media_info['data'][0]['images']['standard_resolution']['url']
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
    # fromalise the request url using the instagram API and attaching access token with it
    request_url=(BASE_URL+"users/%s/media/recent/?access_token=%s") %(user_id,ACCESS_TOKEN)
    print "get request url: %s" %(request_url)
    # hitting the url using get() and using the json function to decode the object and storing it in user_media
    user_media=requests.get(request_url).json()

    if user_media['meta']['code']==200:
        if len(user_media['data']):
            image_name=user_media['data'][0]['id']+".jpeg"
            image_url=user_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url,image_name)
            print "your image has been downloaded"
        else:
            print "post does not exist"
    else:
        print "status code is other than 200 received"



#funtion is use to display the name of user who  recently like the post of media id vala user
def get_recent_like(insta_username):
    media_id=get_post_id(insta_username)
    # fromalise the request url using the instagram API and attaching access token with it
    request_url=(BASE_URL+"media/%s/likes?access_token=%s") %(media_id,ACCESS_TOKEN)
    print "GET request url : %s" %(request_url)
    # hitting the url using get() and using the json function to decode the object and storing it in own_media
    like_info=requests.get(request_url).json()

    if like_info['meta']['code']==200:
        if len(like_info['data']):
            for x in range(len(like_info['data'])):
                print str(x)+"."+like_info['data'][x]['username']
        else:
             print "post does not exist"
    else:
        print "status code is other than 200 received"

# function is use to display the recent comment on the users post (media id vala)

def get_recent_comments(insta_username):
    media_id=get_post_id(insta_username)
    # fromalise the request url using the instagram API and attaching access token with it
    request_url=(BASE_URL+"media/%s/comments?access_token=%s") %(media_id,ACCESS_TOKEN)
    print "GET request url:%s" %(request_url)
    # hitting the url using get() and using the json function to decode the object and storing it in own_media
    comment_info=requests.get(request_url).json()

    if comment_info['meta']['code']==200:
        if len(comment_info['data']):
            for x in range(len(comment_info['data'])):
                print "comments are :"
                print str(x)+" . "+comment_info['data'][x]['from']['username']+" : "+comment_info['data'][x]['text']
        else:
            print "post have no comments"
    else:
        print "status code is other than 200 received"


#function is use to like the user post by its media_id
def like_a_post(insta_username):
    media_id=get_post_id(insta_username)
    # fromalise the request url using the instagram API and attaching access token in payload
    request_url=(BASE_URL+"media/%s/likes") %(media_id)
    #when we are using post function access_token is attached in payload
    payload= {"access_token":ACCESS_TOKEN}
    print "POST request url %s" %(request_url)
    # hitting the url using post() and using the json function to decode the object and storing it in post_like
    post_like=requests.post(request_url,payload).json()

    if post_like['meta']['code']==200:
        print "like was successful"
    else:
        print "your like was unsuccessful. try again !"


#function post_a_comment() use to add comment on instagram post
def post_a_comment(username):
    media_id=get_post_id(username)
    #take text from user which is use to comment on post
    comment_text=raw_input("your comment")
    #using post() access token and the comment_text attachde in payload
    payload = {"access_token": ACCESS_TOKEN, "text": comment_text}
    request_url=(BASE_URL+"media/%s/comments") %(media_id)
    print "post request url %s" %(request_url)
    # hitting the url using post() and using the json function to decode the object and storing it in comment_info
    comment_info=requests.post(request_url,payload).json()

    if comment_info['meta']['code']==200:
        print "successfully added a new comment"
    else:
        print"unable to add comment .try again!"

def delete_negative_comment(insta_username):
    media_id=get_post_id(insta_username)
    # fromalise the request url using the instagram API and attaching access token with it
    request_url=(BASE_URL+"media/%s/comments?access_token=%s") %(media_id,ACCESS_TOKEN)
    print "GET request url :%s" %(request_url)
    # hitting the url using get() and using the json function to decode the object and storing it in comment_info
    comment_info=requests.get(request_url).json()


    if comment_info['meta']['code']==200:
        if len(comment_info['data']):
        #
            print "what you want to do ?"
            print "1.delete neagtive comments"
            print "2.delete the comment with not accepted content"
            choice=int(raw_input("enter your choice "))
            if choice==1:
                for x in range(0,len(comment_info['data'])):
                    comment_id=comment_info['data'][x]['id']
                    comment_text=comment_info['data'][x]['text']
                    blob= TextBlob(comment_text,analyzer=NaiveBayesAnalyzer())
                    # when negtive comment bot will delete
                    if (blob.sentiment.p_neg > blob.sentiment.p_pos):
                        print "Negitive comment :%s"%(comment_text)
                        delete_url=(BASE_URL+"media/%s/comments/%s/?access_token=%s") %(media_id,comment_id,ACCESS_TOKEN)
                        print "DELETE request url :%s" %(delete_url)
                        delete_info=requests.delete(delete_url).json()

                        if delete_info['meta']['code']==200:
                            print "Negative comment successfully deleted !"
                        else:
                            print "unable to delete comment"
                    else:
                        print "positive comment :%s " %(comment_text)
                # when user don't like the content of comment
            if choice==2:
                # not_accepted_text is use to delete comment which user dont like
                # eg- friends call the user by diffent name which user dont like
                not_accepted_text = raw_input("enter the word that you don't want in comment bot will delete that comment: ")

                for x in range(0,len(comment_info['data'])):
                    comment_id=comment_info['data'][x]['id']
                    comment_text=comment_info['data'][x]['text']
                    if not_accepted_text in comment_text:
                        print "Negative comment :%s " %(comment_text)
                        delete_url=(BASE_URL+"media/%s/comments/%s/?access_token=%s") %(media_id,comment_id,ACCESS_TOKEN)
                        delete_info = requests.delete(delete_url).json()

                        if delete_info['meta']['code']==200:
                            print "comment successfully deleted!\n"
                        else:
                            print "unable to delete comment "
                    else:
                        print "comment %s does not contain not_accepted_text " %(str(x))

        else:
            print "There is no comment in this post"
    else:
        print "status code other than 200 received"

def get_own_likes():
    #fromalise the request url using the instagram API and attaching access token with it
    request_url=(BASE_URL+"users/self/media/liked?access_token=%s") %(ACCESS_TOKEN)
    print "GET request url :%s " %(request_url)
    # hitting the url using get() and using the json function to decode the object and storing it in own_media
    own_media=requests.get(request_url).json()
    #checking if the status code is 200 i.e accepted or success
    if own_media['meta']['code']==200:
        # checking is the the data  exist in json object
        if len(own_media['data']):
            #printing the id of most recent liked media
            print "id "+own_media['data'][0]['user']['id']
            print "id "+own_media['data'][1]['images']['thumbnail']['url']
            # using urllib to download the most recent post
            image_name=own_media['data'][0]['id']+".jpeg"
            image_url=own_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url,image_name)
            print "your image has been downloaded"
        else:
            print"There is no recent post"

    else:
        print "status code other than 200 received"



def start_bot():
    while True:
        print "\n"
        print "Hey! welcome to instabot"
        print "Here are your menu options"
        print "1.Get your own details"
        print "2.Get details of user by username"
        print "3.Get your own recent post"
        print "4.Get the recent post of user by username"
        print "5.Get the list of people who have liked the recent post of a user"
        print "6.Like recent post of a user"
        print "7.Get the the list of comments on recent post"
        print "8.Make a comment on recent post of a user"
        print "9.Delete a negative comment from recent post of user"
        print "10.Get the  recent media liked by you"
        print "11.Exit"

        choice=int(raw_input("Enter your choice"))
        if choice == 1:
            self_info()
        elif choice == 2:
            user_name=raw_input("enter the instagram username of the user")
            get_user_info(user_name)
        elif choice == 3:
            get_own_post()
        elif choice == 4:
            user_name=raw_input("enter the instagram username of the user")
            get_users_posts(user_name)
        elif choice == 5:
            user_name=raw_input("enter the instagram username of the user")
            get_recent_like(user_name)
        elif choice == 6:
            user_name=raw_input("enter the instagram username of the user")
            like_a_post(user_name)
        elif choice == 7:
            user_name=raw_input("enter the instagram username of the user")
            get_recent_comments(user_name)
        elif choice == 8:
            user_name=raw_input("enter the instagram username of the user")
            post_a_comment(user_name)
        elif choice == 9:
            user_name=raw_input("enter the instagram username of the user")
            delete_negative_comment(user_name)
        elif choice == 10:
            get_own_post()
        elif choice==11:
            exit()



start_bot()