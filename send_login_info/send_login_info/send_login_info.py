import rclpy    # ROS 2のクライアントのためのライブラリ
from rclpy.node import Node  # ノードを実装するためのNodeクラス
from login_info_msgs.msg import LoginInfo, LoginInfoArray  # 通信の型

import subprocess

rclpy.init()
node = Node("send_login_info")  # ノード作成（nodeという「オブジェクト」を作成）
pub = node.create_publisher(LoginInfoArray, "login_info", 10)  # パブリッシャのオブジェクト作成


def get_logged_in_users_info():  # whoから情報を取得しリストに入れる関数
    # whoコマンドを実行
    result = subprocess.run(['who'], stdout=subprocess.PIPE, text=True)
    output = result.stdout.strip()

    users_info = []  # リストを用意
    for line in output.split("\n"):  # 行毎に繰り返し
        parts = line.split()  # 空白で一行を分割
        user = parts[0]  # ユーザー名
        terminal = parts[1]  # ログイン媒体
        login_time = ' '.join(parts[2:4])  # ログイン時刻
        if len(parts) >= 5:  # 要素が5個以上なら
            ip_address = parts[4].strip('()')  # IPアドレスを()を取り除いて取得
        else:
            ip_address = "none"  # ローカルの場合

        users_info.append({  # 情報をリストに追加
            "user": user,
            "terminal": terminal,
            "login_time": login_time,
            "ip_address": ip_address
        })

    return users_info


def cb():  # 定期実行されるコールバック関数
    msg = LoginInfoArray()  # メッセージ配列のオブジェクト
    info = get_logged_in_users_info()
    for entry in info:
        user_msg = LoginInfo()  # 各ユーザーの情報を格納するメッセージ
        user_msg.user = entry['user']
        user_msg.terminal = entry['terminal']
        user_msg.login_time = entry['login_time']
        user_msg.ip_address = entry['ip_address']
        #print(get_logged_in_users_info())
        msg.users.append(user_msg)  # 配列に追加
    #print("Publishing msg:", msg)  # デバッグ出力
    pub.publish(msg)  # 配列をまとめて送信


def main():
    node.create_timer(1, cb)  # タイマー設定
    rclpy.spin(node)  # 実行（無限ループ）
