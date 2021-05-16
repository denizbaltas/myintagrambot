from selenium import webdriver
from PyQt5 import QtWidgets
import sys  
import random
from selenium.webdriver.common.keys import Keys
import time
from PyQt5 import QtCore, QtGui, QtWidgets
from selenium.webdriver.chrome.options import Options

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(90, 140, 131, 31))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 60, 61, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 90, 61, 20))
        self.label_2.setObjectName("label_2")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(90, 120, 121, 17))
        self.checkBox.setObjectName("checkBox")
        self.Username_Edit = QtWidgets.QLineEdit(self.centralwidget)
        self.Username_Edit.setGeometry(QtCore.QRect(100, 60, 113, 20))
        self.Username_Edit.setObjectName("Username_Edit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 90, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.Unfolloweveryone = QtWidgets.QPushButton(self.centralwidget)
        self.Unfolloweveryone.setGeometry(QtCore.QRect(470, 200, 271, 91))
        self.Unfolloweveryone.setObjectName("Unfolloweveryone")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(470, 320, 271, 151))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 420, 191, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.Takipcileritakipedilcek = QtWidgets.QLineEdit(self.centralwidget)
        self.Takipcileritakipedilcek.setGeometry(QtCore.QRect(240, 390, 191, 20))
        self.Takipcileritakipedilcek.setObjectName("Takipcileritakipedilcek")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(250, 220, 191, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(210, 240, 121, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(334, 240, 121, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(160, 220, 91, 21))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Login"))
        self.label.setText(_translate("MainWindow", "Username : "))
        self.label_2.setText(_translate("MainWindow", "Password : "))
        self.checkBox.setText(_translate("MainWindow", "Visible Browser"))
        self.Unfolloweveryone.setText(_translate("MainWindow", "Stop Following Everyone"))
        self.pushButton_3.setText(_translate("MainWindow", "Stop Following Everyone if He is not following you"))
        self.pushButton_2.setText(_translate("MainWindow", "Follow first 100 followers of this user"))
        self.pushButton_4.setText(_translate("MainWindow", "Make list of Followings"))
        self.pushButton_5.setText(_translate("MainWindow", "Make list of followers"))
        self.label_3.setText(_translate("MainWindow", "Person to stalk : "))

        
class Myapp(QtWidgets.QMainWindow):
    def __init__(self): 
        super(Myapp,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.girisyapildi = False

        self.ui.checkBox.stateChanged.connect(self.visible)
        self.ui.pushButton.clicked.connect(self.girisyap)
        self.ui.pushButton_2.clicked.connect(self.takipbotu)
        self.ui.pushButton_3.clicked.connect(self.gtbotu)
        self.ui.pushButton_5.clicked.connect(self.takipcilistesial)
        self.ui.pushButton_4.clicked.connect(self.takiplistesial)
        self.ui.Unfolloweveryone.clicked.connect(self.unfolloweveryone)

        self.headless = True
        self.ssend = False

    def takipbotu(self):
        if self.girisyapildi and self.islemyapiliyor == False :  
            self.islemyapiliyor = True
            self.newfollowercount = 0
            self.pagename = self.ui.Takipcileritakipedilcek.text()
            self.browser.get("https://www.instagram.com/"+self.pagename+"/")
            print("please wait")
            time.sleep(3)
            self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()
            time.sleep(2)
            action = webdriver.ActionChains(self.browser)
            while True: 
                self.browser.find_element_by_css_selector("div[role=dialog] ul").click()
                time.sleep(0.21)
                action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
                time.sleep(0.21)
                self.newfollowercount = len(self.browser.find_element_by_css_selector("div[role=dialog] ul").find_elements_by_css_selector("li"))
                print(f"finding people for following {self.newfollowercount}/100")
                if self.newfollowercount > 100 :
                    break
            time.sleep(2)
            
            self.allpagefollowers = self.browser.find_element_by_css_selector("div[role=dialog] ul").find_elements_by_css_selector("li")
            for self.takip in self.allpagefollowers : 
                a = random.randint(3,5)
                time.sleep(a)
                self.takip.find_element_by_css_selector("div button").click()
                print("someone followed")
            self.islemyapiliyor = False
            print("Successful")
        else : 
            print("Please Login First")
            
    def gtbotu(self):
        if self.girisyapildi and self.islemyapiliyor == False :  
            self.islemyapiliyor = True

            self.pagename = self.username
            self.browser.get("https://www.instagram.com/"+self.pagename+"/")
            print("please wait")
            time.sleep(4)
            self.myfollowers =self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/span').text
            self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()
            time.sleep(1)
            self.foundfollowers = 0
            self.myallfollowers = []
            action = webdriver.ActionChains(self.browser)
            while self.foundfollowers + 5 <= int(self.myfollowers) : 
                self.browser.find_element_by_css_selector("div[role=dialog] ul").click()
                action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
                time.sleep(0.51)
                self.foundfollowers = len(self.browser.find_element_by_css_selector("div[role=dialog] ul").find_elements_by_css_selector("li"))
                print(f"please wait we are making a list of your followers {self.foundfollowers}/{self.myfollowers}")

            time.sleep(1)
            self.allnames = self.browser.find_element_by_css_selector("div[role=dialog] ul").find_elements_by_css_selector("li")
            for self.name in self.allnames : 
                self.followername = self.name.find_element_by_css_selector("a").get_attribute("href")
                self.myallfollowers.append(self.followername)


            self.browser.get("https://www.instagram.com/"+self.pagename+"/")
            time.sleep(4)
            self.takipedilenler = self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a/span').text

            self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a').click()
            time.sleep(2)
            self.takipedilenlerinsayisi = 0
            action = webdriver.ActionChains(self.browser)
            while self.takipedilenlerinsayisi +5 <= int(self.takipedilenler):
                self.browser.find_element_by_css_selector("div[role=dialog] ul").click()
                action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
                time.sleep(0.35)

                self.takipedilenlerinsayisi = len(self.browser.find_element_by_css_selector("div[role=dialog] ul").find_elements_by_css_selector("li"))
                print(f"please wait we are making a list of your followings {self.takipedilenlerinsayisi}/{self.takipedilenler}")
            time.sleep(2)    
            self.takipedilenlerinisimleri = self.browser.find_element_by_css_selector("div[role=dialog] ul").find_elements_by_css_selector("li")

            for self.a in range(len(self.takipedilenlerinisimleri)) : 
                self.cifttaraflitakip = False
                for self.b in self.myallfollowers :
                    if self.takipedilenlerinisimleri[self.a].find_element_by_css_selector("a").get_attribute("href") == self.b : 
                        self.cifttaraflitakip = True

                if not self.cifttaraflitakip : 
                    self.takipedilenlerinisimleri[self.a].find_element_by_css_selector("div button").click()
                    time.sleep(0.31)
                    self.browser.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[1]').click()
                    time.sleep(0.21)
                    print("someone unfollowed")
            self.islemyapiliyor = False
            print("Successful")
        else :
            print("Please Login First")
             
    def visible(self,number): 
        if number == 2 : 
            self.headless = False 
            print("Browser is visible now")
        elif number == 0 : 
            print("Browser is invisible now")
            self.headless = True

    def takipcilistesial(self):
        if self.girisyapildi and self.islemyapiliyor == False :  
            self.islemyapiliyor = True
            print("please wait")

            self.pagename = self.ui.lineEdit.text()
            self.newfollowercount = 0
            self.browser.get("https://www.instagram.com/"+self.pagename+"/")
            time.sleep(3)

            self.takipciler = self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').find_element_by_css_selector("span").text
            self.takipciler = int(self.takipciler)
            self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()
            time.sleep(2)

            action = webdriver.ActionChains(self.browser)

            self.txtcreated = False
            while True : 
                try : 
                    self.allfollowers = self.browser.find_element_by_css_selector("div[role=dialog] ul").find_elements_by_css_selector("li")
                    self.browser.find_element_by_css_selector("div[role=dialog] ul").click()
                    action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
                except Exception : 
                    self.txtcreated = True
                    break
                time.sleep(0.35)
                self.newfollowercount = len(self.browser.find_element_by_css_selector("div[role=dialog] ul").find_elements_by_css_selector("li"))
                print(f"Making a list of followings {self.newfollowercount}/{self.takipciler}")

                if self.newfollowercount + 10 > self.takipciler :
                    self.allfollowers = self.browser.find_element_by_css_selector("div[role=dialog] ul").find_elements_by_css_selector("li")
                    break
            print("please wait")
            time.sleep(10)
            if not self.txtcreated : 
                for self.user in self.allfollowers :
                    self.followername = self.user.find_element_by_css_selector("a").get_attribute("href")
                    file = open("followers.txt","a",encoding="utf-8")
                    file.write(self.followername + "\n")
                self.islemyapiliyor = False
                print("followers.txt created")
    
        else : 
            print("Please login first")
                
    def takiplistesial(self):
        if self.girisyapildi and self.islemyapiliyor == False :  
            self.islemyapiliyor = True

            self.pagename = self.ui.lineEdit.text()
            self.newfollowercount = 0
            self.browser.get("https://www.instagram.com/"+self.pagename+"/")
            time.sleep(3)
            print("please wait")

            self.takipciler = self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a').find_element_by_css_selector("span").text
            self.takipciler = int(self.takipciler)
            self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a').click()
            time.sleep(2)

            action = webdriver.ActionChains(self.browser)
            self.txtcreated = False
            while True : 
                try : 
                    self.allfollowers = self.browser.find_element_by_css_selector("div[role=dialog] ul").find_elements_by_css_selector("li")
                    self.browser.find_element_by_css_selector("div[role=dialog] ul").click()
                    action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
                except Exception : 
                    self.txtcreated = True
                    break
                time.sleep(0.35)
                self.newfollowercount = len(self.browser.find_element_by_css_selector("div[role=dialog] ul").find_elements_by_css_selector("li"))
                print(f"Making a list of followings {self.newfollowercount}/{self.takipciler}")

                if self.newfollowercount + 10 > self.takipciler :
                    self.allfollowers = self.browser.find_element_by_css_selector("div[role=dialog] ul").find_elements_by_css_selector("li")
                    break
            print("please wait")
            time.sleep(10)
            if not self.txtcreated : 
                for self.user in self.allfollowers :
                    self.followername = self.user.find_element_by_css_selector("a").get_attribute("href")
                    file = open("followers.txt","a",encoding="utf-8")
                    file.write(self.followername + "\n")
                self.islemyapiliyor = False
                print("followers.txt created")

        else : 
            print("Please login first")

    def unfolloweveryone(self):
            if self.girisyapildi and self.islemyapiliyor == False :  

                self.islemyapiliyor = True
                self.pagename = self.username
                while True : 
                    self.browser.get("https://www.instagram.com/"+self.pagename+"/")
                    print("please wait")
                    action = webdriver.ActionChains(self.browser)
                    self.takiptencikilanlar = 0 
                    self.takipedilenler = self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a/span').text

                    self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a').click()

                    time.sleep(4)
                    self.newfollowers = self.browser.find_element_by_css_selector("div[role=dialog] ul").find_elements_by_css_selector("li")
                    self.avaiblefollowings = self.browser.find_element_by_css_selector("div[role=dialog] ul").find_elements_by_css_selector("li")

                    while True :
                        for gereksiz in range(len(self.newfollowers)) :
                            try : 
                                self.avaiblefollowings[self.takiptencikilanlar].find_element_by_css_selector("div button").click()
                                time.sleep(0.3)
                                self.browser.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[1]').click()
                                time.sleep(0.25)
                                self.takiptencikilanlar += 1
                                print(f"{self.takiptencikilanlar} user unfollowed")
                                waittime = random.randint(3,4)
                                time.sleep(waittime)
                            except Exception :
                                break

            else :
                print("Please Login First")
                
    def girisyap(self): 
        print("logging please wait")
        self.islemyapiliyor = True

        self.password = self.ui.lineEdit_2.text()
        self.username = self.ui.Username_Edit.text()
        self.girisyapildi = True

        if len(self.password) < 6 : 
            print("Your password very short")

        else:        

            self.useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 OPR/74.0.3911.203"
            self.options = Options()
            self.options.add_experimental_option("prefs", {"intl.accept_languages" : "tr"})
            if self.headless : 
                self.options.add_argument('--headless')
            self.options.add_argument(f'user-agent={self.useragent}')
            self.options.add_argument('--disable-gpu') 
            self.browser = webdriver.Chrome(executable_path="C://Users/deniz/OneDrive/Desktop/python/chromedriver.exe",chrome_options=self.options)

            self.url = "https://www.instagram.com"
            self.browser.get(self.url)
            time.sleep(2)
            print("logging please wait a little bit")

            if self.ssend: 
                self.send()

            self.browser.find_element_by_id("loginForm").find_element_by_css_selector("input[name=username]").send_keys(self.username)
            self.browser.find_element_by_id("loginForm").find_element_by_css_selector("input[name=password]").send_keys(self.password)
            self.browser.find_element_by_css_selector("button[type=submit]").click()

            time.sleep(2)
            try : 
                self.alert = self.browser.find_element_by_id("slfErrorAlert").text
                if self.alert == "Girdiğin kullanıcı adı bir hesaba ait değil. Lütfen kullanıcı adını kontrol et ve tekrar dene." or self.alert == "Üzgünüz, şifren yanlıştı. Lütfen şifreni dikkatlice kontrol et." : 
                    print("wrong username or password")
            except Exception :
                time.sleep(1)
                print("login successful")
                self.islemyapiliyor = False
                

def app():
    app = QtWidgets.QApplication(sys.argv)
    win = Myapp()
    win.show()
    sys.exit(app.exec_())

app()
