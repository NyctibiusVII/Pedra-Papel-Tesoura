import random

options = ['Pedra', 'Papel', 'Tesoura']
action_options = ['quebra', 'embrulha', 'corta']

def play_game():
    player_1 = ''

    def ask():
        nonlocal player_1

        player_1_value =\
        input('\n\t----- Pedra, Papel ou Tesoura? -----\
            \n> Digite (1) e aperte Enter para jogar PEDRA.\
            \n> Digite (2) e aperte Enter para jogar PAPEL.\
            \n> Digite (3) e aperte Enter para jogar TESOURA.\
            \n- opção (1), (2) ou (3): ')

        if not player_1_value.isdigit() or\
        (player_1_value.isdigit() and\
        int(player_1_value) not in [1, 2, 3]):
            print('\n@@@ Valor Invalido @@@')
            return ask()

        player_1 = options[int(player_1_value)-1]
    ask()

    player_2 = random.choice(options)

    return who_win(player_1, player_2)

def who_win(player_1: str, player_2: str):
    def message(winner: int):
        winning_player = player_1 if winner == 1 else player_2
        losing_player = player_2 if winner == 1 else player_1

        option_index = options.index(winning_player)
        action = action_options[option_index]

        print(f'\n\t----- JOGADOR {winner} VENCEU! -----\
              \n> Jogador 1 jogou: {player_1}\
              \n> Jogador 2 jogou: {player_2}\
              \n- {winning_player} {action} {losing_player}')

    if player_1 == player_2:
        print('\n\t----- Escolhas iguais, joguem novamente! -----')
        play_game()

    if player_1 == 'Pedra':
        if player_2 == 'Papel':
            message(2)
            ask_play_game_again()
        if player_2 == 'Tesoura':
            message(1)
            ask_play_game_again()

    if player_1 == 'Papel':
        if player_2 == 'Pedra':
            message(1)
            ask_play_game_again()
        if player_2 == 'Tesoura':
            message(2)
            ask_play_game_again()

    if player_1 == 'Tesoura':
        if player_2 == 'Pedra':
            message(2)
            ask_play_game_again()
        if player_2 == 'Papel':
            message(1)
            ask_play_game_again()

def ask_play_game_again():
    def ask():
        want_game =\
        input('\n\t----- Deseja jogar novamente? -----\
            \n> Digite (s) e aperte Enter para jogar de novo.\
            \n> Digite (n) e aperte Enter para encerar o jogo.\
            \n- sim (s) ou não (n): ')

        if want_game == 's':
            print('\n/// Novo Jogo ///')
            return play_game()
        elif want_game == 'n': return
        else:
            print('\n@@@ Valor Invalido @@@')
            return ask()
    ask()

print('\n/// Jogo Iniciado ///')
play_game()
print('\n/// Jogo Encerrado ///')