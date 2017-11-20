class EventShoot:
    @staticmethod
    def shoot(attacker, prey):
        print(attacker.name + " наносит " + str(attacker.attack) + " урона " + prey.name)
        damage = attacker.attack
        if damage < prey.health:
            prey.health -= damage
        elif damage == prey.health:
            prey.amount -= 1
            prey.health = prey.fullHealth
        else:
            difference = damage - prey.health #30
            if difference >= prey.fullHealth:
                killedAmount = difference//prey.fullHealth
                print("Kill " + str(killedAmount))
                remainingHealth = difference%killedAmount
                print("remaining " + str(remainingHealth))
                prey.amount -= killedAmount

                if remainingHealth == 0:
                    prey.amount -= 1
                    prey.health = prey.fullHealth
                else:
                    prey.health = remainingHealth
            else:
                prey.amount -= 1
                prey.health = prey.fullHealth - difference

        print(attacker.name + " Amount " + str(attacker.amount) + " HP = " + str(attacker.health))
        print(prey.name + " Amount " + str(prey.amount) + " HP = " + str(prey.health))