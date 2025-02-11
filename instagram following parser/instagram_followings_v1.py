import json
import sys


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("enter the follower and following json files as command line argiments.")
        sys.exit(1)

    followers_file = sys.argv[1]
    following_file = sys.argv[2]
    followers,following = [],[]
    with open(followers_file,'r') as file:
        for line in file:
            if("value" in line):
                username = line.split(': "')[1].strip('",')[:-3]
                followers.append(username)
    with open(following_file,'r') as file:
        for line in file:
            if("value" in line):
                username = line.split(': "')[1].strip('",')[:-3]
                following.append(username)
    followers, following = set(followers), set(following)
    followersYouDontFollow = followers-following
    followingDontFollowYou = following-followers
    print(followingDontFollowYou)
    with open('dontfollowyou.txt','w') as file:
        for username in followingDontFollowYou:
            file.write(username + '\n')

    print(len(followingDontFollowYou))
    


