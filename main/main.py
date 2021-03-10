from PyQt5 import QtCore, QtGui, QtWidgets
from malModule.malScrapper import mal_search

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # Main Window Setup
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1081, 613)
        
        #Palette Setup
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        MainWindow.setPalette(palette)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # Name Bar Frame
        self.namebar = QtWidgets.QFrame(self.centralwidget)
        self.namebar.setGeometry(QtCore.QRect(0, 0, 1081, 51))
        
        # Name Bar Palette
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.namebar.setPalette(palette)
        self.namebar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.namebar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.namebar.setObjectName("namebar")
        self.namebar.setStyleSheet("background-color:black;")
        
        
        
                                #TOP BAR
        
        
        #User Name
        self.user = QtWidgets.QLabel(self.namebar)
        self.user.setGeometry(QtCore.QRect(20, 8, 151, 37))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.user.setFont(font)
        self.user.setTextFormat(QtCore.Qt.AutoText)
        self.user.setScaledContents(True)
        self.user.setAlignment(QtCore.Qt.AlignCenter)
        self.user.setObjectName("user")
        self.user.setStyleSheet("color:white;")
        
        #Search Text Field
        self.search = QtWidgets.QLineEdit(self.namebar)
        self.search.setGeometry(QtCore.QRect(810, 8, 161, 37))
        self.search.setObjectName("search")
        self.search.setStyleSheet("background-color:white; border-radius:5px; color:black;")
        
        #Search Button
        self.searchbtn = QtWidgets.QPushButton(self.namebar)
        self.searchbtn.setGeometry(QtCore.QRect(980, 8, 93, 37))
        self.searchbtn.setDefault(True)
        self.searchbtn.setObjectName("searchbtn")
        self.searchbtn.clicked.connect(self.searchbtn_pressed)
        self.searchbtn.setStyleSheet("background-color:grey;color:white;")
        
        #Profile Pic
        self.pp = QtWidgets.QLabel(self.centralwidget)
        self.pp.setGeometry(QtCore.QRect(10, 60, 291, 221))
        self.pp.setText("")
        self.pp.setObjectName("pp")
        self.pp.setPixmap(QtGui.QPixmap("./def.jpg"))
        
        #User info Label
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 290, 151, 261))
         
        font.setFamily("NSimSun")
        font.setPointSize(11)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(30, 20, 101, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(30, 50, 61, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(30, 80, 61, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(30, 110, 81, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(30, 140, 47, 13))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(30, 170, 71, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(30, 200, 91, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(30, 230, 71, 16))
        self.label_9.setObjectName("label_9")
        
        
        
                                #User Info Data
                                
                                
                                
                                
        self.user_info = QtWidgets.QFrame(self.centralwidget)
        self.user_info.setGeometry(QtCore.QRect(150, 290, 161, 261))
         
        font.setFamily("NSimSun")
        font.setPointSize(11)
        self.user_info.setFont(font)
        self.user_info.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.user_info.setFrameShadow(QtWidgets.QFrame.Raised)
        self.user_info.setObjectName("user_info")
        
        #last online
        self.last_online = QtWidgets.QLabel(self.user_info)
        self.last_online.setGeometry(QtCore.QRect(30, 20, 110, 20))
        self.last_online.setObjectName("last_online")
        #sex
        self.sex = QtWidgets.QLabel(self.user_info)
        self.sex.setGeometry(QtCore.QRect(30, 50, 81, 16))
        self.sex.setObjectName("sex")
        #birthday
        self.birthday = QtWidgets.QLabel(self.user_info)
        self.birthday.setGeometry(QtCore.QRect(30, 80, 111, 16))
        self.birthday.setObjectName("birthday")
        #joined
        self.joined = QtWidgets.QLabel(self.user_info)
        self.joined.setGeometry(QtCore.QRect(30, 110, 111, 16))
        self.joined.setObjectName("joined")
        #forum posts
        self.forum_posts = QtWidgets.QLabel(self.user_info)
        self.forum_posts.setGeometry(QtCore.QRect(30, 140, 47, 13))
        self.forum_posts.setObjectName("forum_posts")
        #reviews
        self.reviews = QtWidgets.QLabel(self.user_info)
        self.reviews.setGeometry(QtCore.QRect(30, 170, 71, 16))
        self.reviews.setObjectName("reviews")
        #recommends
        self.recommendations = QtWidgets.QLabel(self.user_info)
        self.recommendations.setGeometry(QtCore.QRect(30, 200, 91, 16))
        self.recommendations.setObjectName("recommendations")
        #friends
        self.friends = QtWidgets.QLabel(self.user_info)
        self.friends.setGeometry(QtCore.QRect(30, 230, 71, 16))
        self.friends.setObjectName("friends")
        
        #anime info label frame
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(350, 60, 111, 31))
         
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        
        #Lines
            
        self.line_1 = QtWidgets.QFrame(self.centralwidget)
        self.line_1.setGeometry(QtCore.QRect(770, 52, 31, 511))
        self.line_1.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_1.setObjectName("line_1")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(790, 120, 281, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(310, 100, 471, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(310, 310, 471, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(790, 289, 281, 21))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(790, 420, 281, 20))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        
        
        #Anime info Labels Pallete
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        
        
        #Anime Info labels
        
        
        self.w_label = QtWidgets.QLabel(self.centralwidget)
        self.w_label.setGeometry(QtCore.QRect(320, 120, 91, 31))
        self.w_label.setPalette(palette)
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(12)
        self.w_label.setFont(font)
        self.w_label.setObjectName("w_label")
        self.w_label.setStyleSheet("color:green;")
                
        self.c_label = QtWidgets.QLabel(self.centralwidget)
        self.c_label.setGeometry(QtCore.QRect(320, 160, 101, 31))
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(12)
        self.c_label.setFont(font)
        self.c_label.setObjectName("c_label")
        self.c_label.setStyleSheet("color:blue;")
        
        self.p_label = QtWidgets.QLabel(self.centralwidget)
        self.p_label.setGeometry(QtCore.QRect(320, 200, 131, 31)) 
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(12)
        self.p_label.setFont(font)
        self.p_label.setObjectName("p_label")
        self.p_label.setStyleSheet("color:grey;")
        
        self.o_label = QtWidgets.QLabel(self.centralwidget)
        self.o_label.setGeometry(QtCore.QRect(320, 240, 91, 31)) 
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(12)
        self.o_label.setFont(font)
        self.o_label.setObjectName("o_label")
        self.o_label.setStyleSheet("color:yellow;")
        
        self.d_label = QtWidgets.QLabel(self.centralwidget)
        self.d_label.setGeometry(QtCore.QRect(320, 280, 91, 31))
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(12)
        self.d_label.setFont(font)
        self.d_label.setObjectName("d_label")
        self.d_label.setStyleSheet("color:red;")
        
        self.e_label = QtWidgets.QLabel(self.centralwidget)
        self.e_label.setGeometry(QtCore.QRect(580, 150, 101, 31)) 
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(12)
        self.e_label.setFont(font)
        self.e_label.setObjectName("e_label")     
        
        self.r_label = QtWidgets.QLabel(self.centralwidget)
        self.r_label.setGeometry(QtCore.QRect(580, 200, 101, 31)) 
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(12)
        self.r_label.setFont(font)
        self.r_label.setObjectName("r_label")

        self.days_label = QtWidgets.QLabel(self.centralwidget)
        self.days_label.setGeometry(QtCore.QRect(580, 250, 131, 31)) 
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(12)
        self.days_label.setFont(font)
        self.days_label.setObjectName("days_label")
        
        self.label_31 = QtWidgets.QLabel(self.centralwidget)
        self.label_31.setGeometry(QtCore.QRect(580, 60, 111, 31)) 
        font.setPointSize(16)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(330, 340, 111, 31)) 
        font.setPointSize(16)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(330, 400, 131, 31))
        font.setPointSize(16)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
                
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(330, 470, 121, 31)) 
        font.setPointSize(16)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        
        
        
        
                                #ANIME INFO DATA                             
                                
              
              
              
                                
        #total              
        self.total = QtWidgets.QLabel(self.centralwidget)
        self.total.setGeometry(QtCore.QRect(470, 50, 61, 51)) 
        font.setFamily("OCR A Extended")
        font.setPointSize(14)
        self.total.setFont(font)
        self.total.setObjectName("total")               
        #onhold             
        self.on_hold = QtWidgets.QLabel(self.centralwidget)
        self.on_hold.setGeometry(QtCore.QRect(470, 240, 51, 31))
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(12)
        self.on_hold.setFont(font)
        self.on_hold.setObjectName("on_hold")
        self.on_hold.setStyleSheet("color:yellow;")
        #dropped
        self.dropped = QtWidgets.QLabel(self.centralwidget)
        self.dropped.setGeometry(QtCore.QRect(470, 280, 51, 31))
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(12)
        self.dropped.setFont(font)
        self.dropped.setObjectName("dropped")
        self.dropped.setStyleSheet("color:red;")
        #completed
        self.completed = QtWidgets.QLabel(self.centralwidget)
        self.completed.setGeometry(QtCore.QRect(470, 160, 51, 31)) 
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(12)
        self.completed.setFont(font)
        self.completed.setObjectName("completed")
        self.completed.setStyleSheet("color:blue;")
        #watching
        self.watching = QtWidgets.QLabel(self.centralwidget)
        self.watching.setGeometry(QtCore.QRect(470, 120, 51, 31)) 
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(12)
        self.watching.setFont(font)
        self.watching.setObjectName("watching")
        self.watching.setStyleSheet("color:green;")
        #plan to watch
        self.plan_to_watch = QtWidgets.QLabel(self.centralwidget)
        self.plan_to_watch.setGeometry(QtCore.QRect(470, 200, 51, 31))
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(12)
        self.plan_to_watch.setFont(font)
        self.plan_to_watch.setObjectName("plan_to_watch")
        self.plan_to_watch.setStyleSheet("color:grey;")
        #rewatched
        self.rewatched = QtWidgets.QLabel(self.centralwidget)
        self.rewatched.setGeometry(QtCore.QRect(710, 200, 51, 31)) 
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(12)
        self.rewatched.setFont(font)
        self.rewatched.setObjectName("rewatched")
        #episodes
        self.episodes = QtWidgets.QLabel(self.centralwidget)
        self.episodes.setGeometry(QtCore.QRect(710, 150, 51, 31)) 
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(12)
        self.episodes.setFont(font)
        self.episodes.setObjectName("episodes")
        #days
        self.days = QtWidgets.QLabel(self.centralwidget)
        self.days.setGeometry(QtCore.QRect(710, 250, 51, 31)) 
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(12)
        self.days.setFont(font)
        self.days.setObjectName("days")
        #mean
        self.mean = QtWidgets.QLabel(self.centralwidget)
        self.mean.setGeometry(QtCore.QRect(700, 50, 61, 51)) 
        font.setFamily("OCR A Extended")
        font.setPointSize(14)
        self.mean.setFont(font)
        self.mean.setObjectName("mean")
        #recents
        self.recents = QtWidgets.QLabel(self.centralwidget)
        self.recents.setGeometry(QtCore.QRect(470, 340, 301, 61))
        font.setFamily("Rockwell")
        font.setPointSize(9)
        self.recents.setFont(font)
        self.recents.setScaledContents(True)
        self.recents.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.recents.setWordWrap(True)
        self.recents.setObjectName("recents")
        #favourites
        self.favourites = QtWidgets.QLabel(self.centralwidget)
        self.favourites.setGeometry(QtCore.QRect(470, 400, 301, 61)) 
        font.setFamily("Rockwell")
        font.setPointSize(9)
        self.favourites.setFont(font)
        self.favourites.setScaledContents(True)
        self.favourites.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.favourites.setWordWrap(True)
        self.favourites.setObjectName("favourites")
        #characters
        self.c = QtWidgets.QLabel(self.centralwidget)
        self.c.setGeometry(QtCore.QRect(470, 470, 301, 91))
        font.setFamily("Rockwell")
        font.setPointSize(9)
        self.c.setFont(font)
        self.c.setScaledContents(True)
        self.c.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.c.setWordWrap(True)
        self.c.setObjectName("c")
        
        
        # Manga Info Labels
                 
                      
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(850, 50, 111, 31))
        font.setPointSize(16)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(850, 90, 111, 31))
        font.setPointSize(16)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        
        self.o_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.o_label_2.setGeometry(QtCore.QRect(830, 230, 91, 31)) 
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(12)
        self.o_label_2.setFont(font)
        self.o_label_2.setObjectName("o_label_2")
        self.o_label_2.setStyleSheet("color:yellow;")
        
        self.d_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.d_label_2.setGeometry(QtCore.QRect(830, 260, 91, 31)) 
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(12)
        self.d_label_2.setFont(font)
        self.d_label_2.setObjectName("d_label_2")
        self.d_label_2.setStyleSheet("color:red;")
        
        self.c_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.c_label_2.setGeometry(QtCore.QRect(830, 170, 101, 31)) 
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(12)
        self.c_label_2.setFont(font)
        self.c_label_2.setObjectName("c_label_2")
        self.c_label_2.setStyleSheet("color:blue;")
        
        self.w_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.w_label_2.setGeometry(QtCore.QRect(830, 140, 91, 31))
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(12)
        self.w_label_2.setFont(font)
        self.w_label_2.setObjectName("w_label_2")
        self.w_label_2.setStyleSheet("color:green;")
        
        self.p_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.p_label_2.setGeometry(QtCore.QRect(830, 200, 131, 31)) 
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(12)
        self.p_label_2.setFont(font)
        self.p_label_2.setObjectName("p_label_2")
        self.p_label_2.setStyleSheet("color:grey;")
        
        self.e_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.e_label_2.setGeometry(QtCore.QRect(830, 300, 101, 31))
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(12)
        self.e_label_2.setFont(font)
        self.e_label_2.setObjectName("e_label_2")
        
        self.r_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.r_label_2.setGeometry(QtCore.QRect(830, 360, 101, 31)) 
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(12)
        self.r_label_2.setFont(font)
        self.r_label_2.setObjectName("r_label_2")
                
        self.e_label_3 = QtWidgets.QLabel(self.centralwidget)
        self.e_label_3.setGeometry(QtCore.QRect(830, 330, 101, 31)) 
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(12)
        self.e_label_3.setFont(font)
        self.e_label_3.setObjectName("e_label_3")
        
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(800, 440, 71, 31))
        font.setPointSize(12)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(800, 500, 101, 31)) 
        font.setPointSize(12)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        
        self.days_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.days_label_2.setGeometry(QtCore.QRect(830, 390, 131, 31)) 
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(12)
        self.days_label_2.setFont(font)
        self.days_label_2.setObjectName("days_label_2")
        
        
        #Manga info Labels Pallete
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        
        
        
        
        
                                #MANGA INFO DATA
                                
                                
                                
                                
        #total
        self.mtotal = QtWidgets.QLabel(self.centralwidget)
        self.mtotal.setGeometry(QtCore.QRect(970, 40, 61, 51))
        font.setFamily("OCR A Extended")
        font.setPointSize(14)
        self.mtotal.setFont(font)
        self.mtotal.setObjectName("mtotal")
        #mean
        self.mmean = QtWidgets.QLabel(self.centralwidget)
        self.mmean.setGeometry(QtCore.QRect(970, 80, 61, 51))
        font.setFamily("OCR A Extended")
        font.setPointSize(14)
        self.mmean.setFont(font)
        self.mmean.setObjectName("mmean")
        #read
        self.read = QtWidgets.QLabel(self.centralwidget)
        self.read.setGeometry(QtCore.QRect(980, 170, 51, 31)) 
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(12)
        self.read.setFont(font)
        self.read.setObjectName("read")
        self.read.setStyleSheet("color:blue;")
        #on hold
        self.on_hold_m = QtWidgets.QLabel(self.centralwidget)
        self.on_hold_m.setGeometry(QtCore.QRect(980, 230, 51, 31))  
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(12)
        self.on_hold_m.setFont(font)
        self.on_hold_m.setObjectName("on_hold_m")
        self.on_hold_m.setStyleSheet("color:yellow;")
        #dropped
        self.dropped_m = QtWidgets.QLabel(self.centralwidget)
        self.dropped_m.setGeometry(QtCore.QRect(980, 260, 51, 31)) 
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(12)
        self.dropped_m.setFont(font)
        self.dropped_m.setObjectName("dropped_m")
        self.dropped_m.setStyleSheet("color:red;")
        #reading
        self.reading = QtWidgets.QLabel(self.centralwidget)
        self.reading.setGeometry(QtCore.QRect(980, 140, 51, 31))
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(12)
        self.reading.setFont(font)
        self.reading.setObjectName("reading")
        self.reading.setStyleSheet("color:green;")
        #plan to read
        self.plan_to_read = QtWidgets.QLabel(self.centralwidget)
        self.plan_to_read.setGeometry(QtCore.QRect(980, 200, 51, 31)) 
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(12)
        self.plan_to_read.setFont(font)
        self.plan_to_read.setObjectName("plan_to_read")
        self.plan_to_read.setStyleSheet("color:grey;")
        #chapters
        self.chapters = QtWidgets.QLabel(self.centralwidget)
        self.chapters.setGeometry(QtCore.QRect(980, 300, 51, 31))
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(12)
        self.chapters.setFont(font)
        self.chapters.setObjectName("chapters")
        #reread
        self.reread = QtWidgets.QLabel(self.centralwidget)
        self.reread.setGeometry(QtCore.QRect(980, 360, 51, 31)) 
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(12)
        self.reread.setFont(font)
        self.reread.setObjectName("reread")
        #days
        self.days_m = QtWidgets.QLabel(self.centralwidget)
        self.days_m.setGeometry(QtCore.QRect(980, 390, 51, 31)) 
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(12)
        self.days_m.setFont(font)
        self.days_m.setObjectName("days_m")
        #volumes
        self.volumes = QtWidgets.QLabel(self.centralwidget)
        self.volumes.setGeometry(QtCore.QRect(980, 330, 51, 31)) 
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(12)
        self.volumes.setFont(font)
        self.volumes.setObjectName("volumes")
        #recent
        self.recents_m = QtWidgets.QLabel(self.centralwidget)
        self.recents_m.setGeometry(QtCore.QRect(910, 440, 171, 61)) 
        font.setFamily("Rockwell")
        font.setPointSize(9)
        self.recents_m.setFont(font)
        self.recents_m.setScaledContents(True)
        self.recents_m.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.recents_m.setWordWrap(True)
        self.recents_m.setObjectName("recents_m")
        #favourites
        self.favourite_m = QtWidgets.QLabel(self.centralwidget)
        self.favourite_m.setGeometry(QtCore.QRect(910, 500, 171, 61))
        font.setFamily("Rockwell")
        font.setPointSize(9)
        self.favourite_m.setFont(font)
        self.favourite_m.setScaledContents(True)
        self.favourite_m.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.favourite_m.setWordWrap(True)
        self.favourite_m.setObjectName("favourite_m")
        
        
        #Menubar Setup
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1081, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        #Statusbar Setup
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        
        
        
        
                            #LABEL TEXT
        
        
        
        
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "malProfiler"))
	MainWindow.setWindowIcon(QtGui.QIcon("malProfiler"))
        
        #Top Bar
        self.user.setText(_translate("MainWindow", "Search First"))
        self.search.setText(_translate("MainWindow", "Name Here"))
        self.searchbtn.setText(_translate("MainWindow", "Search"))
        
        #User Labels
        
        self.label_2.setText(_translate("MainWindow", "Last Online"))
        self.label_3.setText(_translate("MainWindow", "Gender"))
        self.label_4.setText(_translate("MainWindow", "B.Day"))
        self.label_5.setText(_translate("MainWindow", "Joined"))
        self.label_6.setText(_translate("MainWindow", "Posts"))
        self.label_7.setText(_translate("MainWindow", "Reviews"))
        self.label_8.setText(_translate("MainWindow", "Recommends"))
        self.label_9.setText(_translate("MainWindow", "Friends"))
        
        self.last_online.setText(_translate("MainWindow", "Last Online"))
        self.sex.setText(_translate("MainWindow", "Gender"))
        self.birthday.setText(_translate("MainWindow", "B.Day"))
        self.joined.setText(_translate("MainWindow", "Joined"))
        self.forum_posts.setText(_translate("MainWindow", "Posts"))
        self.reviews.setText(_translate("MainWindow", "Reviews"))
        self.recommendations.setText(_translate("MainWindow", "Recommends"))
        self.friends.setText(_translate("MainWindow", "Friends"))
        
        #Anime Labels
        
        self.label.setText(_translate("MainWindow", "Anime  :"))
        self.w_label.setText(_translate("MainWindow", "Watching"))
        self.c_label.setText(_translate("MainWindow", "Completed"))
        self.p_label.setText(_translate("MainWindow", "Plan to Watch"))
        self.o_label.setText(_translate("MainWindow", "On Hold"))
        self.d_label.setText(_translate("MainWindow", "Dropped"))
        self.e_label.setText(_translate("MainWindow", "Episodes"))
        self.r_label.setText(_translate("MainWindow", "Rewatched"))
        self.days_label.setText(_translate("MainWindow", "Days"))
        self.label_12.setText(_translate("MainWindow", "Fav Chars"))
        self.label_11.setText(_translate("MainWindow", "Fav Anime"))
        self.label_10.setText(_translate("MainWindow", "Recents"))
        self.label_31.setText(_translate("MainWindow", "Mean  :"))
        
        self.total.setText(_translate("MainWindow", "0"))
        self.on_hold.setText(_translate("MainWindow", "0"))
        self.dropped.setText(_translate("MainWindow", "0"))
        self.completed.setText(_translate("MainWindow", "0"))
        self.watching.setText(_translate("MainWindow", "0"))
        self.plan_to_watch.setText(_translate("MainWindow", "0"))
        self.rewatched.setText(_translate("MainWindow", "0"))
        self.episodes.setText(_translate("MainWindow", "0"))
        self.days.setText(_translate("MainWindow", "0"))      
        self.mean.setText(_translate("MainWindow", "0"))       
        self.recents.setText(_translate("MainWindow", "_"))        
        self.favourites.setText(_translate("MainWindow", "_"))        
        self.c.setText(_translate("MainWindow", "_"))
        
        #Manga Labels
        
        self.label_13.setText(_translate("MainWindow", "Manga  :"))
        self.e_label_3.setText(_translate("MainWindow", "Volumes"))
        self.label_16.setText(_translate("MainWindow", "Recents"))
        self.label_17.setText(_translate("MainWindow", "Fav Manga"))
        self.label_14.setText(_translate("MainWindow", "Mean    :"))
        self.o_label_2.setText(_translate("MainWindow", "On Hold"))
        self.d_label_2.setText(_translate("MainWindow", "Dropped"))
        self.c_label_2.setText(_translate("MainWindow", "Read"))
        self.w_label_2.setText(_translate("MainWindow", "Reading"))
        self.e_label_2.setText(_translate("MainWindow", "Chapters"))
        self.r_label_2.setText(_translate("MainWindow", "Reread"))
        self.days_label_2.setText(_translate("MainWindow", "Days"))
        self.p_label_2.setText(_translate("MainWindow", "Plan to Read"))
        
        self.mtotal.setText(_translate("MainWindow", "0"))
        self.mmean.setText(_translate("MainWindow", "0"))
        self.on_hold_m.setText(_translate("MainWindow", "0"))
        self.dropped_m.setText(_translate("MainWindow", "0"))
        self.read.setText(_translate("MainWindow", "0"))
        self.reading.setText(_translate("MainWindow", "0"))
        self.plan_to_read.setText(_translate("MainWindow", "0"))
        self.chapters.setText(_translate("MainWindow", "0"))
        self.reread.setText(_translate("MainWindow", "0"))
        self.days_m.setText(_translate("MainWindow", "0"))
        self.volumes.setText(_translate("MainWindow", "0"))
        self.recents_m.setText(_translate("MainWindow", "_"))
        self.favourite_m.setText(_translate("MainWindow", "_"))

    def searchbtn_pressed(self):
            user_info, anime_info, manga_info = mal_search(str(self.search.text()))

            self.pp.setPixmap(QtGui.QPixmap("./pp.jpg"))
            self.user.setText(user_info["user"])
            self.sex.setText(user_info["sex"])
            self.recommendations.setText(user_info["recommendations"])
            self.reviews.setText(user_info["reviews"])
            self.joined.setText(user_info["joined"])
            self.forum_posts.setText(user_info["forum_posts"])
            self.last_online.setText(user_info["last_online"])
            self.birthday.setText(user_info["birthday"])
            self.friends.setText(user_info["friends"])
            
            self.total.setText(anime_info["total"])
            self.on_hold.setText(anime_info["on_hold"])
            self.dropped.setText(anime_info["dropped"])
            self.completed.setText(anime_info["completed"])
            self.watching.setText(anime_info["watching"])
            self.plan_to_watch.setText(anime_info["plan_to_watch"])
            self.rewatched.setText(anime_info["rewatched"])
            self.episodes.setText(anime_info["episodes"])
            self.days.setText(anime_info["days"])
            self.mean.setText(anime_info["mean"])
            self.recents.setText(anime_info["recents"])
            self.favourites.setText(anime_info["favorites"])
            self.c.setText(anime_info["characters"])
            
            self.mtotal.setText(manga_info["total"])
            self.mmean.setText(manga_info["mean"])
            self.on_hold_m.setText(manga_info["on_hold"])
            self.dropped_m.setText(manga_info["dropped"])
            self.read.setText(manga_info["read"])
            self.reading.setText(manga_info["reading"])
            self.plan_to_read.setText(manga_info["plan_to_read"])
            self.chapters.setText(manga_info["chapters"])
            self.reread.setText(manga_info["reread"])
            self.days_m.setText(manga_info["days"])
            self.volumes.setText(manga_info["volumes"])
            self.recents_m.setText(manga_info["recent"])
            self.favourite_m.setText(manga_info["favorite"])

import sys
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())