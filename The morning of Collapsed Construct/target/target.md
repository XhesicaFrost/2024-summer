一个结合了superhot中的时间流动特点，移动则加快，停止则减慢的弹幕游戏

按照时间充裕程度加上关卡，无尽等模式

等待开发：

​	敌人：坍缩体：随机刷新位置，跟踪玩家 finished

​			无差别轰炸：随机选择一条直线，可以同时存在多条，同时攻击

​				具体实现，一个炸弹类，一个轰炸group，一个炸弹group

​					每产生一次轰炸就首先产生一条线，1s，红色，警告，然后取出轰炸group，产生足够的炸弹，扔到炸弹group里，炸弹group元素存在3s后小时。
​                    finished
​					

​			染污躯壳突袭：出现一个污染躯壳，随机一条直线(水平或者垂直)，冲刺(finished)

​			国度：存在一段时间，不可碰触(finished)

​	玩家：隐藏 ：空格键，有冷却系统，可以隐藏3s不受攻击 finished

​	控制系统：统计存活时长，游戏结束的页面（finished），游戏背景