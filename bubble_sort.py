import time
def bubble_sort(list1):
    start = time.time();
    counter1=len(list1)-1;
    for counter in range(1,len(list1)-1):
        for counter2 in range(0,counter1):
            if list1[counter2]>list1[counter2+1]:
                temp=list1[counter2];
                list1[counter2]=list1[counter2+1];
                list1[counter2+1]=temp;
        counter1=counter1-1;

    print 'The sorted array is '+ `list1`;
    end = time.time();
    print 'The run time is ' + `end-start` + ' seconds';



bubble_sort([12,8.56,-4,-45,69,100,-5000,45.8,65]);
print ''
bubble_sort([10,10,10,10,10,10,10,10,10,10,10,10,10]);
print ''
bubble_sort([12,120,45,78,-95,100,-2000,2.36,15,-98,0,456,742,65.25,125,74,54.21]);
print ''
bubble_sort([10,9,8,7,6,5,4,3,2,1,0]);
print ''
bubble_sort([-2.3695]);
print ''
bubble_sort([]);
print ''
bubble_sort([5.125,-96.45]);
print ''
bubble_sort([0,0]);
print ''
bubble_sort([12.58,74.25,-56.25]);
print ''
bubble_sort([]);
print ''
bubble_sort(range(1,2500));
print ''
bubble_sort(range(1,201));
print ''
bubble_sort(range(1,51));
print ''
bubble_sort(range(1,21));
print ''
bubble_sort(range(1,11));
print ''
