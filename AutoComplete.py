class TrieNode(): 
	def __init__(self): 
		self.children = {} 
		self.last = False

class Trie(): 
	def __init__(self): 
		self.root = TrieNode() #initialising the trie. 
		self.word_list = [] 

	def formTrie(self, keys): 
		for key in keys: 
			self.insert(key) #inserting one key to the trie. 

	def insert(self, key):  
		node = self.root 

		for a in list(key): 
			if not node.children.get(a): 
				node.children[a] = TrieNode() 

			node = node.children[a] 

		node.last = True

	def search(self, key): 
		node = self.root 
		found = True

		for a in list(key): 
			if not node.children.get(a): 
				found = False
				break
			node = node.children[a] 
		return node and node.last and found 

	def suggestionsRec(self, node, word): #recursively find suggestion and append to the world_list
		if node.last: 
			self.word_list.append(word) 

		for a,n in node.children.items(): 
			self.suggestionsRec(n, word + a) 

	def printAutoSuggestions(self, key): 
		node = self.root 
		not_found = False
		temp_word = '' 

		for a in list(key): 
			if not node.children.get(a): 
				not_found = True
				break

			temp_word += a 
			node = node.children[a] 

		if not_found: 
			return 0
		elif node.last and not node.children: 
			return -1

		self.suggestionsRec(node, temp_word) 

		for s in self.word_list: 
			print(s) 
		return 1

 
keys = input("Enter list of words: ").split() 
key = input("Enter key value to find suggestions: ") 
status = ["Not found", "Found"] 

t = Trie()  
t.formTrie(keys) 
comp = t.printAutoSuggestions(key) 

if comp == -1: 
	print("No other strings found with this prefix\n") 
elif comp == 0: 
	print("No string found with this prefix\n") 

