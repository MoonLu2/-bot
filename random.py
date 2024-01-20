import random

def symbol_gen():
    symbol_list = '1234%$&amp;()pojuGUIPOJU567890LUDA'
    book_list = '📕📗📘📙📖📚📓📒'
    smile_list = '🤗😎😍🤣😂😭😢🤐😐😑😶🙂🤩🥰🤔😴🥱😡🥳😇🤠🤥🤫🧐🤭☠'
    womanandman_list = '👩👨🧑👧👼👩‍💻👨‍💻🧛‍♀️🧛‍♂️🧜‍🧜‍🧚‍🧚‍👸🤴'
    fav_list = '💍💎🎈🎒👑🛶🎯🏆🧩♟🏹⚔🛡🎁🎀🎄🎃🔮🎲🎹🥁🔒🔓🖌💸⌛'

    main_list = fav_list + womanandman_list + symbol_list + smile_list + book_list
    symbols = random.choice(main_list)

    return symbols
