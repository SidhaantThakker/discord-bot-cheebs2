# bot.py
import os
import discord
import praw
import TTTAI
import PlayTTT
import copy
import random
from dotenv import load_dotenv

load_dotenv()

client = discord.Client()


TOKEN = os.environ.get("bot-token")


reddit = praw.Reddit(
    client_id=os.environ.get("client-id"),
    client_secret=os.environ.get("client-secret"),
    user_agent=os.environ.get("user-agent"),
)


@client.event
async def on_message(message):

    if message.author == client.user:
        return

    print(message.author.display_name + " : " + message.content)

    if message.content.startswith("$help"):
        await message.channel.send(
            "Cheebs here, I'm kinda new and don't know nobody, for now I just fetch reddit posts and play TicTacToe, use $reddithelp to learn more and $tictactoe to play"
        )

    elif message.content.startswith("$reddithelp"):
        helperText = (
            "So,%s you need help, and where do you come? Crawling back to me. \n Here's the lowdown - \n $reddit {subredditname} {top/hot/new/rising/controversial/gilded} {number of posts} \n $reddit {subredditname} {topnth/hotnth/newnth/risingnth/controversialnth/gildednth} {post at nth position}"
            % (message.author.mention)
        )
        await message.channel.send(helperText)

    # reddit stuff

    elif message.content.startswith("$reddit"):

        reddit = praw.Reddit(
            client_id=os.environ.get("client-id"),
            client_secret=os.environ.get("client-secret"),
            user_agent=os.environ.get("user-agent"),
        )
        sub = "cats"
        type = "top"
        lim = 1
        li = message.content.split()
        print(li[0])
        if len(li) > 1:
            print(li[1])
            sub = li[1]
        if len(li) > 2:
            print(li[2])
            type = li[2]
        if len(li) > 3:
            print(li[3])
            lim = int(li[3])

        if type == "top":
            for submission in reddit.subreddit(sub).top(limit=lim):
                if len(submission.selftext) <= 2000:
                    embed = discord.Embed(
                        title=submission.title, description=submission.selftext
                    )
                else:
                    embed = discord.Embed(
                        title=submission.title,
                        description="That post is way too long and I'm not typing out all of it, here's a link - "
                        + submission.shortlink,
                    )

                imgFlag = not submission.is_self
                if imgFlag:
                    embed.set_image(url=submission.url)

                print(submission.shortlink)
                await message.channel.send(embed=embed)

        if type == "new":
            for submission in reddit.subreddit(sub).new(limit=lim):
                if len(submission.selftext) <= 2000:
                    embed = discord.Embed(
                        title=submission.title, description=submission.selftext
                    )
                else:
                    embed = discord.Embed(
                        title=submission.title,
                        description="That post is way too long and I'm not typing out all of it, here's a link - "
                        + submission.shortlink,
                    )

                imgFlag = not submission.is_self
                if imgFlag:
                    embed.set_image(url=submission.url)

                print(submission.shortlink)
                await message.channel.send(embed=embed)

        if type == "hot":
            for submission in reddit.subreddit(sub).hot(limit=lim):
                if len(submission.selftext) <= 2000:
                    embed = discord.Embed(
                        title=submission.title, description=submission.selftext
                    )
                else:
                    embed = discord.Embed(
                        title=submission.title,
                        description="That post is way too long and I'm not typing out all of it, here's a link - "
                        + submission.shortlink,
                    )

                imgFlag = not submission.is_self
                if imgFlag:
                    embed.set_image(url=submission.url)

                print(submission.shortlink)
                await message.channel.send(embed=embed)

        if type == "topnth":
            submission = list(reddit.subreddit(sub).top(limit=lim))[lim - 1]
            if len(submission.selftext) <= 2000:
                embed = discord.Embed(
                    title=submission.title, description=submission.selftext
                )
            else:
                embed = discord.Embed(
                    title=submission.title,
                    description="That post is way too long and I'm not typing out all of it, here's a link - "
                    + submission.shortlink,
                )

            imgFlag = not submission.is_self
            if imgFlag:
                embed.set_image(url=submission.url)

            print(submission.shortlink)
            await message.channel.send(embed=embed)

        if type == "newnth":
            submission = list(reddit.subreddit(sub).new(limit=lim))[lim - 1]
            if len(submission.selftext) <= 2000:
                embed = discord.Embed(
                    title=submission.title, description=submission.selftext
                )
            else:
                embed = discord.Embed(
                    title=submission.title,
                    description="That post is way too long and I'm not typing out all of it, here's a link - "
                    + submission.shortlink,
                )

            imgFlag = not submission.is_self
            if imgFlag:
                embed.set_image(url=submission.url)

            print(submission.shortlink)
            await message.channel.send(embed=embed)

        if type == "hotnth":
            submission = list(reddit.subreddit(sub).hot(limit=lim))[lim - 1]
            if len(submission.selftext) <= 2000:
                embed = discord.Embed(
                    title=submission.title, description=submission.selftext
                )
            else:
                embed = discord.Embed(
                    title=submission.title,
                    description="That post is way too long and I'm not typing out all of it, here's a link - "
                    + submission.shortlink,
                )

            imgFlag = not submission.is_self
            if imgFlag:
                embed.set_image(url=submission.url)

            print(submission.shortlink)
            await message.channel.send(embed=embed)

        if type == "rising":
            for submission in reddit.subreddit(sub).rising(limit=lim):
                if len(submission.selftext) <= 2000:
                    embed = discord.Embed(
                        title=submission.title, description=submission.selftext
                    )
                else:
                    embed = discord.Embed(
                        title=submission.title,
                        description="That post is way too long and I'm not typing out all of it, here's a link - "
                        + submission.shortlink,
                    )

                imgFlag = not submission.is_self
                if imgFlag:
                    embed.set_image(url=submission.url)

                print(submission.shortlink)
                await message.channel.send(embed=embed)

        if type == "controversial":
            for submission in reddit.subreddit(sub).controversial(limit=lim):
                if len(submission.selftext) <= 2000:
                    embed = discord.Embed(
                        title=submission.title, description=submission.selftext
                    )
                else:
                    embed = discord.Embed(
                        title=submission.title,
                        description="That post is way too long and I'm not typing out all of it, here's a link - "
                        + submission.shortlink,
                    )

                imgFlag = not submission.is_self
                if imgFlag:
                    embed.set_image(url=submission.url)

                print(submission.shortlink)
                await message.channel.send(embed=embed)

        if type == "risingnth":
            submission = list(reddit.subreddit(sub).rising(limit=None))[lim - 1]
            if len(submission.selftext) <= 2000:
                embed = discord.Embed(
                    title=submission.title, description=submission.selftext
                )
            else:
                embed = discord.Embed(
                    title=submission.title,
                    description="That post is way too long and I'm not typing out all of it, here's a link - "
                    + submission.shortlink,
                )

            imgFlag = not submission.is_self
            if imgFlag:
                embed.set_image(url=submission.url)

            print(submission.shortlink)
            await message.channel.send(embed=embed)

        if type == "controversialnth":
            submission = list(reddit.subreddit(sub).controversial(limit=None))[lim - 1]
            if len(submission.selftext) <= 2000:
                embed = discord.Embed(
                    title=submission.title, description=submission.selftext
                )
            else:
                embed = discord.Embed(
                    title=submission.title,
                    description="That post is way too long and I'm not typing out all of it, here's a link - "
                    + submission.shortlink,
                )

            imgFlag = not submission.is_self
            if imgFlag:
                embed.set_image(url=submission.url)

            print(submission.shortlink)
            await message.channel.send(embed=embed)

        if type == "gilded":
            for submission in reddit.subreddit(sub).gilded(limit=lim):
                if len(submission.selftext) <= 2000:
                    embed = discord.Embed(
                        title=submission.title, description=submission.selftext
                    )
                else:
                    embed = discord.Embed(
                        title=submission.title,
                        description="That post is way too long and I'm not typing out all of it, here's a link - "
                        + submission.shortlink,
                    )

                imgFlag = not submission.is_self
                if imgFlag:
                    embed.set_image(url=submission.url)

                print(submission.shortlink)
                await message.channel.send(embed=embed)

        if type == "gildednth":
            submission = list(reddit.subreddit(sub).gilded(limit=None))[lim - 1]
            if len(submission.selftext) <= 2000:
                embed = discord.Embed(
                    title=submission.title, description=submission.selftext
                )
            else:
                embed = discord.Embed(
                    title=submission.title,
                    description="That post is way too long and I'm not typing out all of it, here's a link - "
                    + submission.shortlink,
                )

            imgFlag = not submission.is_self
            if imgFlag:
                embed.set_image(url=submission.url)

            print(submission.shortlink)
            await message.channel.send(embed=embed)

    # TicTacToe
    global TheBoard
    X = "X"
    O = "O"
    M = None
    whee = ""
    end = False
    intro = "Tic Tac Toe board initialized \n start messages directly with $move, and enter move as follows \n use 0, 1, 2, 3, 4 ... \n or 00, 01, 02, 10, 11 ..."

    if message.content.startswith("$tictactoe"):
        TheBoard = TTTAI.ini_board()
        await message.channel.send(intro)

    if message.content.startswith("$move"):
        user = message.content[6:8]
        inp = PlayTTT.conv(user)
        p = int(inp[0])
        q = int(inp[1])
        if not PlayTTT.canplay(copy.deepcopy(TheBoard), p, q):
            await message.channel.send("Illegal")
            return
        TheBoard[p][q] = X

        end = TTTAI.terminal(copy.deepcopy(TheBoard))
        if end:
            embed = discord.Embed(
                title="Tic Tac Toe",
                description=" " + PlayTTT.dispdiscy(copy.deepcopy(TheBoard)),
            )
            embed.colour = random.randint(0, 16777215)
            await message.channel.send(embed=embed)
            if TTTAI.winner(TheBoard) == X:
                whee = "X wins"
            elif TTTAI.winner(TheBoard) == O:
                whee = "O wins"
            else:
                whee = "Tie"
            await message.channel.send(whee)
            return

        AI = random.choice(TTTAI.minimax(copy.deepcopy(TheBoard)))
        p = AI[0]
        q = AI[1]
        TheBoard[p][q] = O
        print(PlayTTT.dispdiscy(copy.deepcopy(TheBoard)))
        end = TTTAI.terminal(copy.deepcopy(TheBoard))
        if end:
            embed = discord.Embed(
                title="Tic Tac Toe",
                description=" " + PlayTTT.dispdiscy(copy.deepcopy(TheBoard)),
            )
            embed.colour = random.randint(0, 16777215)
            await message.channel.send(embed=embed)
            if TTTAI.winner(TheBoard) == X:
                whee = "X wins"
            elif TTTAI.winner(TheBoard) == O:
                whee = "O wins"
            else:
                whee = "Tie"
            await message.channel.send(whee)
            return
        embed = discord.Embed(
            title="Tic Tac Toe",
            description=" " + PlayTTT.dispdiscy(copy.deepcopy(TheBoard)),
        )
        embed.colour = random.randint(0, 16777215)
        await message.channel.send(embed=embed)


@client.event
async def on_ready():
    print(f"{client.user} has connected to {client.guilds[0].name}!")


client.run(TOKEN)
