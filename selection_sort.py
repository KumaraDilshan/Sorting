import time
def selection_sort(list1):
    start = time.time();
    for counter in range(1,len(list1)):
        temp=list1[len(list1)-counter];
        position=list1.index(max(list1[:len(list1)-counter+1]));
        list1[len(list1)-counter]=max(list1[:len(list1)-counter+1]);
        list1[position]=temp;

    print 'The sorted array is '+ `list1`;
    end = time.time();
    print 'The run time is ' + `end-start` + ' seconds';

selection_sort([12,8.56,-4,-45,69,100,-5000,45.8,65]);
print ''
selection_sort([10,10,10,10,10,10,10,10,10,10,10,10,10]);
print ''
selection_sort([12,120,45,78,-95,100,-2000,2.36,15,-98,0,456,742,65.25,125,74,54.21]);
print ''
selection_sort([10,9,8,7,6,5,4,3,2,1,0]);
print ''
selection_sort([-2.3695]);
print ''
selection_sort([]);
print ''
selection_sort([5.125,-96.45]);
print ''
selection_sort([0,0]);
print ''
selection_sort([12.58,74.25,-56.25]);
print ''
selection_sort([]);
print ''
selection_sort(range(1,2500));
print ''
selection_sort(range(1,201));
print ''
selection_sort(range(1,51));
print ''
selection_sort(range(1,21));
print ''
selection_sort(range(1,11));
print ''
