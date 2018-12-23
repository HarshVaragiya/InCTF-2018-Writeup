# Crypto - AuthRW Challenge 
# Attack & Defence Type 

## Crypto Specifications : 16 Bytes CBC Encryption,Decryption + 16 bytes IV 

Service seems simple at first, you can either generate a cookie or use a cookie.

# data = "username=admin:role=ordinary" + padding

# cookie = CBC.encrypt(data)

to get the flag(current one), we need to generate a cookie such that username=admin
and role is ordinary..

the catch is (obviously), if we try to generate a cookie with username=admin,
then cookie isn't generated! (lol)

so we need to Forge a cookie! (Just Kidding) 

the clue is in CBC Decryption Process..

after the CipherText is decrypted, it is XORed with the IV and we get plaintext

the key here is the way that the cookie is exported to the user!

my entered data-> username = admio (you'll know why, in a minute)

# cookie = IV[16 bytes] + encrypted data[32 bytes in my case]

as my username is admio, i get the cookie corresponding to that ..!
surely that won't give us the flag, but..! what you're forgetting is that IV is given.

in the decryption code, IV from the cookie is used to decrypt it and not the globally stored one
so that is out attack point...! [CBC Bit flipping attack kinda thingy]

as we can modify the IV, we can XOR the final plaintext with anything we want..!

so as username = admio -> 0x61646d696f -> so last o corresponds to : 0x6F - 01101111

and we need to modify it to admin -> 0x61646d6966e -> last n corresponds to : 0x6E - 01101110

so we need to flip the last bit in the plaintext "username=admio" to change the Plaintext!

"username=admio:role=ordinary" + padding

so we need to change IV such that IV2(modified) when XORed with Decrypted CT gives

"username=admin:role=ordinary" + padding

so we have to xor it with 0x010000 to changeg it (block size = 16 bytes )


iv2 = iv1(original)  ^ (normal plaintext ) ^ (required plaintext)

iv2 = iv1(original)  ^ 0x010000 (xor of required plaintext with put plaintext)


so doing that we can generate a cookie such that when decrypted on an unpatched system

it will give us the FLAG!!!


patch would involve checking the cookie iv with global iv to see if cookie is "poisoned"
and if it is.. connection is rejected!

attack code with auto-submitter is given! 

auto-submitter functionality is provided by a function sumbit_flag..!

# flag is submitted every 30 seconds  ¯\_(ツ)_/¯ SIMPLY!


Turns out that most teams could not even start the service because we had to generate 
keys to start the service (md5 hash of the key given on ctf thingy)...
they didn't see all files correctly! ... this wasn't much help there as we could not get many points
by exploiting this vulnerability ...
