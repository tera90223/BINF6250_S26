# Introduction
This project implements the Neighbor-Joining algorithm to construct a phylogenetic tree from a set of sequences. Pairwise sequence distances are first calculated using the Smith-Waterman local alignment algorithm. The Neighbor-Joining algorithm iteratively joins pairs of nodes, creates internal nodes and calculates branch lengths. The final tree is converted to Newick format and visualized.

# Pseudocode

```
1. Read input sequences from FASTA file.

2. Store sequences in a dictionary mapping the sequence ID to the sequence string

3. Compute a distance matrix:
        For each pair of sequences (i, j):
            Align the sequences using the Smith-Waterman alignment.
            Trace back the optimal alignment.
            Compute the normalized Hamming distance between the aligned sequences.
            Store the distance in a distance matrix

4. Initialize a tree structure with each sequence as a leaf node.

5. While n > 2:
        Compute a Q-matrix using the current distance matrix.
        identify the pair of nodes (i, j) with the minimum Q value.
        Calculate the branch lengths from i and j to a new internal node k (di and dj respectively).
        Add the internal node k to the tree and connect it to i and j with the branch lengths (di and dj).
        Create a new matrix of size n-1.
        Copy the distances between the remaining nodes into the new matrix.
        Calculate and save the distances between the new node k and the remaining nodes into the new matrix.
        Update the distance matrix.
        Update the list of node labels.
        Update n -> n -= 1.

6. Convert the final tree structure into a Newick string format.

7. Plot the phylogenetic tree from the Newick string.


```

# Successes

Our group worked collaboratively to understand the Neighbor Joining algorithm by researching the concept and discussing it via an example as a team. Through this approach, we were able to differentiate between neighbor joining and other additive tree reconstruction methods grounding our overall understanding of phylogenetic tree construction. We also reused our previous Smith-Waterman algorithm and adapted it so that it returned distance scores instead of similarity scores for our analysis. 

# Struggles
We had two main struggles throughout the project, but working together and doing additional research, we were able to overcome them. First, we were pretty confused with the Neighbor-Joining algorithm shown in class. While conceptually we could follow the steps, we didn't quite grasp how internal nodes were created and how we should choose which leaf nodes were connected to it. This caused us to not be able to implement it, so we decided to do some research and find a different approach. We realized this was an additive phylogenetic approach, and found an alternative to the Neighbor-Joining, which calculated a Q-matrix and started with the closest leaf nodes (shorter distances in our matrix). We were able to map each step and understand how the nodes were being computed, which made it easier for us to implement, so we decided to go with this approach.

Secondly, we struggled with the tree traversal once it had been built to obtain a Newick string. Our first struggle here was understanding the Newick representation, as we hadn't heard of it before. Doing some outside research we were able to understand the syntax and representation. Most importantly, we were unsure of how to traverse the tree to create this string. We initially had a directed tree, where each node had parents and children. However, we realized that we needed an unrooted tree, where directionality was not necessary, so we changed our approach to simply keep track of neighbors (nodes to which our current node is connected to, regardless of the level). Our recursive call `_graph()` uses a depth-first search (DFS) approach, where we fully explore a path/subtree (go to the deepest level) before moving on to the next one. This function keeps track of the current node and the node we just came from, ensuring we don't "go backwards" when traversing. This was a hard approach to arrive to, as we understood the problem conceptually but were not sure how implement it. However, once we realize that we could keep track of what node we were coming from within the function (as parameter `came_from`), we arrived at an answer.

This was a challenging project to implement, where the conceptual understanding of the algorithm was easier to grasp (after team discussions and walk-throughs), and the implementation proved to be the main challenge. However, we were able to solve our issues as a team and arrive at a solution we were happy with. 
  

# Personal Reflections
## Group Leader
Chantera: For this project, our group did not follow the approach discussed in class. Instead, we conducted additional research on the neighbor joining algorithm and developed our own implementation using the pseudocode provided in the notebook. This challenged me to think more critically about the algorithm rather than simply following the approach taught in class. I also enjoyed the opportunity to implement a class without a given framework skeleton as it gave me a chance to strengthen my object-oriented programming skills. Lastly, I learned so much from Marcos and Meghana. They were great teammates and their input deepened my understanding.

## Other member
Marcos: As mentioned in the other reflections, we did not follow the algorithm discussed in class, as we were struggling to understand how to implement it in python. We did some research and found that what we had talked about in class referred to additive phylogentics, and found a similar (yet different) Neighbor-Joining algorithm. Discussing that as a team and walking through it step-by-step really helped me understand the calculations being done and how it all fit together. After discussing it as a team, I felt more confident about my understanding and ability to implement it. We were able to use some of our code from the previous dynamic programming project and adapt it for this. We had the chance to work with object-oriented programming and create our own classes, which was useful experience as I don't practice it that much. lastly, converting our tree to a Newick string for plotting was quite challenging. First, I was not familiar with this representation, so I had to do some research to understand how it worked. Second, the conversion forced us to think about how to traverse the tree recursively, respecting the appropriate node levels and branch lengths. This required some extensive researh and thinking, not only about the conceptual plan, but also about how to implement it. Nontheless, it was very rewarding to see a finalized graph and getting experience with recursion again. 


Meghana: The concept for this project was a little difficult for me to understand initially, particularly how the internal nodes of the tree were created based on the calculated distances and branch lengths. Our group spent a lot of time discussing the algorithm and we spent a significant amount of time on the pseudocode, making sure each of us understood the process. Once I understood how it worked, the implementation was much simpler.

# Generative AI Appendix
As per the syllabus
