import math
    
def FindBall(balls, num_iterations):
    
    try:
        if balls[0] == balls[1]:
            print('We weigh the balls: ' + str(balls[0]) + ' and ' + str(balls[1]))
    except:
        pass
        
    for num_balls in balls:
        
        # The end of recursion
        if num_iterations == 0:
            print('NEXT ---->')
            return True     
        
        print('The number of balls: ' + str(num_balls) + ', The number of remaining iteration: '  + str(int(num_iterations)))
        
        # Math part
        previous_degree = num_iterations - 1
        divider = 3**previous_degree
        num_dividers = num_balls // divider
        rest = num_balls % divider
        result = [int(divider)] * int(num_dividers)
        
        if not rest == 0:
            result.append(rest)
            
        new_num_iterations = num_iterations-1
        
        print('Separation of balls: ' + str(result))
        print('----------------------')      
        
        # Recursion
        FindBall(result, new_num_iterations)


# Input
while True:
    num_balls = input('Enter the number of balls: ')
    if type(num_balls) == int:
        if num_balls > 1:
            break
        else:
            print('the number of balls must be > 1\n')
    else:
        print('The number of balls must be natural number!!!\n')
    
        

# Get number of min iterations
num_iterations = math.log(num_balls,3)

# Get the previous degree of 3
if num_iterations % 3 == 0:
    previous_degree = num_iterations - 1
else:
    previous_degree = int(str(num_iterations).split('.')[0])
    num_iterations = previous_degree + 1


# Output    
FindBall([num_balls], num_iterations)
print('We find it!!! Minimum number of weighings: ' + str(int(num_iterations)))