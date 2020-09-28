#include "mainwindow.h"

#include<QUrl>

MainWindow::MainWindow(QWidget *parent) : QMainWindow(parent) {

	mediaContent = new QMediaContent(QUrl("http://192.168.43.1:8080/video"));
	mp = new QMediaPlayer();
	mp->setMedia(*mediaContent);
	v = new QVideoWidget;
	mp->setVideoOutput(v);
	setCentralWidget(v);
	v->show();
	mp->play();
}

MainWindow::~MainWindow() {
	delete mediaContent;
	delete mp;
	delete v;

}

