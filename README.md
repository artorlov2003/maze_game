**Игра лабиринт**.\
Игрок появляется в левом верхнем углу карты, ему нужно добраться до другого персонажа, появившегося в другом месте карты
(крипер гонится за игроком, игрок за коровой итд)\
Ходить можно на стрелки или `WASD`.
Игрок при перемещении доходит до ближайшей стены или развилки.\
При удержании `LSHIFT` можно перемещаться на 1 блок.\
В игре есть динамит. Он появляется на карте в случайных местах, возможное количество динамита на уровне зависит от
выбранного уровня сложности. Динамит можно собирать. Для этого нужно наступить на него, он подберется автоматически.
Чтобы взорвать динамит игрок нажимает `E`, динамит взрывает стены в радиусе 4 блоков (манхэттенское расстояние). Чем
дальше стена от игрока стена, тем меньше шанс её взрыва. При первом запуске игры игроку дается 10 динамита.
В игре есть система сложности. Для уменьшения/увеличения сложности игрок должен использовать кнопки `-`/`=` (`-`/`+`)
Сложность от 2 до исчерпания возможностей компьютера. От сложности зависит размер лабиринта.\
Лабиринт генерируется _процедурно_, автоматически. Лабиринт всегда проходим, причём единственным путём (если не считать
захождения в тупики и возможности взорвать стену)\
У каждого лабиринта есть свой уникалиный номер (Seed). От него зависит расположение стен, динамита, цели, текстуры
игрока, цели, пола и стен.
Если игрок захочет пройти какой-то лабиринт позже, он может запомнить/запистать Seed лабиринта и ввести его когда
захочет. Для стирания нужно нажимать `backspace`, для ввода печатать цифры. Seed работает только на одной сложности (мне
нравится лабиринт 1548311435 на сложности 10, его можно пройти за 1 нажатие)\
После успешного прохождения лабиринта игроку показывают время прохождения. Время отсчитывается с момента первого
движения. После прохождения лабиринта игрок может продолжить ходить по лабиринту или нажать пробел для перехода к
следующему.\
Если игроку не понравился лабиринт, он может нажать `R` для создания нового.\
При выходе из игры и при переходе на следующий уровень игра сохраняется. Сохраняется количество пройденных уровней,
динамита и выбранная сложность. Если игрок хочет сбросить свой прогресс, он может удалить файл save.json\
(Есть секретный режим дискотеки, для его активации нужно напечатать _cheat_, для выхода нажать `Esc`)\
Запуск игры: `python3 main.py`