#!tetris-lang

cols :=	8;
rows :=	16;
maxsize_x := 4;
maxsize_y := 4;

var gravity := 1;

colors := [
	[0,   0,   0  ],
	[255, 0,   0  ],
	[0,   150, 0  ],
	[0,   0,   255],
	[255, 120, 0  ],
	[255, 255, 0  ],
	[180, 0,   255],
	[0,   220, 220]
];

// [0,  1,  2,  3]
// [4,  5,   6, 7]
// [8,  9,  10, 11]
// [12, 13, 14, 15]

var blockI := [
	[4,5,6,7],
	[1,5,9,13]
];
var blockL := [
	[5,9,13,14],
	[9,10,11,13]
	[5,6,10,14],
	[6,8,9,10]
];
var blockJ := [
	[6,10,13,14],
    [5,9,10,11],
    [6,7,10,14,
    [5,6,7,9]
];
var blockT := [
	[0,1,2,5],
	[1,4,5,9],
    [1,4,5,6],
    [1,5,6,9]
];
var blockS := [
	[1,2,4,5],
	[0,4,5,9]
];
var blockZ := [
	[0,1,5,6],
	[2,5,6,9]
];

blocks := [
	blockI,
	blockJ,
	blockL,
	blockT,
	blockS,
	blockZ
]

onLeftButton(block) begin
	block.moveLeft(1);
end

onRightButton(block) begin
	block.moveRight(1)
end

onUpButton(block) begin
end

onDownButton(block) begin
	block.moveDown(1);
end

onAButton(block) begin
	block.rotateLeft();
end

onBButton(block) begin
	block.rotateRight();
end

onXButton(block) begin
end

onYButton(block) begin
end

fall(block) begin
	block.moveDown(gravity) + 1;
end

fallEnd(newBlock) begin
	newBlock := getRandomBlock();
	score := score + 1;
	clearLines();
end


// Implement these in python backend
========================================================================


// can be overwritten
cols
rows
maxsize_x
maxsize_y

colors
blocks

// internal

block.moveLeft(amt)
block.moveRight(amt)
block.moveUp(amt)
block.moveDown(amt)
block.rotateLeft()
block.rotateRight()
block.rotateRandom()

getRandomBlock()
getRandomColor()
clearLines()

