import random

AVAILABLE_CHARACTERS = {}

 

class Player :

    def __init__(self, name, life, money = 10):
        """
        PARAM : - name : str
                - life : float
                - money : float
        initialisate team to empty list, game and direction to None
        """
        # TODO
        self.name = name 
        self.life = life 
        self.money = money
        self.team = []
        self.game = None
        self.direction = None

    @property
    def is_alive(self):
        # TODO
        return self.life > 0
    
    @property
    def is_not_alive(self):
        return self.life <= 0


    def get_hit(self, damages):
        """
        Take the damage to life
        PARAM : - damages : float
        """
        # TODO
        self.life -= damages


    def new_character(self):
        """
        Ask to player where add a new Character,
        check if enough monney
        and create the new one
        """
        for key, val in AVAILABLE_CHARACTERS.items() :
            print(val.__str__(self))

        selection = input(f" {self.name} : Wich character do you want for the battle ? (C = Character, F = Fighter, T = Tank, A = Assassin, K = Knight, S = Shield, D = Dodger, G = Gunner, B = Boss) (enter if none) : ")
        if selection != "" :
            while selection != "C" and selection != "F" and selection != "T" and selection != "A" and selection != "K" and selection != "S" and selection != "D" and selection != "G" and selection != "B" :
                selection = input(f" {self.name} : Wich character do you want for the battle ? (C = Character, F = Fighter, T = Tank, A = Assassin, K = Knight, S = Shield, D = Dodger, G = Gunner, B = Boss) (enter if none) : ")

        if selection == "C" :
            line = input(f" {self.name}: Wich line would you place the new one (0-{self.game.nb_lines-1}) ? (enter if none) ")
            if line != "":
                line = int(line)
                if 0<=line<=self.game.nb_lines-1 :
                    if self.money >= Character.base_price :
                        column = 0 if self.direction == +1 else self.game.nb_columns-1
                        Character(self,(line,column))

        if selection == "F" :
            line = input(f" {self.name}: Wich line would you place the new one (0-{self.game.nb_lines-1}) ? (enter if none) ")
            if line != "":
                line = int(line)
                if 0<=line<=self.game.nb_lines-1 :
                    if self.money >= Fighter.base_price :
                        column = 0 if self.direction == +1 else self.game.nb_columns-1
                        Fighter(self,(line,column))


        if selection == "T" : 
            line = input(f" {self.name}: Wich line would you place the new one (0-{self.game.nb_lines-1}) ? (enter if none) ")
            if line != "":
                line = int(line)
                if 0<=line<=self.game.nb_lines-1 :
                    if self.money >= Tank.base_price :
                        column = 0 if self.direction == +1 else self.game.nb_columns-1
                        Tank(self,(line,column))

        if selection == "A" : 
            line = input(f" {self.name}: Wich line would you place the new one (0-{self.game.nb_lines-1}) ? (enter if none) ")
            if line != "":
                line = int(line)
                if 0<=line<=self.game.nb_lines-1 :
                    if self.money >= Assassin.base_price :
                        column = 0 if self.direction == +1 else self.game.nb_columns-1
                        Assassin(self,(line,column))

        if selection == "K" : 
            line = input(f" {self.name}: Wich line would you place the new one (0-{self.game.nb_lines-1}) ? (enter if none) ")
            if line != "":
                line = int(line)
                if 0<=line<=self.game.nb_lines-1 :
                    if self.money >= Knight.base_price :
                        column = 0 if self.direction == +1 else self.game.nb_columns-1
                        Knight(self,(line,column))

        if selection == "S" :
            line = input(f" {self.name}: Wich line would you place the new one (0-{self.game.nb_lines-1}) ? (enter if none) ")
            if line != "":
                line = int(line)
                if 0<=line<=self.game.nb_lines-1 :
                    if self.money >= Shield.base_price :
                        column = 0 if self.direction == +1 else self.game.nb_columns-1
                        Shield(self,(line,column))

        if selection == "G" :
            line = input(f" {self.name}: Wich line would you place the new one (0-{self.game.nb_lines-1}) ? (enter if none) ")
            if line != "":
                line = int(line)
                if 0<=line<=self.game.nb_lines-1 :
                    if self.money >= Gunner.base_price :
                        column = 0 if self.direction == +1 else self.game.nb_columns-1
                        Gunner(self,(line,column))

        if selection == "D" :
            line = input(f" {self.name}: Wich line would you place the new one (0-{self.game.nb_lines-1}) ? (enter if none) ")
            if line != "":
                line = int(line)
                if 0<=line<=self.game.nb_lines-1 :
                    if self.money >= Dodger.base_price :
                        column = 0 if self.direction == +1 else self.game.nb_columns-1
                        Dodger(self,(line,column))

        if selection == "B" :
            line = input(f" {self.name}: Wich line would you place the new one (0-{self.game.nb_lines-1}) ? (enter if none) ")
            if line != "":
                line = int(line)
                if 0<=line<=self.game.nb_lines-1 :
                    if self.money >= Boss.base_price :
                        column = 0 if self.direction == +1 else self.game.nb_columns-1
                        Boss(self,(line,column))

        

    def __str__(self) :
        return f"{self.name} : {self.life} PV - {self.money} $"


class IA :

    def __init__(self, name, life, money):
        self.name = name 
        self.life = life 
        self.money = money
        self.team = []
        self.game = None
        self.direction = None

    @property
    def is_alive(self):
        # TODO
        return self.life > 0
    
    @property
    def is_not_alive(self):
        return self.life <= 0


    def get_hit(self, damages):
        """
        Take the damage to life
        PARAM : - damages : float
        """
        # TODO
        self.life -= damages

    def new_character(self) :


        for key, val in AVAILABLE_CHARACTERS.items() :
            print(val.__str__(self))

        selection = random.randint(1, 10)
        if selection != 10 :
            while selection != 1 and selection != 2 and selection != 3 and selection != 4 and selection != 5 and selection != 6 and selection != 7 and selection != 8 and selection != 9 :
                selection = random.randint(1, 10)

        if selection == 1 :
            line = random.randint(1, self.game.nb_lines-1)
            if line != "":
                line = int(line)
                if 0<=line<=self.game.nb_lines-1 :
                    if self.money >= Character.base_price :
                        column = 0 if self.direction == +1 else self.game.nb_columns-1
                        Character(self,(line,column))

        if selection == 2 :
            line = random.randint(1, self.game.nb_lines-1)
            if line != "":
                line = int(line)
                if 0<=line<=self.game.nb_lines-1 :
                    if self.money >= Fighter.base_price :
                        column = 0 if self.direction == +1 else self.game.nb_columns-1
                        Fighter(self,(line,column))


        if selection == 3 : 
            line = random.randint(1, self.game.nb_lines-1)
            if line != "":
                line = int(line)
                if 0<=line<=self.game.nb_lines-1 :
                    if self.money >= Tank.base_price :
                        column = 0 if self.direction == +1 else self.game.nb_columns-1
                        Tank(self,(line,column))

        if selection == 4 : 
            line = random.randint(1, self.game.nb_lines-1)
            if line != "":
                line = int(line)
                if 0<=line<=self.game.nb_lines-1 :
                    if self.money >= Assassin.base_price :
                        column = 0 if self.direction == +1 else self.game.nb_columns-1
                        Assassin(self,(line,column))

        if selection == 5 : 
            line = random.randint(1, self.game.nb_lines-1)
            if line != "":
                line = int(line)
                if 0<=line<=self.game.nb_lines-1 :
                    if self.money >= Knight.base_price :
                        column = 0 if self.direction == +1 else self.game.nb_columns-1
                        Knight(self,(line,column))

        if selection == 6 :
            line = random.randint(1, self.game.nb_lines-1)
            if line != "":
                line = int(line)
                if 0<=line<=self.game.nb_lines-1 :
                    if self.money >= Shield.base_price :
                        column = 0 if self.direction == +1 else self.game.nb_columns-1
                        Shield(self,(line,column))

        if selection == 7 :
            line = random.randint(1, self.game.nb_lines-1)
            if line != "":
                line = int(line)
                if 0<=line<=self.game.nb_lines-1 :
                    if self.money >= Gunner.base_price :
                        column = 0 if self.direction == +1 else self.game.nb_columns-1
                        Gunner(self,(line,column))

        if selection == 8 :
            line = random.randint(1, self.game.nb_lines-1)
            if line != "":
                line = int(line)
                if 0<=line<=self.game.nb_lines-1 :
                    if self.money >= Dodger.base_price :
                        column = 0 if self.direction == +1 else self.game.nb_columns-1
                        Dodger(self,(line,column))

        if selection == 9 :
            line = random.randint(1, self.game.nb_lines-1)
            if line != "":
                line = int(line)
                if 0<=line<=self.game.nb_lines-1 :
                    if self.money >= Boss.base_price :
                        column = 0 if self.direction == +1 else self.game.nb_columns-1
                        Boss(self,(line,column))

        

    def __str__(self) :
        return f"{self.name} : {self.life} PV - {self.money} $"



class Game :

    def __init__(self,player0, player1, nb_lines=6,nb_columns=15):
        """
        PARAM : - player0 : Player
                - player1 : Player
                - nb_lines : float
                - nb_columns : float
        - update players' direction and game
        - initialisate player_turn to 0
        """
        # TODO
        self.players = [player0, player1]
        self.nb_lines = nb_lines
        self.nb_columns = nb_columns
        player0.direction = +1
        player1.direction = -1
        player0.game = self
        player1.game = self 
        self.player_turn = 0 


    @property
    def current_player(self):
        # TODO
        return self.players [self.player_turn]
       

    @property
    def oponent(self):
        # TODO
        return self.players [(self.player_turn + 1) %2]
    
        
    @property
    def all_characters(self):
        # TODO
        return self.players[0].team + self.players[1].team
    


    def get_character_at(self, position):
        """
        PARAM : - position : tuple
        RETURN : character at the position, None if there is nobody
        """
        # TODO
        for character in self.all_characters :
            if character.position == position :
                return character

        return None

    def place_character(self, character, position):
        """
        place character to position if possible
        PARAM : - character : Character
                - position : tuple
        RETURN : bool to say if placing is done or not
        """
        # TODO
        if not self.get_character_at(position) and 0 <= position[0] < self.nb_lines and 0 <= position[1] < self.nb_columns :
            character.position = position
            return True

        return False

    def draw(self):
        """
        print the board
        """
        print(f"{self.players[0].life:<4}{'  '*self.nb_columns}{self.players[1].life:>4}")

        print("----"+self.nb_columns*"--"+"----")

        for line in range(self.nb_lines):
            print(f"|{line:>2}|", end="")
            for col in range(self.nb_columns):
                # TODO
                character_at_position = self.get_character_at((line, col))
                if character_at_position != None :
                    print(f"{character_at_position.design}", end = " ")
                else :
                    print(".", end=" ")
            print(f"|{line:<2}|")

        print("----"+self.nb_columns*"--"+"----")

        print(f"{self.players[0].money:<3}${'  '*self.nb_columns}${self.players[1].money:>3}")


    def play_turn(self):
        """
        play one turn :
            - current player can add a new character
            - current player's character play turn
            - oponent player's character play turn
            - draw the board
        """
        # TODO
        self.current_player.new_character()
        for character in self.all_characters :
            character.play_turn()
        self.draw()



    def play(self):
        """
        play an entire game : while current player is alive, play a turn and change player turn
        """
        # TODO
        while self.current_player.is_alive :
            self.play_turn()
            if self.player_turn == 0 :
                self.player_turn = 1
            else :
                self.player_turn = 0


    def menu() :
        enter = input("---------- WELCOME IN THE ARENA, CHALLENGER(S) ! Press ENTER to continue your journey ! ----------")
        print("-------------------------------------------------------------------------")
        print("--- If you want a battle versus an IA, press 1 ---")
        print("--- If you want a battle versus an other player, press 2 ---")
        print("--- If you want some informations about the game or the differents characters, press 3 ---")
        print("-------------------------------------------------------------------------")
        choice = input("What do you want to do ? : ")
        if choice == "1" :
            print("START THE BATTLE")
            player_name = input("What is your name, challenger ? ")
            p_solo = Player(f"{player_name}", 10, 10)
            print(p_solo)
            ia = IA("Oragadon", 10, 10)
            print(ia)
            jeu = Game(p_solo, ia)
            jeu.draw()
            jeu.play()
            #If the player is dead, the game is over
            if p_solo.is_not_alive :
                print("You are dead ! You lost the game !")
                enter_2 = input("----- Press Enter to return to the main menu -----")
                Game.menu()
            #If the IA is dead, the player win the game
            elif ia.is_not_alive :
                print("You win the game !")
                enter_2 = input("----- Press Enter to return to the main menu -----")
                Game.menu()
            else :
                print("ERROR")
                enter_2 = input("----- Press Enter to return to the main menu -----")
                Game.menu()
            
            

        elif choice == "2" :
            print("START THE BATTLE")
            p1_name = input("What is your name, first challenger ? ")
            p2_name = input("What is your name, second challenger ? ")
            p1 = Player(f"{p1_name}", 10, 10)
            print(p1)
            p2 = Player(f"{p2_name}", 10, 10)
            print(p2)
            jeu = Game(p1, p2)
            jeu.draw()
            jeu.play()
            #If the first player is dead, the second player win the game
            if p1.is_not_alive :
                print(f"{p2.name} win the game !")
                enter_2 = input("----- Press Enter to return to the main menu -----")
                Game.menu()
            #If the second player is dead, the first player win the game
            elif p2.is_not_alive :
                print(f"{p1.name} win the game !")
                enter_2 = input("----- Press Enter to return to the main menu -----")
                Game.menu()
            else :
                print("ERROR")
                enter_2 = input("----- Press Enter to return to the main menu -----")
                Game.menu()
            

        elif choice == "3" :
            print("--------------------------------------------------------")
            print("You are a new player ? That's not a problem ! We are here to help you !")
            print("The aim of the game is to destroy the enemy's base with your characters who go in the battlefied.")
            print("You have some money for buying the characters.")
            print("When a character die, the player who killed the character collects half of the price that the other player paid for him.")
            print("There are 9 class of characters :")
            print("Character : $1 - Life : 5, Strenght : 1")
            print("Fighter : $2 - Life : 5, Strenght : 2")
            print("Tank : $3 - Life : 10, Strenght : 1, move every two turns")
            print("Assassin : $4 - Life : 3, Strenght : 5")
            print("Knight : $3, Life = 5, Strenght : 1 (3 if critical hit)")
            print("Shield : $3, Life = 6, Strenght = 1, One chance out of two to block the attack")
            print("Gunner : $3, Life = 3, Strenght = 1, Shoot Strenght = 3 (Shoot three cases in front), Can't do damages to the enemy base")
            print("Dodger : $2, Life = 3, Strenght = 1, One chance out of three to dodge the attack")
            print("Boss : $8, Life = 7, Strenght = 3 (6 if critical hit), Move every two turns, one chance out of two to block the attack")
            enter_2 = input("----- Press Enter to return to the main menu -----")
            Game.menu()







### PERSONNAGES ###
class Character :

    base_price = 1
    base_life = 5
    base_strength = 1
    base_shoot_strength = 0 



    def __init__(self, player, position):
        """
        PARAM : - player : Player
                - position : tuple
        Set player to player in param.
        Set life, strength and price to base_life, base_strength and base_price.
        Place th character at the position
        If OK : add the current character to the player's team and take the price
        """

        self.player = player
        self.life = self.base_life
        self.strength = self.base_strength
        self.shoot_strength = self.base_shoot_strength
        self.price = self.base_price

        ok = self.game.place_character(self, position)
        if ok :
            self.player.team.append(self)
            self.player.money -= self.price


    @property
    def direction(self):
        # TODO
        return self.player.direction


    @property
    def game(self):
        # TODO
        return self.player.game

    @property
    def enemy(self):
        # TODO
        if self.direction == 1 :
            return self.game.players[1]
        else :
            return self.game.players[0]

    @property
    def design(self):
        # TODO
        if self.direction == 1 :    
            return ">"
        else :
            
            return "<"


    def move(self):
        """
        the character move one step front
        """
        # TODO
        
        self.game.place_character(self, (self.position[0], self.position[1] + self.direction))




    def get_hit(self, damages):
        """
        Take the damage to life. If dead, the character is removed from his team and return reward
        PARAM : damages : float
        RETURN : the reward due to hit (half of price if the character is killed, 0 if not)
        """
        # TODO
        reward = self.price / 2
        self.life -= damages
        if self.life <= 0 :
            self.player.team.remove(self)
            return reward
        else :
            return 0


    def attack(self):
        """
        Make an attack :
            - if in front of ennemy's base : hit the base
            - if in front of character : hit him (and get reward)
        """
        # TODO
        if (self.player.direction == -1 and self.position[1] == 0) or (self.player.direction == 1 and self.position[1] == self.game.nb_columns - 1) :
            self.enemy.get_hit(self.strength)

        position_in_front = (self.position[0], self.position[1] + self.direction)

        character_in_front = self.game.get_character_at(position_in_front)

        if character_in_front != None :
            reward = character_in_front.get_hit(self.strength)
            self.player.money += reward





    def play_turn(self):
        """
        play one turn : move and attack
        """
        # TODO
        self.move()
        self.attack()


    def __str__(self):
        """
        return a string represent the current object
        """
        # TODO
        return " Character : $ = 1, Life = 5, Strenght = 1 "

AVAILABLE_CHARACTERS["C"] = Character


class Fighter (Character) :

    base_price = 2
    base_strength = 2

    @property
    def design(self) :
        if self.direction == 1 :
            return "|"
        else :
            return "|"

    def __str__(self) :
        return " Fighter : $ = 2, Life = 5, Strenght = 2 "

AVAILABLE_CHARACTERS["F"] = Fighter

class Tank (Character) :

    base_price = 3
    base_life = 10

    def __init__(self, player, position) :
        self.turn_to_move = False
        super().__init__(player, position)

    @property
    def design(self):
        if self.direction == 1 :
            return "O"
        else :
            return "O"

    def move(self) :
        if self.turn_to_move == False :
            self.turn_to_move = True 
        else :
            super().move()
            self.turn_to_move = False

    def __str__(self) :
        return " Tank : $ = 3, Life = 10, Strenght = 1, move every two turns "

AVAILABLE_CHARACTERS["T"] = Tank

class Assassin (Character) :
    base_price = 4
    base_life = 3
    base_strength = 5

    @property
    def design(self):
        if self.direction == 1 :
            return "]"
        else :
            return "["

    def __str__(self) :
        return " Assassin : $ = 4, Life = 3, Strenght = 5"

AVAILABLE_CHARACTERS["A"] = Assassin

class Knight (Character) :
    base_price = 3

    def __init__(self, player, position) :
        super().__init__(player, position)

    @property
    def design(self) :
        if self.direction == 1 :
            return "!"
        else :
            return "!"

    def attack(self) :
        hit = self.strength
        if random.randint(0, 7) == 7 :
            hit *= 3
            if (self.player.direction == -1 and self.position[1] == 0) or (self.player.direction == 1 and self.position[1] == self.game.nb_columns -1) :
                self.enemy.get_hit(hit)

            position_in_front = (self.position[0], self.position[1] + self.direction)

            character_in_front = self.game.get_character_at(position_in_front)

            if character_in_front != None :
                reward = character_in_front.get_hit(hit)
                self.player.money += reward

        else :
            super().attack()


    def __str__(self) :
        return " Knight : $ = 3, Life = 5, Strenght = 1 (3 if critical hit)"

AVAILABLE_CHARACTERS["K"] = Knight



class Shield (Character) :

    base_price = 3
    base_life = 6
    base_strength = 1

    def __init__(self, player, position) :
        super().__init__(player, position)

    @property
    def design(self):
        if self.direction == 1 :
            return ")"
        else :
            return "("
    

    def attack(self) :
        if random.randint(0, 1) == 1 :
            self.player.get_hit(0)
        else :
            super().attack()


    def __str__(self) :
        return " Shield : $ = 3, Life = 6, Strength = 1 (One chance out of two to block the attack) "

AVAILABLE_CHARACTERS["S"] = Shield


class Gunner (Character) :

    base_price = 3
    base_life = 3
    base_strength = 1
    base_shoot_strength = 3

    def __init__(self, player, position) :
        super().__init__(player, position)

    @property
    def design(self):
        if self.direction == 1 :
            return "}"
        else :
            return "{"
    

    def move(self) :
        self.game.place_character(self, (self.position[0], self.position[1]) )


    def attack(self) :
        position_in_front = (self.position[0], self.position[1] + self.direction)
        position_in_line = (self.position[0], self.position[1] + (3*self.direction)) 
        character_in_line = self.game.get_character_at(position_in_line)
        character_in_front = self.game.get_character_at(position_in_front)
        if character_in_line != None and not character_in_front != None:
            reward = character_in_line.get_hit(self.shoot_strength)
            self.player.money += reward
        elif character_in_front != None :
            reward = character_in_front.get_hit(self.strength)
            self.player.money += reward

    def __str__(self) :
        return " Gunner : $ = 3, Life = 3, Strenght = 1, Shoot Strenght = 3 (shoot three cases in front), Can't do damages to the enemy base "
        

AVAILABLE_CHARACTERS["G"] = Gunner

class Dodger (Character) :
    base_price = 2
    base_life = 3
    base_strength = 1



    def __init__(self, player, position) :
        super().__init__(player, position)

    @property
    def design(self):
        if self.direction == 1 :
            return "~"
        else :
            return "~"

    def move(self) :
        position_in_front = (self.position[0], self.position[1] + self.direction)

        character_in_front = self.game.get_character_at(position_in_front)

        if character_in_front != None and random.randint(0, 2) == 2 :
            self.game.place_character(self, (self.position[0], self.position[1] + (2*self.direction)))   
        else :
            super().move()

    def __str__(self) :
        return " Dodger : $ = 2, Life = 3, Strenght = 1, One chance out of three to dodge the attack "

AVAILABLE_CHARACTERS["D"] = Dodger

class Boss (Character) :
    base_price = 8
    base_life = 7
    base_strength = 3

    def __init__(self, player, position) :
        self.turn_to_move = False
        super().__init__(player, position)

    @property
    def design(self) :
        if self.direction == 1 :
            return "@"
        else :
            return "@"

    def move(self) :
        if self.turn_to_move == False :
            self.turn_to_move = True 
        else :
            super().move()
            self.turn_to_move = False

    def attack(self) :
        hit = self.strength
        if random.randint(0, 7) == 7 :
            hit *= 2
            if (self.player.direction == -1 and self.position[1] == 0) or (self.player.direction == 1 and self.position[1] == self.game.nb_columns -1) :
                self.enemy.get_hit(hit)

            position_in_front = (self.position[0], self.position[1] + self.direction)

            character_in_front = self.game.get_character_at(position_in_front)

            if character_in_front != None :
                reward = character_in_front.get_hit(hit)
                self.player.money += reward

        else :
            super().attack()

    

        
    def __str__(self) :
        return " Boss : $ = 8, Life = 7, Strenght = 3 (6 if critical hit), move every two turns, one chance out of two to block the attack "
            

AVAILABLE_CHARACTERS["B"] = Boss





if __name__ == "__main__":
    # TODO
    Game.menu()

