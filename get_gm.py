import requests
import episode_transcript_urls as e

def generate_gm(script_path, season, episode):
    script = open(script_path, "r")
    store_path = "season_" + str(season) + "/s" + str(season) + "_ep" + str(episode) + ".txt"
    gm = open(store_path, "a")
    ols = open("one_liners.txt", "a")

    denoter = "<b>George Michael:</b>"
    length = len(denoter)
    counter = 0
    
    for line in script:
        if denoter in line:
            # index = where denoter STARTS
            index = line.find(denoter)
            # .strip accounts for the space at the beginning
            gm_dialogue = line[index + length:].strip()

            episode_credits = "- S{}E{}".format(season, episode)

            if len(gm_dialogue.split(" ")) <= 1:
                ols.write(gm_dialogue + "\n")
                ols.write(" | - > 1-word line from s" + str(season) + " e" + str(episode) + " at line #" + str(counter) + "\n")

            else:
                gm.write(gm_dialogue + "\n")
                gm.write(episode_credits + "\n")

            counter += 1

    script.close()
    gm.close()

    return counter


def pull_script_from_wiki(url):
    # URL of the webpage you want to read
    # e.g. url = 'https://arresteddevelopment.fandom.com/wiki/Transcript_of_Pilot'

    # send a GET request to the URL
    response = requests.get(url)

    # check if the request was successful (status code 200)
    if response.status_code == 200:
        # print the content of the response (HTML content of the webpage)
        fp = open("html_body.txt", "w")
        fp.write(response.text)
    else:
        # print an error message if the request was not successful
        print(f"Error: Unable to fetch webpage. Status code: {response.status_code}\nFor webpage: {url}")

    return "html_body.txt"

total_lines = 0

for s, season in enumerate(e.seasons):
    for en, ep in enumerate(season):
        total_lines += generate_gm(pull_script_from_wiki(ep), s + 1, en + 1)


print(total_lines)





