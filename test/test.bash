#!/bin/bash 
# SPDX-FileCopyrightSPDX-FileCopyrightText: 2025 Kakeru Tanaka
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build --symlink-install #ビルド　actinsで使うのであげる前にコメントアウト切る sudoで実行してもパッケージ見つからない
source $dir/.bashrc

echo "Starting ROS2 node for testing..."
ros2 run send_login_info send_login_info &  #nodeを起動
ROS2_PID=$! #終了時にnodeを止めるためにプロセスIDを取得

sleep      #ノードが起動するのを待つ

#テストを実行
echo "Running tests..."/
ros2 topic list
if ros2 topic list | grep -q "/login_info"; then    #アクティブなトピックにlogin_infoがあるなら
    echo "Topic /login_info exists. Test passed."
else
    echo "Topic /login_info does not exist. Test failed."
    kill $ROS2_PID  #nodeをキル
    exit 1  #終了コード1
fi  #シェルの条件分岐はfiで囲む

kill $ROS2_PID #nodeをキル
echo "successfully." 
exit 0 