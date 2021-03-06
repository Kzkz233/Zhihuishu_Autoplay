from traceback import print_tb
from tracemalloc import stop
from typing import Optional
from selenium import webdriver
import time
import os

def Login(website):
    try:
        browser.get(website)#打开课程网站
        print("======网站开启成功")
        time.sleep(1)
    except:
        print("======网站开启失败,请尝试重启")
    time.sleep(1)

def AutoClick():
    while True:
        try:
            if browser.find_element_by_xpath("//*[@id='playTopic-dialog']/div/div[1]/div/h4"):
                print("======成功检测到弹题")
                if browser.find_element_by_xpath("//*[@class='topic-list']/li[1]"):
                    browser.find_element_by_xpath("//*[@class='topic-list']/li[1]").click()
                    print("========点击选项")
                    time.sleep(0.6)
                    browser.find_element_by_xpath("//*[@id='playTopic-dialog']/div/div[1]/button").click()
                    print("========点击关闭")
                    time.sleep(0.6)
                    browser.find_element_by_xpath("//*[@id='vjs_container']/div[8]").click()
                    print("========点击继续")
                    print("======点击弹题成功")
                else:
                    print("======点击弹题失败")
        except:
            print("======未检测到弹题/点击选项失败")
        time.sleep(0.5)
        try:
          if browser.find_element_by_id("playButton").get_attribute("class") == "playButton":
                time.sleep(1)
                if browser.find_element_by_id("playButton").get_attribute("class") == "playButton":
                    print("======检测到本节内容已播完，点击播放下一节内容")
                    browser.find_element_by_xpath("//*[@id='vjs_container']/div[8]").click()
                    time.sleep(0.5)
                    browser.find_element_by_id("nextBtn").click()
                    time.sleep(2)
                    browser.find_element_by_id("playButton").click()
                    time.sleep(2)
        except:
            print("======检测是否播完当前视频失败")
        print("======进行下一次循环检测")

# 主函数
if __name__ == "__main__":
    webSite = "https://www.zhihuishu.com/"
    browser = webdriver.Chrome()
    browser.maximize_window()
    Login(webSite)
    start = int(input("打开课程界面并使视频在“播放中”后,运行自动点击弹题程序请输入1,想要关闭程序请输入0:"))
    if(start):
        AutoClick()
    else:
        os._exit(0)