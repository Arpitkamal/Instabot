import requests

ACCESS_TOKEN='3058343516.08021fa.52601b83bc7a4805957fdc846befcdea'
BASE_URL='https://api.instagram.com/v1/'

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


def get_user_id(insta_name):
    request_url= BASE_URL+"users/search?q=%s&%s"%(insta_name,ACCESS_TOKEN)
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


def get_user_info(insta_name):
    user_id=get_user_id(insta_name)
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



