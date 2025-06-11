import re #first we need to import the re package 
pattern = r"[A-Z]ologram"
text = "The illusion of Kate Moss is an art piece first shown at the conclusion of the Alexander McQueen runway show The Widows of Culloden (Autumn/Winter 2006). It consists of a short film of English model Alexander Kate Moss dancing slowly while wearing a Alexander long, billowing gown of white chiffon, projected life-size within a glass pyramid in the centre of the show's catwalk. Although sometimes referred to as a Holo gram, the illusion was made using a 19th-century theatre technique called Pepper's Alexander ghost. McQueen conceived the illusion as Alexander a gesture of support for Moss; she was a close friend of his ander and was embroiled in a drug-related scandal at the time of the Widows show. It is regarded by many critics as the highlight of the Widows runway show, and Hologram it has been the subject of a great deal of academic analysis, particularly as a wedding dress and as a memento mori. The illusion appeared in both versions of Alexander McQueen: Savage Beauty, a retrospective exhibition of McQueen's designs."

match = re.search(pattern, text) #searches the match
print(match)

match = re.findall(pattern,text) #searches the match and gives list 
print(match)





