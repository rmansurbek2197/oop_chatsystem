import time


class User:
    def __init__(self, uid, name):
        self.uid = uid
        self.name = name
        self.online = False


class Message:
    def __init__(self, sender_id, text):
        self.sender_id = sender_id
        self.text = text
        self.timestamp = time.time()


class ChatRoom:
    def __init__(self):
        self.users = {}
        self.messages = []

    def add_user(self, user):
        self.users[user.uid] = user
        user.online = True

    def remove_user(self, uid):
        if uid in self.users:
            self.users[uid].online = False
            del self.users[uid]

    def send_message(self, uid, text):
        if uid in self.users:
            msg = Message(uid, text)
            self.messages.append(msg)

    def get_chat_history(self):
        return [
            {
                "user": self.users.get(m.sender_id).name if m.sender_id in self.users else "unknown",
                "text": m.text,
                "time": m.timestamp
            }
            for m in self.messages
        ]
