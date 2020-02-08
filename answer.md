## Interview Questions

Explain in detail the workings of a dynamic array:
* What is the runtime complexity to access an array, add or remove from the front, and add or remove from the back?

  - Access -- array has an O(1).
  - Adding or removing -- from the front it's O(n) due to reindexing; from the back (i.e. at end of array) it's O(1) as it takes one step.


* What is the worse case scenario if you try to extend the storage size of a dynamic array?

   - Because it'll need to expand, this will be done in O(n) time.

Explain how a blockchain is structured. What are the blocks, what is the chain? How is the data organized?

- Blockchain is structured as a series of connected hash tables (blocks) containing a timestamp, a list of transactions, proof, and the hash of the previous block. When a next block is created, this data is hashed and stored within that block, thus chaining the blocks.
 
Explain how proof of work functions. How does it operate. How does this protect the chain from attack. What kind of attack is possible?

- A technique to combat attacks, for example illegally modifying a block's data. The proof of work takes a lot computation to solve -- uses the SHA-256 hashing function to create the hash of the previous block.
