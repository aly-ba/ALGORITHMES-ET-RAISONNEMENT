Recherche( tab, val)
   pour de i de 0 a tab.taille -1
     si tab[i ] == val
	   retourner i
	 fin si 
   fin pour 
   retourner -1
fin Recherche
//recherche en python

def recherche(x):
  """ done l'indice ou se trouve la valeur de x dans (1 si n'existe pas)"""
  i=0
  while i <len(z) and s[i][0] !=x :
      i =i+1
	  si i == len(s):
	     i=-1   # pas trouvé
	retourn i
		 
	 
//recherche dichotomique
recherch(entier tab[], entier val, entier g, entier d) 
     pendant que (g<=d)
	    entier milieu = (g+d)/2
		si (tab[miliieu == val )
		   alors retourner milieu
		Fin si 
		si tab[milieu] <val 
		  alors g =milieu+1
		sinon 
		     d = milieu-1 
    Fin pendant que
	 retourner -1  
fin recherche


def recherche_dichotomique(s,x):
  """
      recherche dichotomique ou binaire de x dans s
      résultat:
           donne l'indice où se trouve la valeur de x dans s
           (-1 si n'existe pas)
  """
  bi, bs = 0, len(s)
  m = (bi+bs)//2
  while bi < bs and x != s[m][0]:
     m = (bi+bs)//2
     if s[m][0] < x:
        bi = m+1
     else:
        bs = m  # x est avant ou est trouvé

  if  len(s) <= m or s[m][0] != x:  # pas trouvé
      m = -1
  return m