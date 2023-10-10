def flip_coins(num_coins):
    coins = ['heads'] * num_coins

    for i in range(num_coins):
        if (i + 1) % 2 == 0:
            coins[i] = 'tails' if coins[i] == 'heads' else 'heads'

        if (i + 1) % 3 == 0:
            coins[i] = 'tails' if coins[i] == 'heads' else 'heads'

    return coins


# Simulate flipping 100 coins
num_coins = 100
result = flip_coins(num_coins)

# Print the result
for i, coin in enumerate(result):
    print(f'Coin {i+1}: {coin}')
