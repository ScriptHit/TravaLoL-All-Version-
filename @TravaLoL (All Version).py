import requests
import json
import os
import sys
import urllib.parse
import six
import riotgames_api

lolcapi = riotgames_api.LeagueOfLegendsClientAPI()

def createlobby():
    lolcapi.post('/lol-lobby/v2/lobby', {"queueId": 700})
    
def userinfo(username):
    summoner = lolcapi.get('/lol-summoner/v1/summoners?name=%s' % username)
    accountid = summoner.get("summonerId")
    return accountid
        
def menu():
    print('----------------------------------------------------------------')
    print('@TravaLOL - 1. Username')
    print('@TravaLOL - 2. SummonerID')
    print('@TravaLOL - 3. Check User')
    print('@TravaLOL - 4. Create a Lobby (TFT Tutorial)')
    print('@TravaLOL - 5. Credits')
    print('----------------------------------------------------------------')
    selection = int(input('Choose a option: '))
    global accountid
    if selection == 1:  
        user = input('Username: ')
        userformated = urllib.parse.quote(user)
        accountid = userinfo(userformated)
    if selection == 2:
        accountid = input('SummonerID: ')
    if selection == 3:  
        user = input('Username: ')
        userformated = urllib.parse.quote(user)
        accountid = userinfo(userformated)
        print('----------------------------------------------------------------')
        print('@TravaLOL - SummonerID: %s' % accountid)
        menu()
    if selection == 4:
        createlobby()
        menu()
    if selection == 5:
        print('----------------------------------------------------------------')
        print("@TravaLOL - Made by: @dollyXtoddy")
        menu()    
    ## // Antigo sistema de whitelist //
    #try:
        #with six.moves.urllib.request.urlopen('Lista de usuários na whitelist') as f:
            #test2 = f.read().decode('utf-8')
            #teste3 = json.loads(test2)
            #for i in teste3['whitelist']:
                #if accountid == i['id']:
                    #anykey = input('@TravaLOL - Whitelisted User. \nPress ENTER to continue...')
                    #menu()
    #except urllib.error.URLError as e:
        #print(e.reason)        
    while True:
        print('-------')
        r = lolcapi.post('/lol-lobby/v2/lobby/invitations', [{"toSummonerId":accountid}])
        print('@TravaLOL - Invite: %s (%s)' % (r.status_code, accountid))
        print('-------')
        r2 = lolcapi.post('/lol-lobby/v2/lobby/members/%s/kick' % accountid)
        print('@TravaLOL - Kick: %s (%s)' % (r2.status_code, accountid))
        print('-------')
    
try:
    menu()
except KeyboardInterrupt:
    sys.exit(0)