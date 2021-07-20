

usermsg = input("tell me about how you're feeling. \n \n")

etcanswers = [
  "I see, thank you for having the courage to tell a stranger like me about you emotions.", "how fascinating!", "i'm sorry to hear that.", "tell me more...", "thanks for sharing.", "that's unfortunate.", "how wonderful!", "are you with anybody?", ]
tenseDict = {
  "i":"you",
  "am":"are",
  "my":"your",
  "you":"i",
  "are":"am",
  "your":"my"}
pronouns = [
  "i", "am", "my", "you", "are", "your"
]


def matchRule(rule, usermsg):
  rule = rule.split(' ')
  ruleIndex = 0
  wildcard = ""
  wildcards = []
  
  for sentIndex in range(len(usermsg)):
  
    #rule matches * position
    if rule[ruleIndex] == "*":
      
      #if end of rule
      if ruleIndex == len(rule) - 1:
        wildcard += ' '.join(usermsg[sentIndex:])
        wildcards.append(wildcard.strip())
        break

      #if current usermsg is the next literal in rule
      elif usermsg[sentIndex] == rule[ruleIndex + 1]:
        #wildcard is done, so is next literal 
        wildcards.append(wildcard.strip())
        wildcard = ""
        ruleIndex += 2 #next literal
     
      else: # matches wildcard again
        #add to wildcard purgatory
        wildcard += usermsg[sentIndex] + ' '
    
    #word matches rule
    elif usermsg[sentIndex] == rule[ruleIndex]:
      ruleIndex += 1 
  
    #word doesnt match rule
    elif not usermsg[sentIndex] == rule[ruleIndex]:
      return None 
  
  if ruleIndex >= len(rule)-1:
    return wildcards
  else:
    return None

while usermsg != "exit":
  usermsg = usermsg.split(' ')

	# matching using matchRule
  responses = { #wc = matchRule output wildcards
    "i am *" : lambda wc: "Why are you " + wc[0], 
    "i want *" : lambda wc: "how can you get " + wc[0],
		"you are *" : lambda wc: "What makes you think that I am " + wc[0],
    "are you *" : lambda wc: "it is always possible that i am " + wc[0],
    "life is *" : lambda wc: "How long has life been " + wc[0],
    "i want to *" : lambda wc: "how can you " + wc[0],
    "i am with *" : lambda wc: "do you like " + wc[0],
    "i am * today" : lambda wc: "were you " + wc[0] + " yesterday",
    "i am * because *" : lambda wc: "Are you always " + wc[0] + " when " + wc[1], 
	}

  for rule in responses.keys():
    result = matchRule(rule, usermsg)

 
    if result != None:
      for element in result:
        if " " in element: 
          pass
  usermsg = input()
