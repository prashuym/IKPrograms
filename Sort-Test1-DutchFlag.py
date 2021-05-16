def dutch_flag_sort(balls):
    lenBalls = len(balls)
    # Green Flag is used as the iterator to move in one direction
    # Red Flag and BlueFlag are used to indicate the position where the next Red or Blue element should go.
    RedF = GreenF = 0
    BlueF = lenBalls - 1
    
    while (GreenF <= BlueF) :
        # print(RedF,balls[RedF], GreenF,balls[GreenF], BlueF,balls[BlueF], balls)
        if balls[GreenF] == 'B' :
            balls[GreenF], balls[BlueF] = balls[BlueF], balls[GreenF]
            BlueF -= 1
        elif balls[GreenF] == 'R' :
            balls[GreenF], balls[RedF] = balls[RedF], balls[GreenF]
            RedF += 1
            GreenF += 1
        elif balls[GreenF] == 'G':
            GreenF += 1

        # print(RedF,GreenF,BlueF,balls)
    return

if __name__ == "__main__":
    arr = ['G', 'R']
    dutch_flag_sort(arr)
    print (arr)
