# GM_Twitter_Bot
Python tweet bot using tweepy module and Twitter API.

There are several files in this package. 

The episode_transcript_urls.py file just holds a couple lists of urls. There are 3 important lists, they hold all of the urls for the different Arrested Development Wiki pages with transcripts of every episode in the first three seasons. The first three seasons of the show Arrested Development are the only important seasons, though one could easily extend this method to the fourth. 

The get_gm.py program is designed to webscrape urls from the collections of urls in episode_transcript_urls.py. It grabs the html from each one, sifts through it for George Michael's lines in the transcript and saves each of these lines to a new file in the appropriate season folder, appending a newline character and an episode credit, e.g. '- S2E4'.

The main.py file looks at the text file storing the information about exactly what line should be tweeted next (from which episode/season), tweets it, and updates the counters. It also prints some information about its success to a file labeled output. It does a few other menial things, but you can explore them for yourself.

The com.example.gmikebot.plist file is a launch agent file which allows the main.py program to be run every 2 hours. This file was written with the help of ChatGPT, but I incorporated the calendar aspect, to give it a start time of 1:00 PM (though that's slightly irrelevant now that it's running), and I learned a lot about .plist files, launch agents, and XML along the way. I'm confident next time I'll be able to manage the launch agent aspects of a program like this on my own. Figuring it out this time was easily the longest part of the whole process, which also means it was the most gratifying to complete.

All in all I learned a lot from this project, and had a lot of fun. I had never used the Twitter API nor the tweepy module before, and learning about both was useful not just for making a chatbot, but for familiarizing myself with using new modules and APIs in general. This project also gave me the chance to learn about launch agents, and that process was interesting, frustrating, and so rewarding. 

You can find the bot at @george_mikebot on Twitter! Though George Michael only has ~950 lines in Arrested development (I filtered out almost all of his one-word lines, which you can see in the one_liners.txt file), so this bot will probably only be running for 2 months or so. 

Thanks for reading!

Theo
