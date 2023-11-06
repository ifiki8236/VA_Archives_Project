# my_list = [["Adam", 4, 7, 9, 10],
#            ["Catherine", 10, 8, 1, 9],
#            ["John", 10, 9, 7, 7],
#            ["Pedro", 10, 9, 7.5, 9],
#            ["Wanda", 9, 6.5, 4.5, 10]]
# sum= 0
# for t in range(len(my_list)):
#     size= len(my_list[t])
# for i in range(size):
#     print(my_list[i][0],end=': ')
#     for j in range(size-1):
#         num= my_list[i][j+1]
#         sum+=num
#         edemidiong=sum/(size-1)
#     print(f'{edemidiong:.2f}')
#         # print('')
#     sum= 0


# def sumAvg(text, search):
#     if not search in text:
#         return(f'The line of text provided doesn’t contain the character ‘{search}’')
#     else:
#         numbers= '01123456789'
#         sum= 0
#         digit_amount= 0
#         for i in list(text):
#             if i in numbers:
#                 sum+=int(i)
#                 digit_amount+=1
#         avg= sum/digit_amount
#         return(f'The sum of the digits is {sum}\nThe average is {avg:.2f}')

# if __name__ == '__main__':
#     my_string= input('Enter the string: ').lower()
#     search_char= input('Give me the search character: ').lower()
#     # length= len(my_string)
#     # print(length)

#     print(sumAvg(my_string,search_char))




print(sum(2,1))