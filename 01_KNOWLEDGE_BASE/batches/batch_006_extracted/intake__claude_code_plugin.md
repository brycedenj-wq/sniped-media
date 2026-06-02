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

Claude Code Plugin - Ralph Wiggum

14:52

Claude Code Ralph Wiggum plugin tutorial --- build apps autonomously without writing code. This official Anthropic plugin lets Claude Code loop through complex multi-step tasks, iterating until your app is complete. 37 features in 4 minutes. No code written. This changes everything about how we build AI apps.

What You\'ll Learn:

Installing Ralph Wiggum via Claude Marketplace (step-by-step)

Writing PRDs (Product Requirements Documents) that actually work

Using /ralph-loop with iterations and completion criteria

Sprint-based AI development with Kanban workflow

Real debugging when things break (Scrum Master mode)

Combining with front-end design plugin for better UI

Token usage considerations and cost trade-offs

Why Watch:

See Claude Code build a full dashboard autonomously

Real workflow with real errors --- not cherry-picked demos

Learn the PRD structure that gets the best results

Understand when Ralph works and when it doesn\'t

Practical token cost considerations (Opus plan recommended)

Combine plugins for design + development in one workflow

Install Claude Code Marketplace:

/plugin marketplace add anthropics/claude-code

Install Claude Code Ralph Wiggums:

/plugin install ralph-loop@claude-plugins-official

Ralph Wiggum Prompt:

/ralph-loop:ralph-loop \"Read and implement all requirements in ./ai-ops-dashboard-prd.md

Build a single index.html file using React, Tailwind, and Recharts via CDN.

Work through each epic in order. Verify each works before proceeding.

If blocked after 25 iterations, document blockers and continue with remaining work.

When all requirements complete and checklist passes, output:

\<promise\>DASHBOARD_COMPLETE\</promise\>\" \--max-iterations 35 \--completion-promise \"DASHBOARD_COMPLETE\"

Start the app locally:

run this on localhost

Resources

PRD - AI Ops Dashboard

App HTML - AI Ops Dashboard

Claude Code Plugin - Ralph Wiggum - YouTube Builds + Resources - 2026 · The AI Edge37 features in 4 minutes (no code)

37 features, four minutes, and I didn\'t

write a single line of code. Ralph

Wiggum. Yep. The Simpsons character is

now an extended plug-in within Claude

Code. Enables Claude Code to run for

hours on its own and able to complete

multi-step complex tasks and build

entire apps. In this video, I\'m going to

walk us through exactly how this setup

works, installing it, getting it up and

running, the best prompts to use, how to

structure them, and how it\'s completely

shifting how we build AI apps. and make

sure to come across to the community if

you want to get access to all of the

prompts, templates, everything I\'ve used

in this video. So, let\'s jump straight

in. So, what is Ralph Wigum? Well,

essentially, it\'s enabling our code to

be able to autonomously work in the

background over an extended period of

time to achieve a specific goal. What we

want to do is have a really clear

instruction, and this is going to be our

PRD, which we\'re going to touch on in a

second. We\'re then going to give it the

tasks that it needs to complete. And

then we\'re going to check each time we

iterate through, has that task actually

been completed? And that\'s where Ralph

steps in. We\'re basically saying if it\'s

completed all of the different user

stories and tasks we\'ve asked it to

complete, then we\'re going to be done.

If it hasn\'t, then we\'re going to keep

looping through until it\'s achieved

everything and we\'ve got the end result

with perhaps a few bugs that we need to

go through and just tidy up. Think of it

as like having sprints that were able to

achieve. But what are sprints? Well, if

you never heard the term before, it\'s

been used for many, many years in

software development and many other

different ways of going through and

completing short stints of actually

achieving a specific goal or piece of

work. So, for example, here, say we\'ve

got all of these different tasks that we

want to complete. We wouldn\'t be able to

do all of them in one go. So, what we

would do is get rid of this and say we

would choose one specific task that we

want to work on. That\'s what we would

put maybe as the highest priority that

we need to achieve. We would then have

this as the first task that we\'re going

to go through and complete. And this

helps build out that multi-phase plan of

what we want to achieve in what order.

So it could be that we\'ve got the

several tasks here and we would step by

step previously with AI get it to

complete each one in a specific order.

The reason for this is because maybe

some of these tasks actually relate to

each other specific design elements or

theory or logic anything like this we

need to make sure it almost happens

sequentially in the order that we want.

What we\'re able to do with Ralph is it\'s

able to take over this process and it

helps us prioritize the different ones.

So you may be familiar with aspects like

camb boards where we\'re able to go

through and manually specify the

different tasks in the backlog that we

want to achieve and then periodically

move them through to say being in

progress. So we\'re working on it at the

moment. We can call out if we\'ve got any

issues that block it. And then we can

also move it to done once we\'ve

completed that entire tasks. This is

What Ralph Wiggum can (and can\'t) do

where we\'re able to go through with

Ralph and analyze all of the different

tasks we want to complete and then move

them through the process of developing

the different aspects to add them into

the code that we want. But what is Ralph

actually really good at? Well, that\'s

why I mentioned around the PRDS and

having a really clear defined task for

it to complete because it\'s really good

at those well- definfined tasks, clear

criteria, iteration and refinement,

green field projects, and automatic

verification, i.e. tests, user case

stories, all of these different things

it can do and verify if it\'s achieved

that output correctly. What it tends to

struggle with though is anything that

requires human judgment, design

decisions, oneshots, unclear success

criteria or production debugging. And

what this means for us is the biggest

difference is actually the skill in the

operator because it\'s going to come down

to writing really good prompts, not just

using the best model. And what this

really means for how we use it dayto-day

is that we need to spend way more time

upfront on the product requirements

document or PRD. And what this does is

it really clearly defines the end result

that you\'re trying to achieve. So what

you want to build, its purpose, its

features, its functionalities, and its

behavior. We want a really clear goal of

what it\'s going to do, the output. We

want the user stories of how customers,

clients are going to interact it, any

designs and interactions from the user

and then any clarifications and

questions at the end. And what this

really means for us as the user is once

we\'ve specified all of this detail to

Ralph and Claude\'s code is able to go

through and start iterating on the

design and the development to achieve

this goal as quickly as possible. But

for us as the user, what it means is

we\'re essentially turning into something

called a scrum master where all we\'re

tending to do is actually specify the

work package or in this case the PRD and

what we want it to achieve and then go

through and just help refine those

outputs, remove blockers, explain

anything in a bit more details really to

get that output that we want to achieve.

Installing + running /ralph-loop (live demo)

So now let\'s come through and get it

installed. We\'re going to do VS Code

just to get it set up and we\'re going to

launch Claude within this application.

We\'re going to say yes, we\'re happy for

it to proceed. Now, the GitHub

repository I\'ll include linked down

below so that you can find it nice and

easily. And this is the official one

from Anthropic with all of the different

details, best practices, any escape

hatches, the philosophy of how we use

it, and much much more. They\'ve also got

the original technique from the original

designer Jeffrey Huntley in here with

some of the information. And they\'ve got

another version in here as well, which

is the orchestrator, which is definitely

worth a read because it just enhances

some of the features that the normal

version of RAM also includes. So to get

it installed in this case, I\'m going to

come across to VS Code just to show you

all the different files and everything

for the app we\'re developing. We\'re

going to do claude in our terminal just

to start up the process. And now we need

to go through and install the official

Ralph Wiggum plugin. So first, if you

haven\'t got the marketplace installed,

you\'ll need to come through and install

it with this command here. That will

just make sure that you can access all

of these different extra plugins that we

want to use. Next, we want to type this

command in here, which is going to

install the official plugin that we want

to use. We\'re going to say yes, we want

to install for us and we\'ll let that run

through. As you can see there, it\'s now

successfully installed. Now, we\'re going

to restart it. So, to restart it, we\'re

going to do forward slashexit. We\'re

just going to exit there. And now, as we

can see at the coming back through. So,

just for formatting, I\'m just going to

get up a new terminal for us to go

through. So, we\'ll do clawed. It\'s just

going to bring it back up for us as we

can see there. And now we\'ve got it all

installed and we can use it. Now to

check it\'s there, we\'re just going to do

plugins and list. So now we can see all

of the different plugins that are

installed. If we just come across, as we

can see here, we\'ve got the Ralph Loop

and Ralph Wiggums all installed, ready

to go. So if we just come back out of

here, so now we\'ll be able to start

going through and actually getting it to

produce our output. Now, as I mentioned

before, the PRD or product requirements

document is really important. So all of

this is going to be included in the

community. Again, all of the links, all

of the different commands, everything

can run through. But what I want to

showcase is just how much detail we

really need to go into explaining the

different user stories, what we want the

outcome to achieve, some of the

different elements involved. Again, I

just got Claude to do this quick example

here, but we really want to give it as

much information as possible. the

criteria is checking against everything

can hear so that when we let it run in

the background it\'s able to give us the

best possible output and as we can see

at the end there the completion

checklist. So the use case that I\'ve got

for us today is that we want to build a

complete AI opportunity management

dashboard. Think of this as like an

opportunity hopper if you\'ve used that

in industry before that helps businesses

track, evaluate, and prioritize AI

automation opportunities. As we can see

here, we\'re just going to get it to go

through and get the output. I\'ve just

said it\'s a demo just to make sure it

doesn\'t build it out too complex and

take forever. So, what we\'re now going

to do is just come to our terminal on

the right. Of course, we\'ve got this as

a reference document. So to use it in

the request, we\'re going to do a forward

slash because we\'re going to be

executing this within our code. As you

can see here, it\'s popped up, but just

to find it, you want to start typing

Ralph, and it will show you all of the

different commands in here. We\'re going

to be using the Ralph loop. So we want

to do tab, and it\'s going to bring it

into our terminal, into our command

face. Here we then need to add our

prompt, the number of iterations and the

completion text. We\'re going to paste

our request in here saying that we want

it to read our PRD document. And then we

want it to go through verify which order

it should start generating the output

in. It\'s got up to 25 iterations without

blockers. And we say that we want it to

confirm that dashboard is complete at

the end. And it\'s got a maximum of 35

iterations that it\'s able to do, i.e.

keep looping round until it helpfully

achieves the output. But something to

keep in mind is this is going to be

using a lot of your tokens. So again,

that\'s why you need more of those opus

plans to really get the output, but it\'s

a time tradeoff versus what this would

cost you to outsource it to developers

or your own time and everything like

this. So now we\'re happy with that.

We\'re just going to press enter and it\'s

going to start going through and

generating everything. As we can see

here, it\'s now reading that PR document

to confirm the requirements of what we

want it to achieve. And now it should

start going through and actually

iterating over and over again until we

get that output. So there we go. After 4

minutes to get back, we\'re going to say

run this local host. We\'ll just get it

through. Whilst it\'s doing that, on the

left hand side here, we can see all of

the HTML that for our app. So hopefully

that\'s ready to go. We\'ll say yes. So we

can check out what that response looks

like. Okay. So when I load it up, it

doesn\'t show me anything. So we do have

Debugging errors + design improvements

an error. So we do command option J. It

looks like we got some errors here. So

we\'re just going to copy this reference

one. Come back across to Cay and say I

have the current error. Please resolve

ASAP. We\'ll send this off. see if it\'s

able to go through and just update the

code. So then we can see it nice and

easily. Again, this is why we\'re

starting to have more of that scrum mast

role against this and anti-gravity and

many others. We\'re starting to get a few

changes that go through in the

background, but it\'s helping do a lot of

the heavy lifting. So let\'s come back

across. We\'ll just close this down and

refresh and see if it\'s now ready to go.

We\'re still getting errors. We\'ll just

come back and cross and say still

getting errors. We\'ll see if it can go

through and solve it for us. Okay, so it

says it\'s ready to go. We\'ll come back

and just test this out. And there we go.

It looks like we\'re all up and ready.

So, we\'ve got the camb board. We got the

portfolio priority matrix. So, it looks

like it thought it succeeded on a few of

those, but as we saw, it failed. So, as

we can see here, it looks like we can

move them all across nice and easily,

which is great. That\'s exactly what we

want. If we see the priority matrix, it

looks like we can open these all up nice

and easy. We\'ve got the calculator in

here. So, let\'s just change that to 45.

Yeah, it looks like everything\'s working

nice and as it should in the background.

If we come back across to the camb

board, add an opportunity. We\'ll say

plud and then code. We\'ll say that it\'s

going to be an operations priority.

We\'ll say hi. ROI will say that we spend

50 hours a week. We\'re £85 an hour, two

employees affected, and it\'s going to be

£2,000 to implement it. So, as we can

see there, it looks like everything\'s

working correctly. It looks like the

clause code said the ROI isn\'t

calculated. So, it looks like that\'s an

error. We\'ll just go through and top

that up, make sure that that\'s working

correctly. But then, as you can see,

they\'re able to get something set up

incredibly quickly. And it\'s getting

easier and easier to just iterate all of

these designs, improving the outputs as

much as possible. If we wanted our

design to look better, which we

definitely can, we\'ll come back across.

We\'ll just do forwards and then plugins.

And then another one that I\'ve got

installed that is really good is front

end designs as we can see here. So,

we\'ll just make sure that that\'s

installed on this version so that we can

use it. We can say using and then front

end designs please improve the design of

the dashboard into a black and gold

theme. So as we can see there it\'s going

through nice and quickly improving what

we want the output to be. Let\'s check

out that final result and see how it\'s

impacted it. There we go. It\'s all gone

through and updated everything cuz we

wanted to. So now if we refresh this we

should get a 10 times better looking

dashboard. And there we go. As we can

see straight away, I mean, it\'s not

100%. I would change some of the fonts.

I think anti-gravity is absolutely

nailing the design of some of their

dashboards in there as well. As we can

see, it\'s a little bit funky on the

right hand side here. It doesn\'t look

like these are distributed correctly for

the bar chart, but it does have all of

the information in there that we want

to. As we can see, we\'re able to get our

ideas set up incredibly quickly. And

again, Ralph Wiggum is just enabling us

to get through those iterations, the

user stories as much as possible. But

remember, the product requirements

document or PRD, really explaining what

you want the success criteria is just

the best thing to use across all of

these different tools regardless. Make

sure to comment down below if there\'s

anything else you\'d love us to build

with anti-gravity, NA10, Claude Code,

all of these different AI tools out

there. And make sure to come across to

the community if you want to get access

to all of the prompts, templates,

everything I\'ve used in this video, as

well as hundreds of other templates that

you can use with other businesses or

even your own business as well. And stay

tuned for more around AI automation and

have a great day.

All

From the series

16:16

32 Tricks to Level Up Claude Code in 16 Mins

Nat
