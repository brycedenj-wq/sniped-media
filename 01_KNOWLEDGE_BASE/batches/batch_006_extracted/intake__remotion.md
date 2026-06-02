1

Community

Classroom

Calendar

Members

Map

Leaderboards

About

The AI Edge

1

YouTube Builds + Resources - 2026

0%

Claude Code

Built an AI SaaS in 20 Minutes (Claude Code + n8n)

Claude Code Plugin - Ralph Wiggum

Claude Code Creates Videos in Minutes! (Remotion)

Claude Code Now Has SUPERPOWERS! (plugin)

Claude Code Made 3x Faster Websites! (Astro)

Claude Code Agent Teams: Token Cost Worth It?

Claude is Now an AI Hacker! (Shannon)

Claude Code Remote Control Is a Game Changer!

Watch Your Claude Code Agents Working!

Claude Code /Loop Feature Saves Hours of Work!

Claude Code Now Has Full Google Workspace Access!

Claude Code Skills Now Improve Themselves! (2.0)

Claude Code + Nano Banana 2 = Apple-Style Sites!

Claude Code Skills Can Now Improve Themselves!

Every New Claude Code Feature Explained! (2026)

Every Claude Code Concept Explained for Non-Coders

Stop Installing Thousands of Claude Code Skills!

Claude Code + Obsidian = AI That Never Forgets!

Claude Live Artifacts Setup Is Probably Broken!

Claude Design Makes Websites INSANELY easy!

Claude Cowork

Claude Cowork Just Broke the Internet!

Claude Releases

Google Antigravity

Google Gemini

n8n

Opencode

Clawdbot / Openclaw

2025 Videos

Claude Code Creates Videos in Minutes! (Remotion)

11:48

The complete Remotion + Claude Code tutorial --- learn how to set up and use the viral Agent Skills integration that\'s blowing up in 2026, letting you generate animated videos, explainers, and motion graphics just by describing them in natural language. Remotion (the React-based framework for programmatic videos) + Claude Code\'s new official skill turns prompts into full Remotion projects --- no After Effects, no Premiere Pro, no manual timeline dragging. Ideal for devs, marketers, creators, and anyone wanting autopilot video content (product demos, GitHub explainers, social shorts, personalised reels).

In this video, I walk you through the full setup (one-command install, Claude Code integration, project creation), run a real example turning a GitHub repo into an animated overview video, show iterations with prompts (better transitions, images, colors), and share my honest take after testing it (super fast for prototypes and automation, but expect some reprompting and manual tweaks for polish --- not 100% magic yet, but insanely promising).

What You\'ll Learn:

What Remotion + Claude Code Agent Skills actually does (prompt → code → rendered video)

Step-by-step installation (npx create-video, add Remotion skill, Claude Code boot)

Running Remotion dev server and previewing in browser

Using Claude in plan/execute mode to generate and refine video code

Pulling in assets (images from GitHub, custom colours, animations)

Iterating with targeted prompts (fix transitions, add glows, match branding)

Real demo: GitHub repo explainer video from scratch

Honest review: Strengths (speed, reusability, programmatic power) vs. limitations (visual reasoning quirks, iteration needed, best for structured/explainers)

MCP Install:

{

\"mcpServers\": {

\"remotion-documentation\": {

\"command\": \"npx\",

\"args\": \[\"@remotion/mcp@latest\"\]

}

}

}

Remotion Skills

\$ npx skills add remotion-dev/skills

Remotion Project Install:

npx create-video@latest

Resources

Remotion

Remotion (on X)

Remotion Github

Remotion Examples

Claude Code Creates Videos in Minutes! (Remotion) - YouTube Builds + Resources - 2026 · The AI EdgeRemotion + Claude Code Tutorial

Remotion lets you completely edit and

create videos just using code. And now

we\'re able to use it with clawed code as

a fantastic skill. All you need to do is

describe what you want and it will go

off and generate it. If you\'re a real

estate agent, that can mean providing it

a load of different property images like

you can see here and then telling it to

go through. actually create a quick

video that we could put on the website

explaining what that listing is, some of

the key features to go with it as well

and a call to action at the end to make

sure that we get it running on autopilot

24/7. Or if you just got a favorite

sport, for example, like we can see in

the background, Formula 1, you could

just go through and get it to create a

nice quick video showing the different

teams this year, how they\'re able to

perform, what their different numbers

are, some different maps. And again, all

of this can be done by just a simple

line within your Claude code. And that\'s

the power of Remotion. In this video,

I\'m going to show you how you can set up

Remotion on your computer and enable

Claude Code to be able to go through and

generate all of this for you by just a

simple prompt to get the output. We\'re

also going to walk through the best

framework to get the best results. And

we\'re going to do a quick example

together all around bringing a GitHub

repo to life. Let\'s get straight into

it. And if you want to learn more about

AI and automation, make sure to come

across to our community. We\'ve got tons

and tons of insights. You can even get

one-on-one time with me and much much

more to get ahead with AI. Now, to set

it up, it\'s nice and simple. We just

need to run this command here, which

I\'ll include in the link down below so

that you can go through and set it up

yourself nice and easily. Copy this.

We\'re going to open up a new terminal

in, for example, VS Code. We\'re going to

enter it in there, which is going to

start the process of going through and

cloning it into our specific repository.

We\'re able to choose specific agents, or

we can come through and choose all

agents. To show you the difference, if

we come into here, you\'ll be able to see

the different ones that we\'re able to

access or what we\'re able to do is if we

just come up to the top, we\'re going to

say that we want to have it for claw

code. Today, we\'re going to press enter.

We\'re going to say that we want it to be

a global skill and we\'re going to have

it as sis link. We\'re then going to come

through and say yes, we be installed and

it\'s going to go through and just make

sure it\'s ready to be set up. Once we\'ve

done this, we\'re then going to come

across and copy this command that

they\'ve got here to actually start going

through and generating our videos. We

then want to come through, open up a

folder for us to store everything that

we\'re going to be generating today. So,

we\'re just going to come through and

create a new folder to store everything.

We\'re going to call it GitHub. And then

we\'re going to do open. Now, we\'ll have

everything showing up on the left hand

side. We\'ll bring our terminal back up.

We\'ve now got that folder name as you

can see here. And then we\'re just going

to press npx create video latest and it

should go through and make sure that

we\'re able to use it straight away. Now

what you\'ll see here is they\'ve got a

few templates ready to go. All of them

are optimized to give you specific

outputs. So it\'s definitely worth

looking through here depending on the

output you\'re trying to achieve each

time you go through. For today, we\'re

just going to come up and use blank. So

we\'re going to press enter. We\'re going

to say yes for Tailwind CSS. Same for

the agent skills. And now it should go

through and get everything set up for

us. As we can see on the left hand side

there. Now we\'ve gone through and got

all of it installed. And we\'ve got some

of the other ones on the left hand side

here. So for example, we don\'t need Open

Code, VS Code, and Gemini and a few

others. So you can go through and delete

them. We\'re going to come down. We need

to copy this command here. We\'re just

going to open up another new terminal

just to show you everything step by

step. We\'re going to run npmi npm rundev

and this should go through get

everything installed for us and set up

ready to go. So there we go. It\'s now

running through and getting us all set

up. This is going to enable us to come

through and actually use this code here.

So we\'ll copy this, come across to a

Chrome browser, paste in there, and now

we can see our video editing interface

that we want to use. So this is the

base. How are we going to get Claude to

go through and actually run it? Well,

what we\'re going to do is come back

across. We\'re going to create a new

terminal. We\'re now going to type Claude

in here to boot up our Claude code

instance. We\'re going to say, I have

given you the ability to run remotion as

a skill. Please go through and just

double check what it is, how it works

before we go through and actually create

an output. We\'re just going to go

through to plan mode just to make sure

that it understands it because of course

we want all of the context, all of the

skills to be understood so that we can

get that better output. Speaking of how

we get better outputs, we want to use

Remotion like we\'re creative directors.

So, what does this mean? Well, it\'s not

going to be able to go off and just do

everything on its own. What we need is a

Best Prompts for Remotion AI Videos

good structured framework to approach it

with. First of all, we\'re going to need

to give it a really clear idea of what

we want to achieve. Step one, do this.

This is the output we want. These are

the different scenes we want and

everything like that to give it a clear

instruction on what we\'re looking to

achieve. Next, we also want to provide

it with any reference material. That

could be any documents, i.e. a creative

brief that you\'ve already created, any

links to any websites, images, anything

like that you wanted to reference or any

assets, i.e. images that maybe you\'ve

already taken and you wanted to utilize

to get the output. We then want to chunk

up the work as we go through and develop

it. So, we want to start with maybe

section one, i.e. the first couple of

slides or the first iteration. Then

we\'re going to go through and try the

next part again taking it piece by piece

layering on top and then we\'re going to

get our output after that. Then what

you\'ll find is actually after you get

the output you\'ll probably start having

a loop where you keep going through

round and round and round making sure

that you add any reference material but

likely just refining the output that is

already produced. So if we come back

across what we\'ll see here is it\'s now

gone through and it should have

understood all of the different skills

as we can see here. We\'re now going to

come to the bottom and explain the

creative brief that we want it to

complete. So there we go. We\'re just

going to come through and say that we

want it to go through and create a

overview explainer video with icons,

animations, everything like this. And

we\'re going to use the GitHub repository

which if we come across is going to be

based on this vibe camb which is getting

lots of interest at the moment. And this

is how we can go through and massively

improve the planning and execution

whilst we\'re going through and building

our apps. So, because Claude Code has

got access to the internet, we\'re going

to copy the URL, come across, and just

paste it into here, then we\'ll be able

to send it off to make sure that it goes

through and actually references the

Remotion video instructions, the best

practices before we let it go through

and actually create the video. But I

just wanted to go through and show you a

few quick examples. So, this one here is

all around tracking your fitness

journey. Again, we\'re able to have audio

over the top of this. We can connect it

into platforms like 11 Labs. We can give

it music and much much more to help get

a really nice polished output at the end

that we\'ll be able to use on here on

LinkedIn on marketing campaigns and

everything else. And there\'s another

video here all around the actual

validation of an idea. As we can see,

it\'s actually going to have a call to

action at the end which is specific to

the business that he runs. It\'s got

those purple and blue fonts and color

schemes which I don\'t really like. Looks

very vibe coded. But again, we\'re able

to go through completely change this to

our own color scheme. As you saw in the

back of there, it\'s got some animations

that go through as well. So, it helps

bring it to life without needing an

animator and all these other things.

Yes, it\'s not perfect, but again, this

is the first iteration of this new tool

that we\'re starting to get used and I\'m

sure that it will massively improve over

time. There\'ll be lots of plugins for

skills to get better outputs and much

much more. Another one I found really

interesting from Reotion themselves as

well, we\'re able to have travel ones as

well. So for example, right to left from

Zurich across to New York and we can get

access to all of the source code as well

to understand how they achieve this

output and replicate it for ourselves.

So there we go. We just got our plan

back from Claude. It\'s gone through and

explained what we should do, the

different sections. It\'s understood of

course all of the different elements

that we\'ve got. It\'s gone through and

analyzed the repository that we gave it

access to as well. We\'re going to have a

title and intro. We\'re going to have the

problem. We\'re going to have multi-agent

support. some key features, call to

action. So, we\'re going to come down.

We\'re going to say yes, auto accept

edits, and let it run through. So, there

we go. It\'s going to do it all for us.

So, we\'re going to come back across to

our local host dashboard. And now, what

we\'ll be able to see is where we\'ve got

all of the information ready to go.

Improving AI Video Output

We\'ll be able to see any of the assets

that it pulls into here as well, which

is going to be part of our public

folder, which I\'ll show you back in the

repo in a second. Got the composition,

i.e. the different file that we\'ve

generated. We\'re going to press play. We

got a icon that comes up the top. We got

19,000 stars. It\'s got a few animated

icons coming through. Looks more like a

PowerPoint transition. So, we definitely

want to change that. Overall, it does

look quite good. It\'s quite easy to

understand. It\'s got the command. Yep.

Which we\'ll be able to see there. So,

overall, I don\'t think it\'s 100%, but

it\'s incredibly good to think that took

what 5 minutes, 10 minutes to go through

and get this output. We didn\'t need any

animators. And this is just the start.

We can come back across. We can come to

the left and see if it\'s got any public

skills and icons in here, which it

doesn\'t. So, we can come down and say

great, but I need you to pull in some of

the images from the GitHub repo to use.

Just for time, I\'m going to come back

and copy the image address. And then one

image one, we\'ll paste in there. We\'ll

then say image two. We\'ll come back

across. Copy this one as well. Paste in

there. We\'ll also say please can you

improve the transitions to be more as as

please elevate fine to make it look more

an actual editor had gone and done this

for us. Please utilize industry best

practice. We\'ll send it off and see what

it\'s able to do on that next iteration.

There we go. It said that it\'s made all

the changes in here that we needed it

to. If we come to the left hand side,

we\'ll also see that we\'ve now got those

two icons or images us to be able to use

and reference as well. So, let\'s come

back across. And there we go. Straight

away, we can already see that icon. So,

we\'re just going to press play. See it

come through in the background here. I

really like that new design. It\'s got

some purple in the background as well.

The transition straight away looked a

lot better than it did before. It looks

like we\'ve got the interface. Again, I

don\'t like the purples and blues. They

always look awful. Always looks really

vioded. So, we could definitely go

through and change that. We\'ve also got

the glow in the background, which I

really like. And it had that action at

the end here. We just come across

showing the actual link to our

repository as well. So, it\'s great to

see that we\'re going through. It\'s

definitely some improvements that we can

make. But to think this was done in 5

minutes. You can go off, make a cup of

tea, or coffee, whatever it may be, and

it\'s able to produce these outputs. This

is so much easier than it was before.

Now, what we can do as well is, of

course, we can screenshot specific

parts. So, for example, this make sure

to copy it. We\'ll then come back across.

We\'ll paste our image into the

conversation. We\'ll say great, but I

need this slide to look. We\'ll do this

as the last edit again. Really making it

targeted on what we want to achieve. So,

there we go. It says it\'s generated

everything for us. So, let\'s come back

across. We just refresh everything. And

we\'ll go play

10x your productivity. 19,000 developers

already have. One command is all it

takes. Try Vibe Canvan today.

Is Remotion + Claude Code Worth It?

So, there we go. That\'s how we can go

through and start to get videos

generated on autopilot and edited with

claw code. Is it 100%? Nope. But it\'s

incredibly good for a starting off

project. And I\'m sure that this will get

much much better over time, specialist

skills. And if you want to learn more

about AI and automation, click the first

link in the description. Come across to

the community. And if you want AI built

for your business, click the second one.

Stay tuned for more around AI

automation. And have a great day.
