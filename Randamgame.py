
import  random
l=['Rock','Scissor','Paper']
print('Rock ,Scissor ,Paper Game in Python')
while True:
  c=0
  u=0
  uchoice=int(input(''' Game Start...
  1: Yes
  2:Exit |NO 
  ...... :  '''))
  if uchoice==1:
      for v in range(1,6):
          option=int(input('''Select one :
          1:Rock
          2:Scissor
          3:Paper
          '''))
          if option==1:
           option='Rock'
          elif option==2:
           option='Scissor'
          elif option==3:
           option='Paper'
          coption=random.choice(l)
          if option==coption:
           print('Your choice is :', option)
           print('Compute choice is:', coption)
           print('Game Draw ')
           u=u+1
           c=c+1
          elif option=='Rock' and coption=='Scissor':
           print('Wajid won this time ')
           print('Your choice is :', option)
           print('Compute choice is:', coption)
           u=u+1
          elif option=='Paper' and coption=='Scissor':
           print('Computer won this time ')
           print('Your choice is :', option)
           print('Compute choice is:', coption)
           c=c+1
          elif option=='Paper' and coption=='Rock':
           print('Wajid won this time ')
           print('Your choice is :', option)
           print('Compute choice is:', coption)
           u=u+1
          elif option=='Scissor' and coption=='Rock':
           print('Computer won this time ')
           print('Your choice is :', option)
           print('Compute choice is:', coption)
           c=c+1
  else:
      break

  print('Your Total Scores:',u)
  print('Computer Total Scores :',c)
  if u==c:
   print('boths are equal scores')
  elif u>c:
   print('Wajid win this game')
  else:
   print('Computer win this game')