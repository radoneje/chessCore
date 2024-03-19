 
 
 
 
##/** Request the current clock state. */
DGT_SEND_CLK   = 0x41
##/** Request the current board state. */
DGT_SEND_BRD   = 0x42
#/** Request periodic updates. */
DGT_SEND_UPDATE= 0x43
#/** Request updates for board state. */
DGT_SEND_UPDATE_BRD  = 0x44
#/** Request the board's serial number. */
DGT_RETURN_SERIALNR  = 0x45
#/** Request the board's bus adress. */
DGT_RETURN_BUSADRES  = 0x46
#/** Request the trademark message. */
DGT_SEND_TRADEMARK   = 0x47
#/** Request transmission of moves stored in the board's EEPROM. */
DGT_SEND_EE_MOVES= 0x49
#/** Request updates when board or clock state changes. */
DGT_SEND_UPDATE_NICE = 0x4b
#/** Request battery status. */
DGT_SEND_BATTERY_STATUS  = 0x4c
#/** Request the board's version information. */
DGT_SEND_VERSION = 0x4d
#/** (Draughts) Requests the state of the black squares. */
DGT_SEND_BRD_50B = 0x50
#/** (Draughts) Set the board to scan only the black squares. */
DGT_SCAN_50B   = 0x51
#/** (Draughts) Requests the state of the white squares. */
DGT_SEND_BRD_50W = 0x52
#/** (Draughts) Set the board to scan only the white squares. */
DGT_SCAN_50W   = 0x53
#/** (Draughts) Set the board to scan the whole board. */
DGT_SCAN_100   = 0x54
#/** Request the board's long serial number. */
DGT_RETURN_LONG_SERIALNR = 0x55

#/* Clock messages. */
#/** Set clock state. */
DGT_CLOCK_MESSAGE = 0x2b
#/** Change main display. */
DGT_CMD_CLOCK_DISPLAY   = 0x01
#/** Change icons on clock. */
DGT_CMD_CLOCK_ICONS = 0x02
#/** End custom display. */
DGT_CMD_CLOCK_END = 0x03
#/** Request current button pressed. */
DGT_CMD_CLOCK_BUTTON= 0x08
#/** Request clock version. */
DGT_CMD_CLOCK_VERSION   = 0x09
#/** Programmatically set clock times and running state. */
DGT_CMD_CLOCK_SETNRUN   = 0x0a
#/** Change beep state. */
DGT_CMD_CLOCK_BEEP= 0x0b
#/** Start of clock message. */
DGT_CMD_CLOCK_START_MESSAGE = 0x03
#/** End of clock message. */
DGT_CMD_CLOCK_END_MESSAGE   = 0x00

SQUARES = [
  'a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8',
  'a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7',
  'a6', 'b6', 'c6', 'd6', 'e6', 'f6', 'g6', 'h6',
  'a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5', 'h5',
  'a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'h4',
  'a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3',
  'a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2',
  'a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1'
]
PIECES = [
{ "role": None, "color": None },
{ "role": 'pawn', "color": 'white' },
{ "role": 'rook', "color": 'white' },
{ "role": 'knight', "color": 'white' },
{ "role": 'bishop', "color": 'white' },
{ "role": 'king', "color": 'white' },
{ "role": 'queen', "color": 'white' },
{ "role": 'pawn', "color": 'black' },
{ "role": 'rook', "color": 'black' },
{ "role": 'knight', "color": 'black' },
{ "role": 'bishop', "color": 'black' },
{ "role": 'king', "color": 'black' },
{ "role": 'queen', "color": 'black' },
{ "role": None, "color": None }, # PIECE1
{ "role": None, "color": None }, # PIECE2
{ "role": None, "color": None }, # PIECE3
]