def main ():
    total = 0
    mode = True
    with open('input.txt', 'r') as file:
        text = file.read()
        
        for i in range(len(text)):
            if text[i] == 'm':
                if text[i:i+4] == 'mul(':
                    closing_index = text[i+4:i+4+8].find(')') # Find the first index of a ) at a max of 7 chars after the (
                    if closing_index != -1: # if ) was found
                        closing_index = closing_index + 1 # Because the index found starts at 0
                        numbers =text[i+4:i+4+closing_index-1].split(',')
                        
                        if len(numbers) == 2:
                            if (numbers[0].isdigit() and numbers[1].isdigit()):
                                total = total + (int(numbers[0]) * int(numbers[1]))
                                
    print(total)
main()