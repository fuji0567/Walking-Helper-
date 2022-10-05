import RPi.GPIO as GPIO
import time
import sys, os

# ボタンを押したらプログラムを呼び出す
if __name__ == "__main__":
    # GPIOピン番号設定
    pin1 = 15
    pin2 = 21

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin1, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    GPIO.setup(pin2, GPIO.IN, pull_up_down = GPIO.PUD_UP)

    # ボタンクリック待機中
    print("ボタン待機中...")

    while True:
        button1 = GPIO.input(pin1)
        button2 = GPIO.input(pin2)


        cmd = ""
        if button1 == False:
            # ボタン1の処理
            cmd = "sudo shutdown -h now"# 例です

        elif button2 == False:
            # ボタン2の処理
            cmd = "sudo python3 /home/unity/Document/0915.py"# 例です

        # 実行
        if cmd != "":
            os.popen(cmd).readline().strip()
            time.sleep(1)# ボタンを押した後のチャタリング防止のため

        time.sleep(0.1)

    GPIO.cleanup()
