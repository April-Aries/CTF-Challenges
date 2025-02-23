# substitution2

| Information | Description |
| :-- | :-- |
| Category | Crypto |
| Difficulty | Medium |

# Problem Description

It seems that another encrypted message has been intercepted.
The encryptor seems to have learned their lesson though and now there isn't any punctuation!
Can you still crack the cipher? 
Download the message [here](https://artifacts.picoctf.net/c/113/message.txt).

> Hint: Try refining your frequency attack, maybe analyzing groups of letters would improve your results?

# Solution


Compared with substitution1, the message doesn't provide any blank space so that it's hard to tell common words like "the", "a", etc. However, it's okay if we do analysis on each character instead of using common words. Likewise, let's see the result from online word frequency analyzer.

```text=
there exist several other well established high school computer security competitions including cyber patriot and us cyber challenge these competitions focus primarily on systems administration fundamentals which are very useful and marketable skills however we believe the proper purpose of a high school computer security competition is not only to teach valuable skills but also to get students interested in and excited about computer science defensive competitions are often laborious affairs and come down to running checklists and executing config scripts offense on the other hand is heavily focused on exploration and improvisation and often has elements of play we believe a competition touching on the offensive elements of computer security is therefore a better vehicle for tech evangelism to students in american high schools further we believe that an understanding of offensive techniques is essential for mounting an effective defense and that the tools and configuration focus encountered in defensive competitions does not lead students to know their enemy as effectively as teaching them to actively think like an attacker pico c t f is an offensively oriented high school computer security competition that seeks to generate interest in computer science among high schoolers teaching them enough about computer security to pique their curiosity motivating them to explore on their own and enabling them to better defend their machines the flag is pico c t f n r m ny duff c
```

It seems that the flag is not recover well. This is due to digits inside the flag. Let me put on the digits and the puzzle is easily solved.

:triangular_flag_on_post:: `picoCTF{n6r4m_4n41y515_15_73d10u5_702f03fc}`
