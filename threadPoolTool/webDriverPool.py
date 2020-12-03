from main import normalThread as Nt
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chromeOptions
from bs4 import BeautifulSoup as BS

'''
功能目标
-1.提供傻逼也能直接用的封装和操作方式(我觉得可以参考一下js的冒泡机制和回调机制)
0. 提供数量有上限（按照内存控制？如果可以的话）的浏览器服务池
1. 通过浏览器模拟获取 soup 提供下一步操作
2. 提供方便的js插入调试？
3. 提供方便的长文本输入调试
4. 提供有效的元素渲染检测方式（404返回对抗）
'''


class ChromeDriverHelper:
    def __init__(self):
        '''
        用于模拟浏览器进行爬虫操作
        变量说明：

        model               : 工作模式 work dev test
        driver              : 驱动器（浏览器控制对象）
        driverStatus        : 驱动器状态
        chrome_options      : 浏览器运行参数 - 可设置无头模式等
        Soup                : 默认保存当前soup
        '''
        
        self.model = 'def' 
        self.driver = {}
        self.driverStatus = False
        self.chrome_options = chromeOptions()
        self.Soup = {}
    
    def start(self,HeadLess=True):
        '''
        开启浏览器
        默认使用chrome 无头模式 需要Chrome版本60以上
        '''
        self.driverStatus = True
        if HeadLess:
            self.chrome_options.add_argument("--headless")
            self.driver = webdriver.Chrome(options = self.chrome_options)
        else:
            self.drivrt = webdriver.Chrome()
    
    def __getSoupFunc(self,url):
        '''
        直接访问url并获取对应的soup
        '''
        self.driver.get(url)
        html = self.driver.page_source
        soup = BS(html,'html.parser')
        return soup
            
    def getSoup(self,url,asd):
        '''
        通过url获取对应soup快捷方式
        此处本意是为了规避多次创建driver造成性能损耗，不过目前未检测（留个坑）
        '''
        # if self.driverStatus == True:
        #     return self.__getSoupFunc(url)
        # else:
        print(asd)
        self.start()
        return self.__getSoupFunc(url)
            
            
    def selectByCss(self,selectStr,soup=False):
        '''
        通过css对soup进行筛选
        '''
        Soup = {}
        if soup!=False:
            Soup = soup
        elif soup == False:
            Soup = self.Soup
        return Soup.select(str(selectStr))
    
    
    def UseJsInChrome(self,js):
        '''
        在浏览器中直接使用js操作
        其本质在于对文档流底部加入新的js并解析执行
        '''
        try:
            self.driver.execute_script(str(js))
        except:
            self.log('warning:error in UseJsInChrome withJs:')
            self.log(str(js))
    
    def log(self,word):
        '''
        普通的报错封装
        '''
        if self.model != 'work':
            print(word)
            

# url = "https://item.jd.com/72248184380.html"
# lists = []
# for x in range(10):
#     lists.append({})
# for x in range(10):
#     helper = ChromeDriverHelper()
#     lists[x]= Nt(helper.getSoup,(url,"asd"),1)
#     print(x)
# for x in lists:
#     x.run()