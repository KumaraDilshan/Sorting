import time
def insertion_sort(list1):
    start = time.time();
    for counter in range(0,len(list1)):
        num=list1[counter];
        for counter1 in range(0,counter):
            if list1[counter1]>num:
                list1[counter1+1:counter+1]=list1[counter1:counter];
                list1[counter1]=num;
                break;
    print 'The sorted array is '+ `list1`;
    end = time.time();
    print 'The run time is ' + `end-start` + ' seconds';

insertion_sort([12,8.56,-4,-45,69,100,-5000,45.8,65]);
print ''
insertion_sort([10,10,10,10,10,10,10,10,10,10,10,10,10]);
print ''
insertion_sort([12,120,45,78,-95,100,-2000,2.36,15,-98,0,456,742,65.25,125,74,54.21]);
print ''
insertion_sort([10,9,8,7,6,5,4,3,2,1,0]);
print ''
insertion_sort([-2.3695]);
print ''
insertion_sort([]);
print ''
insertion_sort([5.125,-96.45]);
print ''
insertion_sort([0,0]);
print ''
insertion_sort([12.58,74.25,-56.25]);
print ''
insertion_sort([]);
print ''
insertion_sort(range(1,2500));
print ''
insertion_sort(range(1,201));
print ''
insertion_sort(range(1,51));
print ''
insertion_sort(range(1,21));
print ''
insertion_sort(range(1,11));
print ''
