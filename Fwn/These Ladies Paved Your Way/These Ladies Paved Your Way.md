# These Ladies Paved Your Way

## Description

Per womenintech.co.uk, these 10 women paved your way as technologists. One of them holds more than 100 issued patents and is known for writing understandable textbooks about network security protocols. What other secrets does she hold?

Author: Clearedge

### Files

[WomenInTech.zip](./WomenInTech.zip)

## Approach

First let's extract all the images. Personally I like using [7zip](https://www.7-zip.org) because CTFs like putting in hidden files :(

If we search up "radia perlman patents" on Google, it says she holds over 100 U.S. patents (it didn't say this for any of the other names).

If we do `cat radia_perlman.jpg|strings` ([here](./radia_perlman.jpg)'s the image by the way) there are two lines of interest:

```text
U3Bhbm5pbmdUcmVlVmlnCg==
VpwtPBS{r0m5 0W t4x3IB5}
```

The first string is [base64](https://en.wikipedia.org/wiki/Base64) which we can decode with [this site](https://www.base64decode.org/). `U3Bhbm5pbmdUcmVlVmlnCg==` is `SpanningTreeVig`. "Vig" is the first 3 characters of "Vigenere" which is a plausible cipher.

`VpwtPBS{r0m5 0W t4x3IB5}` can be decoded with [Vigenere cipher](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher) using `SpanningTreeVig` as the key.

Decoded flag [here](https://gchq.github.io/CyberChef/#recipe=Vigen%C3%A8re_Decode('SpanningTreeVig')&input=VnB3dFBCU3tyMG01IDBXIHQ0eDNJQjV9)

## Flag

DawgCTF{l0t5 0F p4t3NT5}
