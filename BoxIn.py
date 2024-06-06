class Maillon:

	def __init__(self, valeur, precedent=None, suivant=None):
		self.valeur = valeur
		self.precedent = precedent
		self.suivant = suivant


class File:

	def __init__(self):
		self.longueur = 0
		self.debut = None
		self.fin = None

	def enfiler(self, valeur):
		if self.longueur == 0:
			self.debut = self.fin = Maillon(valeur)
		else:
			self.fin = Maillon(valeur, self.fin)
			self.fin.precedent.suivant = self.fin
		self.longueur += 1


	def defiler(self):
		if self.longueur > 0:
			valeur = self.debut.valeur
			if self.longueur > 1:
				self.debut = self.debut.suivant
				self.debut.precedent = None
			else:
				self.debut = self.fin = None
			self.longueur -= 1
		return valeur


	def estVide(self):
		return self.longueur == 0






def bfs(G,s) :
	P = {s :None}
	Q = File()
	Q.enfiler(s)
	while not(Q.estVide()) :
		u = Q.defiler()
		for v in G[u] :
			if v in P : continue
			P[v]=u
			Q.enfiler(v)
	return P



G = { }
G['a'] = ['b','c']
G['b'] = ['a','d','e']
G['c'] = ['a','d']
G['d'] = ['b','c','e']
G['e'] = ['b','d','f','g']
G['f'] = ['e','g']
G['g'] = ['e','f','h']
G['h'] = ['g']
G['i'] = ['j','f','e']


P = bfs(G,'b')
print(P)