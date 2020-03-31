def find_best(weight):
  if weight <=2:
    cost1 = weight*1.50+20
    cost2 = weight*4.5
    cost3 = 125
    if cost1<cost2 and cost1<cost3:
      best_option= "The cheapest way to ship" + str(weight)+ "pound package is using ground shipping and it will cost $"+str(cost1)+"."
      return best_option
    elif cost2<cost1 and cost2<cost3:
      best_option1 = "The cheapest way to ship" + str(weight)+ " pound package is using Drone shipping and it will cost $"+str(cost2)+"."
      return best_option1
    elif cost3<cost1 and cost3<cost1:
      best_option2 = "The cheapest way to ship" + str(weight)+ "pound package is using Drone shipping and it will cost $"+str(cost3)+"."
      return best_option2
    else:
      print ("ERRorrr")
  elif weight <=6:
    cost1 = weight*3+20
    cost2 = weight*9
    cost3 = 125  
    if cost1<cost2 and cost1<cost3:
      best_option= "The cheapest way to ship" + str(weight)+ "pound package is using ground shipping and it will cost $"+str(cost1)+"."
      return best_option
    elif cost2<cost1 and cost2<cost3:
      best_option1 = "The cheapest way to ship" + str(weight)+ " pound package is using Drone shipping and it will cost $"+str(cost2)+"."
      return best_option1
    elif cost3<cost1 and cost3<cost1:
      best_option2 = "The cheapest way to ship" + str(weight)+ "pound package is using Drone shipping and it will cost $"+str(cost3)+"."
      return best_option2
    else:
      print ("ERRorrr")
  elif weight <=10:
    cost1 = weight*4+20
    cost2 = weight*12
    cost3 = 125
    if cost1<cost2 and cost1<cost3:
      best_option= "The cheapest way to ship" + str(weight)+ "pound package is using ground shipping and it will cost $"+str(cost1)+"."
      return best_option
    elif cost2<cost1 and cost2<cost3:
      best_option1 = "The cheapest way to ship" + str(weight)+ " pound package is using Drone shipping and it will cost $"+str(cost2)+"."
      return best_option1
    elif cost3<cost1 and cost3<cost1:
      best_option2 = "The cheapest way to ship" + str(weight)+ "pound package is using Drone shipping and it will cost $"+str(cost3)+"."
      return best_option2
    else:
      print ("ERRorrr")
  else :
    cost1 = weight*4.75+20
    cost2 = weight*14.25
    cost3 = 125
    if cost1<cost2 and cost1<cost3:
      best_option= "The cheapest way to ship" + str(weight)+ "pound package is using ground shipping and it will cost $"+str(cost1)+"."
      return best_option
    elif cost2<cost1 and cost2<cost3:
      best_option1 = "The cheapest way to ship" + str(weight)+ " pound package is using Drone shipping and it will cost $"+str(cost2)+"."
      return best_option1
    elif cost3<cost1 and cost3<cost1:
      best_option2 = "The cheapest way to ship" + str(weight)+ "pound package is using Drone shipping and it will cost $"+str(cost3)+"."
      return best_option2
    else:
      print ("ERRorrr")
#test 
print (find_best(41.25))
