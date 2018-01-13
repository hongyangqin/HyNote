# 下载所有的gist文件,  并移动所有文件到当期目录下
import json
from subprocess import call
from urllib import request
import os
import re
import shutil
USER = '285571052'

url = "https://api.github.com/users/%s/gists" % USER;

u = request.urlopen(url)	

gists = json.load(u)
for gist in gists:
	call(['git', 'clone', gist['git_pull_url']])
	
n = u.headers.get('link', None)
ID = re.search('<https://api.github.com/user/(\S+)/', n ).group(1)
a = re.search('page=(\d+)>[\S\s]+page=(\d+)>', n )
first = int(a.group(1));
last = int(a.group(2));

for ii in range(first , last + 1):
	url = 'https://api.github.com/user/17291060/gists?page=%d'%ii;
	u = request.urlopen(url)	
	gists = json.load(u)
	for gist in gists:
		call(['git', 'clone', gist['git_pull_url']])

d='.' 

dirs = [os.path.join(d,o) for o in os.listdir(d) if os.path.isdir(os.path.join(d,o))]

cnt = 0

for dir in dirs : 
	files = [os.path.join(dir,o) for o in os.listdir(dir) if os.path.isfile(os.path.join(dir,o))]
	for file in files:
		[a,ext] = os.path.splitext(file)
		shutil.move(file , '%d%s'%(cnt,ext))
		cnt = cnt + 1