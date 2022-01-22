# Author: Huang Shang Xue
# Email address: 1204745933@qq.com
# Development time 2022/1/21 14:51
import  requests



def Get_tag_url(username,reponame,platform):
    response = requests.get("https://api.github.com/repos/%s/%s/releases/latest" % (username, reponame))
    tag = response.json()["tag_name"]
    if tag :
        print(tag)
    else:
        print("Error: not fount tag version")
        exit(2)
    download_url = 'https://github.com/%s/%s/releases/download/%s/%s_%s.tar.gz' % (username, reponame,tag, reponame,platform)
    print(download_url)
    return download_url



if __name__ == '__main__':
    username = "peerXu"
    reponame = "meepo"
    platform = "linux_amd64"
    Get_tag_url(username, reponame,platform)
