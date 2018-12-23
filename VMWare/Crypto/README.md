# Crypto Challenge - RSA 

## Simple Question, uses Chinese Remainder Theorem.

3 x1024 bit RSA Keys are used to encrypt a message m (flag) with e = 3

All Keys have e = 3 -- VIMP

2x keys are provided straight forward, and one key (key3), is used to encrypt two other messages

m1 = "Best of luck for this challenge you will definitely need it"

and 

m2 = "Try harder, if you have trouble just google!!!"

and the cipher texts are given (c1 and c2 ) encrypted with Key3

then the flag string (m) is encrypted with keys 1,2,and 3 and ciphertexts
c1_flag , c2_flag , c3_flag are given!

as e = 3 , if we know n1,n2 and n3, we can use Chinese Remainder Theorem to get
the message m!

-> We need to find n3!



as two messages are given -> m1 and m2, we know that
 
1.c1 = (m1**e) % n3 , and
2.c2 = (m2**e) % n3 

so, as we know m1**3 and m2**3 

n31 = (m1**3) - c1 = n3 * a (for some a) 
n32 = (m2**3) - c2 = n3 * b (for some b)

... and c1 and c2, we can find n3 as n3 is clearly the GCD of the two(n31 and n32) 

n3 = GCD (n31,n32)

once we know n3 , n2 , n1 and encrypted cipher texts... we can use CRT to get flag directly!

using CRT code from : https://github.com/ashutosh1206/Crypton/blob/master/RSA-encryption/Attack-Hastad-Broadcast/hastad_unpadded.py

we get the flag as : inctf{H@5htaD_Br0adCa5t_@ft3r_R3tr1eving_M0dulu3_b3c0m3s_e@Sy}

Cool!

