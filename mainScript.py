from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg
import numpy as np
from MainForm import Ui_MainWindow
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#win = pg.GraphicsWindow(title="Basic plotting examples")
#win.resize(1000,600)
#win.setWindowTitle('pyqtgraph example: Plotting')
#
## Enable antialiasing for prettier plots
#pg.setConfigOptions(antialias=True)
#
#p1 = win.addPlot(title="Basic array plotting", y=np.random.normal(size=100))
#
#p2 = win.addPlot(title="Multiple curves")
#p2.plot(np.random.normal(size=100), pen=(255,0,0), name="Red curve")
#p2.plot(np.random.normal(size=110)+5, pen=(0,255,0), name="Green curve")
#p2.plot(np.random.normal(size=120)+10, pen=(0,0,255), name="Blue curve")
#
#p3 = win.addPlot(title="Drawing with points")
#p3.plot(np.random.normal(size=100), pen=(200,200,200), symbolBrush=(255,0,0), symbolPen='w')
#
#
#win.nextRow()
#
#p4 = win.addPlot(title="Parametric, grid enabled")
#x = np.cos(np.linspace(0, 2*np.pi, 1000))
#y = np.sin(np.linspace(0, 4*np.pi, 1000))
#p4.plot(x, y)
#p4.showGrid(x=True, y=True)
#
#p5 = win.addPlot(title="Scatter plot, axis labels, log scale")
#x = np.random.normal(size=1000) * 1e-5
#y = x*1000 + 0.005 * np.random.normal(size=1000)
#y -= y.min()-1.0
#mask = x > 1e-15
#x = x[mask]
#y = y[mask]
#p5.plot(x, y, pen=None, symbol='t', symbolPen=None, symbolSize=10, symbolBrush=(100, 100, 255, 50))
#p5.setLabel('left', "Y Axis", units='A')
#p5.setLabel('bottom', "Y Axis", units='s')
#p5.setLogMode(x=True, y=False)
#
#p6 = win.addPlot(title="Updating plot")
#curve = p6.plot(pen='y')
#data = np.random.normal(size=(10,1000))
#ptr = 0
#def update():
#    global curve, data, ptr, p6
#    curve.setData(data[ptr%10])
#    if ptr == 0:
#        p6.enableAutoRange('xy', False)  ## stop auto-scaling after the first data set is plotted
#    ptr += 1
#timer = QtCore.QTimer()
#timer.timeout.connect(update)
#timer.start(50)
#
#
#win.nextRow()
#
#p7 = win.addPlot(title="Filled plot, axis disabled")
#y = np.sin(np.linspace(0, 10, 1000)) + np.random.normal(size=1000, scale=0.1)
#p7.plot(y, fillLevel=-0.3, brush=(50,50,200,100))
#p7.showAxis('bottom', False)
#
#
#x2 = np.linspace(-100, 100, 1000)
#data2 = np.sin(x2) / x2
#p8 = win.addPlot(title="Region Selection")
#p8.plot(data2, pen=(255,255,255,200))
#lr = pg.LinearRegionItem([400,700])
#lr.setZValue(-10)
#p8.addItem(lr)
#
#p9 = win.addPlot(title="Zoom on selected region")
#p9.plot(data2)
#def updatePlot():
#    p9.setXRange(*lr.getRegion(), padding=0)
#def updateRegion():
#    lr.setRegion(p9.getViewBox().viewRange()[0])
#lr.sigRegionChanged.connect(updatePlot)
#p9.sigXRangeChanged.connect(updateRegion)
#updatePlot()

# Enable antialiasing for prettier plots
pg.setConfigOptions(antialias=True)
ui = Ui_MainWindow()

address_book = ['andreas.vonkaenel@drivetek.ch']
msg = MIMEMultipart()    
sender = "avonk@gmx.ch"
subject = "Testmail"
body = "This is my email body"

msg['From'] = sender
msg['To'] = ','.join(address_book)
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))
text=msg.as_string()
#print text
# Send the message via our SMTP server
s = smtplib.SMTP('mail.gmx.net', 587)
s.starttls()
pwd = "%L6\\\\9])a}1S"
s.login("avonk@gmx.ch", pwd)
s.sendmail(sender, address_book, text)
s.quit()        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.HelloWorldLabel.setText("ClickMe - no please not!!!")
    ui.graphicsView.plot(title="Basic array plotting", y=np.random.normal(size=100))
    ui.graphicsView.showGrid(True, True, 0.5)
    ui.graphicsView.showAxis('bottom', True)
    ui.graphicsView.setLabel('left', "Y Axis", units='A')
    MainWindow.show()
    sys.exit(app.exec_())