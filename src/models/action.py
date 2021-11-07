class Action:
    def __init__(self, text):
        self.text = text

    def get(self):
        return {
            "哈囉, Phoebe": {"action": "揮手", "text": "Hello, {username}"},
            "看起來不太好吃 我媽以前": {"action": "靜止", "text": ""},
            "Phoebe 人死了之後 到底去哪裡": {"action": "說話", "text": "墳墓 一般都是火葬，現在沒有人土葬"},
        }[self.text]
