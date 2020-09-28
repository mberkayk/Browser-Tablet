#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QVideoWidget>
#include <QMediaContent>
#include <QMediaPlayer>

class MainWindow : public QMainWindow
{
	Q_OBJECT

public:
	MainWindow(QWidget *parent = nullptr);
	~MainWindow();

private:
	QMediaContent *mediaContent;
	QMediaPlayer *mp;
	QVideoWidget *v;
};
#endif // MAINWINDOW_H
