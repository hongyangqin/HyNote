# 压缩父路径下的所有名为assets目录下的图片
import sys
from PIL import Image
import os
import shutil
d='.' 
files=[]

for dp, dn, fs in os.walk(d):
	if "assets" in dp and not "bak" in dp:
		for f in fs:
			try:
				fname = os.path.join(dp, f)
				bakdir = os.path.join(dp, 'bak')
				if not os.path.exists(bakdir) :
					os.mkdir(bakdir)
				ori =os.path.join(bakdir,f)
				shutil.move(fname , ori)
				im=Image.open(ori)
				im.save(fname,format='JPEG')
				origsize = os.path.getsize(ori)
				newsize = os.path.getsize(fname)
				print(origsize , newsize)
			except:
				continue
			
	
	


