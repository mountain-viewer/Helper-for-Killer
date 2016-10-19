# -*- coding: utf-8 -*-

import requests

# User number
num_users = 877

# Patterns
pattern_username = '<span id="fullname" class="robotomedium">'
pattern_groupnumber = '<span class="param">Группа:</span> <span class="pull-right">'
pattern_phonenumber = '<span class="param">Телефон:</span> <span class="pull-right">'
pattern_roomnumber = '<span class="param">Комната:</span>  <span class="pull-right">'

# Bad request
bad_request = 'Сайт общежития №2 (ФИВТ) - 404 (Not Found)'

# Find username in HTML doc and return it
def get_username(page_content):
  if page_content.find(bad_request) != -1:
    return 'Deleted profile'
  
  begin = page_content.find(pattern_username)

  if begin == -1:
    return 'No name'

  end = page_content.find('</span>', begin + len(pattern_username))

  return page_content[begin + len(pattern_username) : end]


# Find group number in HTML doc and return it
def get_groupnumber(page_content):
  if page_content.find(bad_request) != -1:
    return 'Deleted profile'
  
  begin = page_content.find(pattern_groupnumber)
  
  if begin == -1:
    return 'No group number'

  end = page_content.find('</span>', begin + len(pattern_groupnumber))
  
  return page_content[begin + len(pattern_groupnumber) : end]


# Find phone number in HTML doc and return it
def get_phonenumber(page_content):
  if page_content.find(bad_request) != -1:
    return 'Deleted profile'
  
  begin = page_content.find(pattern_phonenumber)

  if begin == -1:
    return 'No phone number'

  end = page_content.find('</span>', begin + len(pattern_phonenumber))
  
  return page_content[begin + len(pattern_phonenumber) : end]


# Find room number in HTML doc and return it
def get_roomnumber(page_content):
  if page_content.find(bad_request) != -1:
    return 'Deleted profile'
  
  begin = page_content.find(pattern_roomnumber)

  if begin == -1:
    return 'No room number'

  end = page_content.find('</span>', begin + len(pattern_roomnumber))
  
  return page_content[begin + len(pattern_roomnumber) : end]


# Get userinfo as a tuple
def get_userinfo(session, profile_format, id):
  webpage = session.get(profile_format % id)
  content = webpage.content
  
  return (get_username(content),
          get_groupnumber(content),
          get_phonenumber(content),
          get_roomnumber(content),
          profile_format % id)



# Iterating over all pages
def loop(session, profile_format):
  result = []
  for id in xrange(1, num_users + 1):
    print 'Processing at the moment: ' + profile_format % id
    result.append(get_userinfo(session, profile_format, id))
  return result


# Authentication and downloading info
def create_session(auth_address, user, passwd, home_address, profile_format):
  with requests.Session() as session:
    session.get(auth_address)
    csrftoken = session.cookies['csrftoken']
    
    login_data = dict(csrfmiddlewaretoken=csrftoken,
                      username=user,
                      password=passwd,
                      next='/')

    session.post(auth_address, data=login_data, headers={"Referer": home_address})
    result = loop(session, profile_format)

    return result




