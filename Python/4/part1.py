def main():
    total = 0
    with open('input.txt', 'r') as file:
        arr = file.read().splitlines()
        # print(arr)
        
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                # if arr[i][j] == 'X':
                    # print(i)
                    # print(j)
                    
                    for k in range(i - 1, i + 1):
                        for l in range(j - 1, j + 1):
                            # if i - 4 < 0 or j  - 4 < 0:
                            
                                continue
                            print(arr[k][l], end='')
                        #     print(' ' + str(i))
                    print('')
main()