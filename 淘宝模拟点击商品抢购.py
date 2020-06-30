from selenium import webdriver
import datetime
import time


# 登录淘宝首页
def login():
    # 打开淘宝首页，并扫码登录
    brower.get('https://www.taobao.com')
    if brower.find_element_by_partial_link_text('亲，请登录'):
        brower.find_element_by_partial_link_text('亲，请登录').click()
        print('请在15秒内完成扫码。。。')
        time.sleep(15)
        brower.get('https://cart.taobao.com/cart.htm')
        now = datetime.datetime.now()
        print('login success:', now.strftime('%Y-%m-%d %H:%M:%S'))


# 实现商品购买
def buy(times):
    flag = True
    while flag:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        if now >= times:
            flag = False
            while True:
                try:
                    if brower.find_element_by_id('J_SelectAll1'):
                        brower.find_element_by_id('J_SelectAll1').click()
                        break
                except:
                    print('找不到全选按钮')
            while True:
                try:
                    if brower.find_element_by_partial_link_text('结 算'):
                        brower.find_element_by_partial_link_text('结 算').click()
                        print('结算成功。。。')
                        break
                except:
                    print('结算失败。')
            while True:
                try:
                    if brower.find_element_by_partial_link_text('提交订单'):
                        brower.find_element_by_partial_link_text('提交订单').click()
                        now1 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
                        print('抢购成功时间：%s' % now1)
                        break
                except:
                    pass


# 启动函数
if __name__ == '__main__':
    times = input('请输入抢购时间。格式(2019-05-24 18:00:00.000000):')
    brower = webdriver.Firefox(executable_path='D:\\Program Files\\geckodriver.exe')
    login()
    buy(times)
