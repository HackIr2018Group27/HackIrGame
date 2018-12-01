from pygame import *
from math import *
init()

# class that handles everything related to the player
class Player:

    def __init__(self, x, y, suddenDeath, color, radius):
        # directions is a list containing states for moving up, down, left or right
        # speed is thepllayers speed constant (subject to change if upgrades are implemented)
        # x and y are thepllayers technical x and yplosition value, but they do not represent the hitbox. Think of them as theplosition of the top-left corner of the IMAGE for thepllayer.
        # original_image acts as a constant reference to the original image, and is used to avoid distortion
        # image is what changes during theplrogram
        # rect is the box of the IMAGE for thepllayer, it does not represent the hitbox.
        # hitbox w and h are the Height and Width of the hitbox for the player. they are constant.
        # center x and y represent the middle of the box of the IMAGE for thepllayer.
        # hitbox is what the enemy is going to want to show in order to lower thepllayers' health. it's dimensions are constant, but it moves with thepllayer.
        self.directions = [False, False, False, False]
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius
        self.hitbox_side = int(sqrt(2) * (radius*2) / 2)
        self.hitbox = Rect(self.x - self.hitbox_side, self.y - self.hitbox_side, self.hitbox_side,
                           self.hitbox_side)

        self.sd = suddenDeath
        self.show = 0

        # player stats
        self.gun = 1
        self.speed = 10
        if suddenDeath:
            self.max_health = 1000
            self.health = 1000
        else:
            self.max_health = 1
            self.health = 1

    # handles movement and health of player
    def update(self, enemy, enemyBullets):
        # if any direction states are true, movespllayer in said direction using self.speed
        if self.directions[0]:
            if 0 < self.y:
                self.y -= self.speed
        if self.directions[1]:
            if self.y < 700:
                self.y += self.speed
        if self.directions[2]:
            if 0 < self.x:
                self.x -= self.speed
        if self.directions[3]:
            if self.x < 1000:
                self.x += self.speed
                # update hitBox and muzzle x/y

        self.hitbox = Rect(self.x - 20, self.y - 20, 40, 40)
        # updates mouse x and y interpretation

        # check if any enemy bullets show the player
        for b in enemyBullets:
            if self.hitbox.colliderect(b.rect):
                self.health -= b.dmg
                self.show = 120

        if self.hitbox.colliderect(enemy.hitbox):
            try:
                self.x -= int(self.speed * (enemy.x - self.x) / hypot(enemy.x - self.x, enemy.y - self.y))
                self.y -= int(self.speed * (enemy.y - self.y) / hypot(enemy.x - self.x, enemy.y - self.y))
            except:
                pass  # catches divide by 0 errors

    # Draws player and player health in top-left
    def draw(self, screen):

        # draws player
        draw.circle(screen, self.color, (self.x, self.y), self.radius)

        # draws health
        if not self.sd:
            if self.health > 0:
                pass
                # draw.rect(screen, (255 * (1 - self.health // self.max_health), 255 * self.health // self.max_health, 0),
                #           (15, 15, int(500 * self.health / self.max_health), 25))
                # screen.blit(fontHealth.render("%i/%i" % (self.health, self.max_health), 1, (0, 0, 255)),
                #             (250 - fontHealth.size("%i/%i" % (self.health, self.max_health))[0] // 2, 20))


class Bullet:
    def __init__(self, x, y, target_x, target_y, enemy, listBullets, color, radius, boundX, boundY):

        self.list = listBullets
        # loads image of bullet
        # x is the x position of the bullet
        self.x = x
        # y is the y position of the bullet
        self.y = y
        # originalx is the original x position of the bullet,
        self.originalx = x
        # originaly is the original y position of the bullet,
        self.originaly = y
        # target_x is where the bullet is going to,
        self.target_x = target_x
        # target_y is the where the bullet is going to,
        self.target_y = target_y
        # vel is the velocity that the bullet moves at
        self.vel = 20
        # rnge is the range of the bullet, in frames
        self.rnge = 50
        # prog is the progress of the bullet, in frames
        self.prog = 0
        # dmg is the damage that the bullet will do upon impact
        self.dmg = 1
        self.dmg_mult = 1
        # deathtick is the timer for enemy death
        self.deathTick = 0
        # rect is the hitbox of the bullet
        self.rect = Rect(self.x - radius, self.y - radius, int(radius*2), int(radius*2))
        self.boundX = boundX
        self.boundY = boundY
        self.radius = radius
        self.color = color

    def update(self):
        # Increases Progress of the bullet
        try:
            self.x += int((self.vel) * (self.target_x - self.originalx) /
                          (sqrt((self.target_x - self.originalx) ** 2 +
                                (self.target_y - self.originaly) ** 2)))
            self.y += int((self.vel) * (self.target_y - self.originaly) /
                          (sqrt((self.target_x - self.originalx) ** 2 +
                                (self.target_y - self.originaly) ** 2)))
        except:
            pass  # catches divide by zero errors

        self.rect.center = [self.x, self.y]

    def check(self, enemy):
        # Checks if the bullet is out of range, then deletes it, if it is
        if self.prog >= self.rnge:
            return True
        # checks if bullets are out of bounds
        elif not 0 < self.x < self.boundX or not 0 < self.y < self.boundY:
            return True

        else:
            # checks if bullet hits target hitbox, if so, starts a timer that kills the bullet after 1 frame
            if self.rect.colliderect(enemy.hitbox):
                    self.deathTick += 1

            if self.deathTick > 1:
                return True

    # draws each bullet
    def draw(self, screen):
        draw.circle(screen, self.color, (self.x, self.y), self.radius)



