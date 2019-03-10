# coding:utf-8
import configparser
import os

ini_path = os.path.join(os.path.dirname(__file__), 'config.ini')


class Function:
    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cf.read(ini_path)

    def read_file(self, section, option):
        """
        读取配置文件信息，返回对应数据
        :param section:
        :param option:
        :return:
        """

        return self.cf.get(section, option)

    def write_file(self, section, option, value):
        """
        写入配置文件
        :param section:
        :param option:
        :param value:
        :return:
        """
        self.cf.set(section, option, value)
        self.cf.write(open(ini_path, 'w+'))
