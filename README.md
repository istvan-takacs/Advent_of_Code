***Advent of Code 2025***

 This is a documentation of my journey and development through the problem set being released by the wonderful people behind Advent of code (full credits to them down below). This is only intended to be a journal of my progress through the 12 fun problems, adnd the takeaway lessons learned through it.

**Notes:**

*Day 1:* 
Quite a challenging problem especially with the second part. So many cases to consider with the turning of the dial accounting for all the edge cases. Once my approach was consolidated, the actual solution manifested itself in a fairly straightforward way.

*Day 2:*
I have been putting off learning RegEx for ages, so I was super excited once this problem gave me an excuse to dip my toes into that world as well. After having worked my way through a few tutorials on it, the problem itself turned out to be quite straightforward.  
I understand that string manipulation may have been a lot faster and more optimised perfoarmance-wise, however I wanted to challenge myself. This also allowed for a super easy Part 2.

*Day 3:*
Part 1 of this challenge was actually quite straightforward. I selected the largest digit from the string and then constructed all possible combinations with every other digit in the array that result in 2 digit number and just taken the maximum of that. Finally, added it all up into a sum.  
Part 2 proved to be quite a challenge, since I needed to completely reconsider my approach to this problem to handle 12 digits. I first thought to get a non-strictly decreasing subsequence of 12, but unfortunately not all the numbers can produce a subsequence like that.   
My second approach tried brute-forcing it and filtering through all the generated subsequences, but that was way too inefficient.   
Lastly, I constructed an approach that dynamically keeps track of the length of the remaining string that we can choose our next digit from based on how many elements there are in the initial and output arrays. Iteratively sliding this window, makes sure that the subsequence is going to be the largest possible one. I was quite proud of this solution at the end, though admittedly it took a very long time to come up with it.  


--- Credits for creating Advent of Code ---

Puzzles, Code, & Design: Eric Wastl

Beta Testing:
Ben Lucek, JP Burke, Aneurysm9, Andrew Skalski

Community Managers: Danielle Lucek and Aneurysm9

