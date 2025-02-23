# substitution0

| Information | Description |
| :-- | :-- |
| Category | Crypto |
| Difficulty | Medium |

# Problem Description

A message has come in but it seems to be all scrambled.
Luckily it seems to have the key at the beginning.
Can you crack this substitution cipher?
Download the message [here](https://artifacts.picoctf.net/c/154/message.txt).

> Hint: Try a frequency attack. An online tool might help.

# Solution

Instead of substitution method like caesar cipher, which shift certain steps to encode plaintext, substitution is another classic encoding approach. For substitution, each letter maps another letters without repetition. To solve such encoding scheme, I use an online word frequency analyzer, [quipqiup](https://www.quipqiup.com/). It's easy to figure out the flag!

Here is the result after analysis.

```text=
ABCDEFGHIJKLMNOPQRSTUVWXYZ Hereupon Legrand arose, with a grave and stately air, and brought me the beetle from a glass case in which it was enclosed. It was a beautiful scarabaeus, and, at that time, unknown to naturalists—of course a great prize in a scientific point of view. There were two round black spots near one extremity of the back, and a long one near the other. The scales were exceedingly hard and glossy, with all the appearance of burnished gold. The weight of the insect was very remarkable, and, taking all things into consideration, I could hardly blame Jupiter for his opinion respecting it. The flag is: picoCTF{5UB5717U710N_3V0LU710N_357BF9FF}
```

Besides, the message provides mapping at the beeginning of the text as problem description says.

:triangular_flag_on_post:: `picoCTF{5UB5717U710N_3V0LU710N_357BF9FF}`
