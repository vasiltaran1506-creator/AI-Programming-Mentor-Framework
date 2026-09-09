import pytest



class FlyBehavior:

    def execute(self, name):
        return True


class SwimBehavior:

    def execute(self, name):
        return True


class SpeakBehavior:

    def execute(self, name):
        return True


class RunBehavior:

    def execute(self, name):
        return True


class Bird:

    def __init__(self, name, fly_behavior=None, swim_behavior = None, speak_behavior=None, run_behavior=None) -> None:

        self.name = name

        self.fly_behavior = fly_behavior
        self.swim_behavior = swim_behavior
        self.speak_behavior = speak_behavior
        self.run_behavior = run_behavior

    def fly(self):
        if self.fly_behavior:
            return self.fly_behavior.execute(self.name) 
        else:
            return False


    def swim(self):
        if self.swim_behavior:
            return self.swim_behavior.execute(self.name)
        else:
            return False

    def speak(self):
        if self.speak_behavior:
            return self.speak_behavior.execute(self.name)
        else:
            return False

    def run(self):
        if self.run_behavior:
            return self.run_behavior.execute(self.name)
        else:
            return False


eagle = Bird(
    name="eagle",
    fly_behavior=FlyBehavior(),
)

parrot = Bird(
    name="parrot",
    fly_behavior=FlyBehavior(),
    speak_behavior=SpeakBehavior()
)

penguin = Bird(
    name="penguin",
    swim_behavior=SwimBehavior()
)

straus = Bird(
    name="straus",
    run_behavior=RunBehavior()
)

def test_eagle_fly():
    assert eagle.fly() == True

def test_penguin_cant_fly_can_swim():
    assert penguin.fly() == False
    assert penguin.swim() == True

def test_parrot_speak():
    assert parrot.speak() == True

def test_straus_run():
    assert straus.run() == True