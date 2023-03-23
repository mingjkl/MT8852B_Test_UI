/*
 * @Author: emmovo
 * @Date: 2023-03-20 15:49:44
 * @LastEditors: emmovo
 * @LastEditTime: 2023-03-21 09:47:35
 * @FilePath: \VISA-TEST\mainwindow.cpp
 * @Description: 
 * 
 * Copyright (c) 2023 by mingjkl@live.com/emmovo.com, All Rights Reserved. 
 */
#include "mainwindow.h"
#include "ui_mainwindow.h"

#include "visa.h"
#include <QDebug>
#include "visatype.h"


static ViStatus status;
static ViSession defaultRM;
static ViSession instr;
static ViUInt32 retCount;
static ViChar buf[256];
static ViUInt32 bufSize = sizeof(buf);


MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    
    status = viOpenDefaultRM(&defaultRM);
    if(status < VI_SUCCESS)
    {
        qDebug() << "Could not open VISA";
    }
}

MainWindow::~MainWindow()
{
    delete ui;
}

