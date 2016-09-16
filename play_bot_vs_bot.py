import subprocess
from ScrabbleGame import *
from ScrabblePlayer import *
from ScrabbleBot import *
from ScrabbleVisualizer import *

if __name__ == "__main__":
    sg = ScrabbleGame(BOARD_SIZE)
    player1 = ScrabbleBot(sg.drawTiles(RACK_MAX_SIZE), sg)
    player2 = ScrabbleBot(sg.drawTiles(RACK_MAX_SIZE), sg)

    p1turn = True
    if VISUALIZE:
        # Launch game viewer in a separate process
        subprocess.Popen([PYTHON_EXECUTABLE, "run_visualizer.py"])

    scores = {"player1":0, "player2":0}

    consecutive_passes = 0
    while True:
        print sg.board
        #print "BOARD VALUE:", sg.getBoardValue()
        print scores
        if VISUALIZE:
            sg.dumpBoardImage()
        if p1turn:
            curr_player = player1
        else:
            curr_player = player2

        m = curr_player.chooseMove(sg.board)
        if len(m) > 0:
            consecutive_passes = 0
            if sg.isLegalMove(m) and curr_player.hasTiles(m):
                print m
                points = sg.finalMove(m)
                curr_player.updateRack(m)
                print "SCORE %d POINTS" % points
                curr_player.receiveScore(points)
                if p1turn:
                    scores['player1'] += points
                else:
                    scores['player2'] += points
        else:
            print "PLAYER PASSED"
            consecutive_passes += 1

        if len(curr_player.rack) == 0 or consecutive_passes == 6:

            print "GAME OVER"
            print scores
            break

        p1turn = not p1turn






















#
