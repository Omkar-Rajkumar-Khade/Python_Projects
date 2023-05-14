# import necessary libraries
from typing import List, Dict
import tkinter as tk
import requests
import nltk

# download corpus if not already present
nltk.download('words')

# define the structure of Trie node
class TrieNode:
    def __init__(self):
        self.isEndOfWord = False # flag to indicate if the node represents the end of a word
        self.children = {} # dictionary of children nodes for the current node, with key as the character and value as the child node pointer

# function to insert a word into the Trie
def insert(root: TrieNode, word: str) -> None:
    node = root

# iterate over each character in the word
    for ch in word:
        # if the current character is not a child of the current node, create a new child node for it
        if ch not in node.children:
            node.children[ch] = TrieNode()

        # move the node pointer to the child node for the current character
        node = node.children[ch]

    # mark the final node as the end of a word
    node.isEndOfWord = True

# function to search for a word in the Trie
def search(root: TrieNode, word: str) -> bool:
    node = root

    # iterate over each character in the word
    for ch in word:
        # if the current character is not a child of the current node, the word is not in the Trie
        if ch not in node.children:
            return False

        # move the node pointer to the child node for the current character
        node = node.children[ch]

    # return True if the final node is marked as the end of a word, False otherwise
    return node.isEndOfWord

# function to recursively suggest words in the Trie starting with a given prefix
def suggest(root: TrieNode, prefix: str, suggestions: List[str]) -> None:
    # if the current node represents the end of a word, add the prefix to the list of suggestions
    if root.isEndOfWord:
        suggestions.append(prefix)

    # if the current node has no children, return
    if len(root.children) == 0:
        return

    # iterate over each child node of the current node
    for ch, child in root.children.items():
        # recursively suggest words starting with the current child node and update the prefix
        suggest(child, prefix + ch, suggestions)

# function to get a list of suggestions for a given prefix
def autoSuggest(root: TrieNode, prefix: str) -> List[str]:
    suggestions = []

    node = root

    # iterate over each character in the prefix
    for ch in prefix:
        # if the current character is not a child of the current node, there are no suggestions for the prefix
        if ch not in node.children:
            return suggestions

        # move the node pointer to the child node for the current character
        node = node.children[ch]

    # recursively suggest words starting with the final node for the prefix and add them to the list of suggestions
    suggest(node, prefix, suggestions)

    return suggestions

def main():
    # create the root node of the Trie
    root = TrieNode()

    # insert words from dictionary list into Trie
    # dictionary = ["apple", "amazon", "awesome", "banana", "book", "orange", "graph", "lemon", "leaf", "Rishab"]
    # get list of words from dictionary
    dictionary = nltk.corpus.words.words()
    for word in dictionary:
        insert(root, word.lower())

    # create GUI
    window = tk.Tk()
    window.title("Auto Suggest")

    # create labels and entry box
    label1 = tk.Label(window, text="Enter prefix:")
    label1.grid(row=0, column=0)

    entry1 = tk.Entry(window)
    entry1.grid(row=0, column=1)

    label2 = tk.Label(window, text="Suggestions:")
    label2.grid(row=1, column=0)

    output = tk.Text(window, height=20, width=30)
    output.grid(row=1, column=1)

    
    # function to handle button click event and display suggestions
    def suggestWords():
        prefix = entry1.get()
        suggestions = autoSuggest(root, prefix)
        output.delete(1.0, tk.END)
        if len(suggestions) == 0:
            output.insert(tk.END, "No suggestions found for the prefix: " + prefix)
        else:
            for suggestion in suggestions:
                output.insert(tk.END, suggestion + "\n")


    # create button to trigger suggestion
    button1 = tk.Button(window, text="Suggest", command=suggestWords)
    button1.grid(row=2, column=1)

    window.mainloop()
if __name__ == '__main__':
    main()
