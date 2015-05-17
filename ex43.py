import random
class Scene(object):

    def enter(self):
        print "should be implemented in subclass"
        exit(1)


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        next_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')
        while next_scene!=last_scene:
            current = next_scene
            print current
            next_scene_string = current.enter()
            next_scene = self.scene_map.next_scene(next_scene_string)
        next_scene.enter()


class Finished(Scene):
    def enter(self):
        print "Game is now over"
       # exit(0)
        return "finished"

class Death(Scene):

    def enter(self):
        print "you are dead, that is sad :("
        exit(0)

class CentralCorridor(Scene):

    def enter(self):
        print "You stand in a central corridor"
        guess =raw_input("> ")
        if guess =="1":
            return "laser_weapon_armory"
        else:
            return "death"

class LaserWeaponArmory(Scene):

    def enter(self):
        print "lasers woho"
        return "finished"
        

class TheBridge(Scene):

    def enter(self):
        pass

class EscapePod(Scene):

    def enter(self):
        pass


class Map(object):

    scenes = {
              "central_corridor" : CentralCorridor(),
              "death" : Death(),
              "laser_weapon_armory" : LaserWeaponArmory(),
              "the_bride" : TheBridge(),
              "escape_pod" : EscapePod(),
              "finished" : Finished() }


    def __init__(self, start_scene):
        self.start_scene = start_scene

        

    def next_scene(self, scene_name):
        return Map.scenes[scene_name]

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()