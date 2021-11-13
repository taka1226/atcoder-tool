#!/usr/bin/python3

import os
import shutil
from os.path import expanduser
#sudo 権限で実行する

env_file_path = None;
system_makefile_path = "/usr/share/atcoder/Makefile"
system_maincpp_path = "/usr/share/atcoder/main.cpp"

# makefile, main.cpp を /usr/share/atcoder ディレクトリに移す
os.makedirs("/usr/share/atcoder")
shutil.copyfile("./Makefile", "/usr/share/atcoder/Makefile")
shutil.copyfile("./main.cpp", "/usr/share/atcoder/main.cpp")


# /home/takahiro/.atcoder/env に環境変数を設定する(このときに atcoder の username, password を設定する)
home_directory = expanduser("~")  #windows にも対応
env_file_path = home_directory + "/.atcoder/env"
username = input("atcoder username: ")
password = input("atcoder password: ")
#ここでusername, password が正しいことをチェックする

os.makedirs("/root/.atcoder")
with open(env_file_path, 'w') as f:
    f.write("USERNAME=" + username)
    f.write("PASSWORD=" + password)
    f.write("MAKEFILE_FILEPATH=" + system_makefile_path)
    f.write("MAINCPP_FILEPATH=" + system_maincpp_path)

#メインスクリプトの方に一行挿入する
with open("main.py") as f:
    data = f.readlines()

data.insert(7, 'dotenv_path = Path("' + home_directory + '/.atcoder/env")')

with open("/usr/bin/atcoder-tool", mode='w') as f:
    f.writelines(data)
