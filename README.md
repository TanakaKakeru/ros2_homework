# ros2_homework
[![test.bash](https://github.com/TanakaKakeru/ros2_homework/actions/workflows/test.yml/badge.svg)](https://github.com/TanakaKakeru/ros2_homework/actions/workflows/test.yml)

ロボットシステム学の第二回課題提出用のリポジトリです。
このリポジトリ内には2つのROS2パッケージが入っています。

# send_login_infoパッケージ

ノードが実行されているコンピュータのログイン情報を送信するためのパッケージです。

## send_login_infoノード

ノードを実行中のコンピュータに現在ログインしているユーザー名、ターミナル名、ログイン時刻、IPアドレスを、後述のLoginInfoArrayArray型のリスト"users"でトピック"login_info"に1秒間隔に流します。IPアドレスが不明な場合は表示がnoneになります。実行にはリポジトリに同梱されたlogin_info_msgsパッケージが必要となります。

### トピックに流れる情報
ros2 topic echoで確認できる情報の例です。
```
$ ros2 topic echo login_info
users:
- user: user1
  terminal: pts/1
  login_time: 2025-01-01 13:23
  ip_address: none
- user: user2
  terminal: pts/8
  login_time: 2025-01-01 15:33
  ip_address: ::1
---
```
# login_info_msgsパッケージ

send_login_infoで使用するメッセージの型が入ったパッケージです。

## LoginInfo型

ユーザー名、ターミナル名、ログイン時刻、IPアドレスを格納するstrings型が4つ入った型です。中の要素名はuser、terminal、login_time、ip_addressとなっています。

## LoginInfoArray型

LoginInfo型をリストとして使用できるようにしたものです。

# インストール方法

send_login_infoディレクトリとlogin_info_msgsディレクトリを、ros2のワークスペースディレクトリ内のsrcの下に配置してビルドした後、souceで再読み込みしてください。

- 例
```
$ mv ros2_homework/send_login_info ros2_homework/login_info_msgs ~/ros_ws/src/.
$ cd ~/ros2ws 
$ colcon build
$ source ~/.bashrc
```

# 実行に必要なソフトウェア
- Python
- ROS2

# テスト環境
- Ubuntu 22.04 LTS (ROS2 humble)

# ライセンス
- このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．

© 2025 Kakeru Tanaka
