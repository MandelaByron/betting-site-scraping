from datetime import datetime
import requests
import json
import time
from itertools import count
competions={
    'England':"https://vleague1.premierbet.incentivegames.com/sportsapi/vcompetition/1",
    'Spain':"https://vleague1.premierbet.incentivegames.com/sportsapi/vcompetition/2",
    'Africa':"https://vleague1.premierbet.incentivegames.com/sportsapi/vcompetition/3",
    'World':"https://vleague1.premierbet.incentivegames.com/sportsapi/vcompetition/4"
}
# table = "https://vleague1.premierbet.incentivegames.com/sportsapi/vcompetition/1/23/table"
competion_status_url = "https://vleague1.premierbet.incentivegames.com/sportsapi/vcompetition/1"
# matches_url= "https://vleague1.premierbet.incentivegames.com/sportsapi/vcompetition/1/17"
# result_url = "https://vleague1.premierbet.incentivegames.com/sportsapi/vcompetition/1/15/results"

payload = ""
headers = {
    "authority": "vleague1.premierbet.incentivegames.com",
    "accept": "application/json, text/plain, */*",
    "accept-language": "en-US,en;q=0.5",
    "cache-control": "no-cache",
    "dnt": "1",
    "pragma": "no-cache",
    "referer": "https://vleague1.premierbet.incentivegames.com/",
    
    "sec-ch-ua-mobile": "?0",

    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "sec-gpc": "1",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
}
def get_response(url):
    response = requests.get(url, headers=headers)
    print(response.status_code)
    return response.json()
def datefromtimestamp(timestamp):
    date = datetime.utcfromtimestamp(timestamp/1000).strftime('%Y-%m-%d %H:%M:%S')
    return date


response = get_response(competion_status_url)
data=response
gameweek=data["currentGameWeekId"]
#result_url = f"https://vleague1.premierbet.incentivegames.com/sportsapi/vcompetition/1/{gameweek}/results"
def get_results(competion_slug):
    

        ##"https://vleague1.premierbet.incentivegames.com/sportsapi/vcompetition/1
    # result_url = f"{competion_slug}/{gameweek}/results"
    # response = get_response(result_url)
    for i in count(1):
        result_url = f"{competion_slug}/{gameweek}/results"
        response = get_response(result_url)
        status =response['matches'][0]['status']
        print("match status -",status)
        if status == 'fulltime':
            break
        
    results =[]
    for match in response['matches']:
        #print(match)
        home_team = match['homeTeam']['teamName']
        away_team = match['awayTeam']['teamName']
        status = match['status']    
        home_team_score = match['homeScore']
        away_team_score = match['awayScore']
        res ={
            'status':status,
            "team_1":home_team, # type:str
            "team_2":away_team, # type:str
            "team_1_score":home_team_score, # type:int
            "team_2_score":away_team_score
        }
        
        results.append(res)
        #print(res)
    return results

def get_odds(competion_slug):
     ##"https://vleague1.premierbet.incentivegames.com/sportsapi/vcompetition/1
    matches_url = f"{competion_slug}/{gameweek}"

    match_data=get_response(matches_url)
    season_number = match_data['seasonNumber']
    season_start_ts = match_data['seasonStartTime']
    start_time =datefromtimestamp(season_start_ts)
    odds_list = []
    for index,match in enumerate(match_data['matches']):
        
        #print(match['homeTeam']['teamName'],' - ' , match['awayTeam']['teamName'])
        home_team=match['homeTeam']['teamName']
        away_team=match['awayTeam']['teamName']
        markets = match['markets']
        
        btts_yes = markets[1]['selections'][0]['price']['decimal']
        btts_no = markets[1]['selections'][1]['price']['decimal']
        
        over = markets[2]['selections'][0]['price']['decimal']
        under =markets[2]['selections'][1]['price']['decimal']
        
        home_win = markets[0]['selections'][0]['price']['decimal']
        away_win = markets[0]['selections'][2]['price']['decimal']
        draw = markets[0]['selections'][1]['price']['decimal']
        
        dc_12 =markets[3]['selections'][0]['price']['decimal']
        dc_1x =markets[3]['selections'][1]['price']['decimal']
        dc_2x =markets[3]['selections'][2]['price']['decimal']
        #get_markets(markets=markets)
        odds = {
            
            "index":index, # type:int This is the position of the match
            "team_1":home_team, # type:str
            "team_2":away_team, 
            "btts":{
                    "odds":{
                    "Yes": btts_yes, # type:float
                    "No": btts_no # type:float
                }
                
            },
            "o/u 2.5":{
                "odds": {
                    "Over": over,
                    "Under": under
                }
            },
            
            "1X2":{
                "odds":{
                    "1":home_win,
                    "x":draw,
                    "2":away_win
                }
            },
            
            "dc": {
                "odds":{
                    "12":dc_12,
                    "1x":dc_1x,
                    "2x":dc_2x
                }
            }
                    
      
        }
                    
 
        #print(odds)
        odds_list.append(odds)
    return odds_list

    


def get_table(competion_slug):
    url = f"{competion_slug}/{gameweek}/table"
    response  = get_response(url)
    table_items =[]
    for i in response['table']:
        team_name = i['team']['teamName']
        home_wins = i['stats']['home']['won']
        away_wins = i['stats']['away']['won']
        wins = home_wins + away_wins
        home_draws = i['stats']['home']['drawn']
        away_draws = i['stats']['away']['drawn']
        draws = home_draws + away_draws
        home_loss = i['stats']['home']['lost']
        away_loss = i['stats']['away']['lost']
        losses  = home_loss + away_loss
        points = i['stats']['points']
        
        items={
            "team":team_name, # type:str
            "W":wins, # type:str
            "D":draws, # type:str
            "L":losses, # type:str
            "PTS":points, # type:str
        }
        #print(items)
        table_items.append(items)
        
    return table_items


data_items=[]

for key,value in competions.items():

    
    response = get_response(value)
    data=response
    gameweek=data["currentGameWeekId"]
    season_number=data['seasonNumber']
    start_time_ts = data['seasonStartTime']
    start_time = datefromtimestamp(start_time_ts)
    #get_results(competion_slug=value)
    
    odds = get_odds(value)
   # time.sleep(160)
    results = get_results(value)
    table = get_table(value)
    
    items={
            "season":season_number, # type:str
            "start_time":start_time, # type: timestamp
            "regions":{
                key:{
                    "Games":odds,
                    'Results':results,
                    'League Table':table
                },
                
            }
    }
    #print(items)
    data_items.append(items)
json_data = json.dumps(data_items,indent=2)    
with open('data.json','w') as fp:
    
    fp.write(json_data)
#print(items)