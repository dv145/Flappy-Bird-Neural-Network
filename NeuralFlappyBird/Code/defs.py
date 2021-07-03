DISPLAY_W = 960
DISPLAY_H = 540
FPS = 30

DATA_FONT_SIZE = 18
DATA_FONT_COLOR =  (40,40,40)
BG_FILENAME = '../BG.png'

PIPE_FILENAME = '../Pipe.png'
PIPE_SPEED = 70/1000
PIPE_DONE = 1
PIPE_MOVING = 0
PIPE_UPPER = 1
PIPE_LOWER = 0

PIPE_ADD_GAP = 160
PIPE_MIN = 80
PIPE_MAX = 500
PIPE_START_X = DISPLAY_W
PIPE_GAP_SIZE = 160
PIPE_FIRST = 400

BIRD_FILENAME = '../Robin.png'
BIRD_START_SPEED = -0.32
BIRD_START_X = 200
BIRD_START_Y = 200 
BIRD_ALIVE = 1
BIRD_DEAD = 0
GRAVITY = 0.001

GENERATION_SIZE = 60

NNET_INPUTS = 2
NNET_HIDDEN = 5
NNET_OUTPUTS = 1

JUMP_CHANCE = 0.5

MAX_Y_DIFF = DISPLAY_H - PIPE_MIN - PIPE_GAP_SIZE/2
MIN_Y_DIFF = PIPE_GAP_SIZE/2 - PIPE_MAX
Y_SHIFT = abs(MIN_Y_DIFF)
NORMALIZER = abs(MIN_Y_DIFF) + MAX_Y_DIFF

MUTATION_WEIGHT_MODIFY_CHANCE = 0.2
MUTATION_ARRAY_MIX_PERC = 0.5

MUTATION_CUT_OFF = 0.4
MUTATION_BAD_TO_KEEP = 0.2
MUTATION_MODIFY_CHANCE_LIMIT = 0.4