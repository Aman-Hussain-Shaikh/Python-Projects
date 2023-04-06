from plyer import notification
import time

if __name__ =='__main__':
    while True:
        notification.notify(
            title="Focus on Study",
            message="You are very close to achieve your goal",
            app_icon="E:\Python_Projects\#5 Take a break desktop notification\icon.ico",
            timeout=5)
        time.sleep(2400)

#pythonw pythonapp.py