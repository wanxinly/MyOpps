import pyautogui
import time
# import sys
# locations = [r'qiyong.png', r'tijiao.png',r'chongzhi.png']

# write with selenium module later

pyautogui.FAILSAFE = False


class ClickTarget(object):
    position_colors = [(47, 115, 177), (250, 253, 255), (255, 212, 118), (0, 50, 134),
                       (220, 233, 240), (102, 102, 51), (229, 145, 105), (233, 242, 251)]

    positions = [(123, 402), (610, 179), (578, 213), (130, 384),
                 (483, 532), (226, 67), (85, 875), (90, 12)]

    def __init__(self, x, y):
        self.x = x
        self.y = y

    #def move_to(self, count):
    #    location = r'c:\users\administrator\desktop\x\\'
    #    button = pyautogui.locateOnScreen(location + locations[count])
    #    button_x, button_y = pyautogui.center(button)
    #    pyautogui.moveTo(button_x, button_y)
    #    return button_x, button_y

    @staticmethod
    def delay_time(seconds):
        time.sleep(seconds)

    def target_color(self):
        return ClickTarget.position_colors[ClickTarget.positions.index((self.x, self.y))]

    def target_position(self):
        print('目标点坐标值: ', (self.x, self.y), ' 目标点灰度值: ', ClickTarget.target_color(self))

    @staticmethod
    def refresh_window():
        pyautogui.hotkey('f5')
        time.sleep(2)
        pyautogui.hotkey('enter')
        ClickTarget.delay_time(1)

    def move_mice(self):
        print('移动鼠标并准备点击.........., 测试当前鼠标位置参数')
        pyautogui.moveTo(self.x, self.y)  # 移动鼠标至目标点
        mice_position = pyautogui.position()  # 获取鼠标点位置参数
        mice_color = pyautogui.screenshot().getpixel(mice_position)  # 获取鼠标点灰度
        print('鼠标处坐标值:', mice_position, '  鼠标处灰度值: ', mice_color)  # 打印鼠标点位置和灰度

    def click_point(self):
        ClickTarget.target_position(self)
        ClickTarget.move_mice(self)
        ClickTarget.delay_time(0.5)
        # 测试鼠标点灰度和目标点固定灰度是否一致
        while True:
            if pyautogui.pixelMatchesColor(self.x, self.y, ClickTarget.target_color(self)):
                pyautogui.click(self.x, self.y, button='left')  # 测试成功点击
                print('参数正确，点击:', pyautogui.position())    # 点击位置
                break
            else:
                print('当前位置错误，程序重新执行')  # 错误信息
                ClickTarget.refresh_window()
                ClickTarget.delay_time(1)

    @staticmethod
    def input_number():
        num_list = input('请输入工号,多个工号以逗号结尾: ').split(',')
        for num in num_list:
            ClickTarget(123, 402).click_point()
            time.sleep(2)
            ClickTarget(610, 179).click_point()
            pyautogui.typewrite(num)
            pyautogui.hotkey('enter')
            time.sleep(1)
            ClickTarget(578, 213).click_point()
            time.sleep(3)
            ClickTarget(130, 384).click_point()
            time.sleep(3)
            pyautogui.click(483, 532, button='left')
            time.sleep(0.5)
            pyautogui.hotkey('alt', 'r')
            time.sleep(9)
            pyautogui.hotkey('f11')
            time.sleep(1)
            pyautogui.typewrite(num)
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'f11')
            time.sleep(1)
            pyautogui.hotkey('tab')
            time.sleep(1)
            pyautogui.typewrite('111111')
            time.sleep(1)
            pyautogui.hotkey('tab')
            time.sleep(1)
            pyautogui.typewrite('111111')
            time.sleep(1)
            pyautogui.hotkey('ctrl', 's')
            time.sleep(3)
            pyautogui.click(85, 875, button='left')
            time.sleep(1)
            pyautogui.click(90, 12, button='left')

if __name__ == "__main__":
    ClickTarget(123, 402).input_number()


