import pytest



class EmailNotification:

    def send(self, message):
        return message


class SMSNotification:

    def send(self, message):
        return message


class PushNotification:

    def send(self, message):
        return message


class NotificationProcessor:

    def create_notification_type(self, type: str):
        if type == "email":
            return self.create_email()
        elif type == "push":
            return self.create_push()
        elif type == "sms":
            return self.create_sms()
        else:
            raise ValueError(f"Unknown type: {type}")

    def create_email(self):
        return EmailNotification()

    def create_push(self):
        return PushNotification()

    def create_sms(self):
        return SMSNotification()



def test_type_email():
    processor = NotificationProcessor()
    email = processor.create_notification_type("email")
    assert email.send("test1") == "test1"

def test_type_sms():
    processor = NotificationProcessor()
    sms = processor.create_notification_type("sms")
    assert sms.send("test1") == "test1"
    

def test_type_push():
    processor = NotificationProcessor()
    push = processor.create_notification_type("push")
    assert push.send("test1") == "test1"

def test_invalid():
    processor = NotificationProcessor()
    with pytest.raises(ValueError):
        invalid = processor.create_notification_type("invalid")
    