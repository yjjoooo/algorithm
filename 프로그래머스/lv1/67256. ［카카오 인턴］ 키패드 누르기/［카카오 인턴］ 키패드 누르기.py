class Hand():
    def __init__(self):
        self.left = [0, 0]
        self.right = [2, 0]
    
    def move_left(self, location, answer):
        self.left = location
        answer += 'L'
        
        return answer
    
    def move_right(self, location, answer):
        self.right = location
        answer += 'R'
        
        return answer
    
    def location_left(self):
        return self.left
    
    def location_right(self):
        return self.right

def location(num):
    if num == 0:
        return [1, 0]
    
    x, y = 0, 0
    
    if num % 3 == 0:
        x = 2
    elif num % 3 == 1:
        x = 0
    elif num % 3 == 2:
        x = 1
    else:
        print('Error')
        
    if num <= 3:
        y = 3
    elif num <= 6:
        y = 2
    elif num <= 9:
        y = 1
    
    return [x, y]

def get_distance(l, d):
    a = abs(l[0] - d[0])
    b = abs(l[1] - d[1])
    
    return a + b

def solution(numbers, hand):
    answer = ''
    _hand = Hand()
    
    for number in numbers:
        destination = location(number)
        
        if number in [1, 4, 7]:
            answer = _hand.move_left(destination, answer)
        elif number in [3, 6, 9]:
            answer = _hand.move_right(destination, answer)
        elif number in [2, 5, 8, 0]:
            lh_distance = get_distance(_hand.location_left(), destination)
            rh_distance = get_distance(_hand.location_right(), destination)
            
            if lh_distance < rh_distance:
                answer = _hand.move_left(destination, answer)
            elif lh_distance > rh_distance:
                answer = _hand.move_right(destination, answer)
            elif lh_distance == rh_distance:
                if hand == 'left':
                    answer = _hand.move_left(destination, answer)
                elif hand == 'right':
                    answer = _hand.move_right(destination, answer)
                else:
                    print('Error')
            else:
                print('Error')
    
    return answer