# RMSdashboard
 A simple dashboard for the Raspberry Pi Meteor System (RMS) that makes using a touchscreen easy.

 Configuration:
 RMSdashboard is configure through the dash.config file. 

 Note: This package makes use of the QT Virtual Keyboard and will likely require extra components to be installed if you want to use it. Something like the following (from https://stackoverflow.com/questions/63719347/install-qtvirtualkeyboard-in-raspberry-pi/63720177#63720177) should do the trick.

sudo apt-get update
sudo apt install git build-essential
sudo apt-get install python3-pyqt5 qt5-default qtdeclarative5-dev libqt5svg5-dev qtbase5-private-dev qml-module-qtquick-controls2 qml-module-qtquick-controls qml-module-qt-labs-folderlistmodel
sudo apt-get install '^libxcb.*-dev' libx11-xcb-dev libglu1-mesa-dev libxrender-dev libxi-dev libxkbcommon-dev libxkbcommon-x11-dev
git clone -b 5.11 https://github.com/qt/qtvirtualkeyboard.git
cd qtvirtualkeyboard
qmake 
sudo make
sudo make install
