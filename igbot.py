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
        MainWindow.resize(951, 698)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(140, 0, 231, 161))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.username_edit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.username_edit.setObjectName("username_edit")
        self.verticalLayout.addWidget(self.username_edit)
        self.sifre_edit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.sifre_edit.setObjectName("sifre_edit")
        self.verticalLayout.addWidget(self.sifre_edit)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 62, 47, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 20, 61, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 340, 121, 51))
        self.label_3.setObjectName("label_3")
        self.stalklanacak = QtWidgets.QLineEdit(self.centralwidget)
        self.stalklanacak.setGeometry(QtCore.QRect(100, 360, 113, 20))
        self.stalklanacak.setObjectName("stalklanacak")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(70, 380, 173, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.takiplerial = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.takiplerial.setObjectName("takiplerial")
        self.horizontalLayout.addWidget(self.takiplerial)
        self.takipcilerial = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.takipcilerial.setObjectName("takipcilerial")
        self.horizontalLayout.addWidget(self.takipcilerial)
        self.gtbtn = QtWidgets.QPushButton(self.centralwidget)
        self.gtbtn.setGeometry(QtCore.QRect(700, 340, 250, 130))
        self.gtbtn.setObjectName("gtbtn")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(340, 340, 249, 121))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.takipedilcekig = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.takipedilcekig.setObjectName("takipedilcekig")
        self.verticalLayout_2.addWidget(self.takipedilcekig)
        self.ototakipbtn = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.ototakipbtn.setObjectName("ototakipbtn")
        self.verticalLayout_2.addWidget(self.ototakipbtn)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 490, 941, 161))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(140, 170, 291, 81))
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 951, 21))
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
        self.label.setText(_translate("MainWindow", "Password : "))
        self.label_2.setText(_translate("MainWindow", "Username : "))
        self.label_3.setText(_translate("MainWindow", "Person to stalk: "))
        self.takiplerial.setText(_translate("MainWindow", "His Follwings"))
        self.takipcilerial.setText(_translate("MainWindow", "His Followers"))
        self.gtbtn.setText(_translate("MainWindow", "Stop Following Everyone If He isn't Following You"))
        self.ototakipbtn.setText(_translate("MainWindow", "Follow The First 100 Followers of This User"))

class Myapp(QtWidgets.QMainWindow):
    def __init__(self): 
        super(Myapp,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.girisyapildi = False

        self.ui.pushButton.clicked.connect(self.girisyap)
        self.ui.ototakipbtn.clicked.connect(self.takipbotu)
        self.ui.gtbtn.clicked.connect(self.gtbotu)
        self.ui.takipcilerial.clicked.connect(self.takipcilistesial)
        self.ui.takiplerial.clicked.connect(self.takiplistesial)

    
    def takipbotu(self):
        if self.girisyapildi and self.islemyapiliyor == False :  
            self.islemyapiliyor = True
            self.newfollowercount = 0
            self.pagename = self.ui.takipedilcekig.text()
            self.browser.get("https://www.instagram.com/"+self.pagename+"/")
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
                if self.newfollowercount > 100 :
                    break
            time.sleep(2)
            
            self.allpagefollowers = self.browser.find_element_by_css_selector("div[role=dialog] ul").find_elements_by_css_selector("li")
            for self.takip in self.allpagefollowers : 
                a = random.randint(1,3)
                time.sleep(a)
                self.takip.find_element_by_css_selector("div button").click()
            self.islemyapiliyor = False
            self.ui.label_4.setText("Successful")
        else : 
            self.ui.label_5.setText("Please Login First")
            

    def gtbotu(self):
        if self.girisyapildi and self.islemyapiliyor == False :  
            self.islemyapiliyor = True

            self.pagename = self.username
            self.browser.get("https://www.instagram.com/"+self.pagename+"/")
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
                time.sleep(0.51)

                self.takipedilenlerinsayisi = len(self.browser.find_element_by_css_selector("div[role=dialog] ul").find_elements_by_css_selector("li"))
            time.sleep(2)    
            self.takipedilenlerinisimleri = self.browser.find_element_by_css_selector("div[role=dialog] ul").find_elements_by_css_selector("li")

            for self.a in range(len(self.takipedilenlerinisimleri)) : 
                self.cifttaraflitakip = False
                for self.b in self.myallfollowers :
                    if self.takipedilenlerinisimleri[self.a].find_element_by_css_selector("a").get_attribute("href") == self.b : 
                        self.cifttaraflitakip = True

                if not self.cifttaraflitakip : 

                    self.takipedilenlerinisimleri[self.a].find_element_by_css_selector("div button").click()
                    time.sleep(0.71)
                    self.browser.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[1]').click()
                    time.sleep(0.71)
                self.islemyapiliyor = False
                self.ui.label_4.setText("Successful")
        else :
            self.ui.label_5.setText("Please Login First")
             

    def takipcilistesial(self):
        if self.girisyapildi and self.islemyapiliyor == False :  
            self.islemyapiliyor = True

            self.ui.label_4.setText("takipçi listesi çıkartılıyor ....")
            self.pagename = self.ui.stalklanacak.text()
            self.newfollowercount = 0
            self.browser.get("https://www.instagram.com/"+self.pagename+"/")
            time.sleep(3)

            self.takipciler = self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a').find_element_by_css_selector("span").text
            self.takipciler = int(self.takipciler)
            self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a').click()
            time.sleep(2)

            action = webdriver.ActionChains(self.browser)
            while True : 

                self.browser.find_element_by_css_selector("div[role=dialog] ul").click()
                action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
                time.sleep(0.65)
                self.newfollowercount = len(self.browser.find_element_by_css_selector("div[role=dialog] ul").find_elements_by_css_selector("li"))
                if self.newfollowercount + 10 > self.takipciler :
                    self.allfollowers = self.browser.find_element_by_css_selector("div[role=dialog] ul").find_elements_by_css_selector("li")
                    break

            for self.user in self.allfollowers :
                self.followername = self.user.find_element_by_css_selector("a").get_attribute("href")
                file = open("asensutakipcileri.txt","a",encoding="utf-8")
                file.write(self.followername + "\n")
            self.islemyapiliyor = False
            self.ui.label_4.setText("Successful")
        else : 
            self.ui.label_5.setText("Please Login First")
                

    def takiplistesial(self):
        if self.girisyapildi and self.islemyapiliyor == False :  
            self.islemyapiliyor = True

            self.pagename = self.ui.stalklanacak.text()
            self.newfollowercount = 0
            self.browser.get("https://www.instagram.com/"+self.pagename+"/")
            time.sleep(3)

            self.takipciler = self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').find_element_by_css_selector("span").text
            self.takipciler = int(self.takipciler)
            self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()
            time.sleep(2)

            action = webdriver.ActionChains(self.browser)
            while True : 

                self.browser.find_element_by_css_selector("div[role=dialog] ul").click()
                action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
                time.sleep(0.65)
                self.newfollowercount = len(self.browser.find_element_by_css_selector("div[role=dialog] ul").find_elements_by_css_selector("li"))
                self.ui.label_4.setText("takip listesi çıkartılıyor ....")
                if self.newfollowercount + 10 > self.takipciler :
                    self.allfollowers = self.browser.find_element_by_css_selector("div[role=dialog] ul").find_elements_by_css_selector("li")
                    break

            for self.user in self.allfollowers :
                self.followername = self.user.find_element_by_css_selector("a").get_attribute("href")
                file = open("asensutakipcileri.txt","a",encoding="utf-8")
                file.write(self.followername + "\n")
            self.islemyapiliyor = False
            self.ui.label_4.setText("Successful")
        else : 
            self.ui.label_5.setText("Please Login First")

    def girisyap(self): 
        self.islemyapiliyor = True

        self.password = self.ui.sifre_edit.text()
        self.username = self.ui.username_edit.text()
        self.girisyapildi = True
       

        self.useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 OPR/74.0.3911.203"
        self.options = Options()
        self.options.add_experimental_option("prefs", {"intl.accept_languages" : "tr"})
        self.options.add_argument('--headless')
        self.options.add_argument(f'user-agent={self.useragent}')
        self.options.add_argument('--disable-gpu') 
        self.browser = webdriver.Chrome(executable_path="C://Users/deniz/OneDrive/Desktop/python/chromedriver.exe", chrome_options=self.options)

        self.url = "https://www.instagram.com"
        self.browser.get(self.url)
        time.sleep(2)

        self.browser.find_element_by_xpath('//*[@id="loginForm"]/div[1]/div[1]/div/label/input').send_keys(self.username)
        self.browser.find_element_by_xpath('//*[@id="loginForm"]/div[1]/div[2]/div/label/input').send_keys(self.password)
        self.browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click()

        time.sleep(2)
        try : 
            self.alert = self.browser.find_element_by_id("slfErrorAlert").text
        except Exception : 
            pass

        if self.alert == "Girdiğin kullanıcı adı bir hesaba ait değil. Lütfen kullanıcı adını kontrol et ve tekrar dene." or self.alert == "Üzgünüz, şifren yanlıştı. Lütfen şifreni dikkatlice kontrol et." : 
            self.ui.label_4.setText("Wrong Username or Password")
        else : 
            time.sleep(1)
            self.ui.label_4.setText("Login Successful")
            self.islemyapiliyor = False

def app():
    app = QtWidgets.QApplication(sys.argv)
    win = Myapp()
    win.show()
    sys.exit(app.exec_())

app()