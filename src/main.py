

# Player
player_hp = 5
player_shield = 2
player_atack_power = 2
player_atack_cost = 1
player_energy = 3

# Enemy
enemy_hp = 8
enemy_shield = 5
enemy_atack_power = 4


def main():
    global player_hp, player_shield, player_atack_power, player_atack_cost, player_energy, enemy_hp, enemy_shield, enemy_atack_power

    while player_hp > 0:
        while enemy_hp > 0:
            while player_energy > 0:
                player_atack_power = 2
                print(f"Nepritel ma {enemy_hp} zivotu, {enemy_shield} stitu.")
                print(f"Hrac ma {player_hp} zivotu, {player_shield} stitu a {player_energy} energie.")
                print(f"Hrac utoci silou {player_atack_power} na nepritele")
                if enemy_shield > 0:
                    if player_atack_power > enemy_shield:
                        player_atack_power -= enemy_shield
                        enemy_shield = 0
                    else:
                        enemy_shield -= player_atack_power
                        player_atack_power = 0
                enemy_hp -= player_atack_power
                player_energy -= 1
                if enemy_hp < 1:
                    print(f"Nepritel byl porazen.")
                    return
            enemy_atack_power = 4
            print(f"Nepritel ma {enemy_hp} zivotu, {enemy_shield} stitu.")
            print(f"Nepritel utoci silou {enemy_atack_power} na hrace(Zbyva mu: {player_hp} zivotu, {player_shield} stitu).")
            if player_shield > 0:
                if enemy_atack_power > player_shield:
                    enemy_atack_power -= player_shield
                    player_shield = 0
                else:
                    player_shield -= enemy_atack_power
                    enemy_atack_power = 0
            player_hp -= enemy_atack_power
            if player_hp < 1:
                print(f"Hrac byl porazen.")
                return
            player_energy = 3

        print(f"Nepritel byl porazen.")
        return
    print(f"Hrac byl porazen.")
    return


main()
