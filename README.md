运行命令
开启激光雷达：roslaunch limo_bringup limo_start.launch pub_odom_tf:=false
开启SLAM：roslaunch limo_bringup limo_gmapping.launch
开启导航：roslaunch limo_bringup limo_navigation_diff.launch
开启键盘操作：roslaunch limo_bringup limo_teletop_keyboard.launch

保存地图：
cd ~/agilex_ws/src/limo_ros/limo_bringup/maps/ 
rosrun map_server map_saver –f [mapname]

修改启动地图：
roscd limo_bringup/launch
vi limo_navigation_diff.launch
改第20行

启动设定目的地节点：
rosrun limo_controller limo_control_20231215.py

修改移动速度：
cd agilex_ws/src/limo_ros/limo_bringup/param/diff
vi planner.yaml
修改第13行的max_vel_x
