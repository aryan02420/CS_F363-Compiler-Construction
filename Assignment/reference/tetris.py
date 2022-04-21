import TLGameEngine

TLGameEngine.set_cols(8)
TLGameEngine.set_rows(16)
TLGameEngine.set_maxsize_x(4)
TLGameEngine.set_maxsize_y(4)
TLGameEngine.set_gravity(1)

TLGameEngine.set_color(
	[
		[0,   0,   0  ],
		[255, 0,   0  ],
		[0,   150, 0  ],
		[0,   0,   255],
		[255, 120, 0  ],
		[255, 255, 0  ],
		[180, 0,   255],
		[0,   220, 220]
	]
)


blockI = [
	[4,5,6,7],
	[1,5,9,13]
]

blockL = [
	[5,9,13,14],
	[9,10,11,13]
	[5,6,10,14],
	[6,8,9,10]
]

blockJ = [
	[6,10,13,14],
    [5,9,10,11],
    [6,7,10,14],
    [5,6,7,9]
]

blockT = [
	[0,1,2,5],
	[1,4,5,9],
    [1,4,5,6],
    [1,5,6,9]
]

blockS = [
	[1,2,4,5],
	[0,4,5,9]
]

blockZ = [
	[0,1,5,6],
	[2,5,6,9]
]

TLGameEngine.set_blocks(
	[
		blockI,
		blockJ,
		blockL,
		blockT,
		blockS,
		blockZ
	]
)

def onLeftButton():
	TLGameEngine.block.moveLeft(1)

def onRightButton() :
	TLGameEngine.block.moveRight(1)

def onUpButton() :
	pass

def onDownButton() :
	TLGameEngine.block.moveDown(1)

def onAButton() :
	TLGameEngine.block.rotateLeft()

def onBButton() :
	TLGameEngine.block.rotateRight()

def onXButton() :
	pass

def onYButton() :
	pass

TLGameEngine.fall():
	TLGameEngine.block.moveDown(get_gravity()) + 1


