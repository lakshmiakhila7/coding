#include <iostream>
#include<vector>
using namespace std;
int main() {
	int num;
	cin >> num;    //Reading input from STDIN
	vector<long long>a(num);
	for(int i=0;i<num;i++){
		cin>>a[i];
	}
	long long sum=0;
	for(int i=0;i<num;++i){
		sum+=a[i];
	}
	cout<<sum<<endl;
	return 0;// Writing output to STDOUT
}
