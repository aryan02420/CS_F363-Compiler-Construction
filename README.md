<p align="center">
<img align="centre" width="250" height="200" src="https://user-images.githubusercontent.com/68325029/166507968-9db4e119-2624-489a-8bf9-79327a4e063a.png">
</p>

# CS_F363-Compiler-Construction Project | BlockBusters

# Description
BlockBuster is a feature-packed, complete end-to-end tetris game engine that enables the user to design creative variants 2D tetris. It provides a comprehensive set of common tools, so that users can focus on bringing their imagination to life without having to reinvent the wheel. 

Games can be exported with simple steps to a number of major desktop platforms (Linux, macOS). The engine is based on a brand new programming language "tetris-lang" (.tl) designed specifically for the coding of tetris games making it a lot more fluid and beginner friendly. "tetris-lang" is a step towards a paradigm shift where no prerequisite programming knowledge is required to get started on tetris game development. 

So what are you waiting for, quickly get started on your tetris game development journey and we hope you have an immersive and fun experience using BlockBuster!!

# Directory Structure
```
tetrislang/
├── docs
│   ├── engine.html
│   └── index.html
├── .gitignore
├── README.md
├── sample
│   ├── game.py
│   └── tetris.tl
├── setup.py
├── tetrislang
│   ├── assets
│   ├── bin
│   │   └── tetris-lang
│   ├── compiler.py
│   ├── engine.py
│   ├── __init__.py
│   ├── parser.py
│   ├── __pycache__
│   └── scanner.py
└── tetrislang.egg-info

7 directories, 32 files
```
The above tree shows the overall structure of the tetrislang package.
1. scanner.py contains the scanner code. It is present in "tetrislang/" inside the package. Here is the link to the file.
2. grammar.txt contains the BNF grammar that was used to create the parser. Here is a link to the file.
3. parser.py contains the parser code. It is present in "tetrislang/" inside the package. Here is the link to the file.
4. compiler.py contains the final code that combines the scanner and parser. It is present in "tetrislang/" inside the package. Here is the link to the file.
5. engine.py contains the python framework for the Tetris game. It is present in "tetrislang/" inside the package. Here is the link to the file.
6. tetris.tl is a sample code written in "tetris-lang". It is present in "sample/" inside the package. Here is the link to the file.
7. game.py is the executable output that is generated after compiling tetris.tl. It is present in "sample/" inside the package. Here is the link to the file.

# Installation and Environment Setup

## Build Requirements:

* Python 3.6.9+
* pip 9.0.1

## Runtime Requirements:

* Pygame 2.1.2
* sly 0.4

## Using host OS environment:
1. Check to see if your Python installation has pip. Enter the following in your terminal:

        pip3 -h
        
     If you see the help text for pip then you have pip installed, otherwise [download and install pip](https://pip.pypa.io/en/latest/installing.html)

2. Clone the repo from GitHub and install the tetrislang package

      Mac OS / Linux
        
        git clone https://github.com/aryan02420/CS_F363-Compiler-Construction.git
        cd CS_F363-Compiler-Construction/tetrislang/
        pip3 install -e .
        
<!--      Windows
     
        git clone https://github.com/aryan02420/CS_F363-Compiler-Construction.git
        cd CS_F363-Compiler-Construction\tetrislang\
        pip3 install -e . -->


## Using a virtual environment:
1. Check to see if your Python installation has pip. Enter the following in your terminal:

        pip3 -h
        
     If you see the help text for pip then you have pip installed, otherwise [download and install pip](https://pip.pypa.io/en/latest/installing.html)

2. Install the virtualenv package

        pip3 install virtualenv
        
3. Create the virtual environment

        virtualenv tetrisenv
        
4. Activate the virtual environment

      Mac OS / Linux
        
        source tetrisenv/bin/activate
        
<!--      Windows
     
        tetrisenv\Scripts\activate -->

5. Clone the repo from GitHub and install the tetrislang package

      Mac OS / Linux
        
        git clone https://github.com/aryan02420/CS_F363-Compiler-Construction.git
        cd CS_F363-Compiler-Construction/tetrislang/
        pip3 install -e .
        
     Windows
     
        git clone https://github.com/aryan02420/CS_F363-Compiler-Construction.git
        cd CS_F363-Compiler-Construction\tetrislang\
        pip3 install -e .

# How to create a new game
1. Write the "tetris-lang" game code (.tl file). Refer the [documentation](#documentation) section for language syntax and functionalities offered by the engine.
2. Compiling the code written above will generate an executable output file.

        tetris-lang <path to the .tl file>
        
   The above code will create an executable by the name "game.py" in the current directory.
      
   You can use the "-o" to set the output file path.
        
        tetris-lang <path to the .tl file> -o <path of the executable output>
        
3. To start the game immediately after compilation, use the "-e" flag.
        
        tetris-lang <path to the .tl file> -e
        
   Or you can also run the generated executable file as follows:
   
        ./<path of the executable output>

# Demo:
<insert, screenrecording and examples of running>

# Documentation:

* [BlockBuster docs](https://aryan02420.github.io/CS_F363-Compiler-Construction/tetrislang/docs/)
* [tetris-lang Programmers Guide](https://polyester-ricotta-98f.notion.site/TL-Language-Syntax-32b56c9f900b4ba9a19d224f5b5bcec0)
<!-- * [Latest Release Note](https://github.com/cocos2d/cocos2d-x/blob/v4/docs/RELEASE_NOTES.md)
* [Changelog](https://github.com/cocos2d/cocos2d-x/blob/v4/CHANGELOG) -->
    
<!-- # Current State of the Project

**Important notice**: Gameplay is currently non-functional as the internal simulation is replaced by a more sophisticated implementation. You also might experience errors when running a build. Gameplay will return in a later update. Detailed explanations can be found in this [blog post](https://blog.openage.dev/new-gamestate-2020.html).

* What features are currently implemented?
    * See [status page](https://github.com/SFTtech/openage/projects).

* What's the plan?
    * See [doc/milestones.md](/doc/milestones.md). We also have [lists of crazy xor good ideas](/doc/ideas) and a [technical overview for requested features](/doc/ideas/fr_technical_overview.md). -->

<!-- # Future Plans of the project: -->

# Free and open source
BlockBuster is completely free and open source under the very permissive MIT license. No strings attached, no royalties, nothing. The users' games are theirs, down to the last line of engine code. BlockBuster's development is fully independent, empowering users to help shape their engine to match their expectations.    
    
# Contributing to the project

You might ask yourself now "Yeah, this sounds cool and all, but how do *I* participate
and ~~get famous~~ contribute useful features?".

Fortunately for you, there is a lot to do and we are very grateful for help.

## Where do I start?

<!-- * The engine has several [core parts](https://github.com/SFTtech/openage/projects) that need help.
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
  and don't require much previous knowledge. -->
* **Ask us** by reaching out to any of the contributors through the [Contact Us](#contact-us) section. Someone there could need
  help with something.
* You can also **take the initiative** and fix a bug you found, create an issue for discussion or
  implement a feature that we never though of, but always wanted.

## Ok, I found something. What now?

* **[Tell us](#contact-us)**, if you haven't already. Chances are that we have additional information
  and directions.
* **[Read the docs](#documentation)**. They will answer most "administrative"
  questions like what code style is used and how the engine core parts are connected.
* **Read the code** and get familiar with the engine component you want to work with.
* Do not hesitate to **[ask us for help](#contact-us)** if you do not understand something.


## How do I contribute my features/changes?

<!-- * Read the **[contributing guide](/doc/contributing.md)**. -->
* You can upload work in progress (WIP) revisions or drafts of your contribution to get feedback or support.
* Tell us (again) when you want us to review your work.

<!-- ## I want to help, but I'm not a programmer...

Then openage might be a good reason to become one! We have many issues and tasks for beginners. You
just have to ask and we'll find something. Alternatively, lurking is also allowed. -->
       
# Spreading the word!

You can help us spread the word about BlockBuster! We would surely appreciate it!

* Talk about us on Facebook! Our [Facebook Page]()
* Tweet, Tweet! Our [Twitter]()
* Read our [Blog]() and promote it on your social media.
    
    
# Contact us

* Hrishikesh Kusneniwar - [hrishi508](https://github.com/hrishi508)
* Hardik Shah - [hardik01shah](https://github.com/hardik01shah)
* Hitarth Kothari - [hitarthk9](https://github.com/hitarthk9)
* Abhineet Karn - [dootdoot1111](https://github.com/dootdoot1111)
* Abhinav Srivastava - [Abhinav-2405](https://github.com/Abhinav-2405)
* Aryan Tyagi - [aryan02420](https://github.com/aryan02420)

### *Cheers, BlockBusters*
