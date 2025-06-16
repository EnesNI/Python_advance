from module_4.for_loops import number

count = 1

while count <= 5:
    print("interation", count)
    count +=  1

    #loop control statements
    #break

    numbers =  [1,2,3,4,5,6,7]
    target = 4

    for number in numbers:
        print(number)
        if number == target:
            print("targer found")
            break

            #continue
            scores = [68, 20, 58, 48, 92, 72, 73]
            total = 0
            count = 0

            for scroe in scores:
                if score < 50:
                    continue
                    total += score
                    count += 1
                    average = total / count if count > 0 else 0
                    print("Avarage score for scores above 50: ", arerage)
print(score)