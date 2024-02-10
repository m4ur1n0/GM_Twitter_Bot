import os
script_dir = os.path.dirname(os.path.realpath(__file__))

# Change the current working directory to the script directory
os.chdir(script_dir)


import keys as k
import sys
from datetime import datetime
import tweepy

# Get the directory path where the script is located


# def api():
#     auth = tweepy.OAuth1UserHandler(k.API_Key, k.API_Key_Secret, k.Access_Token, k.Access_Token_Secret)
#     # auth.set_access_token(k.Access_Token, k.Access_Token_Secret)

#     return tweepy.API(auth)

# def tweet(api: tweepy.API, msg: str, image_path=None):
#     if image_path:
#         api.update_status_with_media(msg, image_path)
#     else:
#         api.update_status(status=msg)

#     print("tweeted")


# api1 = api()
# tweet(api1, ' :) test', 'george_michael.jpg')
eps_per_season = [22, 18, 13]

with open("output.txt", "a") as f:
    sys.stdout = f


    client = tweepy.Client(consumer_key=k.API_Key,
                        consumer_secret=k.API_Key_Secret,
                        access_token=k.Access_Token,
                        access_token_secret=k.Access_Token_Secret)

    # s_counter
    # SEASON NUMBER
    # EPISODE NUMBER
    # LINE NUMBER 
    s_counter = open("s_counter.txt", "r")
    stats = s_counter.readlines()

    # seasons and episodes will start with 1
    # but lines will start at 0
 
    season = int(stats[0])
    episode = int(stats[1])
    line = int(stats[2])   

    if season == 4:
        exit(0)

    # idrc about how inefficient this is
    str_season = str(season)
    str_ep = str(episode)
    str_line = str(line)

    # now that we know what season, episode, and line we're dealing with, we can close the file
    s_counter.close()



    episode_path = "season_" + str_season + "/s" + str_season + "_ep" + str_ep + ".txt"
    episode_file = open(episode_path, "r")
    episode_lines = episode_file.readlines()

    changed = False

    if (line > len(episode_lines) - 1):
        changed = True
        # time to move on to next episode
        episode += 1
        if (episode > eps_per_season[season - 1]):
            # time to move on to next season
            if (season == 3):
                print("WE'VE COMPLETED THE GOOD PART OF THE SERIES! GOOD JOB!")
                s = open("s_counter.txt", "w")
                s.write('4\n')
                s.write('0\n')
                s.write('0\n')
                s.close()
                exit(0)
            else:
                # if we haven't finished last ep of season 3, but just last ep of
                # seasons 1 or 2:

                season += 1
                episode = 1
                line = 0
        else:
            # if just episode is over, but there are more to go in this season:

            episode += 1
            line = 0
    

    if (changed):
        episode_file.close()

       
        str_season = str(season)
        str_ep = str(episode)
        str_line = str(line)

        episode_path = "season_" + str_season + "/s" + str_season + "_ep" + str_ep + ".txt"
        episode_file = open(episode_path, "r")
        episode_lines = episode_file.readlines()


    # now that we're sure to be at a valid line:

    message = episode_lines[line] + episode_lines[line + 1]
    if len(message) > 280:
        print("THIS MESSAGE WAS TOO LONG TO TWEET, SKIPPED:\n", message, "\n\n")
        exit(0)
    
    
    try:
        response = client.create_tweet(text=message)
        print("TWEETED:\n" + message[0:-1] + "\nAt ", datetime.now(), "\n\n")

    except:
        line += 2
        s_counter = open("s_counter.txt", "w")
        s_counter.write(str(season) + '\n')
        s_counter.write(str(episode) + '\n')
        s_counter.write(str(line))
        exit(0)

    # reset the line pointers in s_counter
    line += 2
    s_counter = open("s_counter.txt", "w")
    s_counter.write(str(season) + '\n')
    s_counter.write(str(episode) + '\n')
    s_counter.write(str(line))




