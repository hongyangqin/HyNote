
Example #4 — Replacing in multiple strings (high performance)
If you have the same replacements and need to perform those operations on many different documents, it can make sense to initialize a Replacer, which will be much faster when used repeatedly. The reason it’s faster is it builds a trie structure under the hood that it keeps in memory, and that structure can be used repeatedly.

# 文档

Search and Replace Strings in Golang — Top 5 Examples

https://medium.com/qvault/search-and-replace-strings-in-golang-top-5-examples-8116a19a15ce