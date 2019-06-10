import logging
import os
import time

root_path = os.getcwd().split("spider-app")[0] + "spider-app" + os.path.sep + "tmp" + os.path.sep
file_path = root_path + "spider-app-%s.log" % time.strftime("%Y-%m-%d")


class SpiderLogger(object):
    def __init__(self):
        self.logging = logging.getLogger()
        self.format = '%(asctime)s [%(filename)s line:%(lineno)d] [%(levelname)s] %(message)s'
        logging.basicConfig(
            level=logging.DEBUG,
            format=self.format
        )

        self.fileHandler = logging.FileHandler(file_path, encoding='utf-8')
        self.fileHandler.setFormatter(logging.Formatter(self.format))
        self.logging.addHandler(self.fileHandler)


if __name__ == '__main__':
    SpiderLogger().logging.info("test")
