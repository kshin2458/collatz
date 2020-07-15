import sys
import logging
import numpy as np
# ログの出力名を設定（1）
logger = logging.getLogger('Logging')
 
# ログレベルの設定（2）
logger.setLevel(10)
 
# ログのコンソール出力の設定（3）
sh = logging.StreamHandler()
logger.addHandler(sh)
 
# ログのファイル出力先を設定（4）
fh = logging.FileHandler('collatz.log')
logger.addHandler(fh)
#logging.basicConfig(level=logging.DEBUG)

i=int(sys.argv[1])
count=0
courses=np.loadtxt("./collatzser.csv", delimiter="\n")
logger.info({"input":i})
while i!=1:
    if i in courses:
        course=i
    if i%2==0:
        i=int(i/2)
        logger.info({"even":i})
    else:
        i=int(3*i+1)
        logger.info({"odd":i})
    count=count+1
print(course)
print(count)
