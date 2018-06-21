# _*_ coding:utf-8  _*_
import random
from  time import sleep
#   Python开发可控的掷色子程序，豹子通杀！
def get_dice():
    return random.randint(1,6)

def the_open(play_dice,computer_dice):
    print("双方开");
    sleep(1)
    print("玩家"+str(play_dice))
    sleep(1)
    print("电脑"+str(computer_dice))
    sleep(1)

def every_game(play_money,computer_money):
    print("Get Ready~~~~~~");
    print("go");
    sleep(2)
    print("双方的筹码");
    print("玩家:"+str(play_money))
    print("电脑:"+str(computer_money))
    sleep(2)
    print("玩家投点")
    sleep(1)
    play_dice = get_dice();
    print("您的点数：" + str(play_dice))
    sleep(2)
    print("电脑投点")
    sleep(1)
    computer_dice = get_dice()
    print("电脑投点完毕")
    sleep(1)
    result=input("玩家放先下注，是否下注？[y?n]")
    if result=='y':
        while True:
            play_bets=input('选择下注范围：[1-{0}]'.format(play_money))
            if int(play_bets)>=1 and int(play_bets)<=int(play_money):
                break;
        print("玩家下注%s"%play_bets)
        sleep(1)
        print ("电脑思考中。。。。。。")
        sleep(2)
        if random.choice('yn')==str('y'):
            computer_best=random.randint(1,computer_money)
            print("电脑下注%s" %computer_best)
            sleep(1)
            the_open(play_dice,computer_dice)
            if play_dice>computer_dice:
                print("玩家胜利！玩家赢得筹码%s"%computer_best)
                play_money+=computer_best
                computer_money-=computer_best
            elif play_dice==computer_dice:
                print ("平局")
            else:
                print("电脑升级！玩家输掉筹码%s"%play_bets)
                play_money-=play_bets
                computer_money+=play_bets
        else:
            print("电脑放弃下注！玩家收回自己的筹码")
            sleep(1)
            the_open(play_dice,computer_dice)
    else:
        print("玩家放弃下注")
        sleep(1)
        the_open(play_dice, computer_dice)
    return [play_money,computer_money]

def play_game():
    print("游戏开始");
    play_money=100
    compuer_money=100
    sleep(1)
    while play_money !=0 and compuer_money !=0:
        money_list=every_game(play_money,compuer_money)
        play_money=money_list[0]
        compuer_money=money_list[1]
    if play_money==0:
        print('电脑获胜')
    else:
        print('玩家获胜')

        
if __name__=='__main__':
        play_game()