<hr>
<br>

 > ## <p style="text-align: center;text-wight:bold;">  G. Factorial </p> 
 > <p style="text-align: center;"> time limit per test : 2 seconds<br>
 >memory limit per test : 64 megabytes<br></p> 
> 
>Given a number N. Print the factorial of number N.<br>
>##### Input<br>
>First line contains a number T (1 ≤ T ≤ 15) number of test cases.
Next T lines will contain a number N (0 ≤ N ≤ 20)
> ##### Output<br>
>For each test case print a single line contains the factorial of N.

<br>

<details>
<summary>Solution</summary>

```cpp

#include <bits/stdc++.h>

using namespace std;
 void init(){cin.tie(0); cin.sync_with_stdio(0);}
int main(){init();

int t;cin>>t;
long long result,n;

for(int i=1;i<=t;i++){
    result=1;
    cin>>n;
    if(n==0){
    result=1;
    }else{
   
    for(int j=n;j>0;j--){
            result*=j;
    }
    }
    cout<<result<<endl;
}
return 0;}
```
</details>
<br>
<br>


<hr>
<br>

 > ## <p style="text-align: center;text-wight:bold;">  H. One Prime </p> 
 > <p style="text-align: center;"> time limit per test : 3 seconds<br>
 >memory limit per test : 64 megabytes<br></p> 
> 
> Given a number X. Determine if the number is prime or not
> 
> Note:
> 
> A prime number is a number that is greater than 1 and has only two factors which are 1 and itself.
> 
> In other words : prime number divisible only by 1 and itself.
> 
> Be careful that 1 is not prime .
> The first few prime numbers are :
<br><br>
![Prime Number](file:///C:/Users/Mohamed/Desktop/cffbbc0a8003151adbd88c8cc77237c56ccb224a.png)

<details>
<summary>Solution</summary>

```cpp

#include <bits/stdc++.h>

using namespace std;
 void init(){cin.tie(0); cin.sync_with_stdio(0);}
int main(){init();

long long x;cin>>x;
string result="YES";
if(x%2==0&&x!=2||x<2){
        cout<<"NO";
}else if(x==2){
    cout<<"YES";
}else {
for(int i=x-1;i>1;i--){
    if(x%i==0){
        result="NO";
    }
}
cout<<result;
}

return 0;}
```
</details>

<br>
<br>
<hr>

<br>


 > ## <p style="text-align: center;text-wight:bold;">  I. Palindrome </p> 
 > <p style="text-align: center;"> time limit per test : 1 seconds<br>
 >memory limit per test : 256 megabytes<br></p> 
> 
>Given a number N
. Print 2 lines that contain the following respectively:
>1. Print N in a reversed order and not leading zeroes.
>2. If N is a palindrome number print "YES" otherwise, print "NO.<br>
>##### Note:<br>
>A palindrome number is a number that reads the same forward or backward.<br>
For example: 12321, 101 are palindrome numbers, while 1201, 221 are not.<br>
A leading zero is any 0 digit that comes before the first nonzero digit in a number for example : numbers (005 , 01 , 0123 , 02 , 000250 ) are leading zeroes but ( 5 , 123 , 20 ,2500 ) not leading zeroes numbers .
>##### Input<br>
>Only one line containing a number N
 (1≤N≤10<sup>7</sup>)
.
> ##### Output<br>
>Print the answer required above.
<br>

<details>
<summary>Solution</summary>

```cpp

#include <bits/stdc++.h>

using namespace std;
 void init(){cin.tie(0); cin.sync_with_stdio(0);}
int main(){init();


return 0;}
```
</details>
<br>
<br>


<hr>
<br>





