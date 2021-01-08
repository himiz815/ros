# 課題2

## 概要
上田隆一先生のスライド(https://ryuichiueda.github.io/robosys2020/lesson10_ros.html#/ )を参考にし改変してROSのコードを作成しました。

## 内容
好きな数値を入力することでその数値ずつプラスされ表示される。

## 動作環境 
OS:Ubuntu 20.04

## 使用したもの
・Raspberry Pi4   


## インストール方法と動かし方 
catkin_ws/src のワークスペースを作る
``` 
$ git clone https://github.com/himiz815/ros.git
```
を行い中のrosworkをcatkin_wsの下に置く
``` 
$ cd ~/catkin_ws
```
``` 
$ catkin_make
```
``` 
$ source ~/.bashrc
```
``` 
端末1,端末2$ cd ~/catkin_ws/src/roswork/script 
```
``` 
端末1,端末2$ cd ~/catkin_ws/src/roswork/script 
```
``` 
端末1$ roscore &
```
``` 
端末1$ chmod +x count.py
```
``` 
端末1$ rosrun roswork count.py
```
``` 
端末2$ chmod +x output.py
```
``` 
端末2$ rosrun roswork output.py
```
好きな数値を入力する

## 動画
https://youtu.be/4HaETYS8fyU

## ライセンス
[GNU General Public License v3.0](https://github.com/kiyoshirou-kawanabe/Robosys_Devicedriver/blob/main/COPYING)
