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

*Day 4:*   
Both parts were quite straightforward to me.   
My experience with grids is limited so the solution to traversing it is a bit overengineered. Once I realised that a simple coordinte offsetting approach would have sufficed my quite atomic functions have been laid out already. Similarly, I was very much conscious of having to rework most of my code for the previous day's problem so I tried to lay strong scalable foundations for whatever would await me at Part 2.  
Turns out Part 2 is actually not that complex, it required only to change the state of the grid based on the information gathered from traversing it. For this I challenged myself with some nested conditional list comprehension.  

*Day 5:*  
This day was a lot of fun. I had a really good time solving it and focusing on list comprehensions. Even if my approach needed to be amended due to the size of the data set this was a super valuable learning experience. As for part 2, merging intervals did not end up being as complex as it could have been especially that, by now I understood that due to the size of the input data, it needed to be fairly optimal.

*Day 6:*  
This day was an adventure. Part 1 was fairly straighforward and gave me a good opportunity to have fun wih list comprehensions. Now that I am familiar with zip(*list) that may not have been super necessary but it was really good practice.  
Part 2 proved to be too difficult to solve without help so I have decided not to share my code that gave me the solution at the end as it is mostly derivative. It has however given me amazing perspective and invaluable insight on how to handle similar problems in the future.  

*Day 7:*   
Reading tachyon manifolds and splitting rays were definitely not on my christmas list, but it was nevertheless a super fun gift. Once I figured out how to parse the input in a usable format the first part itself just asked to count up the number of times a ray is split. Once I have mapped the correct splittings, it was just a matter of counting.
For part 2, I decided to use combinatorics as there was no way that with such a large input file, mapping all possible alternate realities was going to be plausible. We know that every time a ray is split in two, it generates at least two additional realities. I decided to iterate through the already parsed diagram (so that I knew where the possible light splittings might happen) and for every split, counted up the alternate realities generated depending on the three positions above it (top left, top, and top right). Once I consolidated the logic the implementation was actually the easy bit.  


*Day 8:*  
This one has been a really challanging part 1 that took me a good few days to complete. I have never dealt with union-find data structures before so it has been a true treat to familiarize myself with such algotrithms. 
Fortunately, this has been a textbook example of that data structure, even part 2 only requiring minor modification to track whether a union merge has occured and then counting it up which made it easier for me apply what I had learned online.
Today has also allowed me to get to know combinations a little bit, a fantastic library that I am excited to use in the future as its use cases seem unbounded. After creating tuples of the all possible box index combinations and calculating the distance between them came the hard part. Keeping track of joint circuits and merging them if necessary. 
Advent of Code is such a great tool for learning these getting a deeper understanding.

*Day 9:*  
Similarly to day 6 today proved to be too much for me to handle. I ended up reaching for a lot of hints and ideas from external sources to solv this problem, and because of that I will not be sharing it, as it would be mostly derivative.
Part 1 one was simple enough and I could handle the large input dataset just by treting it as a grid, and finding the topmost left and bottom right red tiles and calculating the area between them.  
For Part 2 unfortunately, this approach is too inefficient. I had the idea of using flood fill which I implemented, however, as it was still working on the full grid, it would have taken hours to run through the entire input. This was the point where I relented and used an approach I have seen using coordinate compression and breaking it further down into line segments to identify walls the traversing can't cross. From here flood fill proved useful enough to identify outside points and constructing a check for a what rectangles are inside the polygon ultimately gave the answer.  

|*Final words:*  
I believe that having failed to complete 2 seperate challenges so far has made this a perfect stopping point. For my personal growth and development it is be better to focus on previous years' Advent of Code and give them a go - which is what I will be doing. It will add more to my toolbox and challenge me more, than some problems where I am just not versed enough in data structures and algorithms to attempt. I am looking forward to coming back to the rest of this years' problems in the future and see what I can achieve once I have educated myself more.

--- Credits for creating Advent of Code ---

Puzzles, Code, & Design: Eric Wastl

Beta Testing:
Ben Lucek, JP Burke, Aneurysm9, Andrew Skalski

Community Managers: Danielle Lucek and Aneurysm9

