QT       += core gui

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

CONFIG += c++17

# You can make your code fail to compile if it uses deprecated APIs.
# In order to do so, uncomment the following line.
#DEFINES += QT_DISABLE_DEPRECATED_BEFORE=0x060000    # disables all the APIs deprecated before Qt 6.0.0

SOURCES += \
    main.cpp \
    mainwindow.cpp
    nivisa64.lib

HEADERS += \
    mainwindow.h
    visatype.h
    visa.h

FORMS += \
    mainwindow.ui

# Default rules for deployment.
qnx: target.path = /tmp/$${TARGET}/bin
else: unix:!android: target.path = /opt/$${TARGET}/bin
!isEmpty(target.path): INSTALLS += target

win32:CONFIG(release, debug|release): LIBS += -L$$PWD/./ -lnivisa64
else:win32:CONFIG(debug, debug|release): LIBS += -L$$PWD/./ -lnivisa64d
else:unix: LIBS += -L$$PWD/./ -lnivisa64

INCLUDEPATH += $$PWD/.
DEPENDPATH += $$PWD/.

win32:CONFIG(release, debug|release): LIBS += -L$$PWD/./ -lvisa32
else:win32:CONFIG(debug, debug|release): LIBS += -L$$PWD/./ -lvisa32d
else:unix: LIBS += -L$$PWD/./ -lvisa32

INCLUDEPATH += $$PWD/.
DEPENDPATH += $$PWD/.
