import os
from configparser import ConfigParser


def get(section, option):
    root_path = os.getcwd().split("spider-app")[0] + "spider-app" + os.path.sep + "spider" + os.path.sep
    cp = ConfigParser()
    cp.read(root_path + "config" + os.path.sep + "config.ini")
    return cp.get(section, option)


if __name__ == '__main__':
    print(get("mysql", "host"))
