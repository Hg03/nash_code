import streamlit as st
import random

class CoinTossGame:
    def __init__(self):
        self.players = ['Player 1', 'Player 2']
        self.strategies = ['H', 'T']
        self.payoffs = {player: {'H': 1, 'T': 0} for player in self.players}
        self.nash_equilibrium = {player: random.choice(self.strategies) for player in self.players}

    def get_strategy(self, player):
        return self.nash_equilibrium[player]

    def calculate_nash_equilibrium(self):
        prev_nash_equilibrium = {player: None for player in self.players}

        while prev_nash_equilibrium != self.nash_equilibrium:
            prev_nash_equilibrium = self.nash_equilibrium.copy()

            for player in self.players:
                best_strategy, best_payoff = None, -1

                for strategy in self.strategies:
                    payoff = self._find_nash_equilibrium_strategy(player, strategy)

                    if payoff > best_payoff:
                        best_strategy = strategy
                        best_payoff = payoff

                self.nash_equilibrium[player] = best_strategy

    def _find_nash_equilibrium_strategy(self, player, strategy):
        opponent = self.players[1 - self.players.index(player)]  # The other player
        opponent_strategy = self.nash_equilibrium[opponent]
        return self.payoffs[player][strategy] if strategy == opponent_strategy else 0

    def play(self):
        st.write("Welcome to the Coin Toss Game!")
        st.write("Players:", ', '.join(self.players))

        self.calculate_nash_equilibrium()

        while True:
            current_player = random.choice(self.players)
            opponent = self.players[1 - self.players.index(current_player)]

            st.write(f"\n{current_player}'s turn.")

            # Get the Nash equilibrium strategy for the current player
            strategy = self.get_strategy(current_player)
            st.write(f"{current_player} chooses: {strategy}")

            # Toss the coin
            result = random.choice(['H', 'T'])
            st.write(f"Coin Toss Result: {result}")

            # Determine the winner
            if result == 'H':
                st.write(f"{current_player} wins!")
                break
            else:
                st.write(f"{opponent}'s turn next.")


class RockPaperScissorsGame:
    def __init__(self):
        self.players = ['Player 1', 'Player 2']
        self.strategies = ['rock', 'paper', 'scissors']
        self.payoffs = {player: {'rock': 0, 'paper': 0, 'scissors': 0} for player in self.players}
        self.nash_equilibrium = {player: random.choice(self.strategies) for player in self.players}

    def get_strategy(self, player):
        return self.nash_equilibrium[player]

    def calculate_nash_equilibrium(self):
        prev_nash_equilibrium = {player: None for player in self.players}

        while prev_nash_equilibrium != self.nash_equilibrium:
            prev_nash_equilibrium = self.nash_equilibrium.copy()

            for player in self.players:
                best_strategy, best_payoff = None, -1

                for strategy in self.strategies:
                    payoff = self._find_nash_equilibrium_strategy(player, strategy)

                    if payoff > best_payoff:
                        best_strategy = strategy
                        best_payoff = payoff

                self.nash_equilibrium[player] = best_strategy

    def _find_nash_equilibrium_strategy(self, player, strategy):
        opponent = self.players[1 - self.players.index(player)]  # The other player
        opponent_strategy = self.nash_equilibrium[opponent]
        return self.payoffs[player][strategy] if strategy == self.get_beat_strategy(opponent_strategy) else 0

    def get_beat_strategy(self, strategy):
        if strategy == 'rock':
            return 'paper'
        elif strategy == 'paper':
            return 'scissors'
        else:  # strategy == 'scissors'
            return 'rock'

    def play(self):
        st.write("Welcome to the Rock-Paper-Scissors Game!")
        st.write("Players:", ', '.join(self.players))

        self.calculate_nash_equilibrium()

        while True:
            current_player = random.choice(self.players)
            opponent = self.players[1 - self.players.index(current_player)]

            st.write(f"\n{current_player}'s turn.")

            # Get the Nash equilibrium strategy for the current player
            strategy = self.get_strategy(current_player)
            st.write(f"{current_player} chooses: {strategy}")

            # Get the Nash equilibrium strategy for the opponent
            opponent_strategy = self.get_strategy(opponent)
            st.write(f"{opponent} chooses: {opponent_strategy}")

            # Determine the winner
            if strategy == opponent_strategy:
                st.write("It's a tie!")
            elif self.get_beat_strategy(strategy) == opponent_strategy:
                st.write(f"{current_player} wins!")
            else:
                st.write(f"{opponent} wins!")


def cointoss():
    explanation, output = st.tabs(['Explanation','Output'])
    with explanation:
            st.markdown('''
                This code represents a simple two-player coin toss game with the goal of finding the Nash equilibrium and simulating the game based on the calculated Nash equilibrium strategy.

Here's an explanation of the code:

1. The code starts by importing the `random` module to generate random choices during the game.

2. The class `CoinTossGame` is defined to represent the coin toss game. It has the following attributes:
   - `players`: A list containing the names of the players, which are 'Player 1' and 'Player 2'.
   - `strategies`: A list containing the two possible strategies in the game, represented by 'H' (heads) and 'T' (tails).
   - `payoffs`: A dictionary that maps each player to their respective payoff for each strategy. In this case, 'H' yields a payoff of 1, and 'T' yields a payoff of 0 for both players.
   - `nash_equilibrium`: A dictionary that initially assigns a random strategy ('H' or 'T') to each player, which will be updated later to find the Nash equilibrium.

3. The `get_strategy` method takes a player's name as input and returns the Nash equilibrium strategy assigned to that player.

4. The `calculate_nash_equilibrium` method is used to find the Nash equilibrium for each player in the game. It uses the concept of iterative elimination of dominated strategies. The method iteratively updates the strategies of each player based on their best response to the other player's strategy until no further changes occur. In this game, 'H' dominates 'T' since it yields a higher payoff, so the Nash equilibrium for both players will eventually be 'H'.

5. The `_find_nash_equilibrium_strategy` method is a helper function used in `calculate_nash_equilibrium`. It calculates the payoff of a given player's strategy against the strategy of the opponent player.

6. The `play` method simulates a single round of the coin toss game. It starts by displaying a welcome message and the names of the players. Then, it calculates the Nash equilibrium for each player using `calculate_nash_equilibrium`.

7. The game proceeds in a loop, where each iteration represents one player's turn. The current player is randomly chosen, and their Nash equilibrium strategy is determined. The coin is tossed ('H' or 'T' is chosen randomly), and the result is displayed.

8. If the result is 'H' (heads), the current player wins, and the game ends. Otherwise, the game continues with the other player's turn.

9. Finally, in the `__name__ == "__main__"` block, an instance of the `CoinTossGame` class is created, and the `play` method is called twice. This means the game will be played twice, with different random outcomes each time.

It's important to note that in this specific coin toss game, the Nash equilibrium strategy will always be 'H' for both players, as 'H' yields a higher payoff than 'T'. Therefore, the game will always result in Player 1 winning.
                ''')
    with output:
        if st.button('Start Executing the game'):
            game = CoinTossGame()
            game.play()
                
    
        

def rps():
    explanation, output = st.tabs(['Explanation','Output'])
    
    with explanation:
        st.markdown('''
                    This code represents a simple two-player Rock-Paper-Scissors game with the goal of finding the Nash equilibrium and simulating the game based on the calculated Nash equilibrium strategy.

Here's an explanation of the code:

1. The class `RockPaperScissorsGame` is defined to represent the Rock-Paper-Scissors game. It has the following attributes:
   - `players`: A list containing the names of the players, which are 'Player 1' and 'Player 2'.
   - `strategies`: A list containing the three possible strategies in the game, represented by 'rock', 'paper', and 'scissors'.
   - `payoffs`: A dictionary that maps each player to their respective payoff for each strategy. In this case, all the payoffs are initially set to 0.
   - `nash_equilibrium`: A dictionary that initially assigns a random strategy ('rock', 'paper', or 'scissors') to each player, which will be updated later to find the Nash equilibrium.

2. The `get_strategy` method takes a player's name as input and returns the Nash equilibrium strategy assigned to that player.

3. The `calculate_nash_equilibrium` method is used to find the Nash equilibrium for each player in the game. It uses the concept of iterative elimination of dominated strategies. The method iteratively updates the strategies of each player based on their best response to the other player's strategy until no further changes occur. In this game, 'rock' is beaten by 'paper', 'paper' is beaten by 'scissors', and 'scissors' is beaten by 'rock', so the Nash equilibrium for both players will eventually be 'rock'.

4. The `_find_nash_equilibrium_strategy` method is a helper function used in `calculate_nash_equilibrium`. It calculates the payoff of a given player's strategy against the strategy of the opponent player. If the strategy beats the opponent's strategy, it returns the corresponding payoff; otherwise, it returns 0.

5. The `get_beat_strategy` method is another helper function used to determine the strategy that beats a given strategy. For example, if the opponent plays 'rock', this method will return 'paper'.

6. The `play` method simulates a single round of the Rock-Paper-Scissors game. It starts by displaying a welcome message and the names of the players. Then, it calculates the Nash equilibrium for each player using `calculate_nash_equilibrium`.

7. The game proceeds in a loop, where each iteration represents one player's turn. The current player is randomly chosen, and their Nash equilibrium strategy is determined. The opponent's Nash equilibrium strategy is also determined.

8. The chosen strategies of both players are displayed, and the winner is determined based on the Nash equilibrium strategy. If both players choose the same strategy, it's a tie. Otherwise, the player whose strategy beats the opponent's strategy wins.

9. Finally, in the `__name__ == "__main__"` block, an instance of the `RockPaperScissorsGame` class is created, and the `play` method is called. The game will be played once, and the winner or tie outcome will be displayed.

It's important to note that in this specific Rock-Paper-Scissors game, the Nash equilibrium strategy will always be 'rock' for both players, as 'rock' has no dominated strategies (it beats both 'scissors' and 'paper'). Therefore, the game will always result in a tie.
                    ''')
    with output:
        if st.button('Start executing the game'):
            game = RockPaperScissorsGame()
            game.play()

def main():
    st.markdown('# Strategies solved through **Nash Equillibrium** ')
    with st.expander('What is nash equillibrium ?'):
        st.markdown('''
                    Nash equilibrium is a concept in game theory where the optimal outcome is when there is no incentive for players to deviate from their initial strategy. The players have knowledge of their opponent’s strategy and still will not deviate from their initial chosen strategies because it remains the optimal strategy for each player.Overall, an individual can receive no incremental benefit from changing actions, assuming that other players remain constant in their strategies. A game may have multiple Nash equilibria or none at all. 
                    ''')
    game = st.sidebar.selectbox('Select the game',['Coin Toss Game','Rock Paper Scissors'])
    st.info(f'{game}')
    if game == 'Coin Toss Game':
        cointoss()
    elif game == 'Rock Paper Scissors':
        rps()
    
main()