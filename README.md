<insert logo, mast waala bana do koi>

# CS_F363-Compiler-Construction Project | BlockBusters

# Description:
<insert, name of our game engine> Engine is a feature-packed, complete end-to-end tetris game engine that enables the user to design creative variants 2D tetris. It provides a comprehensive set of common tools, so that users can focus on bringing their imagination to life without having to reinvent the wheel. 

Games can be exported with simple steps to a number of major desktop platforms (Linux, macOS, Windows). The engine is based on a brand new programming language "tetris-lang" (.tl) designed specifically for the coding of tetris games making it a lot more fluid and beginner friendly. "tetris-lang" is a step towards a paradigm shift where no prerequisite programming knowledge is required to get started on tetris game development. 

So what are you waiting for, quickly get started on your tetris game development journey and we hope you have an immersive and fun experience using our <insert, name of our game engine> Engine!!    

# Installation and Environment Setup:

## Build Requirements:

* Mac OS X 10.7+, Xcode 8+
* or Ubuntu 14.04+, CMake 3.1+
* or Windows 7+, VS 2015
* Python 2.7.5+(NOT Python 3)
* NDK r16+ is required to build Android games
* Android Studio 3.0.0+ to build Android games(tested with 3.0.0)
* JRE or JDK 1.6+ is required for web publishing

## Runtime Requirements:

* iOS 8.0+ for iPhone / iPad games
* Android 3.0.0+ for Android
* OS X v10.9+ for Mac games
* Windows 7+ for Win games

## Using host OS environment:
1. Check to see if your Python installation has pip. Enter the following in your terminal:

        ```
        $ pip -h
        ```
If you see the help text for pip then you have pip installed, otherwise [download and install pip](https://pip.pypa.io/en/latest/installing.html)

2. Clone the repo from GitHub and install the tetrislang package.
```
$ git clone https://github.com/aryan02420/CS_F363-Compiler-Construction.git
$ cd CS_F363-Compiler-Construction/tetrislang/
$ pip3 install -e .
```

## Using a virtual environment:
1. Setup the pip package manager
Check to see if your Python installation has pip. Enter the following in your terminal:
```
$ pip -h
```
If you see the help text for pip then you have pip installed, otherwise [download and install pip](https://pip.pypa.io/en/latest/installing.html)

2. Clone the repo from GitHub and install the tetrislang package.
```
$ git clone https://github.com/aryan02420/CS_F363-Compiler-Construction.git
$ cd CS_F363-Compiler-Construction/tetrislang/
$ pip install -e .
```


<insert options one can use, normal tetrislang package and also venv>

## Writing in tl and execution:
<insert instructions on how to run the code and get output>

## Demo:
<insert screenrecording and examples of running>

## Documentation:
The official documentation is hosted [here](https://aryan02420.github.io/CS_F363-Compiler-Construction/tetrislang/docs/). It is maintained by the Godot community in its own GitHub repository.

* [All Docs in a single place!](http://docs.cocos2d-x.org/)
* [Online API Reference](http://docs.cocos2d-x.org/api-ref/index.html) _Note that Cocos2d-x and Cocos Creator have different API set_
* [Programmers Guide](https://docs.cocos2d-x.org/cocos2d-x/v4/en/basic_concepts/)
* [Latest Release Note](https://github.com/cocos2d/cocos2d-x/blob/v4/docs/RELEASE_NOTES.md)
* [Changelog](https://github.com/cocos2d/cocos2d-x/blob/v4/CHANGELOG)
<insert syntax explanation and docs for tl language>
    
Current State of the Project
----------------------------

**Important notice**: Gameplay is currently non-functional as the internal simulation is replaced by a more sophisticated implementation. You also might experience errors when running a build. Gameplay will return in a later update. Detailed explanations can be found in this [blog post](https://blog.openage.dev/new-gamestate-2020.html).

* What features are currently implemented?
    * See [status page](https://github.com/SFTtech/openage/projects).

* What's the plan?
    * See [doc/milestones.md](/doc/milestones.md). We also have [lists of crazy xor good ideas](/doc/ideas) and a [technical overview for requested features](/doc/ideas/fr_technical_overview.md).

## Future Plans of the project:

## Free, open source and community-driven
Godot is completely free and open source under the very permissive MIT license. No strings attached, no royalties, nothing. The users' games are theirs, down to the last line of engine code. Godot's development is fully independent and community-driven, empowering users to help shape their engine to match their expectations. It is supported by the Software Freedom Conservancy not-for-profit.

Before being open sourced in February 2014, Godot had been developed by Juan Linietsky and Ariel Manzur (both still maintaining the project) for several years as an in-house engine, used to publish several work-for-hire titles.
    
    
Contributing
============

You might ask yourself now "Yeah, this sounds cool and all, but how do *I* participate
and ~~get famous~~ contribute useful features?".

Fortunately for you, there is a lot to do and we are very grateful for help.

## Where do I start?

* The engine has several [core parts](https://github.com/SFTtech/openage/projects) that need help.
  You can look at the project related issues and find something for you, for example:
    * **Asset Converter:** Converts whatever properietary format used by a Age of Empires 2 into
    open formats. Written mostly in Python 3. There are a lot of TODOs and beginner issues available
    right now, so it's a good place to get your feet wet.
    * **Game simulation:** Also known as the gameplay implementation. Written in C++, using the
    Entity-Component-System paradigm in addition to an event-driven simulation.
    * **Documentation:** We not only document code, but also anything technical about the Genie engine
    and its games. If you like documenting [file formats](/doc/media)
    or thouroughly investigating [game mechanics](/doc/reverse_engineering),
    then this might be the right place to start.
* **Check the issues** [labelled with good first issues](https://github.com/SFTtech/openage/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22). These are tasks that you can start right away
  and don't require much previous knowledge.
* **Ask us** in the [chat](https://app.element.io/#/room/#sfttech:matrix.org). Someone there could need
  help with something.
* You can also **take the initiative** and fix a bug you found, create an issue for discussion or
  implement a feature that we never though of, but always wanted.


## Ok, I found something. What now?

* **[Tell us](#contact)**, if you haven't already. Chances are that we have additional information
  and directions.
* **[Read the docs](/doc)**. They will answer most "administrative"
  questions like what code style is used and how the engine core parts are connected.
* **Read the code** and get familiar with the engine component you want to work with.
* Do not hesitate to **[ask us for help](#contact)** if you do not understand something.


## How do I contribute my features/changes?

* Read the **[contributing guide](/doc/contributing.md)**.
* You can upload work in progress (WIP) revisions or drafts of your contribution to get feedback or support.
* Tell us (again) when you want us to review your work.

## I want to help, but I'm not a programmer...

Then openage might be a good reason to become one! We have many issues and tasks for beginners. You
just have to ask and we'll find something. Alternatively, lurking is also allowed.

----

Cheers, happy hecking.
    
    

Environment Setup
--------------------

Should set up environment before starting a new game or running tests



Should invoke this script if using linux system

```
$ cd cocos2d-x
$ ./install-linux-deps.sh
```

Running Tests
--------------------

```
$ cd cocos2d-x
$ mkdir build
$ cd build
$ cocos run --proj-dir .. -p [mac|win32|android|linux|ios]
```

How to start a new game
-----------------------

    $ cd cocos2d-x
    $ ./setup.py
    $ source FILE_TO_SAVE_SYSTEM_VARIABLE
    $ cocos new MyGame -p com.your_company.mygame -l cpp -d NEW_PROJECTS_DIR
    $ cd NEW_PROJECTS_DIR/MyGame
    $ mkdir build
    $ cd build
    $ cocos run --proj-dir .. -p [mac|win32|android|linux|ios]

You can also create a Lua project with `-l lua`.
    
    
    
Spreading the word!
--------------------------------
You can help us spread the word about cocos2d-x! We would surely appreciate it!

* Talk about us on Facebook! Our [Facebook Page](https://www.facebook.com/cocos2dx/)
* Tweet, Tweet! Our [Twitter](https://twitter.com/cocos2dx)
* Read our [Blog](http://blog.cocos2d-x.org/) and promote it on your social media.
    
    
Contact us
----------

   * Forum: [http://discuss.cocos2d-x.org][9]
   * Twitter: [http://www.twitter.com/cocos2dx][10]
   * Weibo: [http://t.sina.com.cn/cocos2dx][11]




## Directory Structure:
<insert explanation of what folder is where>

```
.
├── Assignment
│   ├── assets
│   │   ├── 46786-50325-1-PB.pdf
│   │   ├── bb.png
│   │   ├── flowchart1.png
│   │   └── phases.jpeg
│   ├── bugs
│   │   └── bugs.txt
│   ├── compiler
│   │   ├── compiler.py
│   │   ├── output
│   │   │   ├── assets
│   │   │   │   ├── arcade.TTF
│   │   │   │   ├── highscore.txt
│   │   │   │   └── mario.ttf
│   │   │   ├── out1
│   │   │   ├── out2
│   │   │   ├── out3
│   │   │   └── tetris
│   │   ├── parser.out
│   │   ├── __pycache__
│   │   │   ├── parser.cpython-38.pyc
│   │   │   └── scanner.cpython-38.pyc
│   │   ├── sample_tlang_code
│   │   │   ├── case1.tl
│   │   │   ├── case2.tl
│   │   │   ├── case3.tl
│   │   │   └── tetris.tl
│   │   └── to_do.txt
│   ├── diagram
│   │   ├── diagram
│   │   │   ├── actparams.png
│   │   │   ├── addop.png
│   │   │   ├── assignmentStatement.png
│   │   │   ├── bitandop.png
│   │   │   ├── bitExpression.png
│   │   │   ├── bitxorop.png
│   │   │   ├── boolExpression.png
│   │   │   ├── cmpop.png
│   │   │   ├── comment.png
│   │   │   ├── compoundStatement.png
│   │   │   ├── conditionalStatement.png
│   │   │   ├── emptyStatement.png
│   │   │   ├── expression.png
│   │   │   ├── fargs.png
│   │   │   ├── functionDeclaration.png
│   │   │   ├── functionStatement.png
│   │   │   ├── loopStatement.png
│   │   │   ├── mulop.png
│   │   │   ├── program.png
│   │   │   ├── relationalExpression.png
│   │   │   ├── rr-1.63.png
│   │   │   ├── shiftop.png
│   │   │   ├── statement.png
│   │   │   ├── statements.png
│   │   │   ├── term.png
│   │   │   ├── unary.png
│   │   │   └── variableDeclaration.png
│   │   └── index.html
│   ├── engine
│   │   ├── assets
│   │   │   ├── arcade.TTF
│   │   │   ├── clear.wav
│   │   │   ├── gameover.wav
│   │   │   ├── highscore.txt
│   │   │   ├── key_press.wav
│   │   │   ├── mario.ttf
│   │   │   └── theme.wav
│   │   ├── __pycache__
│   │   │   └── tetris_engine.cpython-38.pyc
│   │   └── tetris_engine.py
│   ├── lex-diagram
│   │   ├── diagram
│   │   │   ├── AND.png
│   │   │   ├── ASSIGN.png
│   │   │   ├── BEGIN.png
│   │   │   ├── BOOL.png
│   │   │   ├── DO.png
│   │   │   ├── ELSE.png
│   │   │   ├── END.png
│   │   │   ├── EQ.png
│   │   │   ├── FOR.png
│   │   │   ├── FUNCTION.png
│   │   │   ├── GTEQ.png
│   │   │   ├── IDENT.png
│   │   │   ├── IF.png
│   │   │   ├── LTEQ.png
│   │   │   ├── NEQ.png
│   │   │   ├── NOT.png
│   │   │   ├── NUM.png
│   │   │   ├── OR.png
│   │   │   ├── Railroad-Diagram-Generator.png
│   │   │   ├── SAL.png
│   │   │   ├── SAR.png
│   │   │   ├── STRING.png
│   │   │   ├── THEN.png
│   │   │   ├── TO.png
│   │   │   ├── VAR.png
│   │   │   └── WHILE.png
│   │   └── index.html
│   ├── misc
│   │   ├── challenges.txt
│   │   ├── grammar.txt
│   │   ├── language-specs
│   │   ├── misc.txt
│   │   ├── new_grammar.txt
│   │   ├── scanner.txt
│   │   └── to_do.txt
│   ├── parser
│   │   └── tl_parser.py
│   ├── scanner
│   │   ├── midsem.sh
│   │   └── scanner.py
│   └── tests
│       ├── expected
│       │   ├── variable_assignment
│       │   └── variable_declaration
│       ├── input
│       │   ├── variable_assignment
│       │   └── variable_declaration
│       ├── output
│       │   ├── variable_assignment
│       │   └── variable_declaration
│       ├── runner.sh
│       └── tcompiler
├── EndSem Report - BlockBusters.pdf
├── MidSem Report - BlockBusters.pdf
├── README.md
├── requirements.txt
└── tetrislang
    ├── README.md
    ├── setup.py
    ├── tetrislang
    │   ├── assets
    │   │   ├── arcade.ttf
    │   │   ├── clear.wav
    │   │   ├── gameover.wav
    │   │   ├── highscore.txt
    │   │   ├── key_press.wav
    │   │   ├── mario.ttf
    │   │   └── theme.wav
    │   ├── bin
    │   │   └── tetris-lang
    │   ├── compiler.py
    │   ├── engine.py
    │   ├── __init__.py
    │   ├── parser.py
    │   ├── __pycache__
    │   │   ├── compiler.cpython-38.pyc
    │   │   ├── engine.cpython-38.pyc
    │   │   ├── __init__.cpython-38.pyc
    │   │   ├── parser.cpython-38.pyc
    │   │   └── scanner.cpython-38.pyc
    │   └── scanner.py
    └── tetrislang.egg-info
        ├── dependency_links.txt
        ├── not-zip-safe
        ├── PKG-INFO
        ├── requires.txt
        ├── SOURCES.txt
        └── top_level.txt

28 directories, 133 files
```
