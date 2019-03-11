n_arr = []
for _ in range(int(input())):
    n_arr.append(int(input()))
n = max(n_arr)
time = [0]*(n+1)
for i in range(2,n+1):
    time[i] = time[i-1] + 1
    if i%2 == 0:
        time[i] = min(time[i//2]+1, time[i])
    if i%3 == 0:
        time[i] = min(time[i//3]+1, time[i])
for n in n_arr:
    print(time[n])
    
            
    
